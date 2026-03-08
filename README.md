# Cluster-Scale Gravitational Dynamics from De Sitter Entanglement Entropy

**Charles Grant Smith Jr.** — Independent Researcher

## Key Result

Entanglement gravity ($a_u = cH_0/(2\pi)$) + interaction complexity ($w_S$) + 11 eV sterile neutrino = Bullet Cluster lensing offset + cluster mass budget. No cold dark matter.

## Package Contents

| File | Description |
|------|-------------|
| `paper3_PRD.tex` | **Main manuscript** (REVTeX4-2, all corrections) |
| `supplementary_material.md` | Extended calculations, error correction, lensing details |
| `code/paper3_calculations.py` | Reproduces all numerical results |
| `code/bullet_cluster_lensing.py` | Toy Bullet Cluster κ map (1024² FFT solver) |
| `code/neutrino_check.py` | Proves active neutrinos fail (formula error derivation) |
| `data/*.txt` | Computed output tables |
| `figures/figure_kappa_map.png` | 2×2 convergence map |
| `figures/figure_kappa_1D.png` | 1D convergence profile along merger axis |
| `working_documents/` | Development history (archival) |

## Key Numbers

| Parameter | Value | Source |
|-----------|-------|--------|
| $a_u$ | 1.042 × 10⁻¹⁰ m/s² | $cH_0/(2\pi)$, Planck $H_0$ |
| $\nu(y)$ | $1/(1-e^{-\sqrt{y}})$ | Entropy extremization (Paper 2) |
| $\bar{\nu}$ at cluster scale | 3.68 | $y = 0.10$ |
| Sterile neutrino mass | ~11 eV | Cluster mass budget |
| $\Omega_s$ | 0.26 | $m_s/(93.14 h^2)$ |
| Required $\delta_s$ | ~930 | Achievable for cold HDM |

## Critical Correction

Earlier drafts predicted $\sum m_\nu \approx 0.15$–0.3 eV (active neutrinos). This was **wrong** — the overdensity formula was missing a factor of $\delta_b \approx 1400$. The true required overdensity at 0.2 eV is ~51,000, violating Tremaine-Gunn. See `code/neutrino_check.py`. The paper now uses 11 eV sterile neutrinos following Angus (2009) and Haslbauer et al. (2020).

## Reproducing Results

```bash
pip install numpy scipy matplotlib
python code/paper3_calculations.py    # all key numbers
python code/bullet_cluster_lensing.py # toy lensing map (~30 sec)
python code/neutrino_check.py         # active neutrino failure proof
```

## Connection to Papers 1 and 2

| Paper | Result |
|-------|--------|
| Paper 1 (Zenodo: 10.5281/zenodo.18868563) | $a_u$ fits 171 SPARC galaxies, med $\chi^2/\nu$ = 1.41 |
| Paper 2 | Derives $a_u$ and $\nu(y)$ from horizon thermodynamics |
| Paper 3 (this work) | Cluster extension: Bullet offset + sterile ν mass budget |
