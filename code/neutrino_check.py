#!/usr/bin/env python3
"""
neutrino_overdensity_check.py

Checks whether the neutrino mass budget formula in Paper 3 is correct.

The paper claims: delta_nu = (M_nu/M_bary) / (Omega_nu/Omega_b) ~ 35

This script computes delta_nu from first principles to check.
"""
import numpy as np

# Constants
Msun = 1.989e30  # kg
Mpc_m = 3.086e22
G = 6.674e-11
h = 0.674
H0 = h * 100  # km/s/Mpc

# Cosmological densities
rho_crit = 1.878e-29 * h**2  # g/cm^3
rho_crit_Msun_Mpc3 = rho_crit * 1e-3 * (Mpc_m * 100)**3 / Msun  # Msun/Mpc^3

Omega_b = 0.0493
Omega_m = 0.315

rho_b_cosmic = Omega_b * rho_crit_Msun_Mpc3  # Msun/Mpc^3

print("=" * 70)
print("NEUTRINO OVERDENSITY VERIFICATION")
print("=" * 70)
print(f"\nrho_crit = {rho_crit:.4e} g/cm^3")
print(f"rho_crit = {rho_crit_Msun_Mpc3:.4e} Msun/Mpc^3")
print(f"rho_b_cosmic = {rho_b_cosmic:.4e} Msun/Mpc^3")

# Bullet Cluster parameters
M_bary = 3e14  # Msun
R_vir = 2.0    # Mpc
V_cluster = 4/3 * np.pi * R_vir**3  # Mpc^3
rho_bary_cluster = M_bary / V_cluster  # Msun/Mpc^3

print(f"\nBullet Cluster:")
print(f"  M_bary = {M_bary:.1e} Msun")
print(f"  R_vir = {R_vir} Mpc")
print(f"  V_cluster = {V_cluster:.1f} Mpc^3")
print(f"  rho_bary_cluster = {rho_bary_cluster:.4e} Msun/Mpc^3")

# Baryon overdensity
delta_b = rho_bary_cluster / rho_b_cosmic
print(f"\n  delta_b (baryon overdensity in cluster) = {delta_b:.0f}")

# Required neutrino mass
nu_bar = 3.6
M_total_over_M_bary_observed = 7.0
M_nu_over_M_bary = M_total_over_M_bary_observed - nu_bar
M_nu_required = M_nu_over_M_bary * M_bary

print(f"\n  nu_bar = {nu_bar}")
print(f"  M_nu/M_bary needed = {M_nu_over_M_bary:.1f}")
print(f"  M_nu required = {M_nu_required:.2e} Msun")

print("\n" + "=" * 70)
print("CHECKING FORMULA")
print("=" * 70)

for sum_mnu in [0.06, 0.10, 0.15, 0.20, 0.30, 1.0, 2.0, 6.0, 11.0]:
    Omega_nu = sum_mnu / (93.14 * h**2)
    rho_nu_cosmic = Omega_nu * rho_crit_Msun_Mpc3
    
    # Cosmic neutrino mass in cluster volume (no overdensity)
    M_nu_cosmic_in_V = rho_nu_cosmic * V_cluster
    
    # Required overdensity (CORRECT formula)
    delta_nu_correct = M_nu_required / M_nu_cosmic_in_V
    
    # Paper's formula (WRONG?)
    delta_nu_paper = M_nu_over_M_bary / (Omega_nu / Omega_b)
    
    # Neutrino thermal velocity (per species, assuming near-degenerate)
    n_species = 3 if sum_mnu < 5 else 1  # active vs sterile
    m_per_species = sum_mnu / n_species  # eV
    k_B = 1.381e-23
    T_nu = 1.95  # K
    eV_J = 1.602e-19
    c = 2.998e8
    v_th = 3.15 * k_B * T_nu * c / (m_per_species * eV_J) / 1e3  # km/s
    
    print(f"\n  sum_mnu = {sum_mnu:.2f} eV ({n_species} species, {m_per_species:.3f} eV each)")
    print(f"    Omega_nu = {Omega_nu:.5f}")
    print(f"    Omega_nu/Omega_b = {Omega_nu/Omega_b:.4f}")
    print(f"    rho_nu_cosmic = {rho_nu_cosmic:.3e} Msun/Mpc^3")
    print(f"    M_nu_cosmic in V = {M_nu_cosmic_in_V:.3e} Msun")
    print(f"    v_th per species = {v_th:.0f} km/s")
    print(f"    --- delta_nu (CORRECT) = {delta_nu_correct:.0f}")
    print(f"    --- delta_nu (PAPER)   = {delta_nu_paper:.1f}")
    print(f"    --- RATIO (correct/paper) = {delta_nu_correct/delta_nu_paper:.0f}")

print("\n" + "=" * 70)
print("CONCLUSION")
print("=" * 70)
print(f"\nThe paper's formula delta_nu = (M_nu/M_bary)/(Omega_nu/Omega_b)")
print(f"is MISSING the baryon overdensity factor delta_b = {delta_b:.0f}.")
print(f"The correct formula is:")
print(f"  delta_nu = (M_nu/M_bary) * (rho_bary_cluster / rho_nu_cosmic)")
print(f"           = (M_nu/M_bary) / (Omega_nu/Omega_b) * delta_b")
print(f"\nThe required delta_nu is {delta_b:.0f}x larger than claimed.")
print(f"\nFor sum_mnu = 0.20 eV: paper says 35, correct value is {delta_nu_correct:.0f}")
print(f"This is NOT achievable for active neutrinos.")
print(f"\nPublished MOND+neutrino literature uses:")
print(f"  Sanders (2003): 2 eV active neutrinos")
print(f"  Angus (2009): 1.5-2 eV active neutrinos")
print(f"  Haslbauer et al. (2020): 11 eV STERILE neutrinos")
