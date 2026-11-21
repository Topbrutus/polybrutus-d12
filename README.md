# POLYBRUTUS 12D — Exact labelled metric and sixfold spectral mode

**Author and scientific responsibility:** Gabriel St-Pierre (Topbrutus), independent researcher.  
**Status:** Computational mathematical research preprint, not human peer reviewed.  
**AI disclosure:** OpenAI ChatGPT (Astra) substantially assisted exact computations, independent checking, graph-model analysis, code, writing and release operations. It is not a research author.

## Reproducible results at radius R = 1

- **17 vertices** and **136 labelled pairwise squared distances** with exact minimal affine embedding dimension **12**.
- The frozen Polybrutus 11D labelled metric is preserved in full (**120/120** existing pair distances).
- Exactly one new orthogonal unit vector adds **16 squared distances of value 2**.
- Normalized distance histogram `k=4d²/R²`: `{4:6, 7:2, 8:105, 9:3, 10:10, 12:6, 13:2, 16:2}`.
- Complete sum of squared distances: `1135 R²/4`.
- Coordinate-difference rank = centered squared-distance Gram rank = **12**, with exact PSD factorization `B=(HX)(HX)^T`.
- Ideal **chosen** scalar-oscillator weighted Laplacian: exact eigenvalue **17/2** of multiplicity **6**, and **8** of multiplicity **4**. The general technique is established mathematics.
- Two distinct verifier programs PASS; four corrupted/invalid variants are deliberately rejected.

## Independent verification

```sh
python -m pip install sympy==1.14.0
python src/verify_d12.py
python tests/independent_d12.py
```

The second program uses rational squared-distance rules and does **not** import any geometric or symbolic generator.

The `prior/` directory preserves the exact source and certified results from the **D11 frozen GitHub release** `v0.1.0`, commit `b49252a03760ea55301b15a60df3c7317f8e3160`, plus the parent source chain.

## Contents

- `SPECIFICATION_D12.md`, `PREUVE_D12.md`, `PROVENANCE.md` — exact construction, proof, provenance.
- `src/verify_d12.py`, `tests/independent_d12.py` — two reproducible programs (MIT).
- `results/certificate_d12.json` — exact labelled values for **all 136 pairs**.
- `publication/POLYBRUTUS_12D_NOTE.pdf` and `.md` — mathematical preprint, CC BY 4.0.
- `SHA256SUMS.txt` — source tag Git-blob SHA-256 index, excluding itself.

## Related research

- [Polybrutus original seven-point specification](https://github.com/Topbrutus/polybrutus/blob/main/SPECIFICATION.md)
- [Polybrutus 7D, DOI 10.5281/zenodo.24407952](https://doi.org/10.5281/zenodo.24407952)
- [Polybrutus 8D, DOI 10.5281/zenodo.24408344](https://doi.org/10.5281/zenodo.24408344)
- [Polybrutus 9D, DOI 10.5281/zenodo.24408448](https://doi.org/10.5281/zenodo.24408448)
- [Polybrutus 10D, DOI 10.5281/zenodo.24408569](https://doi.org/10.5281/zenodo.24408569)
- [Polybrutus 11D, DOI 10.5281/zenodo.24408650](https://doi.org/10.5281/zenodo.24408650)

**Limitations:** Affine dimension here is an exact metric rank, **not** evidence of additional physical spacetime dimensions. The index 12 has **no demonstrated new connection to the separate historical « 12 de Pythagore » question**. No universal theorem novelty, fundamental particle or empirical measurement is claimed.
