# Proof certificate — Polybrutus affine dimension 12

## A. Exact distance metric

Let `P={p1,...,p16}` denote the frozen D11 radius-one configuration of affine rank 11. Define `q_i=(p_i,0)` for i=1,...,16 and `q17=e13`, orthogonal to the whole old span. Every original squared labelled distance is identical in the new configuration. Because every `q_i` has norm one and `<q_i,q17>=0`,
```
||q17-q_i||² = 1+1-0=2,   i<=16.
```

There are exactly `C(17,2)=136` labelled unordered pairs. The 120 old pairs agree with the frozen D11 certificate; the other sixteen have squared value 2. With `k=4d²`, the histogram is `{4:6,7:2,8:105,9:3,10:10,12:6,13:2,16:2}` and the sum of all squared lengths is `1135/4`.

## B. Minimal dimension is exactly 12

Let `D` be the 17-by-17 matrix of squared distances, `H=I-11ᵀ/17` its centering operator, and `X` the 17-by-13 exact coordinate matrix. SymPy verifies *exactly*:
```
rank([q2-q1,...,q17-q1]) = 12;
rank(B) = 12;
B = -H D H / 2 = (H X)(H X)ᵀ.
```

The explicit Gram factorization proves positive semidefiniteness over the exact algebraic numbers. The centered Gram is uniquely determined by these 136 squared distances, so **every Euclidean realization of this labelled metric has intrinsic affine dimension precisely 12**. Storing its points in 13 coordinates does not imply rank 13.

## C. Ideal weighted-graph spectrum

Define a *mathematical* scalar oscillator at each vertex with equal masses and complete-graph edge weights `w_ij=1/d_ij²`, not a physical experiment. All 16 new couplings are exactly 1/2, so:
```
L12 = [ L11+(1/2)I16   -(1/2)1 ]
      [ -(1/2)1ᵀ             8  ].
```

If `chi16(z)=det(zI-L11)`, the uniform-mode/intergroup-mode decomposition yields:
```
chi17(z)=z(z-17/2)chi16(z-1/2)/(z-1/2).
```

From the previously verified `chi16(z)=z(z-8)^5(z-15/2)^4 f6(z-9/2)`, where `f6(z)=chiP7(z)/z`, substitution gives:
```
chi17(z)=z(z-17/2)^6(z-8)^4 f6(z-5).
```

Direct computation of the *complete* 17-by-17 exact characteristic polynomial confirms this equality. Checks `f6(7/2)!=0` and `f6(3)!=0` ensure that the factors at 17/2 and 8 do not pick up hidden multiplicities. Their exact multiplicities are **6** and **4**, respectively.

The independent rational-metric verifier separately computes every squared distance and the polynomial derivatives proving these root multiplicities, without importing the main program. Four negative controls detect corrupted entries, duplicate points, tilted axes and incorrect labels.

**Limits:** standard orthogonal-extension and graph-join mechanisms are known. No novel spacetime dimension, universal new theorem, particle, empirical physical mode or connection to « 12 de Pythagore » is inferred.
