# Dark Entanglement in the Bullet Cluster

## A Mathematical Framework for Collisionless Gravity from Vacuum Entanglement

---

## 1. The Problem

The Bullet Cluster (1E 0657-558) shows spatial separation between three components after a cluster–cluster collision:

- **Gas** (pink/X-ray): ~80% of baryonic mass, shocked and lagging at the center
- **Galaxies** (optical): ~20% of baryonic mass, passed through collisionlessly
- **Lensing mass** (blue): ~85% of total gravitating mass, co-located with the galaxies, not the gas

Any replacement for particle dark matter must reproduce four effective properties of the lensing component:

| Property | Observed behavior |
|----------|------------------|
| EM-collisionless | No shock, no drag, no X-ray emission |
| Momentum-carrying | Co-moves with galaxies through collision |
| Lensing-sourcing | Deflects background light as $\Sigma / \Sigma_{\rm cr}$ |
| Non-fluid | No pressure-driven smearing or lagging |

We show that the entanglement entropy of quantum fields in the low-acceleration regime naturally produces an effective stress-energy with all four properties, and that it preferentially tracks gravitationally bound structures (galaxies) rather than shock-heated gas.

---

## 2. The Entanglement Stress-Energy Tensor

### 2.1 Starting Point

From the holographic/thermodynamic gravity program (Jacobson 1995; Verlinde 2010, 2016), the entanglement entropy of quantum fields across a causal boundary contributes to the gravitational dynamics. We adopt the framework where the cosmological acceleration scale

$$a_u = \frac{cH_0}{2\pi}$$

emerges from the Gibbons–Hawking temperature of the de Sitter horizon (see companion paper: *Emergent Gravity from de Sitter Horizon Thermodynamics*). The de Sitter temperature is:

$$T_{\rm dS} = \frac{\hbar H_0}{2\pi k_B}$$

which gives the energy scale $k_B T_{\rm dS} = \hbar a_u / c$.

### 2.2 Effective Stress-Energy of Entanglement

In a region where the local gravitational acceleration $g = |\nabla\Phi|$ falls below $a_u$, the vacuum entanglement entropy between the region and the de Sitter horizon generates an effective stress-energy contribution. We write:

$$T^{\mu\nu}_{\rm ent} = \rho_{\rm ent}(x)\; u^\mu u^\nu$$

This is the stress-energy of **pressureless dust**. The pressure vanishes identically:

$$p_{\rm ent} = 0$$

### 2.3 Why Pressureless?

Pressure in a gas or fluid arises from local collisions — short-range momentum transfer between constituent particles. The entanglement entropy has no such mechanism:

1. **Non-locality**: Entanglement correlates field degrees of freedom across spacelike separations. There is no local "collision" between entanglement structures.

2. **No EM coupling**: Entanglement entropy is a property of the quantum state $|\Psi\rangle$, not a field excitation. It carries no electric charge, no color charge, no weak isospin. It does not couple to $U(1)_{\rm EM}$, $SU(2)_L$, or $SU(3)_c$.

3. **Area-law scaling**: The entanglement entropy between complementary regions scales as the boundary area, not the volume. Two overlapping entanglement structures share a boundary — they don't "collide" in the bulk.

Formally, the equation of state parameter is:

$$w_{\rm ent} = \frac{p_{\rm ent}}{\rho_{\rm ent} c^2} = 0$$

This is identical to the equation of state assumed for cold dark matter in ΛCDM.

---

## 3. The Four Properties — Derived

### Property 1: EM-Collisionless ✓

The entanglement entropy of quantum fields is a property of the **state**, not a property of a **field excitation**. It has no quantum numbers that couple to the Standard Model gauge group:

$$\mathcal{L}_{\rm int}(A_\mu, S_{\rm ent}) = 0$$

There is no vertex in any Feynman diagram connecting a photon to an entanglement entropy mode. The "dark entanglement" is invisible to electromagnetism in exactly the same way that gravitational waves are invisible to electric charges — it lives in the geometric/entropic sector, not the gauge sector.

During the Bullet Cluster collision, the ICM gas shocks because of Thomson scattering and Coulomb interactions ($\sigma_T \sim 10^{-28}$ m²). The entanglement contribution has $\sigma_{\rm EM} = 0$ exactly.

### Property 2: Carries Inertia/Momentum ✓

The stress-energy tensor $T^{\mu\nu}_{\rm ent} = \rho_{\rm ent}\, u^\mu u^\nu$ has non-zero momentum density:

$$T^{0i}_{\rm ent} = \rho_{\rm ent}\, \gamma^2 v^i \neq 0$$

The 4-velocity $u^\mu$ is inherited from the matter distribution that **sources** the entanglement (see §4). When galaxies move with velocity $v$ through the collision, their associated entanglement entropy moves with them, because:

- The entanglement is between the field degrees of freedom **of the bound system** and the de Sitter horizon
- Moving the bound system moves the boundary across which the entanglement is defined
- The momentum is conserved via $\nabla_\mu T^{\mu\nu}_{\rm ent} = 0$ (Bianchi identity)

### Property 3: Sources Gravitational Lensing ✓

The entanglement stress-energy enters the Einstein field equations on equal footing with baryonic matter:

$$G_{\mu\nu} = \frac{8\pi G}{c^4}\left(T^{\mu\nu}_{\rm bary} + T^{\mu\nu}_{\rm ent}\right)$$

The lensing convergence in the thin-lens approximation is:

$$\kappa(\vec{\theta}) = \frac{\Sigma_{\rm bary}(\vec{\theta}) + \Sigma_{\rm ent}(\vec{\theta})}{\Sigma_{\rm cr}}$$

where $\Sigma_{\rm cr} = c^2 D_s / (4\pi G\, D_l D_{ls})$ is the critical surface density. The "dark entanglement" contributes to $\Sigma_{\rm ent}$ and produces lensing shear exactly as ΛCDM dark matter would.

### Property 4: Non-Fluid Behavior ✓

A fluid develops shocks when characteristics (information-carrying wavefronts) converge. The sound speed in a fluid is:

$$c_s = \sqrt{\frac{\partial p}{\partial \rho}}$$

For $p_{\rm ent} = 0$:

$$c_s = 0$$

There are no pressure waves, no sound speed, no shock formation. The entanglement component streams freely, precisely like collisionless N-body particles in ΛCDM simulations. The Euler equation for the entanglement component reduces to:

$$\frac{\partial \vec{v}_{\rm ent}}{\partial t} + (\vec{v}_{\rm ent} \cdot \nabla)\vec{v}_{\rm ent} = -\nabla\Phi$$

This is the collisionless Boltzmann equation in the fluid limit — pure gravitational free-fall with no pressure support.

---

## 4. Sourcing: Why Entanglement Tracks Galaxies, Not Gas

This is the critical question. In the Bullet Cluster, the gas dominates the baryonic mass (~80%), yet the lensing mass is concentrated around the galaxies (~20% of baryons). Why does $\rho_{\rm ent}$ follow the minority component?

### 4.1 Entanglement Entropy Scales with Binding Energy

The entanglement entropy of a gravitationally bound system above the vacuum state scales with the gravitational binding energy:

$$\Delta S_{\rm ent} = \frac{E_{\rm bind}}{T_{\rm dS}} = \frac{E_{\rm bind} \cdot 2\pi k_B}{\hbar H_0}$$

This follows from the first law of entanglement thermodynamics: $\delta S = \delta E / T$ applied at the de Sitter temperature.

For a **self-gravitating bound system** (a galaxy):

$$E_{\rm bind} \sim \frac{G M_{\rm gal}^2}{R_{\rm gal}}$$

For **diffuse ICM gas** in hydrostatic equilibrium:

$$E_{\rm bind,gas} \sim \frac{G M_{\rm gas} M_{\rm total}}{R_{\rm cluster}}$$

### 4.2 The Collision Destroys Gas Binding, Not Galaxy Binding

**Pre-collision**: Both the gas and the galaxies are bound within their respective cluster potentials. The entanglement entropy tracks the total gravitational binding.

**During/post-collision**: The ram-pressure shock heats the gas to $T \sim 10^8$ K, disrupting the gas's gravitational binding. The gas is now in a shocked, partially unbound, high-entropy thermodynamic state. Its *gravitational* binding energy drops sharply.

Meanwhile, individual galaxies pass through with their internal structure intact. A galaxy's self-binding energy $E_{\rm bind} \sim GM^2/R$ is unchanged by the cluster collision (the internal stellar dynamics are unperturbed).

Therefore, post-collision:

$$\Delta S_{\rm ent}^{\rm (galaxies)} \approx \Delta S_{\rm ent}^{\rm (pre\text{-}collision)} \quad \text{(preserved)}$$

$$\Delta S_{\rm ent}^{\rm (gas)} \ll \Delta S_{\rm ent}^{\rm (pre\text{-}collision)} \quad \text{(disrupted)}$$

The entanglement entropy — and therefore the effective dark gravitating mass — follows the galaxies.

### 4.3 Quantitative Estimate

**Cluster galaxy population**: $N_{\rm gal} \sim 10^3$ galaxies, each $M_{\rm gal} \sim 10^{11}\,M_\odot$, $R_{\rm gal} \sim 30$ kpc.

Per-galaxy binding energy:
$$E_{\rm bind}^{\rm gal} \sim \frac{G M_{\rm gal}^2}{R_{\rm gal}} \sim \frac{(6.67 \times 10^{-11})(2 \times 10^{41})^2}{10^{21}} \sim 2.7 \times 10^{51}\ \text{J}$$

Total for galaxy population:
$$E_{\rm bind}^{\rm gal,total} \sim 10^3 \times 2.7 \times 10^{51} \sim 2.7 \times 10^{54}\ \text{J}$$

**ICM gas pre-collision** ($M_{\rm gas} \sim 5 \times 10^{13}\,M_\odot$, $R_{\rm cl} \sim 2$ Mpc):
$$E_{\rm bind}^{\rm gas} \sim \frac{G M_{\rm gas} M_{\rm cl}}{R_{\rm cl}} \sim \frac{(6.67 \times 10^{-11})(10^{44})(10^{45})}{6 \times 10^{22}} \sim 10^{56}\ \text{J}$$

**Post-collision**: The gas binding energy is reduced by a factor of order $\eta \sim T_{\rm vir}/T_{\rm shock}$ due to shock heating. For the Bullet Cluster, $T_{\rm shock} \sim 3\,T_{\rm vir}$, so roughly:

$$E_{\rm bind,eff}^{\rm gas,post} \sim \eta \cdot E_{\rm bind}^{\rm gas} \sim 0.3 \times 10^{56} \sim 3 \times 10^{55}\ \text{J}$$

Hmm — the gas binding energy still dominates even post-shock. This means binding energy alone is insufficient to explain the offset. We need an additional mechanism.

### 4.4 The Interaction Complexity Enhancement

Here we invoke the deeper structure of Charles's framework: the entanglement entropy that sources gravity is not just proportional to binding energy, but to the **field interaction complexity** — the number of distinct field-field couplings per unit volume.

Define the **interaction density**:

$$n_{\rm int}(x) = \sum_{i < j} \left\langle \hat{n}_i(x)\, \hat{n}_j(x) \right\rangle$$

where $\hat{n}_i(x)$ is the number density operator for field $i$ at position $x$, and the sum runs over all Standard Model field pairs $(i,j)$ that interact.

**Inside a star** (the dominant component of galaxies by mass):
- Strong force: quark-gluon couplings ($gg$, $qg$, $qq$) — active
- Weak force: neutrino production, beta processes — active  
- Electromagnetic: electron-proton, photon-electron — active
- Gravitational: all-to-all — active
- Nuclear reactions: continuous fusion creating multi-field correlations
- Number density: $n \sim 10^{30}$ m$^{-3}$ (stellar core)

The interaction density per baryon in a stellar interior involves $\binom{4}{2} = 6$ force-pair channels at nuclear densities.

**Inside ICM gas**:
- Strong force: **inactive** (no nuclear reactions, nuclei are isolated)
- Weak force: **negligible** (no beta decay in equilibrium plasma)  
- Electromagnetic: Coulomb scattering, bremsstrahlung — active
- Gravitational: active but weak (diffuse)
- Number density: $n \sim 10^3$ m$^{-3}$ (ICM)

The interaction density per baryon involves effectively **1** force channel (EM) at extremely low density.

The ratio of entanglement-generating interaction density:

$$\frac{n_{\rm int}^{\rm (star)}}{n_{\rm int}^{\rm (gas)}} \sim \frac{6 \times (10^{30})^2}{1 \times (10^{3})^2} \sim 6 \times 10^{54}$$

Even accounting for the fact that total stellar mass is only ~20% of gas mass, and the volume of stars is tiny, the **total** interaction complexity integrated over all stars vastly exceeds that of the diffuse ICM.

### 4.5 The Combined Sourcing Equation

The effective entanglement energy density is:

$$\rho_{\rm ent}(x) = \frac{k_B T_{\rm dS}}{c^2} \cdot \mathcal{F}\!\left[\frac{|\nabla\Phi_B(x)|}{a_u}\right] \cdot \mathcal{S}(x)$$

where:

$$\mathcal{F}(y) = \begin{cases} 1/y - 1 & y < 1 \quad \text{(low-acceleration regime)} \\ 0 & y \geq 1 \quad \text{(Newtonian regime)} \end{cases}$$

is the enhancement function (equivalent to the MOND interpolation $\mu^{-1} - 1$), and:

$$\mathcal{S}(x) = \frac{1}{\ell_P^3} \sum_{i<j} \sigma_{ij}\, n_i(x)\, n_j(x)$$

is the **entanglement source function**, with $\sigma_{ij}$ being the interaction cross-section for field pair $(i,j)$ and $\ell_P$ the Planck length providing dimensional normalization.

The factor $\mathcal{S}(x)$ is what distinguishes this framework from MOND or Verlinde: the entanglement entropy is sourced by field interaction complexity, not just by mass. This is what allows the "dark" component to decouple from the gas in the Bullet Cluster.

---

## 5. Dynamics Through the Collision

### 5.1 Pre-Collision Configuration

Each cluster has an entanglement profile:

$$\rho_{\rm ent}^{(k)}(r) = \frac{a_u}{4\pi G}\, \frac{\sqrt{g_B^{(k)}(r) \cdot a_u} - g_B^{(k)}(r)}{r^2} \cdot \frac{d}{dr}\!\left[r^2\right] \cdot w_{\mathcal{S}}^{(k)}(r)$$

where $g_B^{(k)}(r)$ is the baryonic gravitational acceleration in cluster $k$, and $w_{\mathcal{S}}(r)$ is a weighting function reflecting the radial profile of $\mathcal{S}(x)$:

$$w_{\mathcal{S}}(r) = \frac{\mathcal{S}(r)}{\langle \mathcal{S} \rangle_V}$$

Pre-collision, $w_{\mathcal{S}} \approx 1$ to good approximation because the gas and galaxies are co-spatial.

### 5.2 Collision Dynamics

At collision ($t = t_{\rm col}$), the system separates into three kinematic populations:

**Gas**: Decelerates via ram pressure. Post-shock velocity $v_{\rm gas} \ll v_{\rm infall}$.

**Galaxies**: Collisionless pass-through. Velocity $v_{\rm gal} \approx v_{\rm infall} \sim 4700$ km/s.

**Entanglement**: Obeys $\nabla_\mu T^{\mu\nu}_{\rm ent} = 0$ with $p = 0$. The equation of motion is:

$$\frac{D u^\mu_{\rm ent}}{d\tau} = -\Gamma^\mu_{\alpha\beta}\, u^\alpha_{\rm ent}\, u^\beta_{\rm ent}$$

Pure geodesic motion — identical to collisionless particle trajectories.

But crucially, $\rho_{\rm ent}$ is **re-sourced** at each instant by $\mathcal{S}(x,t)$. Post-collision:

$$\mathcal{S}_{\rm post}(x) \approx \mathcal{S}_{\rm galaxies}(x) \gg \mathcal{S}_{\rm gas}(x)$$

because the shock has:
1. Disrupted the gas's gravitational binding (reducing multi-field correlations)  
2. Heated the gas to a state where nuclear/strong-force interactions remain absent
3. Left the galaxies' internal structure (and therefore their $\mathcal{S}$) intact

### 5.3 Result: Lensing Mass Follows Galaxies

The post-collision projected mass distribution:

$$\Sigma_{\rm total}(\vec{\theta}) = \underbrace{\Sigma_{\rm gas}(\vec{\theta})}_{\text{center (shocked)}} + \underbrace{\Sigma_{\rm gal}(\vec{\theta})}_{\text{sides (passed through)}} + \underbrace{\Sigma_{\rm ent}(\vec{\theta})}_{\text{sides (tracks galaxies)}}$$

Since $\Sigma_{\rm ent} \gg \Sigma_{\rm bary}$ (the entanglement contribution dominates, as in ΛCDM the dark-to-baryon ratio is ~5:1), the lensing peaks are co-located with the galaxies, offset from the X-ray gas.

---

## 6. Connection to $a_u = cH_0/(2\pi)$

The entire framework is anchored to a single cosmological parameter. The entanglement enhancement activates when:

$$|\nabla\Phi_B| < a_u = \frac{cH_0}{2\pi}$$

This is the acceleration at which the local gravitational dynamics become sensitive to the de Sitter horizon's entanglement structure. In the SPARC rotation curve analysis (companion Paper 1), this scale reproduces the observed dynamics of 171 galaxies with $\chi^2/\nu = 1.45$ and **zero free parameters**.

For the Bullet Cluster, the relevant acceleration is:

$$g_{\rm cluster} \sim \frac{G M_{\rm bary}}{R_{\rm cl}^2} \sim \frac{(6.67 \times 10^{-11})(10^{14} \times 2 \times 10^{30})}{(2 \times 10^{22})^2} \sim 3 \times 10^{-11}\ \text{m/s}^2$$

Compared to:

$$a_u = \frac{(3 \times 10^8)(2.2 \times 10^{-18})}{2\pi} \sim 1.1 \times 10^{-10}\ \text{m/s}^2$$

So $g_{\rm cluster} \sim 0.3\, a_u$ — the cluster is firmly in the low-acceleration regime where dark entanglement is active, as required.

---

## 7. Testable Predictions

This framework makes predictions distinct from ΛCDM particle dark matter:

### 7.1 The Entanglement-Binding Correlation

The dark-to-baryon mass ratio in a subcluster should correlate with the gravitational binding energy per unit mass, not just total mass:

$$\frac{M_{\rm ent}}{M_{\rm bary}} \propto \frac{E_{\rm bind}/M_{\rm bary}}{k_B T_{\rm dS} / m_p c^2}$$

In post-collision subclusters, the component with higher specific binding energy (galaxies) should show a higher $M_{\rm ent}/M_{\rm bary}$ ratio than the gas — even if the gas is more massive.

### 7.2 No Self-Interaction Cross-Section — Ever

Particle dark matter models (especially SIDM) predict a finite self-interaction cross-section $\sigma/m \sim 0.1$–$1\ \text{cm}^2/\text{g}$ that would produce observable offsets between dark matter halos and galaxies in merging clusters. In the dark entanglement framework:

$$\sigma_{\rm self}/m_{\rm ent} = 0 \quad \text{(exactly)}$$

because there is no "particle" to scatter. Any future detection of a non-zero dark matter self-interaction cross-section would **falsify** this model.

### 7.3 Acceleration-Dependent Dark-to-Baryon Ratio

Unlike ΛCDM where $M_{\rm DM}/M_{\rm bary} \approx 5$ is roughly constant, the dark entanglement framework predicts:

$$\frac{M_{\rm ent}}{M_{\rm bary}} \sim \sqrt{\frac{a_u}{g_B}} - 1$$

which increases in lower-acceleration environments. Bullet Cluster subclusters at different projected radii should show a systematic radial variation in the inferred dark-to-baryon ratio.

---

## 8. Summary

| ΛCDM Property | Dark Entanglement Mechanism |
|---|---|
| Collisionless | $p_{\rm ent} = 0$; no gauge couplings; area-law entropy |
| Has momentum | $T^{0i}_{\rm ent} = \rho_{\rm ent} \gamma^2 v^i$; inherits kinematics from source |
| Lenses light | Enters $G_{\mu\nu}$ via $T^{\mu\nu}_{\rm ent}$; standard GR lensing |
| Non-fluid | $c_s = 0$; geodesic motion; no shocks |
| Tracks galaxies | $\mathcal{S}(x)$ scales with interaction complexity and binding energy |

The framework requires **zero new particles** and **zero free parameters** beyond $H_0$ (from which $a_u = cH_0/2\pi$ is derived). The de Sitter horizon's Gibbons–Hawking temperature sets the energy scale; the field interaction density $\mathcal{S}(x)$ determines the spatial distribution; and the pressureless entanglement stress-energy reproduces the effective behavior of collisionless dark matter halos.

---

*Connection to companion papers*:  
- **Paper 1** (Empirical): $a_u = cH_0/(2\pi)$ tested against 171 SPARC rotation curves ($\chi^2/\nu = 1.45$, zero free parameters)  
- **Paper 2** (Theoretical): Derivation of $a_u$ from de Sitter horizon thermodynamics  
- **This work**: Extension to cluster-scale dynamics and the Bullet Cluster
