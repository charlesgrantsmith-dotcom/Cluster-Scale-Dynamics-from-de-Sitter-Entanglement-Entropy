# The Interaction Complexity Source Function $\mathcal{S}(x)$

## A Rigorous Definition from Quantum Decoherence Rates

---

## 1. What $\mathcal{S}$ Must Do

The modified Poisson equation for the entanglement density is:

$$\rho_{\rm ent}(x) = \frac{1}{4\pi G}\,\nabla\cdot\!\left[w_{\mathcal{S}}(x)\,(\nu(y) - 1)\,\vec{g}_N(x)\right] \tag{1}$$

where $y = |\vec{g}_N|/a_u$ and $w_{\mathcal{S}} = \mathcal{S}/\langle\mathcal{S}\rangle$.

For this equation to be more than QUMOND with a fudge factor, $\mathcal{S}(x)$ must satisfy six requirements:

| # | Requirement | Why |
|---|-------------|-----|
| R1 | Has well-defined dimensions | Otherwise $w_{\mathcal{S}}$ is meaningless |
| R2 | Computable from standard astrophysical inputs | Otherwise it's not predictive |
| R3 | Large in stellar interiors, small in diffuse plasma | Bullet Cluster offset |
| R4 | Reduces to spatially uniform in relaxed galaxies | SPARC fits preserved |
| R5 | Connected to entanglement entropy generation | Physical motivation |
| R6 | Defined for arbitrary matter states (stars, gas, dust, remnants) | Generality |

---

## 2. The Physical Basis: Decoherence as Entanglement Production

### 2.1 The Connection

When a quantum system interacts with its environment, the interaction produces entanglement between the system and the environment. The rate of entanglement production is the **decoherence rate** — the rate at which off-diagonal elements of the system's reduced density matrix decay.

In the present framework, the "environment" is ultimately the de Sitter horizon. But the local decoherence rate — the rate at which field degrees of freedom at position $x$ become entangled with their surroundings through physical interactions — serves as a proxy for the rate at which entanglement entropy is generated that couples to the horizon through the gravitational channel.

The claim: **regions with higher decoherence rates generate more entanglement entropy per unit mass, and therefore source more entanglement gravity.**

### 2.2 The Decoherence Rate in Matter

For a quantum system (a field mode, a particle) at position $x$, the decoherence rate is:

$$\Gamma_{\rm dec}(x) = \sum_{\alpha} \Gamma_\alpha(x) \tag{2}$$

where $\alpha$ labels the interaction channels (strong, electromagnetic, weak, gravitational) and $\Gamma_\alpha$ is the partial decoherence rate from channel $\alpha$.

Each partial rate has the standard form from open quantum systems theory (Joos & Zeh 1985, Zurek 2003):

$$\Gamma_\alpha(x) = n_\alpha(x)\,\langle\sigma_\alpha v_{\rm rel}\rangle_{\rm th}(x) \tag{3}$$

where:
- $n_\alpha(x)$ is the number density of scattering partners in channel $\alpha$
- $\langle\sigma_\alpha v_{\rm rel}\rangle_{\rm th}$ is the thermally averaged interaction rate coefficient
- The product gives the collision/interaction rate per target particle

This is identical in form to a standard reaction rate in plasma physics or nuclear astrophysics. The difference is interpretive: we are computing it not to track energy transfer but to quantify the rate of quantum correlation (entanglement) production.

---

## 3. Definition of $\mathcal{S}(x)$

### 3.1 The Source Function

$$\boxed{\mathcal{S}(x) = \frac{\rho_B(x)}{m_p}\;\Gamma_{\rm dec}(x) = \frac{\rho_B(x)}{m_p}\sum_\alpha n_\alpha(x)\,\langle\sigma_\alpha v_{\rm rel}\rangle_{\rm th}(x)} \tag{4}$$

**Dimensions**: $[\mathcal{S}] = \text{m}^{-3}\,\text{s}^{-1}\,\text{m}^{-3} = \text{m}^{-6}\,\text{s}^{-1}$

Wait — let me be more careful. The number density of baryons is $n_B = \rho_B/m_p$, and the decoherence rate per baryon is $\Gamma_{\rm dec}$. The total decoherence rate per unit volume is:

$$\mathcal{S}(x) = n_B(x)\;\Gamma_{\rm dec}(x) = \frac{\rho_B(x)}{m_p}\sum_\alpha n_\alpha(x)\,\langle\sigma_\alpha v_{\rm rel}\rangle(x) \tag{5}$$

**Dimensions**: $[\mathcal{S}] = [\text{m}^{-3}][\text{s}^{-1}] = \text{m}^{-3}\,\text{s}^{-1}$

This is the **volumetric decoherence rate** — the number of decoherence events per unit volume per unit time. It has the same dimensions as a reaction rate density, which is standard in nuclear and plasma astrophysics.

### 3.2 The Weighting Function

The dimensionless weighting:

$$w_{\mathcal{S}}(x) = \frac{\mathcal{S}(x)}{\bar{\mathcal{S}}} \tag{6}$$

where $\bar{\mathcal{S}}$ is the mass-weighted mean over the system:

$$\bar{\mathcal{S}} = \frac{\int \mathcal{S}(x)\,\rho_B(x)\,d^3x}{\int \rho_B^2(x)/m_p\,d^3x} = \frac{\int \rho_B\,\Gamma_{\rm dec}\,d^3x}{\int (\rho_B/m_p)\,\rho_B\,d^3x/\int\rho_B\,d^3x} \tag{7}$$

Actually, the normalization is simpler if we define it operationally. For a relaxed, isolated galaxy where all baryons are in a similar environment, $\mathcal{S}(x) \propto \rho_B(x) \times (\text{local } \Gamma_{\rm dec})$ is approximately proportional to $\rho_B^2$ (since denser regions have both more baryons and higher interaction rates). The weighting $w_{\mathcal{S}}$ then tracks $\rho_B$, and when substituted into Eq. (1), it modifies the entanglement density profile in a way that tracks the baryonic profile — i.e., $w_{\mathcal{S}} \approx \text{const}$ to the extent that $\Gamma_{\rm dec}$ per baryon is spatially uniform.

For a system like the Bullet Cluster where $\Gamma_{\rm dec}$ varies enormously between components, $w_{\mathcal{S}}$ is far from constant, and the entanglement density is redirected toward high-$\Gamma_{\rm dec}$ regions.

### 3.3 Practical Normalization

Define $\bar{\mathcal{S}}$ as the baryonic-mass-weighted mean decoherence rate per baryon:

$$\bar{\Gamma}_{\rm dec} \equiv \frac{\int n_B(x)\,\Gamma_{\rm dec}(x)\,d^3x}{\int n_B(x)\,d^3x} = \frac{\int \mathcal{S}(x)\,d^3x}{N_B^{\rm (total)}} \tag{8}$$

where $N_B^{\rm (total)}$ is the total number of baryons in the system. Then:

$$w_{\mathcal{S}}(x) = \frac{\Gamma_{\rm dec}(x)}{\bar{\Gamma}_{\rm dec}} \tag{9}$$

This is simply the local decoherence rate per baryon, normalized to the system average. It is dimensionless, equals 1 on average (by construction), and varies spatially according to the local interaction environment.

---

## 4. Computation of $\Gamma_{\rm dec}$ in Astrophysical Environments

### 4.1 The Interaction Channels

For baryonic matter, the relevant decoherence channels are:

| Channel $\alpha$ | Interaction | Active where | Rate coefficient |
|-------------------|-------------|-------------|------------------|
| Strong (nuclear) | $pp$, $p\alpha$, CNO, triple-$\alpha$, etc. | Stellar cores, supernovae | $\langle\sigma v\rangle_{\rm nuc}(T)$ |
| Electromagnetic (Coulomb) | $e$-$p$, $e$-$e$, $p$-$p$ Coulomb scattering | All ionized matter | $\nu_{\rm ei}(n_e, T)$ |
| Electromagnetic (radiative) | Bremsstrahlung, Compton, photoionization | Hot plasma, stellar envelopes | $\Lambda(T)\,n_e/k_BT$ |
| Weak | Beta decay, neutrino scattering | Stellar cores, neutron stars | $\langle\sigma v\rangle_{\rm weak}(T)$ |
| Gravitational (tidal) | Tidal decoherence from neighboring masses | Dense stellar environments | $\Gamma_{\rm grav}(n_\star, M, r)$ |

In practice, the dominant channels are strong (in stellar cores) and electromagnetic (everywhere ionized matter exists). Weak and gravitational channels are subdominant except in extreme environments (neutron stars, black hole accretion disks).

### 4.2 Stellar Interior: All Channels Active

For a solar-type stellar core ($T \sim 1.5 \times 10^7$ K, $\rho \sim 1.5 \times 10^5$ kg/m³, $n_p \sim 10^{32}$ m$^{-3}$):

**Nuclear (strong) channel**:

The pp-chain rate coefficient at solar-core conditions:

$$\langle\sigma v\rangle_{pp} \approx 4 \times 10^{-50}\;\text{m}^3\,\text{s}^{-1} \tag{10}$$

(This is extremely small because the pp reaction requires quantum tunneling through the Coulomb barrier followed by a weak-force conversion $p \to n$.)

Nuclear decoherence rate per proton:

$$\Gamma_{\rm nuc} = n_p\,\langle\sigma v\rangle_{pp} \approx (10^{32})(4 \times 10^{-50}) = 4 \times 10^{-18}\;\text{s}^{-1} \tag{11}$$

This is tiny — a proton undergoes a nuclear reaction roughly once every $10^{10}$ years.

**Electromagnetic (Coulomb) channel**:

The electron-ion collision frequency in a fully ionized plasma (Spitzer 1962):

$$\nu_{ei} = \frac{4\sqrt{2\pi}}{3}\;\frac{n_e e^4 \ln\Lambda}{m_e^{1/2}(k_BT)^{3/2}} \tag{12}$$

where $\ln\Lambda$ is the Coulomb logarithm ($\approx 2$–$5$ in stellar interiors, $\approx 30$–$40$ in the ICM).

For solar-core conditions ($n_e \approx 10^{32}$ m$^{-3}$, $T = 1.5 \times 10^7$ K, $\ln\Lambda \approx 2$):

$$\nu_{ei}^{\rm (star)} \approx \frac{4\sqrt{2\pi}}{3}\;\frac{(10^{32})(2.56 \times 10^{-76})(2)}{(9.1 \times 10^{-31})^{1/2}(2.07 \times 10^{-16})^{3/2}} \tag{13}$$

Computing the denominator: $(9.1 \times 10^{-31})^{1/2} = 3.02 \times 10^{-16}$, $(2.07 \times 10^{-16})^{3/2} = 9.4 \times 10^{-25}$

Denominator: $3.02 \times 10^{-16} \times 9.4 \times 10^{-25} = 2.84 \times 10^{-40}$

Numerator prefactor: $\frac{4\sqrt{2\pi}}{3} \approx 3.34$

Numerator: $3.34 \times (10^{32})(2.56 \times 10^{-76})(2) = 3.34 \times 5.12 \times 10^{-44} = 1.71 \times 10^{-43}$

$$\nu_{ei}^{\rm (star)} \approx \frac{1.71 \times 10^{-43}}{2.84 \times 10^{-40}} \approx 6 \times 10^{-4}\;\text{s}^{-1} \tag{14}$$

Hmm, that seems low. Let me use the standard approximate formula instead:

$$\nu_{ei} \approx 3.6 \times 10^{-6}\;\frac{Z^2\,n_i\,\ln\Lambda}{T_{eV}^{3/2}}\;\text{s}^{-1} \tag{15}$$

where $n_i$ is in cm$^{-3}$ and $T_{eV}$ is in eV.

Solar core: $n_i \approx 10^{26}$ cm$^{-3}$, $T \approx 1300$ eV, $\ln\Lambda \approx 2$, $Z = 1$:

$$\nu_{ei}^{\rm (star)} \approx 3.6 \times 10^{-6}\;\frac{(1)(10^{26})(2)}{(1300)^{3/2}} = 3.6 \times 10^{-6}\;\frac{2 \times 10^{26}}{4.69 \times 10^4}$$

$$= 3.6 \times 10^{-6} \times 4.26 \times 10^{21} = 1.5 \times 10^{16}\;\text{s}^{-1} \tag{16}$$

**This is the dominant channel.** Each proton in a stellar core undergoes ~$10^{16}$ Coulomb interactions per second.

**Total decoherence rate per baryon in a stellar interior**:

$$\Gamma_{\rm dec}^{\rm (star)} \approx \nu_{ei}^{\rm (star)} \approx 1.5 \times 10^{16}\;\text{s}^{-1} \tag{17}$$

(Nuclear and weak channels are negligible by comparison.)

### 4.3 ICM Plasma: Coulomb Only

For the intracluster medium ($T \sim 10^8$ K $\approx 8600$ eV, $n_e \sim 10^3$ m$^{-3} = 10^{-3}$ cm$^{-3}$, $\ln\Lambda \approx 40$):

$$\nu_{ei}^{\rm (ICM)} \approx 3.6 \times 10^{-6}\;\frac{(1)(10^{-3})(40)}{(8600)^{3/2}} = 3.6 \times 10^{-6}\;\frac{0.04}{7.98 \times 10^5}$$

$$= 3.6 \times 10^{-6} \times 5.01 \times 10^{-8} = 1.8 \times 10^{-13}\;\text{s}^{-1} \tag{18}$$

Each proton in the ICM undergoes a Coulomb scattering roughly once every $10^5$ years.

### 4.4 The Ratio

$$\frac{\Gamma_{\rm dec}^{\rm (star)}}{\Gamma_{\rm dec}^{\rm (ICM)}} = \frac{1.5 \times 10^{16}}{1.8 \times 10^{-13}} \approx 8 \times 10^{28} \tag{19}$$

This is the decoherence rate per baryon ratio. It is enormous because:
- Stellar-core density exceeds ICM density by a factor of ~$10^{29}$ (in CGS: $10^{26}$ vs $10^{-3}$ cm$^{-3}$)
- Stellar-core temperature is ~100× lower than ICM temperature, which *increases* the Coulomb rate ($\nu_{ei} \propto T^{-3/2}$)
- The Coulomb logarithm partially compensates (larger in ICM) but only by a factor of ~20

### 4.5 But: Volume Matters

The ratio above is per baryon. For the Bullet Cluster, what matters is the mass-weighted average $w_{\mathcal{S}}$ over each component.

**Galaxy component**: Only a fraction $f_\star$ of galactic baryons are inside stellar interiors at any given time. The rest are in the interstellar medium (ISM), which has intermediate conditions.

- Fraction of baryons in stellar interiors: $f_\star^{\rm (interior)} \approx f_\star \approx 0.05$–$0.3$ (depending on galaxy type and stellar mass function)
- Baryons in ISM: partially ionized, $n \sim 10^{-1}$–$10^{6}$ cm$^{-3}$, $T \sim 10^2$–$10^6$ K

The mass-weighted decoherence rate for the galaxy component:

$$\bar{\Gamma}_{\rm dec}^{\rm (gal)} = f_\star \cdot \Gamma_{\rm dec}^{\rm (star)} + (1-f_\star)\cdot\Gamma_{\rm dec}^{\rm (ISM)} \tag{20}$$

The ISM decoherence rate varies hugely with phase (molecular clouds vs. hot ISM), but for the warm ionized medium ($n_e \sim 0.1$ cm$^{-3}$, $T \sim 10^4$ K):

$$\nu_{ei}^{\rm (WIM)} \approx 3.6 \times 10^{-6}\;\frac{(1)(0.1)(20)}{(0.86)^{3/2}} \approx 3.6 \times 10^{-6} \times 2.5 = 9 \times 10^{-6}\;\text{s}^{-1} \tag{21}$$

This is much larger than the ICM rate but much smaller than the stellar-core rate. For the mass-weighted average:

$$\bar{\Gamma}_{\rm dec}^{\rm (gal)} \approx f_\star \cdot 1.5 \times 10^{16} + (1-f_\star) \cdot 10^{-5}$$

$$\approx f_\star \times 1.5 \times 10^{16}\;\text{s}^{-1} \tag{22}$$

The stellar-interior term completely dominates, even for small $f_\star$.

### 4.6 The Mass-Weighted Ratio for the Bullet Cluster

$$\frac{w_{\mathcal{S}}^{\rm (gal)}}{w_{\mathcal{S}}^{\rm (gas)}} = \frac{\bar{\Gamma}_{\rm dec}^{\rm (gal)}}{\bar{\Gamma}_{\rm dec}^{\rm (gas)}} = \frac{f_\star \times 1.5 \times 10^{16}}{1.8 \times 10^{-13}} = f_\star \times 8 \times 10^{28} \tag{23}$$

Even with $f_\star = 0.05$ (only 5% of galactic baryons inside stars at a given time):

$$\frac{w_{\mathcal{S}}^{\rm (gal)}}{w_{\mathcal{S}}^{\rm (gas)}} \approx 4 \times 10^{27} \tag{24}$$

The required ratio from the Bullet condition (Eq. 19 of the Bullet paper, now in flux form) is $\gtrsim 10$.

**The constraint is satisfied by 26 orders of magnitude.**

### 4.7 Interpretation of the Enormous Ratio

The ratio being $10^{27}$ rather than $10^1$ means that the Bullet Cluster offset is **not a fine-tuned outcome** — it is an overwhelming consequence of the density contrast between stellar interiors and the ICM. Any reasonable definition of $\mathcal{S}$ based on interaction rates will produce this result.

However, such an extreme ratio raises a concern: does $w_{\mathcal{S}} \gg 1$ near galaxies cause the entanglement density to be concentrated too tightly around the stellar component, rather than forming an extended halo?

The answer is no, because $w_{\mathcal{S}}$ appears inside the divergence (Eq. 1). The entanglement density is not $\propto w_{\mathcal{S}} \times \rho_B$ — it is $\propto \nabla\cdot(w_{\mathcal{S}} \times (\nu-1)\vec{g}_N)$. The divergence distributes the effect spatially. The $w_{\mathcal{S}}$ factor enhances the source *strength* at the galaxy location, but the gravitational field $\vec{g}_N$ and the $\nu$ enhancement operate over the full cluster volume. The result is that the *amplitude* of the entanglement halo is set by $w_{\mathcal{S}}$-weighted regions, while the *extent* of the halo is set by where $g_N < a_u$ — which is everywhere at the cluster scale.

---

## 5. Addressing the Cluster Mass Discrepancy

### 5.1 The Standard QUMOND Deficit

Standard QUMOND (without $w_{\mathcal{S}}$) applied to clusters gives $M_{\rm total}/M_{\rm bary} \sim 2$–$3$, compared to the observed $\sim 6$–$8$. The entanglement density from pure QUMOND is:

$$\rho_{\rm ent}^{\rm (QUMOND)}(x) = \frac{1}{4\pi G}\,\nabla\cdot\!\left[(\nu-1)\vec{g}_N\right] \tag{25}$$

Integrated over the cluster:

$$M_{\rm ent}^{\rm (QUMOND)} = \frac{1}{4\pi G}\oint_S (\nu-1)\vec{g}_N\cdot d\vec{A} = (\bar{\nu} - 1)\,M_B \tag{26}$$

where the last step uses Gauss's theorem and $\bar{\nu}$ is an appropriate flux-weighted average of $\nu$ over the bounding surface.

At the cluster virial radius where $g_N/a_u \sim 0.3$–$0.5$:

$$\bar{\nu} \sim 2$–$2.5 \qquad \Rightarrow \qquad M_{\rm total}/M_{\rm bary} \sim 2$–$2.5 \tag{27}$$

### 5.2 The $w_{\mathcal{S}}$ Enhancement

With $w_{\mathcal{S}}$ inside the divergence:

$$M_{\rm ent}^{(w)} = \frac{1}{4\pi G}\oint_S w_{\mathcal{S}}\,(\nu-1)\,\vec{g}_N\cdot d\vec{A} + \frac{1}{4\pi G}\int_V (\nu-1)\,\vec{g}_N\cdot\nabla w_{\mathcal{S}}\,d^3x \tag{28}$$

The first term is the QUMOND result weighted by $w_{\mathcal{S}}$ at the boundary. If the boundary is in the ICM (outside the galaxies), $w_{\mathcal{S}}$ at the boundary is very small ($\ll 1$), which would *reduce* the entanglement mass — the opposite of what we need.

**This is a problem.** If $w_{\mathcal{S}}$ is enormous inside stars and tiny in the ICM, and the Gauss surface is in the ICM, the surface integral is suppressed. The volume integral from the $\nabla w_{\mathcal{S}}$ term contributes only at the boundaries of galaxies, and its sign depends on the direction of $\vec{g}_N$ relative to $\nabla w_{\mathcal{S}}$.

### 5.3 The Resolution: $w_{\mathcal{S}}$ Must Be Normalized Per Unit Mass, Not Per Unit Volume

The issue is that $\mathcal{S}(x) = n_B\,\Gamma_{\rm dec}$ is a volumetric rate. In a cluster, most of the *volume* is ICM, so the volume-weighted average $\mathcal{S}$ is dominated by the ICM value, making $w_{\mathcal{S}} \gg 1$ inside galaxies and $w_{\mathcal{S}} \ll 1$ in the ICM. But the ICM contains most of the baryonic mass, so the Gauss surface integral is heavily suppressed.

The fix: define $w_{\mathcal{S}}$ as a **mass-weighted** quantity that modulates the *effective gravitating mass per baryon*, not the field equation pointwise. Physically, this means: each baryon contributes to the entanglement gravitational field in proportion to its local decoherence rate.

Rewrite Eq. (1) as:

$$\rho_{\rm ent}(x) = \frac{1}{4\pi G}\,\nabla\cdot\!\left[(\nu(y)-1)\,\vec{g}_N^{(w)}(x)\right] \tag{29}$$

where $\vec{g}_N^{(w)}$ is the Newtonian field sourced by the **decoherence-weighted** baryonic density:

$$\nabla^2\Phi_N^{(w)} = 4\pi G\,w_{\mathcal{S}}(x)\,\rho_B(x) \tag{30}$$

and $\vec{g}_N^{(w)} = -\nabla\Phi_N^{(w)}$.

In this formulation:

1. The total field equation is standard QUMOND, but with the baryonic source replaced by $w_{\mathcal{S}}\,\rho_B$
2. Inside galaxies, $w_{\mathcal{S}} \gg 1$: each stellar baryon sources more "Newtonian" field than its bare mass would suggest
3. In the ICM, $w_{\mathcal{S}} \ll 1$: each ICM baryon sources less field
4. The $\nu$ enhancement then operates on this weighted field

### 5.4 But Wait: This Changes the Newtonian Limit

In the high-acceleration regime ($g \gg a_u$), $\nu \to 1$, and the total gravitational field should reduce to the standard Newtonian field sourced by $\rho_B$ (not $w_{\mathcal{S}}\rho_B$). If we replace $\rho_B$ with $w_{\mathcal{S}}\rho_B$ in Poisson's equation, we modify Newtonian gravity in the strong-field regime, which is tightly constrained by solar system tests and stellar dynamics.

**This is a fatal objection to Eq. (30) as written.**

### 5.5 The Correct Formulation: $w_{\mathcal{S}}$ Modulates Only the Entanglement Term

The total gravitational field must satisfy:

$$\vec{g}_{\rm total}(x) = \vec{g}_N(x) + \vec{g}_{\rm ent}(x) \tag{31}$$

where $\vec{g}_N$ is the standard Newtonian field from bare baryonic mass, and $\vec{g}_{\rm ent}$ is the additional entanglement contribution.

In QUMOND, $\vec{g}_{\rm ent}$ is derived from a phantom potential $\Phi_{\rm ph}$:

$$\nabla^2\Phi_{\rm ph} = \nabla\cdot\!\left[(\nu-1)\,\vec{g}_N\right] \tag{32}$$

We modify this — and only this — with the complexity weighting:

$$\boxed{\nabla^2\Phi_{\rm ph} = \nabla\cdot\!\left[w_{\mathcal{S}}(x)\,(\nu(y)-1)\,\vec{g}_N(x)\right]} \tag{33}$$

The total potential is:

$$\Phi_{\rm total} = \Phi_N + \Phi_{\rm ph} \tag{34}$$

In the Newtonian limit ($\nu \to 1$): $\Phi_{\rm ph} \to 0$ regardless of $w_{\mathcal{S}}$. Standard gravity recovered. ✓

In the deep MOND limit ($\nu \gg 1$): $\Phi_{\rm ph}$ is enhanced by $w_{\mathcal{S}}$ in regions of high interaction complexity. ✓

The entanglement density:

$$\rho_{\rm ent}(x) = \frac{1}{4\pi G}\,\nabla^2\Phi_{\rm ph} = \frac{1}{4\pi G}\,\nabla\cdot\!\left[w_{\mathcal{S}}\,(\nu-1)\,\vec{g}_N\right] \tag{35}$$

This is Eq. (1) — but now we understand its role: it modifies only the phantom/entanglement sector, leaving Newtonian gravity intact.

### 5.6 Cluster Mass with $w_{\mathcal{S}}$: The Gauss Integral Revisited

Integrate Eq. (35) over a sphere of radius $R$ enclosing the cluster:

$$M_{\rm ent}(R) = \frac{1}{4\pi G}\oint_{S(R)} w_{\mathcal{S}}\,(\nu-1)\,\vec{g}_N\cdot d\vec{A} \tag{36}$$

At the cluster virial radius, the Gauss surface passes through the ICM where $w_{\mathcal{S}} \ll 1$. This appears to suppress the entanglement mass — the opposite of what we need.

**However**: the volume integral form (via the product rule) reveals the internal structure:

$$M_{\rm ent}(R) = \underbrace{\frac{1}{4\pi G}\int_V w_{\mathcal{S}}\,\nabla\cdot\!\left[(\nu-1)\vec{g}_N\right]d^3x}_{\text{(A) bulk QUMOND, weighted}} + \underbrace{\frac{1}{4\pi G}\int_V (\nu-1)\,\vec{g}_N\cdot\nabla w_{\mathcal{S}}\,d^3x}_{\text{(B) complexity gradient term}} \tag{37}$$

**Term (A)**: This is the standard QUMOND phantom density, weighted by $w_{\mathcal{S}}$. It is large inside galaxies ($w_{\mathcal{S}} \gg 1$) and small in the ICM ($w_{\mathcal{S}} \ll 1$). Since galaxies occupy a tiny fraction of the cluster volume but $w_{\mathcal{S}}$ is enormous there, the net contribution depends on the volume-integrated product $w_{\mathcal{S}} \times \rho_{\rm ph}^{\rm (QUMOND)}$.

**Term (B)**: This is non-zero only where $w_{\mathcal{S}}$ varies — i.e., at the boundaries of galaxies (stellar surfaces, galaxy-ICM interfaces). The gradient $\nabla w_{\mathcal{S}}$ points outward from galaxies (from high-$w$ to low-$w$), and $\vec{g}_N$ points inward (toward the cluster center). Their dot product is **negative** at the outward-facing side of each galaxy and **positive** at the inward-facing side.

For a galaxy at position $\vec{r}_i$ relative to the cluster center, with the cluster's gravitational field $\vec{g}_N$ pointing toward the center:

- On the side of the galaxy facing the cluster center: $\vec{g}_N \cdot \nabla w_{\mathcal{S}} > 0$ (both point roughly opposite, but $\nabla w$ points outward from galaxy, $g_N$ points toward center — the product depends on angle)
- Integrated over the galaxy boundary, the net contribution is:

$$\Delta M_{\rm ent}^{(i)} \sim \frac{(\nu-1)\,|\vec{g}_N(r_i)|}{4\pi G}\;\Delta w_{\mathcal{S}}\;\times A_{\rm gal} \tag{38}$$

where $\Delta w_{\mathcal{S}} = w_{\mathcal{S}}^{\rm (inside)} - w_{\mathcal{S}}^{\rm (outside)}$ and $A_{\rm gal}$ is the galaxy's effective surface area.

This is difficult to evaluate in general because of the geometric complexity. A numerical computation on a grid is needed (Fix 4 from the roadmap).

### 5.7 A Cleaner Approach: The Effective Baryon Fraction

Rather than evaluating the Gauss integral analytically, consider the physical content.

The $w_{\mathcal{S}}$ modification means that entanglement gravity is sourced preferentially by high-decoherence-rate baryons. In the context of the total cluster, this is equivalent to saying that the **effective baryonic mass** for entanglement sourcing is:

$$M_B^{\rm (eff)} = \int w_{\mathcal{S}}(x)\,\rho_B(x)\,d^3x = \sum_k w_{\mathcal{S}}^{(k)}\,M_k \tag{39}$$

where the sum is over components $k$ (galaxies, ICM, etc.). This effective mass enters the QUMOND calculation in place of the bare baryonic mass, but only in the phantom sector.

For the Bullet Cluster, the bare baryonic masses are:

- Galaxies (stars + ISM): $M_{\rm gal} \sim 0.15\,M_{\rm bary}$ (15% of baryonic mass)
- ICM gas: $M_{\rm gas} \sim 0.85\,M_{\rm bary}$ (85% of baryonic mass)

With the $w_{\mathcal{S}}$ weighting (using the ratio from Eq. 24, but we need to be careful about normalization):

The normalization $\bar{\Gamma}$ is the mass-weighted mean, so:

$$\bar{\Gamma} = f_{\rm gal}\,\Gamma_{\rm gal} + f_{\rm gas}\,\Gamma_{\rm gas} \approx f_{\rm gal}\,\Gamma_{\rm gal} \tag{40}$$

since $\Gamma_{\rm gal} \gg \Gamma_{\rm gas}$. Then:

$$w_{\mathcal{S}}^{\rm (gal)} = \frac{\Gamma_{\rm gal}}{\bar{\Gamma}} = \frac{\Gamma_{\rm gal}}{f_{\rm gal}\,\Gamma_{\rm gal}} = \frac{1}{f_{\rm gal}} \approx 6.7 \tag{41}$$

$$w_{\mathcal{S}}^{\rm (gas)} = \frac{\Gamma_{\rm gas}}{\bar{\Gamma}} = \frac{\Gamma_{\rm gas}}{f_{\rm gal}\,\Gamma_{\rm gal}} \approx \frac{10^{-13}}{0.15 \times 10^{16}} = 7 \times 10^{-29} \approx 0 \tag{42}$$

The effective baryonic mass:

$$M_B^{\rm (eff)} = w_{\mathcal{S}}^{\rm (gal)}\,M_{\rm gal} + w_{\mathcal{S}}^{\rm (gas)}\,M_{\rm gas} \approx \frac{1}{f_{\rm gal}}\,M_{\rm gal} = M_{\rm bary} \tag{43}$$

Wait — the effective mass just equals the total baryonic mass. The $w_{\mathcal{S}}$ weighting, with this normalization, simply redistributes which baryons matter but preserves the total.

**This means $w_{\mathcal{S}}$ cannot close the cluster mass gap through amplitude enhancement alone.** It can only redirect the spatial distribution of the entanglement density — which is exactly what we need for the Bullet offset, but not for the missing mass.

### 5.8 The Honest Conclusion on the Cluster Mass

The cluster mass discrepancy (factor ~2.5–3 deficit relative to observations) is **not resolved** by the $w_{\mathcal{S}}$ modification. The $w_{\mathcal{S}}$ weighting changes *where* the entanglement mass is located (near galaxies rather than gas), but not *how much* there is in total — because the mass-weighted normalization preserves $M_B^{\rm (eff)} = M_{\rm bary}$.

This is the same deficit that all MOND-type theories face at the cluster scale.

**Possible resolutions (to be explored in future work)**:

**(a) Additional hot baryons.** There may be undetected baryonic mass in clusters — warm-hot intergalactic medium (WHIM) filaments, cool gas, or faint stellar populations — that would increase $M_{\rm bary}$ and close the gap. Observations suggest clusters may be "missing" 10–30% of their expected baryonic content.

**(b) The neutrino contribution.** Massive neutrinos ($\sum m_\nu \sim 0.06$–$0.3$ eV) form a hot dark matter component that concentrates in cluster potentials. At the cluster scale, the neutrino mass could contribute an additional factor of ~1.5–2 to the gravitating mass. This is a known effect in both ΛCDM and MOND contexts (Angus et al. 2008, Haslbauer et al. 2020).

**(c) A modified normalization.** If $\bar{\Gamma}$ is normalized not by mass but by volume, or by the Bekenstein-Hawking entropy of the system, the effective mass is no longer conserved and $w_{\mathcal{S}}$ can produce a net enhancement. This would require a physical justification for the alternative normalization.

**(d) The $\nu$ function receives cluster-scale corrections.** The "simple" interpolation $\nu(y) = (1+\sqrt{1+4/y})/2$ is phenomenological. The true interpolation derived from de Sitter thermodynamics may have a steeper behavior at $y \sim 0.1$–$1$ (the cluster regime) that produces more entanglement density. This connects to Paper 2 (the theoretical derivation of $a_u$).

**(e) Multi-scale entanglement.** The framework as written considers entanglement between the system and the de Sitter horizon (a single boundary). In a cluster, there may be additional entanglement boundaries — the cluster's own quasi-horizon (the surface beyond which baryons are not gravitationally bound). Entanglement entropy at this intermediate boundary could provide the missing factor. This is speculative but connects to the hierarchical structure of the theory.

---

## 6. Summary: What $\mathcal{S}$ Does and Does Not Do

### What it does:

| Result | Mechanism |
|--------|-----------|
| Bullet Cluster offset (lensing follows galaxies) | $w_{\mathcal{S}}^{\rm (gal)}/w_{\mathcal{S}}^{\rm (gas)} \sim 10^{27}$ — overwhelming preference for galaxy regions |
| Relaxed galaxy recovery | $w_{\mathcal{S}} \approx 1$ throughout an isolated galaxy — SPARC fits undisturbed |
| Spatial redistribution of entanglement density | $\rho_{\rm ent}$ concentrated near stellar-dominated regions |
| Falsifiable: depends on baryon type | Different $w_{\mathcal{S}}$ for gas-rich vs. star-rich systems at same total mass |
| Computable from standard astrophysics | Uses Spitzer collision frequencies, nuclear reaction rates |

### What it does not do:

| Problem | Status |
|---------|--------|
| Cluster mass discrepancy (factor ~2.5) | **Not resolved** by $w_{\mathcal{S}}$ with mass-weighted normalization |
| Hubble tension | Connection via entropy growth rate is suggestive but depends on resolving the cluster mass |
| CMB acoustic peaks | Not addressed in this paper (requires Boltzmann code integration — Paper 2/Holographic Grammar territory) |

### The honest statement for the paper:

*The interaction complexity source function $\mathcal{S}(x)$, defined as the volumetric quantum decoherence rate from all interaction channels, provides a rigorous, computable mechanism for concentrating the entanglement gravitational density near stellar-dominated regions in merging clusters. This resolves the Bullet Cluster spatial offset without introducing free parameters. However, the total entanglement mass at the cluster scale remains $M_{\rm ent} = (\bar{\nu}-1)M_{\rm bary}$, which is a factor of ~2.5 below the observed mass-to-baryon ratio. The cluster mass discrepancy is an open problem shared with all modified-gravity approaches and may require additional physics (massive neutrinos, undetected baryons, or modified boundary conditions at the cluster scale) for its resolution.*

---

## 7. The Field Equation — Final Form

The complete framework for Paper 3:

**Newtonian sector** (unchanged):
$$\nabla^2\Phi_N = 4\pi G\,\rho_B \tag{44}$$

**Entanglement (phantom) sector**:
$$\nabla^2\Phi_{\rm ph} = \nabla\cdot\!\left[w_{\mathcal{S}}(x)\;(\nu(y)-1)\;\vec{g}_N(x)\right] \tag{45}$$

where:
$$y(x) = \frac{|\vec{g}_N(x)|}{a_u}, \qquad a_u = \frac{cH_0}{2\pi} \tag{46}$$

$$\nu(y) = \frac{1}{2}\left(1 + \sqrt{1 + \frac{4}{y}}\right) \tag{47}$$

$$w_{\mathcal{S}}(x) = \frac{\Gamma_{\rm dec}(x)}{\bar{\Gamma}_{\rm dec}}, \qquad \Gamma_{\rm dec}(x) = \sum_\alpha n_\alpha(x)\,\langle\sigma_\alpha v\rangle(x) \tag{48}$$

**Total gravitational potential**:
$$\Phi_{\rm total} = \Phi_N + \Phi_{\rm ph} \tag{49}$$

**Entanglement density** (for lensing):
$$\rho_{\rm ent}(x) = \frac{1}{4\pi G}\,\nabla^2\Phi_{\rm ph}(x) \tag{50}$$

**Lensing convergence**:
$$\kappa(\vec{\theta}) = \frac{1}{\Sigma_{\rm cr}}\int\!\left[\rho_B + \rho_{\rm ent}\right]dz \tag{51}$$

### Parameters:
- $H_0$: measured (Planck 2018)
- $a_u$: derived from $H_0$ (Eq. 46)
- $\nu(y)$: fixed functional form (Eq. 47)
- $w_{\mathcal{S}}(x)$: computed from known astrophysics (Spitzer collision frequencies, nuclear rates)
- **Free parameters: zero**

### Limits:
- Isolated galaxy, relaxed: $w_{\mathcal{S}} \approx 1$ → standard QUMOND → SPARC fits ($\chi^2/\nu = 1.45$) ✓
- High acceleration ($g \gg a_u$): $\nu \to 1$, $\Phi_{\rm ph} \to 0$ → Newtonian gravity ✓
- Merging cluster: $w_{\mathcal{S}}$ redistributes $\rho_{\rm ent}$ toward galaxies → Bullet offset ✓
- Cluster total mass: $M_{\rm ent} = (\bar{\nu}-1)\,M_{\rm bary}$ → factor ~2.5 deficit (open problem) ✗
