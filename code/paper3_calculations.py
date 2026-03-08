#!/usr/bin/env python3
"""
paper3_calculations.py — Sterile Neutrino Version

Reproduces all numerical results in Paper 3.
Uses 11 eV STERILE neutrinos (Angus 2009, Haslbauer et al. 2020).

The original active neutrino prediction was incorrect — see neutrino_check.py.
"""
import numpy as np, os

c = 2.998e8; G = 6.674e-11; k_B = 1.381e-23; Msun = 1.989e30
kpc_m = 3.086e19; Mpc_m = 3.086e22; eV_J = 1.602e-19
H0 = 67.4e3 / Mpc_m; h = 0.674; Omega_b = 0.0493
a_u = c * H0 / (2 * np.pi)
rho_cr = 1.878e-29 * h**2 * (Mpc_m*100)**3 / (Msun*1e3)  # Msun/Mpc^3

def nu_h(y):
    s = np.sqrt(np.maximum(y, 1e-30))
    return np.where(s > 1e-10, 1/(1-np.exp(-s)), 1/s + 0.5)

if __name__ == '__main__':
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
    os.makedirs(out, exist_ok=True)

    print("=" * 70)
    print("  Paper 3: All Key Numbers (Sterile Neutrino Version)")
    print("=" * 70)

    # §2
    print(f"\n  a_u = {a_u:.4e} m/s^2,  a_u/a_0 = {a_u/1.2e-10:.4f}")

    # §3 Entropy
    S_star = 275 / (k_B * 1.57e7)
    S_ICM = (1e3)**2 * 3e-25 / (k_B * 1e8)
    L_gal = 3e10 * 3.828e26; V_gal = 4/3*np.pi*(15*kpc_m)**3
    S_gal = L_gal / (k_B * 2e7 * V_gal)
    print(f"\n  S_star = {S_star:.3e},  S_ICM = {S_ICM:.3e}")
    print(f"  Per-volume ratio = {S_star/S_ICM:.2e}")
    print(f"  Coarse-grained ratio = {S_gal/S_ICM:.2e}")

    # §6 Cluster mass
    M_b = 3e14; R_vir = 2.0  # Msun, Mpc
    g_B = G * M_b * Msun / (R_vir * Mpc_m)**2
    y = g_B / a_u
    nb = float(nu_h(y))
    print(f"\n  y = {y:.4f},  nu_h = {nb:.3f}")
    print(f"  M_tot/M_bary (ent only) = {nb:.2f},  deficit = {7/nb:.2f}x")

    # §6 Sterile neutrino table
    V_cl = 4/3 * np.pi * R_vir**3
    rho_b_cos = Omega_b * rho_cr
    delta_b = (M_b / V_cl) / rho_b_cos
    M_s_needed = (7 - nb) * M_b
    print(f"\n  delta_b = {delta_b:.0f},  M_s needed = {M_s_needed:.2e} Msun")
    print(f"\n  {'m_s':>6} {'Omega_s':>8} {'v_th km/s':>10} {'delta_s':>8} {'OK?':>8}")
    print(f"  {'-'*44}")
    lines = []
    for ms in [5, 8, 11, 15]:
        Os = ms / (93.14 * h**2)
        rs = Os * rho_cr
        ds = M_s_needed / (rs * V_cl)
        vt = 3.15 * k_B * 1.0 * c / (ms * eV_J) / 1e3
        ok = "Yes" if ds < 1500 else "Marginal"
        print(f"  {ms:>6} {Os:>8.3f} {vt:>10.0f} {ds:>8.0f} {ok:>8}")
        lines.append(f"{ms}\t{Os:.3f}\t{vt:.0f}\t{ds:.0f}\t{ok}")

    # Write all output
    with open(os.path.join(out, 'summary.txt'), 'w') as f:
        f.write("Paper 3: Key Numbers (Sterile Neutrino Version)\n")
        f.write(f"a_u = {a_u:.4e} m/s^2, a_u/a_0 = {a_u/1.2e-10:.4f}\n")
        f.write(f"S_star/S_ICM = {S_star/S_ICM:.2e}\n")
        f.write(f"nu_bar = {nb:.3f}, deficit = {7/nb:.2f}x\n")
        f.write(f"Prediction: m_s ~ 11 eV sterile neutrino\n")

    with open(os.path.join(out, 'neutrino_clustering.txt'), 'w') as f:
        f.write("Sterile Neutrino Budget (CORRECTED)\n")
        f.write(f"Active nu at 0.2 eV requires delta ~ 51000 (IMPOSSIBLE)\n")
        f.write(f"delta_b = {delta_b:.0f}\n\n")
        f.write("m_s\tOmega_s\tv_th\tdelta_s\tfeasible\n")
        for l in lines: f.write(l + "\n")

    with open(os.path.join(out, 'entropy_ratio.txt'), 'w') as f:
        f.write(f"S_star = {S_star:.4e}\nS_ICM = {S_ICM:.4e}\n")
        f.write(f"Ratio = {S_star/S_ICM:.3e}\nCoarse = {S_gal/S_ICM:.3e}\n")

    with open(os.path.join(out, 'bullet_offset_condition.txt'), 'w') as f:
        f.write(f"Required w_S ratio > ~10\nAchieved ~ {S_gal/S_ICM:.0e}\n")

    with open(os.path.join(out, 'cluster_mass_budget.txt'), 'w') as f:
        f.write(f"nu_bar = {nb:.3f}\nDeficit closed by m_s ~ 11 eV sterile nu\n")

    print(f"\n  All outputs written to {out}/")
    print("=" * 70)
