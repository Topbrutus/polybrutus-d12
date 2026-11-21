# Polybrutus 12D: Exact Conservative Completion and Sixfold Spectral Multiplicity

**Research author:** Gabriel St-Pierre  
**Affiliation:** Independent researcher  
**Project:** Polybrutus-X72  
**Date:** 20 November 2026  
**Version:** 0.1.0  
**Status:** Reproducible computational mathematics preprint; not human peer reviewed  
**Parent research:** [Polybrutus 11D, DOI 10.5281/zenodo.24408650](https://doi.org/10.5281/zenodo.24408650)  
**Frozen source release:** [Topbrutus/polybrutus-d12, tag v0.1.0](https://github.com/Topbrutus/polybrutus-d12/tree/v0.1.0) (once publicly released).

## Abstract

An exact **17-point labelled Euclidean distance configuration** is obtained by adding one orthogonal unit-radius point to the independently certified Polybrutus 11D metric, with **minimal affine embedding dimension 12**. The construction conserves **all 120 predecessor pairwise squared distances**, and produces **16 new distances of squared value 2R²**, for **136 total labelled pairwise distances** grouped in eight exact normalized classes. A complete exact coordinate-rank proof, centered squared-distance Gram certificate and a positive-semidefinite Gram factorization are checked with symbolic algebra. A separately implemented rational-arithmetic verifier independently reconstructs the entire 136-entry labelled metric and certifies the Gram rank.

For a **chosen ideal scalar-oscillator model** with complete graph weights `w_ij=R²/d_ij²`, a graph-Laplacian recurrence yields **an eigenvalue 17/2 of exact multiplicity six**, and **an eigenvalue 8 of exact multiplicity four**. The mathematical spectrum is derived symbolically and reproduced independently. It is **not** an observed physical resonance, a new spacetime dimension, a novel universal theorem or proof of the historically unresolved expression « 12 de Pythagore ».

## 1. Canonical provenance and the conservative chain

The Polybrutus configuration originated as seven analytically specified, radius-R points in three-dimensional Euclidean space; its canonical source is publicly available. The archived seven-dimensional completion adjoined five regular-simplex vertices in an orthogonal four-dimensional subspace, preserving all old seven-point distances. This created a 12-vertex metric with intrinsic affine rank seven, archived as [10.5281/zenodo.24407952](https://doi.org/10.5281/zenodo.24407952).

Subsequent certified and separately archived steps were: 8D, 13 vertices and 78 distances ([10.5281/zenodo.24408344](https://doi.org/10.5281/zenodo.24408344)); 9D, 14 vertices and 91 distances ([10.5281/zenodo.24408448](https://doi.org/10.5281/zenodo.24408448)); 10D, 15 vertices and 105 distances ([10.5281/zenodo.24408569](https://doi.org/10.5281/zenodo.24408569)); and 11D, 16 vertices and 120 distances ([10.5281/zenodo.24408650](https://doi.org/10.5281/zenodo.24408650)).

**The present calculation starts from the immutable 11D source release**, `Topbrutus/polybrutus-d11@v0.1.0`, commit `b49252a03760ea55301b15a60df3c7317f8e3160`. The source files and certified exact metrics required for this chain have been copied without alteration from that frozen tag into the `prior/` directory of the 12D source archive. No previously published coordinates were changed.

## 2. Exact 17-point construction

Normalize `R=1` initially. Let `p1,...,p16` be the exact 11D predecessor vectors represented in twelve storage-coordinate slots. The five simplex coordinates obey one exact zero-sum relation, so the predecessor's intrinsic linear space is eleven-dimensional.

Embed each predecessor point by adding a zero at the end, `q_i=(p_i,0)`, for `1<=i<=16`, in thirteen storage slots. Adjoin

```
q17 = e13 = (0,0,0,0,0,0,0,0,0,0,0,0,1).
```

The additional point is orthogonal to all sixteen old vectors and itself has unit norm. Therefore:

```
||q17-q_i||² = ||q17||² + ||q_i||² - 2<q17,q_i> = 2,
i=1,...,16.
```

All 120 predecessor distances are exactly retained and the sixteen new distances have squared value 2. For arbitrary positive `R`, multiply every coordinate by `R`, yielding new squared distances `2R²`.

The number of unordered labelled pairs is `C(17,2)=136`. The exact normalized squared-distance classes `k=4d²/R²` are:

| k | 4 | 7 | 8 | 9 | 10 | 12 | 13 | 16 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Multiplicity | 6 | 2 | **105** | 3 | 10 | 6 | 2 | 2 |

These numbers sum to **136**. The squared-distance sum is exactly:

```
sum_{i<j} d_ij² / R² = 1135/4.
```

At unit radius the centroid in the thirteen storage-coordinate slots equals

```
G = (0,0,1/34,0,0,0,0,0,1/17,1/17,1/17,1/17,1/17).
```

Thirteen storage coordinates are used for convenience, **but the geometric metric is exactly twelve-dimensional** in the affine sense because the simplex block has one exact linear relation.

## 3. Exact certificate of intrinsic affine dimension 12

Denote by `D` the 17-by-17 matrix of exact *squared* labelled Euclidean distances, by `X` the 17-by-13 exact coordinate array, and by `H=I-11ᵀ/17` the centering operator. The centered Euclidean distance Gram matrix is `B=-HDH/2`.

The primary exact SymPy verifier establishes:

```
rank([q2-q1, ..., q17-q1]) = 12;
rank(B) = 12;
B = (HX)(HX)ᵀ.
```

The last identity is an exact factorization, proving positive semidefiniteness without numerical approximations. The matrix `B` is uniquely determined by the complete labelled squared-distance metric. **Every Euclidean realization of the same 136 labelled distances therefore has minimal affine dimension exactly 12**, neither 11 nor 13.

The separately implemented rational reconstruction does not import the primary generator. It uses the original seven-point rational coordinate rules, five regular-simplex interpoint distances, and five new mutually orthogonal unit vectors. Its exact distances agree **136/136** with the primary result, and its centered-distance Gram has rank twelve.

Four deliberate negative-control variants are rejected: tampering with a distance entry, duplicating a vertex (dropping rank), inserting a nonorthogonal vertex, and swapping labels while retaining the distance multiset. The last control establishes why comparison of **labelled** distances matters more than merely comparing histograms.

## 4. Selected weighted-Laplacian model and sixfold eigenvalue

For a theoretical network, place one equal-mass scalar displacement oscillator at each point and choose all-pairs nonnegative spring-like couplings `w_ij=R²/d_ij²`. This graph model is a research choice, **not an observed physical apparatus**.

The new sixteenth-to-seventeenth step creates sixteen equal couplings of weight `1/2`. If `L11` is the 16-by-16 old weighted graph Laplacian and `L12` the 17-by-17 new Laplacian, then:

```
L12 = [ L11 + (1/2)I16      -(1/2)1 ]
      [ -(1/2)1ᵀ                 8   ].
```

Let `chi16(z)=det(zI-L11)` and `chi17(z)=det(zI-L12)`. The uniform mode remains zero; each of the previous fifteen nonuniform modes shifts by `1/2`; a single new intergroup mode appears at eigenvalue `17/2`. Hence:

```
chi17(z) = z(z-17/2)chi16(z-1/2)/(z-1/2).
```

For the original seven-vertex weighted Laplacian, define `f6(z)=chiP7(z)/z`, the polynomial containing its six nonzero modes. The 11D source had already established:

```
chi16(z)=z(z-8)^5(z-15/2)^4 f6(z-9/2).
```

Substitution and exact polynomial simplification therefore yield:

```
chi17(z)=z(z-17/2)^6(z-8)^4 f6(z-5).
```

Direct computation of the **complete exact 17-by-17 characteristic polynomial** confirms this identity. The nonvanishing checks `f6(7/2)!=0` and `f6(3)!=0` ensure that there are no hidden extra factors at either listed root. Thus, in this chosen normalized model:

- `lambda=17/2` has **exact multiplicity 6**.
- `lambda=8` has **exact multiplicity 4**.

The independent rational-distance program computes the full weighted Laplacian and verifies these multiplicities using the derivatives of its characteristic polynomial. No actual frequencies in hertz are claimed because no calibrated mechanical masses, springs or measured system have been specified.

## 5. Reproduce, inspect and falsify

The research archive includes `src/verify_d12.py`, `tests/independent_d12.py`, `results/certificate_d12.json` (all **136** labelled pairs), the frozen source and distance certificates from 8D through 11D in `prior/`, this scientific note, proof/specification files, an automated GitHub Actions test and SHA-256 integrity records.

On a compatible computer run:

```sh
python -m pip install sympy==1.14.0
python src/verify_d12.py
python tests/independent_d12.py
```

Both verifiers must report PASS with the same SHA-256 of the regenerated exact certificate. Corruptions of the input metric or changes in point labels must be caught by the specified negative controls. The published Zenodo release includes the code ZIP from the frozen GitHub scientific tag, this PDF and the standalone exact JSON certificate.

## 6. Limits, precedence and the historical « 12 de Pythagore » question

Orthogonal joins of Euclidean configurations and the corresponding complete-graph spectral shifts are already known mathematical mechanisms. This work contributes an exact, well-provenanced **dimension-12 case** of the Polybrutus construction, not a claim to have invented the underlying orthogonal-extension theorem.

The numerical coincidence that the affine rank is **12** is not by itself evidence for a special Pythagorean twelve-sided shape, a new use of the triple `12²+35²=37²`, or a physical twelve-dimensional universe. Earlier testimony concerning the historical expression « 12 de Pythagore » remains a separate interpretive question. No new physical law, fundamental extra dimension, Higgs-state model or experimental proof is established. Human mathematical peer review is pending.

## 7. Authorship, disclosure, rights

**Human research author and responsible investigator:** Gabriel St-Pierre (independent researcher). He initiated and directs the Polybrutus research programme and the decision to archive each verified dimension.

**Generative AI use disclosure:** OpenAI ChatGPT (Astra) substantially assisted with algebraic reasoning, exact computational scripts, implementation of a separate verification program, theoretical graph-spectrum analysis, source provenance checks, research documentation and drafting. The AI tool is not an author. Independent human peer review remains pending.

**Licensing:** PDF mathematical note and narrative documentation CC BY 4.0; source scripts MIT.

**References:** [canonical Polybrutus specification](https://github.com/Topbrutus/polybrutus/blob/main/SPECIFICATION.md); [Polybrutus 7D](https://doi.org/10.5281/zenodo.24407952); [Polybrutus 8D](https://doi.org/10.5281/zenodo.24408344); [Polybrutus 9D](https://doi.org/10.5281/zenodo.24408448); [Polybrutus 10D](https://doi.org/10.5281/zenodo.24408569); [Polybrutus 11D](https://doi.org/10.5281/zenodo.24408650); [frozen D11 source](https://github.com/Topbrutus/polybrutus-d11/tree/v0.1.0).
