# Supplementary Material

## Cluster-Scale Gravitational Dynamics from De Sitter Entanglement Entropy

**Charles Grant Smith Jr.** — Independent Researcher

---

### S1. Entropy Production Calculations

#### S1.1 Stellar Interior

Standard solar model (Bahcall, Serenelli & Basu 2005): ε_nuc ≈ 275 W/m³, T_c = 1.57 × 10⁷ K.

    S_star = ε_nuc / (k_B T_c) = 1.27 × 10¹⁸ m⁻³ s⁻¹

#### S1.2 ICM Plasma

Bullet Cluster conditions: n_e ≈ 10³ m⁻³, T ≈ 10⁸ K, Λ(T) ≈ 3 × 10⁻²⁵ W m³.

    S_ICM = n_e² Λ(T) / (k_B T) = 2.17 × 10⁻⁴ m⁻³ s⁻¹

#### S1.3 Microphysical Accounting

The entropy production rate S(x) counts **local** irreversible channels:
- Nuclear burning (in stellar cores)
- Coulomb thermalization (in plasmas)
- Viscous/shock dissipation (at fluid interfaces)
- Radiative absorption/emission where photons are reprocessed locally

Entropy **exported** by free-streaming radiation (starlight escaping to infinity) is NOT counted as local production. S(x) is evaluated at the gravitational field solver resolution (~5–30 kpc), matching weak-lensing reconstruction resolution.

---

### S2. Why Active Neutrinos Fail

The original manuscript predicted Σm_ν ≈ 0.15–0.3 eV. This was **incorrect** due to a missing factor.

The paper's formula was:
    δ_ν = (M_ν/M_bary) / (Ω_ν/Ω_b) ≈ 35

The **correct** formula is:
    δ_ν = M_ν_required / (ρ_ν_cosmic × V_cluster)

Because M_bary in the cluster is the **overdense** baryonic mass (δ_b ≈ 1400), the correct δ_ν is:
    δ_ν = (M_ν/M_bary) × δ_b / (Ω_ν/Ω_b) ≈ 35 × 1400 ≈ 51,000

For active neutrinos at 0.2 eV (v_th ≈ 2400 km/s), this violates the Tremaine-Gunn phase-space bound by orders of magnitude.

This is consistent with the published literature:
- Sanders (2003): requires 2 eV neutrinos
- Angus (2009): requires ~2 eV active or ~11 eV sterile
- Haslbauer et al. (2020): uses 11 eV sterile neutrinos

See `code/neutrino_check.py` for the complete derivation.

---

### S3. Sterile Neutrino Properties (m_s ≈ 11 eV)

| Property | Value |
|----------|-------|
| Mass | ~11 eV |
| Ω_s | 0.260 (cf. Ω_DM = 0.265 in ΛCDM) |
| v_th today | ~7 km/s |
| Free-streaming scale | ~few Mpc |
| Required δ_s in cluster | ~930 |
| Tremaine-Gunn limit | ~10⁴ (satisfied) |
| Bound to MW-type galaxy? | No (free-streams through) |
| Bound to rich cluster? | Yes (v_th ≪ v_esc) |

The sterile neutrino is the minimal Standard Model extension (one right-handed neutrino). Its mass is predicted by cluster dynamics, not fitted.

---

### S4. Interpolation Function Comparison at Cluster Scales

Holographic (Paper 2): ν_h(y) = 1/(1 − exp(−√y))
Simple (MOND):         ν_s(y) = (1 + √(1 + 4/y))/2

At y = 0.100 (cluster scale): ν_h = 3.684, ν_s = 3.696. Difference: 0.3%.

---

### S5. Lensing Assumption

QUMOND is non-relativistic. We assume photon deflection is sourced by Φ_tot = Φ_N + Φ_ph with no gravitational slip (Ψ/Φ = 1). This assumption is supported by the Skordis & Złośnik (2021) relativistic MOND theory, which yields QUMOND as its weak-field limit with lensing sourced by the same potential. The no-slip assumption is itself testable by Euclid and Rubin/LSST.

---

### S6. Toy Lensing Map

The file `code/bullet_cluster_lensing.py` solves the w_S-modified QUMOND equation on a 1024² grid for a simplified Bullet Cluster geometry. This is a **toy morphology calculation** demonstrating the direction of the effect, not a best-fit reconstruction. Key results:

- Standard QUMOND: κ peaks at gas location (x ≈ −26 kpc)
- w_S-modified QUMOND: κ peaks at gas location (x ≈ −15 kpc) — modest shift
- Full model (w_S + sterile ν): κ peaks at **galaxy location** (x ≈ −642 kpc)

The dominant effect moving the peak is the sterile neutrino component with pre-collision inertia. The w_S modification provides spatial modulation of the phantom density but contributes a smaller shift than the HDM component in this geometry.

The bullet-side peak does not fully separate from the gas center in this toy model. A full 3D calculation with realistic profiles would be needed for a quantitative comparison to observed lensing reconstructions.
