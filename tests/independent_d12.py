#!/usr/bin/env python3
"""Independent Polybrutus 12D metric and Laplacian verifier.

No import of D12, D11 or any earlier generator. Builds all 136 rational
squared labelled distances from the canonical seven-point relations,
the five regular-simplex vertices, and five orthogonal unit-axis vertices.
"""
import json,hashlib
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
report=json.loads((ROOT/"results"/"certificate_d12.json").read_text(encoding="utf8"))
old=json.loads((ROOT/"prior"/"certificate_d11.json").read_text(encoding="utf8"))
core=[
 (F(0),F(0),F(1)),
 (F(1,2),F(0),F(1,2)),
 (F(-1,4),F(3,4),F(1,2)),
 (F(-1,4),F(-3,4),F(1,2)),
 (F(0),F(0),F(-1)),
 (F(1,2),F(0),F(-1,2)),
 (F(-1,2),F(0),F(-1,2))
]
def squared_distance(i,j):
    if i==j:return F(0)
    if i<7 and j<7:
        a,b,c=(core[i][k]-core[j][k] for k in range(3))
        return 3*a*a+b*b+c*c
    if 7<=i<12 and 7<=j<12:return F(5,2)
    return F(2)

pairs=list(combinations(range(17),2))
exact={(i+1,j+1):squared_distance(i,j) for i,j in pairs}
archived={(int(e["i"]),int(e["j"])):F(e["d2"]) for e in report["labelled_squared_distances"]}
assert len(exact)==136 and exact==archived
oldpairs={(int(e["i"]),int(e["j"])):F(e["d2"]) for e in old["labelled_squared_distances"]}
assert len(oldpairs)==120 and all(exact[k]==v for k,v in oldpairs.items())
assert all(squared_distance(i,16)==F(2) for i in range(16))
hist=Counter(4*squared_distance(i,j) for i,j in pairs)
assert hist==Counter({F(4):6,F(7):2,F(8):105,F(9):3,F(10):10,F(12):6,F(13):2,F(16):2})
assert sum(exact.values(),F(0))==F(1135,4)
D=s.Matrix(17,17,lambda i,j:s.Rational(squared_distance(i,j).numerator,squared_distance(i,j).denominator))
H=s.eye(17)-s.ones(17)/17
assert (-H*D*H/2).rank()==12
D11=D[:16,:16]
H11=s.eye(16)-s.ones(16)/16
assert (-H11*D11*H11/2).rank()==11
L=s.zeros(17)
for i,j in pairs:
    w=1/D[i,j]
    L[i,i]+=w;L[j,j]+=w;L[i,j]-=w;L[j,i]-=w
z=s.Symbol("z")
chi=L.charpoly(z).as_expr()
for value,mult in [(s.Rational(17,2),6),(s.Integer(8),4)]:
    assert all(s.simplify(s.diff(chi,z,k).subs(z,value))==0 for k in range(mult))
    assert s.simplify(s.diff(chi,z,mult).subs(z,value))!=0
assert report["affine_rank"]==report["centered_gram_rank"]==12
assert report["parent_distances_preserved"]==120 and report["new_distances"]==16
p=ROOT/"results"/"certificate_d12.json"
print("INDEPENDENT D12 PASS: 136 rational labelled distances, 120/120 parent preserved, centered Gram rank 12")
print("INDEPENDENT SPECTRUM PASS: eigenvalue 17/2 x6 and eigenvalue 8 x4")
print("CERTIFICATE_SHA256="+hashlib.sha256(p.read_bytes()).hexdigest())
