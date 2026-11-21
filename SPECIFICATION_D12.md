# Polybrutus D12 — exact seventeen-point Euclidean configuration

**Immutable previous release:** `Topbrutus/polybrutus-d11@v0.1.0`, commit `b49252a03760ea55301b15a60df3c7317f8e3160`, Zenodo DOI `10.5281/zenodo.24408650`.

## Exact points

For `R=1`, let `p1,...,p16` be the sixteen D11 unit vectors as represented in twelve storage coordinates. The five-simplex coordinate block satisfies a single exact linear relation. Embed all old points by `q_i=(p_i,0)`. Append `q17=e13=(0,...,0,1)` in the new coordinate. `q17` is orthogonal to all prior vectors and has unit norm.

For arbitrary radius `R>0`, multiply all vector coordinates by `R`:
```
d(q_i,q17)²=2R²,   i=1,...,16.
```

- 17 vertices; 136 unordered pairwise distances.
- 120/120 prior labelled squared distances are unchanged.
- 16 new distances squared exactly `2R²`.
- The **13 coordinate storage slots** have one linear relation; intrinsic affine rank **12**.
- `sum_{i<j}d_ij² = (1135/4) R²`.
- At `R=1` the storage-coordinate centroid is
  `(0,0,1/34,0,0,0,0,0,1/17,1/17,1/17,1/17,1/17)`.

Histogram of normalized squared lengths `k=4d²/R²`:

| k | 4 | 7 | 8 | 9 | 10 | 12 | 13 | 16 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Count | 6 | 2 | **105** | 3 | 10 | 6 | 2 | 2 |

## Chosen ideal oscillator model

For unit masses and complete-graph couplings `w_ij=R²/d_ij²`, all new vertex couplings are 1/2. The weighted Laplacian obeys:

```
L12 = [ L11+(1/2)I16      -(1/2)1 ]
      [ -(1/2)1ᵀ                8   ]
```

The exact monic characteristic polynomial is:
```
chi17(z)=z(z-17/2)^6(z-8)^4 f6(z-5)
```
where `f6(z)=chiP7(z)/z` is the factor for the six nonzero modes of the original Polybrutus seven-point graph. Modes: lambda 17/2 of multiplicity 6; lambda 8 of multiplicity 4.

**No link to new physical dimensions, no verified Pythagorean meaning for the label 12.**
