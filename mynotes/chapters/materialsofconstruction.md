---
title: "Materials of Construction"
author: "PE Study Guide"
date: "2025"
---

# Materials of Construction

## Preliminaries: The Mechanics-of-Materials Toolbox
Before tackling stress-strain diagrams and material selection, we collect the continuum-mechanics definitions and conventions used throughout this chapter. Every later derivation rests on these primitives.

### Force, Stress, and the Internal-Force Hypothesis

```{note}
**The Concept of Stress**
A body in equilibrium under external loads contains **internal forces** that resist deformation. If we make a virtual cut through the body, the internal force per unit area of the cut is the **stress vector** (or traction). For a uniform tensile load applied to a slender prismatic bar, the stress is normal (perpendicular) to the cross-section and uniform across it.

For more general loadings, the stress is a tensor with nine components $\sigma_{ij}$: three normal stresses on each face plus six shear components (related in pairs by moment equilibrium, leaving six independent values). For tensile-test specimens in pure tension along one axis, only one component is nonzero, and we drop the indices and write simply $\sigma$.
```


```{important}
**Definitions**
**Engineering (nominal) stress:**

$$
\sigma = \frac{F}{A_0}
$$

$F$ is the instantaneous applied force; $A_0$ is the *original*, undeformed cross-sectional area. Units: Pa (N/m$^2$), MPa, psi, ksi.

**Engineering (nominal) strain:**

$$
\varepsilon = \frac{\Delta L}{L_0} = \frac{L_i - L_0}{L_0}
$$

$L_0$ is the original gauge length; $L_i$ is the instantaneous length under load; $\Delta L = L_i - L_0$ is the elongation. Dimensionless (m/m, often expressed as “in/in” or as a percent).
```


### Why Engineering vs. True — and Why It Matters

```{note}
**The Engineering–True Distinction**
**Engineering stress** uses $A_0$ (original area). **True stress** uses $A_i$ (instantaneous, deformed area):

$$
\sigma_{true} = \frac{F}{A_i}
$$

Engineering and true stress are identical at zero strain and diverge as the specimen deforms. Up to the onset of necking, the relationship is approximately

$$
\sigma_{true} = \sigma(1 + \varepsilon),   \varepsilon_{true} = \ln(1 + \varepsilon)
$$

After necking begins, the specimen's cross-section is no longer uniform and these formulas break down.

**Design implication.** Engineering stress is used everywhere in design codes (ASME, ASTM) because the original area is what the designer specifies. True stress matters in metal-forming and in research on deformation mechanisms but is rarely used in chemical-plant equipment design. Throughout this chapter, “stress” without qualifier means engineering stress.
```


### Unit Conversions and Practical Magnitudes

```{tip}
**Stress Unit Conversions and Reference Magnitudes**
- $1MPa = 1N/mm^2 = 10^6Pa = 145psi$

- $1GPa = 10^9Pa = 145{,}000psi = 145ksi$

- $1ksi = 1{,}000psi \approx 6.895MPa$

Useful reference magnitudes:


- Atmospheric pressure $\approx 0.1$ MPa or 14.7 psi.

- Yield strength of mild structural steel: $\sim$250 MPa (36 ksi).

- Ultimate tensile strength of high-strength steel: 600–1500 MPa.

- Young's modulus of steel: $E = 207$ GPa (30$\times 10^6$ psi).

- Tensile strength of polymer plastics: 30–80 MPa.
```


### The Tensile Test — Standardized Procedure

```{note}
**ASTM E8 Tensile Test**
The numbers populating the materials handbooks come from a standardized tensile test:


- A carefully-machined cylindrical or flat test specimen is prepared with a reduced “gauge section” between two larger ends (the “shoulders”) that fit into the testing machine grips.

- Standard specimen geometry (ASTM E8/E8M): 0.505-in or 12.5-mm diameter round; 2-in or 50-mm gauge length. Other standards (ISO 6892, EN 10002) prescribe slightly different geometries.

- The specimen is loaded in tension on a Universal Testing Machine (UTM) at a controlled strain rate (typically $10^{-4}$ to $10^{-2}$ s$^{-1}$ for quasi-static tests).

- Force is measured by a load cell; extension by an extensometer attached to the gauge section. Stress is computed from force/$A_0$; strain from extension/$L_0$.

- The recorded $\sigma$–$\varepsilon$ curve is the engineering stress-strain diagram.

Adherence to the ASTM standard is what allows two different labs to obtain comparable numbers. Deviations (different rate, different geometry, different temperature) shift the curve and are routine sources of disagreement between datasets.
```


## Engineering Stress and Strain — Computational Practice
With definitions in hand, we work through the algebra of computing engineering stress and strain from raw tensile-test measurements. The PE exam will give you force, geometry, and gauge length and expect you to produce $\sigma$ and $\varepsilon$ with correct units carried through every step.

### The Computational Recipe

```{important}
For tensile or compressive uniaxial loading:

$$

$$

\begin{align}


\sigma &= \frac{F}{A_0} = \frac{F}{\pi (d_0/2)^2}  (round cross-section)
\sigma &= \frac{F}{A_0} = \frac{F}{w_0  t_0}  (rectangular cross-section, width w, thickness t)
\varepsilon &= \frac{L_i - L_0}{L_0}
\end{align}

$$

$$

Units: $F$ in N gives $\sigma$ in Pa when $A_0$ is in m$^2$. To get MPa, either divide the Pa result by $10^6$ or use $A_0$ in mm$^2$ (then Pa·mm$^2$/m$^2 = $ MPa directly).

The common-units shortcut: $\sigma[MPa] = F[N] / A_0[mm^2]$.
```


### Worked Example: Round Tensile Specimen

```{prf:example} Stress and Strain on a Round Bar
A round metal specimen of original diameter $d_0 = 9.6$ mm and original gauge length $L_0 = 400$ mm is subjected to a tensile force $F = 18{,}000$ N. The deformed gauge length under load is $L_i = 401.5$ mm. Compute (a) the engineering stress, (b) the engineering strain, (c) decide whether the specimen is still in the elastic region given that the material's yield strength is 250 MPa.
```


```{dropdown} Solution Steps
- **Original cross-sectional area.**

$$
A_0 = \pi(\frac{d_0}{2})^2 = \pi(\frac{9.6 \times 10^{-3}}{2})^2 = \pi (4.8 \times 10^{-3})^2
$$

    Step the algebra: $(4.8 \times 10^{-3})^2 = 23.04 \times 10^{-6} = 2.304 \times 10^{-5}$ m$^2$.

$$
A_0 = \pi \times 2.304 \times 10^{-5} = 7.238 \times 10^{-5}m^2
$$

- **Engineering stress.**

$$
\sigma = \frac{F}{A_0} = \frac{18{,}000N}{7.238 \times 10^{-5}m^2} = 2.488 \times 10^{8}Pa = 248.8MPa \approx 249MPa
$$

    Quick double-check via the mm$^2$ shortcut: $A_0[mm^2] = \pi (4.8)^2 = 72.38$ mm$^2$. $\sigma = 18{,}000/72.38 = 248.7$ MPa. \checkmark Same answer.


- **Engineering strain.**

$$
\varepsilon = \frac{L_i - L_0}{L_0} = \frac{401.5 - 400.0}{400.0} = \frac{1.5}{400.0} = 0.00375
$$

    Dimensionless. Often expressed as 0.375%.


- **Elastic-region check.** The applied stress 249 MPa is just below the yield strength 250 MPa — the specimen is at the very edge of elastic behavior. Any small additional load would induce permanent (plastic) deformation. A safety factor for design (typically $\sigma_{design} = \sigma_y / N$ with $N = 2$–$4$) would have flagged this load level long before yield. The strain $\varepsilon = 0.00375$ is also consistent with elastic behavior in steel ($\varepsilon_y \approx \sigma_y / E = 250/207000 \approx 0.0012$ in pure elastic; here at 0.00375 the specimen has crossed slightly into the plastic regime if we trust the 250 MPa yield estimate). The numbers sit on the boundary.


- **Verification.** 249 MPa is a plausible value for a moderately-loaded steel specimen. The strain $3.75 \times 10^{-3}$ is small (typical of elastic-region tensile tests); a strain in the percent range would indicate plastic deformation. The fact that $\varepsilon < 0.01$ supports the conclusion that the specimen is still near its elastic limit.
```


### Worked Example: Rectangular Cross-Section

```{prf:example} Flat Bar in Tension
A flat steel bar with width $w_0 = 25$ mm and thickness $t_0 = 6$ mm is gripped over a gauge length $L_0 = 200$ mm. A force of 45 kN is applied. The gauge length extends by 0.29 mm. Compute stress and strain.
```


```{dropdown} Solution Steps
- **Cross-sectional area.**

$$
A_0 = w_0 \times t_0 = 25 \times 6 = 150mm^2 = 1.5 \times 10^{-4}m^2
$$

- **Stress (mm$^2$ shortcut).**

$$
\sigma = \frac{F}{A_0} = \frac{45{,}000N}{150mm^2} = 300MPa
$$

- **Strain.**

$$
\varepsilon = \frac{0.29}{200} = 1.45 \times 10^{-3}
$$

- **Hooke's law cross-check.** If the material is steel ($E = 207$ GPa = 207{,}000 MPa) and elastic, $\sigma = E\varepsilon$ predicts $\sigma = 207{,}000 \times 1.45 \times 10^{-3} = 300$ MPa. \checkmark Excellent agreement — the elastic-region assumption is consistent.

- **Verification.** Both $\sigma$ and $\varepsilon$ are reasonable for a moderately-loaded steel sample. The agreement between the measured $\sigma$ and the Hooke's-law prediction from $\varepsilon$ tells us the test is in the linear-elastic region and the assumed modulus is correct.
```


### Compression and Shear (Brief)

```{note}
**Beyond Pure Tension**
**Compression:** same formulas with $F$ negative (or, conventionally, sign-flipped so $\sigma_{comp} > 0$). For ductile metals, compressive yield strength is approximately equal to tensile yield strength (the von Mises criterion is symmetric). For brittle materials (concrete, ceramics, cast iron), compressive strength is typically 5–10$\times$ tensile strength.

**Shear:** a tangential force on a surface gives shear stress $\tau = F/A$ and shear strain $\gamma = \Delta x / h$ (relative displacement over height). For metals, shear modulus $G = E / [2(1 + \nu)]$ where $\nu$ is Poisson's ratio (typically 0.3 for steel). Shear yield strength $\tau_y \approx \sigma_y / \sqrt{3} \approx 0.577\sigma_y$ (von Mises) or $\tau_y \approx \sigma_y/2$ (Tresca).
```


```{note}
**Exam Tips — Stress and Strain Computation**
- Use $A_0$, the *original* area, for engineering stress. Always.

- Round-bar area: $A_0 = \pi (d_0/2)^2 = \pi d_0^2/4$. Rectangular: $A_0 = w_0 t_0$.

- Carry units explicitly. The mm$^2$ + N shortcut delivers MPa directly — the most efficient unit choice for the PE exam.

- Engineering strain is dimensionless. Don't multiply by 100 unless you're stating a percent.

- Hooke's-law cross-check ($\sigma = E\varepsilon$) is the fastest sanity check on any elastic-region calculation.
```


## The Engineering Stress-Strain Diagram
The tensile stress-strain curve is the single most important plot in materials engineering. A handful of points read from it define every mechanical property a designer needs: elastic stiffness, yield strength, ultimate tensile strength, fracture strain, toughness, and resilience. We walk the curve from origin to failure.

### The Five Critical Points on a Ductile-Metal Curve

```{note}
**Walking the Curve**
Starting at the origin and following the curve, you encounter (in order):


- **Linear-elastic region.** A straight line with slope $E$ (Young's modulus). Unloading retraces the same line — no permanent deformation. Bonds stretch elastically.

- **Proportional limit.** The highest stress at which strict linearity holds. Slightly below the yield point. Rarely tabulated separately.

- **Yield point (0.2% offset yield strength).** The conventional onset of plastic (permanent) deformation. By convention: draw a line parallel to the elastic slope, offset to the right by $\varepsilon = 0.002$ (0.2%); the intersection with the curve is $\sigma_y$.

- **Ultimate tensile strength (UTS).** The peak of the engineering stress-strain curve. Past this point the specimen *necks* (a local cross-section shrinks rapidly), the engineering stress falls even though the true stress continues to rise.

- **Fracture.** Bonds break; specimen separates. The fracture strain $\varepsilon_f$ measures ductility.
```


### Elastic Region: Hooke's Law and Modulus of Elasticity

```{important}
**Hooke's Law in 1-D**

$$
\sigma = E\varepsilon  (elastic region only)
$$

$E$ is the **Young's modulus** or **modulus of elasticity**, with units of stress (GPa or psi). It is the slope of the linear portion of the stress-strain curve. It quantifies a material's *stiffness* (resistance to elastic deformation) and is largely set by interatomic bond strength — it varies relatively little with alloying or processing.

Typical values (room temperature):


- Steel: $E = 200$–210 GPa. Nearly independent of carbon content, heat treatment.

- Aluminum: $E = 70$ GPa.

- Copper: $E = 110$ GPa.

- Titanium: $E = 110$ GPa.

- Concrete: $E = 25$–30 GPa.

- Wood (along grain): $E = 10$–15 GPa.

- Polymers: $E = 1$–3 GPa.
```


### The Microscopic Picture of Elastic vs. Plastic Deformation

```{note}
**Why Elastic Is Reversible and Plastic Is Not**
At the atomic level, elastic deformation stretches the bonds between atoms while preserving their topological arrangement. Each pair of atoms has an equilibrium separation; small displacements from this equilibrium store energy linearly in the displacement (the spring approximation, $F = -k\Delta x$). Releasing the load returns each atom to its equilibrium position — the deformation is fully recovered.

Plastic deformation, in contrast, involves the *collective motion of crystallographic defects* called **dislocations**. A dislocation is a line defect that lets a half-plane of atoms slip past the lattice by breaking and reforming bonds one row at a time — like sliding a heavy rug by walking a wrinkle across it rather than dragging the whole rug. Once dislocations move, the atomic arrangement is permanently altered; releasing the load doesn't undo the slip.

The transition from elastic to plastic at the yield point occurs because dislocation motion becomes thermodynamically favorable at that critical stress.
```


### The 0.2% Offset Yield Strength Definition

```{note}
**Why “0.2% Offset”?**
For some materials (low-carbon mild steel) the stress-strain curve has a clear “yield point” (an upper and lower yield), a horizontal plateau, and obvious onset of plastic flow. For most metals, the transition from elastic to plastic is gradual — there is no sharp “corner” on the curve.

The 0.2% offset convention solves this by defining a reproducible yield strength: draw a line through the strain axis at $\varepsilon = 0.002$ with slope $E$; the intersection with the stress-strain curve is $\sigma_y$. The 0.2% value is arbitrary but standardized worldwide. Specifying any other offset (0.1%, 0.5%) shifts the reported yield strength somewhat.

Equivalently: $\sigma_y$ is the stress at which, if the specimen were unloaded, it would have an in-built 0.2% permanent (plastic) strain.
```


### Unloading From the Plastic Region

```{note}
If you load past the yield point into the plastic region and then release the load, you do not retrace the loading curve. Instead, the unloading line is *parallel to the elastic slope*. The horizontal distance from this unloading line to the strain axis is the **plastic strain** (permanent set) locked into the specimen; the recovered portion (along the unloading line) is the **elastic strain**, which equals $\sigma_{unload} / E$.

$$
\varepsilon_{total} = \varepsilon_p + \varepsilon_e,   \varepsilon_e = \sigma/E,   \varepsilon_p = \varepsilon_{total} - \sigma/E
$$

**Implication for material properties.** If a specimen is loaded to $\sigma_1$ in the plastic region, then unloaded, then reloaded, the new stress-strain curve follows the elastic line back up to $\sigma_1$, then continues along the original curve. The new effective yield strength is now $\sigma_1$ (work-hardening). The total ductility (strain to fracture) is reduced by the consumed plastic strain.
```


### Necking and Ultimate Tensile Strength

```{note}
**Necking: The Geometric Instability**
For a ductile metal in tension, the engineering stress rises as the specimen work-hardens, reaching a peak at the UTS. Past the peak, work-hardening can no longer keep pace with the geometric softening that comes from area reduction — some region of the gauge section begins to thin faster than the rest, concentrating strain locally. This is the **necking instability**.

Mathematically, the condition for the onset of necking (the Consid\`ere criterion) is

$$
\frac{d\sigma_{true}}{d\varepsilon_{true}} = \sigma_{true}
$$

at which point the engineering stress reaches its maximum (the UTS).

After necking, the engineering stress drops (because the area, defined as $A_0$, hasn't changed but the load required to extend the necked region decreases). The true stress continues to rise. The specimen elongates almost exclusively in the neck region until fracture.
```


### Reading the Curve — All Properties Together

```{tip}
**Mechanical Properties From the Stress-Strain Curve**
- **Modulus of elasticity $E$** = slope of the elastic line.

- **Yield strength $\sigma_y$** = stress at 0.2% offset. Onset of plastic deformation.

- **Ultimate tensile strength (UTS, $\sigma_u$)** = peak of the engineering curve. Maximum sustainable engineering stress.

- **Fracture strength $\sigma_f$** = stress at the failure point (engineering, on the falling part of the curve).

- **Percent elongation at fracture** $= \varepsilon_f \times 100$. Ductility measure.

- **Modulus of resilience $U_r$** = elastic strain energy per unit volume:

$$
U_r = \int_0^{\varepsilon_y} \sigmad\varepsilon = \frac{1}{2}\sigma_y \varepsilon_y = \frac{\sigma_y^2}{2E}
$$

- **Modulus of toughness** = total area under the stress-strain curve up to fracture. Total energy absorbed per unit volume; a combined strength + ductility measure.
```


### Worked Example: Reading All Properties from a Curve

```{prf:example} Property Extraction from a Tensile Test
A steel specimen produces the following readings:


- Stress at $\varepsilon = 0.001$ (elastic region): $\sigma = 200$ MPa.

- Yield (0.2% offset): $\sigma_y = 415$ MPa.

- Peak engineering stress: $\sigma_u = 500$ MPa at $\varepsilon = 0.10$.

- Fracture: $\sigma_f = 380$ MPa at $\varepsilon_f = 0.18$.

Compute $E$, the modulus of resilience, the modulus of toughness (approximate), the elastic and plastic strain at the fracture point.
```


```{dropdown} Solution Steps
- **Young's modulus from the elastic-region point.**

$$
E = \frac{\sigma}{\varepsilon} = \frac{200MPa}{0.001} = 200{,}000MPa = 200GPa
$$

    Consistent with typical steel.

- **Yield strain (elastic limit).**

$$
\varepsilon_y = \frac{\sigma_y}{E} = \frac{415}{200{,}000} = 2.08 \times 10^{-3}
$$

- **Modulus of resilience.**

$$
U_r = \frac{\sigma_y^2}{2E} = \frac{(415)^2}{2 \times 200{,}000} = \frac{172{,}225}{400{,}000} = 0.431MPa = 0.431MJ/m^3
$$

    Recall that MPa = MJ/m$^3$ when interpreting strain-energy density.


- **Modulus of toughness (approximate, triangle + rectangle).** A reasonable approximation treats the curve as an elastic triangle plus a plastic rectangle from $\sigma_y$ to $\sigma_u$ over the plastic strain range. Use the mean stress $(\sigma_y + \sigma_u)/2 = (415 + 500)/2 = 457.5$ MPa across plastic strain $\varepsilon_p \approx 0.18 - 0.002 = 0.178$.

$$
U_T \approx U_r + 457.5 \times 0.178 = 0.43 + 81.4 = 81.8MJ/m^3
$$

    Toughness is dominated by the plastic-region area; resilience is a tiny fraction. This is why ductile materials are so much tougher than brittle ones — the plastic region is where energy is absorbed.


- **Elastic strain at fracture.**

$$
\varepsilon_{e,frac} = \frac{\sigma_f}{E} = \frac{380}{200{,}000} = 1.90 \times 10^{-3}
$$

```


```{dropdown} Solution Steps
- **Plastic strain at fracture.**

$$
\varepsilon_{p,frac} = \varepsilon_f - \varepsilon_{e,frac} = 0.18 - 0.00190 = 0.178 = 17.8%
$$

    The specimen's permanent elongation if recovered just before fracture would be 17.8%. This is the value typically quoted as “% elongation at fracture” on a material data sheet.

- **Ductility interpretation.** 17.8% elongation places this material firmly in the ductile-metal category. Brittle materials fail at $\varepsilon_f < 1%$; ductile metals are typically 10–40%; very ductile (annealed copper, pure aluminum) can reach 50–60%.

- **Verification.** The UTS (500 MPa) exceeds the fracture stress (380 MPa) — consistent with engineering-stress-curve behavior past necking. The yield strain $2.1 \times 10^{-3}$ matches the textbook value for steel ($\sim$0.2%). The strain-energy interpretation (MPa = MJ/m$^3$) is dimensionally sound: Pa $\times$ m/m = J/m$^3$.
```


### Ductile vs. Brittle Behavior

```{note}
**Two Failure Modes**
- **Ductile fracture:** extensive plastic deformation precedes failure; the specimen necks and elongates significantly before separating. Cross-section reduces dramatically at the failure point. Fracture surface shows characteristic “cup-and-cone” geometry with microvoid coalescence. Energy absorbed (toughness) is high.

- **Brittle fracture:** little or no plastic deformation; the specimen breaks without warning at low strain. Fracture surface is flat, mirror-like, often shows chevron markings pointing back to the origin. Energy absorbed is low.

The same material can switch from ductile to brittle when:


- Temperature drops below the ductile-to-brittle transition temperature (DBTT). BCC steels show this transition; FCC metals (austenitic SS, Cu, Al) do not.

- Strain rate is very high (impact loading).

- A stress concentrator (notch, crack, weld defect) is present.

- The state of stress is triaxial (constrains plastic flow).

The 1943 SS *Schenectady* catastrophe (a Liberty ship that fractured in half overnight in cold harbor) is the canonical example of unanticipated ductile-to-brittle transition.
```


```{note}
**Exam Tips — Stress-Strain Curve Reading**
- Yield strength is the design property against permanent deformation. UTS is the property against fracture-limited design. They are different.

- Modulus of elasticity $E$ is the slope of the elastic line — not the yield strength divided by 0.002 (which differs by 0.2%).

- The 0.2% offset construction is a graphical convention; in practice the offset is small and the offset and proportional-limit yield strengths are close.

- For ductile metals, compressive yield $\approx$ tensile yield. For brittle materials, compressive strength is much larger than tensile.

- Resilience $\propto \sigma_y^2/E$. Toughness $\propto$ area under the whole curve — ductile materials excel.
```


## Yield Criteria for Multi-Axial Loading
A real pressure vessel sees biaxial or triaxial stress states, not pure uniaxial tension. To predict yielding from a uniaxial tensile-test yield strength, engineers use yield criteria that project the multi-axial stress state onto an equivalent uniaxial stress.

### Principal Stresses

```{note}
At any point in a loaded body, the stress tensor can be diagonalized; the three eigenvalues are the **principal stresses** $\sigma_1 \geq \sigma_2 \geq \sigma_3$ along three mutually perpendicular principal directions. On these directions, the shear stresses vanish. The maximum shear stress at the point is

$$
\tau_{\max} = \frac{\sigma_1 - \sigma_3}{2}
$$

(half the difference between the algebraically largest and smallest principal stress).

For a thin-walled pressure vessel, the principal stresses are well known:


- Hoop: $\sigma_h = PR/t$

- Longitudinal: $\sigma_\ell = PR/(2t)$

- Radial: $\sigma_r \approx 0$ on the outer wall, $-P$ on the inner wall (small compared to hoop)

So for a cylindrical pressure vessel, $\sigma_1 = \sigma_h, \sigma_2 = \sigma_\ell, \sigma_3 \approx 0$ (or $-P$).
```


### Two Common Yield Criteria

```{important}
**Tresca (Maximum Shear Stress) Criterion**
Yield occurs when the maximum shear stress reaches the yield shear stress measured in uniaxial tension:

$$
\tau_{\max} = \frac{\sigma_1 - \sigma_3}{2} = \frac{\sigma_y}{2}  \Longleftrightarrow  \sigma_1 - \sigma_3 = \sigma_y
$$

Conservative; gives the safest design but slightly under-predicts yield strength.
```


```{important}
**von Mises (Distortion Energy) Criterion**
Yield occurs when the equivalent (von Mises) stress reaches the uniaxial yield strength:

$$
\sigma_{vM} = \sqrt{\frac{1}{2}[(\sigma_1 - \sigma_2)^2 + (\sigma_2 - \sigma_3)^2 + (\sigma_3 - \sigma_1)^2]} = \sigma_y
$$

Slightly less conservative than Tresca; more accurate for most ductile metals. Used in modern finite-element codes by default.

For pure shear ($\sigma_1 = \tau, \sigma_2 = 0, \sigma_3 = -\tau$), Tresca gives $\tau_y = \sigma_y/2$; von Mises gives $\tau_y = \sigma_y/\sqrt{3} = 0.577\sigma_y$. The two differ by about 15% in pure shear; closer in other states.
```


### Worked Example: Yielding of a Pressure Vessel

```{prf:example} When Does the Vessel Wall Yield?
A thin-walled cylindrical pressure vessel has ID = 600 mm, wall thickness 10 mm. The material has $\sigma_y = 250$ MPa. Find the internal pressure at which yielding begins, using (a) Tresca and (b) von Mises criteria.
```


```{dropdown} Solution Steps
- **Compute the principal stresses in terms of $P$.** $R = 300$ mm, $t = 10$ mm.

$$
\sigma_h = \frac{PR}{t} = \frac{P \times 300}{10} = 30 P,   \sigma_\ell = \frac{PR}{2t} = 15 P,   \sigma_r \approx 0
$$

    (with $P$ in MPa and $\sigma$ in MPa). So $\sigma_1 = 30P, \sigma_2 = 15P, \sigma_3 = 0$.


- **(a) Tresca criterion.**

$$
\sigma_1 - \sigma_3 = 30P - 0 = 30P = \sigma_y = 250 \Longrightarrow P_Tresca = \frac{250}{30} = 8.33MPa
$$

- **(b) von Mises criterion.**

$$
\sigma_{vM}^2 = \tfrac{1}{2}[(30P - 15P)^2 + (15P - 0)^2 + (0 - 30P)^2] = \tfrac{1}{2}[225 + 225 + 900]P^2 = 675 P^2
$$

$$
\sigma_{vM} = P\sqrt{675} = 25.98 P = \sigma_y = 250 \Longrightarrow P_vM = \frac{250}{25.98} = 9.62MPa
$$

- **Comparison.** The von Mises criterion allows a 15% higher pressure (9.62 vs. 8.33 MPa). This is the classic 15% gap between the two yield criteria, with Tresca being the conservative bound.


- **Engineering choice.** ASME Section VIII Division 1 implicitly uses a maximum-stress criterion (closer to Tresca with a safety factor). Modern pressure-vessel codes (Sec. VIII Div. 2, EN 13445) and finite-element analyses use von Mises. The 15% difference matters when economic considerations push wall thickness aggressively.


- **Verification.** Both predicted yield pressures are reasonable for a 10-mm-wall, 600-mm-ID vessel in mild steel. Setting a design pressure with a safety factor of 3 (so $P_{design} \approx P_Tresca/3 \approx 2.8$ MPa) is consistent with a typical low-pressure process vessel.
```


```{note}
**Exam Tips — Yield Criteria**
- Tresca is conservative ($\tau_y = \sigma_y/2$); von Mises is more accurate ($\tau_y = 0.577\sigma_y$).

- For a thin-walled cylindrical vessel, $\sigma_h = 2\sigma_\ell$. The hoop direction is the principal direction with the largest stress.

- For combined stress problems, identify $\sigma_1$ and $\sigma_3$ first (algebraic max and min principal stresses); then apply the criterion.
```


## Elastic Material Selection
The simplest material-selection exercise screens candidates against two constraints simultaneously: a yield-stress constraint (don't permanently deform) and a deflection constraint (don't bend more than allowed). Both constraints use elastic-region equations only.

### The Two-Filter Selection Process

```{note}
**Algorithm**
- Compute the applied stress $\sigma = F/A_0$ from the design load and the chosen geometry.

- **Filter 1 (Yield):** reject any candidate whose $\sigma_y < \sigma$ (with a safety factor $N$ if specified, so $\sigma_y < N\sigma$ is the rejection criterion).

- For the survivors, compute the elastic elongation under load using Hooke's law:

$$
\Delta L = \frac{\sigma L_0}{E} = \frac{F L_0}{A_0 E}
$$

- **Filter 2 (Deflection):** reject any candidate whose $\Delta L > \Delta L_{\max}$.

- Among final survivors, choose the cheapest (or the one best meeting secondary criteria: corrosion compatibility, weldability, density, etc.).

The key insight: *strength* (resists yielding, governed by $\sigma_y$) and *stiffness* (resists deflection, governed by $E$) are independent properties. A material can pass one filter and fail the other — selection requires both.
```


### Typical Elastic Properties

```{tip}
**{Elastic Properties of Candidate Construction Materials (room temperature)}**
- **Aluminum (1100, annealed):** $E = 70$ GPa, $\sigma_y = 35$ MPa.

- **Aluminum alloy (6061-T6):** $E = 70$ GPa, $\sigma_y = 250$ MPa.

- **Aluminum alloy (7075-T6):** $E = 72$ GPa, $\sigma_y = 500$ MPa.

- **Copper (annealed):** $E = 110$ GPa, $\sigma_y = 70$ MPa.

- **Copper (cold-worked):** $E = 110$ GPa, $\sigma_y = 250$ MPa.

- **Yellow brass:** $E = 100$ GPa, $\sigma_y = 345$ MPa.

- **Mild carbon steel (A36):** $E = 200$ GPa, $\sigma_y = 250$ MPa.

- **High-strength low-alloy steel:** $E = 207$ GPa, $\sigma_y = 450$–700 MPa.

- **Alloy steel (4140 Q&T):** $E = 207$ GPa, $\sigma_y = 850$–1500 MPa.

- **304 SS:** $E = 193$ GPa, $\sigma_y = 215$ MPa.

- **316 SS:** $E = 193$ GPa, $\sigma_y = 240$ MPa.

- **Ti-6Al-4V:** $E = 114$ GPa, $\sigma_y = 880$ MPa.

Note: $E$ varies surprisingly little across the steel family; nearly all carbon and low-alloy steels are $E = 200$–210 GPa regardless of heat treatment. *Strength varies hugely; stiffness barely.*
```


### Worked Example: Selecting a Tensile Rod

```{prf:example} Material Selection for a Cylindrical Rod
A cylindrical rod is 380 mm long and 10 mm in diameter. It must carry a tensile load of 24{,}500 N without yielding and without elongating more than 0.9 mm. Choose between aluminum (1100, annealed: $\sigma_y = 35$ MPa, $E = 70$ GPa), copper (annealed: $\sigma_y = 70$ MPa, $E = 110$ GPa), yellow brass ($\sigma_y = 345$ MPa, $E = 100$ GPa), and mild steel ($\sigma_y = 450$ MPa, $E = 207$ GPa).
```


```{dropdown} Solution Steps
- **Compute the applied stress.**

$$
A_0 = \pi(d/2)^2 = \pi(0.005)^2 = 7.854 \times 10^{-5}m^2 = 78.54mm^2
$$

$$
\sigma = \frac{F}{A_0} = \frac{24{,}500N}{78.54mm^2} = 312MPa
$$

- **Apply Filter 1: yield strength $> $ applied stress (312 MPa).**


- Aluminum 1100: 35 MPa $< $ 312. **Reject.**

- Copper (annealed): 70 MPa $<$ 312. **Reject.**

- Brass: 345 MPa $>$ 312. Pass.

- Steel: 450 MPa $>$ 312. Pass.

    Survivors: brass and steel.


- **Apply Filter 2: elongation under load $< 0.9$ mm.** Use $\Delta L = \sigma L_0/E$.


- Brass: $\Delta L = (312)(380)/(100{,}000) = 1.186$ mm $> 0.9$. **Reject.**

- Steel: $\Delta L = (312)(380)/(207{,}000) = 0.573$ mm $< 0.9$. Pass.



- **Selection.** Steel is the only candidate satisfying both constraints. Specify mild carbon steel for the rod.


- **Lesson.** Brass had *adequate strength* (a yield-strength margin of 345 vs. 312 = 11%) but *inadequate stiffness* (elongated 32% more than allowed). The deflection constraint rejected an otherwise-acceptable strong material. The deciding property here is $E$, not $\sigma_y$.


- **Verification.** Strain in the steel under load: $\varepsilon = \Delta L/L_0 = 0.573/380 = 1.51 \times 10^{-3}$. Hooke check: $\sigma = E\varepsilon = 207{,}000 \times 1.51 \times 10^{-3} = 313$ MPa, matching the applied 312 MPa. \checkmark
```


### Worked Example: Material Indices for Light-Weight Design

```{prf:example} Ashby Material Index for Minimum-Weight Rod
A tension-loaded rod must meet a stiffness requirement (maximum elongation $\Delta L_{\max}$) at minimum *mass*. The length $L_0$ and load $F$ are fixed by the application; the cross-sectional area $A$ is a free design variable. Which material property combination should be maximized?
```


```{dropdown} Solution Steps
- **Express the constraint.** The stiffness constraint is $\Delta L \leq \Delta L_{\max}$, i.e.\

$$
\frac{F L_0}{A E} \leq \Delta L_{\max} \Longrightarrow A \geq \frac{F L_0}{E \Delta L_{\max}}
$$

- **Express the mass.** The rod mass is

$$
m = \rho A L_0 \geq \rho L_0 \cdot \frac{F L_0}{E \Delta L_{\max}} = \frac{F L_0^2}{\Delta L_{\max}}\frac{\rho}{E}
$$

    Everything inside the second-to-last fraction is a design constant. The only material-dependent factor is $\rho/E$. **Minimum mass** corresponds to **minimum $\rho/E$**, or equivalently **maximum $E/\rho$**.


- **The material index.** $M = E/\rho$ is the **Ashby material index** for “stiffness-limited tensile rod at minimum mass.” Tabulated $E/\rho$ ratios:


- Steel: $E/\rho = 207/7.85 \approx 26$ GPa$\cdot$cm$^3$/g.

- Aluminum 6061: $70/2.7 \approx 26$.

- Titanium: $114/4.5 \approx 25$.

- CFRP (carbon-fiber composite, along fiber): $\sim$70.

    Notice that steel, aluminum, and titanium have nearly the same $E/\rho$ — for stiffness-limited tensile rods at minimum mass, the choice between them is a wash on this criterion. CFRP wins decisively.


- **Verification.** For *strength*-limited tensile design at minimum mass, the same derivation with $\sigma_y$ instead of $E$ gives $M = \sigma_y/\rho$ (“specific strength”), where the rankings differ from the stiffness case — high-strength steels and titanium become attractive.


- **Pedagogical note.** The Ashby approach generalizes the two-filter selection to multi-criteria optimization: tabulate the relevant material index for each constraint, plot materials on $E$–$\rho$ or $\sigma_y$–$\rho$ charts, and identify a Pareto-optimal subset. The PE exam doesn't test the formalism but does test the spirit: strength and stiffness drive different decisions.
```


```{note}
**Exam Tips — Material Selection**
- Selection requires both filters: $\sigma_y > \sigma_{applied}$ *and* $\Delta L < \Delta L_{\max}$.

- Don't confuse strength ($\sigma_y$) with stiffness ($E$). A material can be strong but compliant (brass) or stiff but weak (annealed aluminum).

- For specific (per-mass) properties: $E/\rho$ governs stiffness-limited design, $\sigma_y/\rho$ governs strength-limited.

- All steels have nearly the same $E$; alloy choice changes strength dramatically and stiffness barely at all.
```


## Strengthening Mechanisms (Why Alloys Are Stronger Than Pure Metals)
The yield strength of a metal can range from a few MPa for annealed pure metals to thousands of MPa for high-strength alloys. The variation comes from microstructural features that impede dislocation motion. Five mechanisms dominate.

### The Five Strengthening Mechanisms

```{note}
**Five Ways to Make Steel Stronger**
- **Grain-size strengthening (Hall-Petch).** Grain boundaries impede dislocation motion. Smaller grains $\to$ higher yield strength:

$$
\sigma_y = \sigma_0 + k_y \cdot d^{-1/2}
$$

    where $d$ is the average grain diameter, $\sigma_0$ is the lattice-friction stress, and $k_y$ is the Hall-Petch coefficient (material-specific). Doubling the grain size raises $\sigma_y$ by a factor of $\sqrt{2}$.

- **Solid-solution strengthening.** Foreign atoms (substitutional or interstitial) in the lattice produce local distortions that impede dislocations. Carbon in iron, nickel in copper, zinc in copper (brass). Yield strength rises roughly as the square root of solute concentration.

- **Strain-hardening (cold work).** Plastic deformation introduces new dislocations; the dislocation density rises and they tangle, impeding further motion. The yield strength after cold work approximately equals the stress at which the cold work was applied. Cold-rolled, drawn, or forged products show elevated $\sigma_y$ vs. annealed.

- **Precipitation hardening (age hardening).** Fine second-phase precipitates (Al$_2$Cu in aged 2024 aluminum; $\gamma'$ Ni$_3$Al in Inconel) impede dislocations. Achieved by quench + age heat treatment. The dramatic strength of Al alloys vs. pure Al comes from this mechanism.

- **Phase transformation hardening (martensite).** In steel, rapid quenching of austenite traps carbon in a distorted BCT lattice (martensite). The lattice distortion gives extremely high $\sigma_y$ and hardness but low toughness. Subsequent tempering reduces hardness and restores some toughness.

The mechanisms can be combined. A modern HSLA (high-strength low-alloy) steel uses solid-solution + grain refinement + microalloy precipitation; a maraging steel uses precipitation + low-carbon martensite.
```


### Hall-Petch in Practice

```{important}
**Hall-Petch Calculation**

$$
\sigma_y = \sigma_0 + k_yd^{-1/2}
$$

Typical low-carbon steel: $\sigma_0 \approx 70$ MPa, $k_y \approx 0.74$ MPa$\cdot$m$^{1/2}$ (in SI). With $d$ in m:


- Coarse grain $d = 100\mu$m = $10^{-4}$ m: $d^{-1/2} = 100$ m$^{-1/2}$; $\sigma_y = 70 + 0.74 \times 100 = 144$ MPa.

- Medium grain $d = 25\mu$m: $d^{-1/2} = 200$; $\sigma_y = 70 + 148 = 218$ MPa.

- Fine grain $d = 5\mu$m: $d^{-1/2} = 447$; $\sigma_y = 70 + 331 = 401$ MPa.

A 20$\times$ reduction in grain size nearly triples the yield strength. This is why thermomechanical processing (controlled rolling, accelerated cooling) is a central tool in steel mill metallurgy.
```


```{note}
**Exam Tips — Strengthening Mechanisms**
- Hall-Petch: $\sigma_y = \sigma_0 + k_y d^{-1/2}$. Memorize the $d^{-1/2}$ dependence.

- Cold work raises $\sigma_y$ and lowers ductility; annealing reverses both.

- Precipitation hardening requires a soluble alloying element and a heat-treatment cycle (solution treat + quench + age).

- For pressure-vessel steels, the controlling code (ASME Sec. II) specifies allowable stresses by alloy class — you do not normally compute strengthening explicitly.
```


## Creep and Time-Dependent Deformation
At elevated temperature, materials deform slowly under sustained load even when the stress is below the room-temperature yield strength. This is **creep**, and it is the dominant failure mode in high-temperature equipment: steam-superheater tubes, fired-heater tubes, gas-turbine blades, ammonia-converter shells.

### When Creep Matters

```{note}
**The Temperature Threshold for Creep**
Creep becomes significant above the **homologous temperature** $T/T_m \approx 0.4$, where $T_m$ is the melting point in absolute units (K or $^\circ$R). For carbon steel ($T_m \approx 1810$ K), creep starts to matter above $\sim$450$^\circ$C (720 K). For aluminum ($T_m \approx 930$ K), already at room temperature in absolute terms ($\sim 0.32 T_m$, so creep is marginal). For polymers, creep matters even at room temperature because $T_m$ is low.
```


### The Three Stages of Creep

```{note}
A creep curve plots strain vs. time at constant stress and temperature; it has three regimes:


- **Primary (transient) creep:** strain rate decreases with time as the material work-hardens.

- **Secondary (steady-state) creep:** balance between work-hardening and recovery; strain rate is approximately constant. This is the regime in which most engineering structures operate.

- **Tertiary creep:** strain rate accelerates as microvoids nucleate and grow; ends in rupture.

The steady-state (minimum) creep rate $\varepsilon_s$ is the property most often reported and used in design.
```


### Constitutive Equations

```{important}
**Power-Law (Norton) Creep**
The steady-state creep rate depends on stress and temperature as

$$
\varepsilon_s = A\sigma^n\exp(-\frac{Q_c}{RT})
$$

- $A$, $n$: material constants. $n$ is typically 3–8 for metals; large $n$ means steep stress dependence (small stress change $\to$ big creep-rate change).

- $Q_c$: activation energy for creep, typically close to that of self-diffusion.

- $R$: gas constant; $T$: absolute temperature.

The exponential dependence on $1/T$ means small temperature changes have outsized effects on creep life. A 25$^\circ$C overtemperature on a 500$^\circ$C tube can halve its remaining life.

**Larson-Miller parameter (LMP)**: a single parameter combining temperature and time-to-rupture:

$$
LMP = T(C + \log t_r)
$$

with $T$ in K, $t_r$ in hours, and $C \approx 20$ for most steels. Stress vs. LMP is a master curve — a single line that combines all $T$, $t_r$ pairs. Used to estimate creep life from short-term high-T tests.
```


### Worked Example: Estimating Creep Life from LMP

```{prf:example} Reformer-Tube Service Life
A reformer tube operates at $T = 900^\circ$C (1173 K) under a stress of 25 MPa. From the material's master curve, at stress 25 MPa, LMP = 22{,}000 (T in K, t in hours, C = 20). Estimate the tube's time to rupture.
```


```{dropdown} Solution Steps
- **Solve LMP for $t_r$.**

$$
LMP = T(C + \log t_r) \Longrightarrow \log t_r = \frac{LMP}{T} - C
$$

$$
\log t_r = \frac{22{,}000}{1173} - 20 = 18.76 - 20 = -1.24
$$

- **Compute $t_r$.**

$$
t_r = 10^{-1.24} = 0.058hours = 3.5minutes
$$

    The tube ruptures in about 3.5 minutes. *Not* the design life — the LMP curve was either misread or the chosen stress/temperature combination is well outside the design envelope.


- **Lesson on LMP interpretation.** A reformer tube designed for 100{,}000-hour life at 900$^\circ$C requires

$$
LMP_{design} = 1173 \times (20 + \log 100{,}000) = 1173 \times 25 = 29{,}325
$$

    Reading the material's master curve at LMP = 29{,}325 gives the maximum allowable design stress — typically 5–10 MPa for 100{,}000-hour life on Inconel 800H or HK-40 alloy. The 25 MPa in this example exceeds the allowable, hence the very short life.


- **Verification.** LMP is sensitive: a 100$^\circ$C temperature reduction (from 1173 to 1073 K) at constant LMP raises $t_r$ by $10^{(22000/1073 - 22000/1173)} = 10^{1.73} \approx 54\times$. Conversely, a 100$^\circ$C overtemperature reduces life by the same factor. This Arrhenius sensitivity is why creep-limited equipment is so unforgiving of process upsets.
```


```{note}
**Exam Tips — Creep**
- Creep matters above $T/T_m \approx 0.4$ (absolute scale).

- Three stages: primary (decelerating), secondary (steady-state), tertiary (accelerating to rupture).

- Power-law creep: $\varepsilon = A\sigma^n e^{-Q/RT}$. Small $T$ changes have large effects.

- LMP = $T(C + \log t_r)$, with $C \approx 20$ for steels. Single master curve correlates stress, $T$, and $t_r$.

- ASME Section II Part D allowable stresses at high temperature are creep-limited and decrease sharply with $T$.
```


## Fatigue: Failure Under Cyclic Loading
A part can fail under cyclic loading at stress amplitudes well below the static yield strength. This is **fatigue**, and it is responsible for the majority of in-service failures of rotating equipment, pressure-vessel nozzles, and pipe-support attachments.

### S-N Curve and Endurance Limit

```{note}
**The Stress-Life Approach**
A standard fatigue test cycles a specimen between $\sigma_{\max}$ and $\sigma_{\min}$ (or, more commonly, fully reversed: $\sigma_{\min} = -\sigma_{\max}$). The number of cycles to failure $N_f$ is recorded for each stress amplitude $S_a = (\sigma_{\max} - \sigma_{\min})/2$. The resulting plot of $S_a$ vs. $\log N_f$ is the **S-N curve**.

For **ferrous metals**, the S-N curve approaches a horizontal asymptote at large $N_f$ (typically $> 10^7$ cycles). The asymptotic stress is the **endurance limit** $S_e$ — below this stress amplitude, the material can survive infinite cycles. Roughly $S_e \approx 0.5\sigma_u$ for low-strength steel; deviates above $\sigma_u \approx 1400$ MPa.

For **non-ferrous metals** (aluminum, copper) the S-N curve continues to decline indefinitely — no true endurance limit. A “fatigue strength” at $10^7$ or $10^8$ cycles is reported instead.
```


### Modified Goodman Diagram for Mean Stress

```{important}
**Mean-Stress Correction**
Most fatigue data is for fully reversed loading ($\sigma_{mean} = 0$). Real components see superposed mean stress; a tensile mean reduces the allowable amplitude.

The **modified Goodman** criterion:

$$
\frac{S_a}{S_e} + \frac{\sigma_{mean}}{\sigma_u} = \frac{1}{N}
$$

where $N$ is the design safety factor against fatigue. Solve for the allowable $S_a$ given a known $\sigma_{mean}$.

The **Soderberg** criterion replaces $\sigma_u$ with $\sigma_y$; more conservative.
```


### Stress Concentrators

```{note}
**Why Welds and Holes Dominate Fatigue Life**
A discontinuity (hole, notch, weld toe, change in section) locally amplifies stress. The **stress concentration factor** $K_t$ multiplies the nominal stress to give the actual peak stress at the discontinuity:

$$
\sigma_{peak} = K_t\sigma_{nominal}
$$

Typical values: small drilled hole in a wide plate $K_t = 3$; sharp notch $K_t = 5$–10; weld toe $K_t = 2$–4 (depending on geometry and grinding).

In fatigue, the **fatigue stress concentration factor** $K_f$ replaces the geometric $K_t$, with $K_f \leq K_t$ (the difference accounts for “notch sensitivity” of the material). The allowable amplitude in Goodman is divided by $K_f$.

**Practical implication.** Welds are the dominant fatigue-initiation site in chemical-plant pressure vessels. Code-prescribed fatigue curves (ASME Sec. VIII Div. 2 Annex 3-F) embed the weld $K_f$ implicitly and assign design-fatigue-curve allowable stresses much lower than parent-metal yield.
```


```{note}
**Exam Tips — Fatigue**
- S-N curve: amplitude vs. cycles to failure. Ferrous metals have an endurance limit ($\approx 0.5\sigma_u$); non-ferrous do not.

- Mean-stress correction: modified Goodman or Soderberg. Tensile mean reduces allowable amplitude.

- Stress concentrators dominate fatigue life. Weld design and surface finish are critical.

- ASME Sec. VIII Div. 2 fatigue analysis is mandatory above certain cycle counts.
```


## Corrosion: Thermodynamic Foundations
Mechanical strength alone never selects a material for a chemical plant; chemical compatibility with the process fluid usually dominates. We start with the thermodynamic basis of corrosion (why metals corrode) and then survey the mechanistic categories (how they corrode in practice).

### The Electrochemical Nature of Corrosion

```{note}
**Corrosion Is an Electrochemical Cell**
Aqueous corrosion of a metal is a redox process consisting of two coupled half-reactions:


- **Anodic** (oxidation): metal dissolves into solution, releasing electrons:

$$
\mathrm{M \rightarrow M^{n+} + ne^-}  (e.g., \mathrm{Fe \rightarrow Fe^{2+} + 2e^-})
$$

- **Cathodic** (reduction): the released electrons reduce some species in the environment. In oxygenated water:

$$
\mathrm{O_2 + 2 H_2O + 4 e^- \rightarrow 4 OH^-}
$$

    In acid:

$$
\mathrm{2H^+ + 2e^- \rightarrow H_2}
$$

The two half-reactions must proceed at equal electron-transfer rates (charge balance). At the metal surface they are typically spatially separated: pits of anodic dissolution surrounded by larger cathodic regions. This separation is what makes corrosion damage so non-uniform and so hard to predict.
```


### Standard Electrode Potentials and the Nernst Equation

```{important}
**Standard Electrode Potential**
Each half-reaction has a characteristic **standard electrode potential** $E^\circ$ measured vs. the standard hydrogen electrode (SHE) at unit activity and 25$^\circ$C:


- $\mathrm{Au^{3+} + 3e^- \to Au}$: $E^\circ = +1.50$ V (very noble).

- $\mathrm{Cu^{2+} + 2e^- \to Cu}$: $E^\circ = +0.34$ V.

- $\mathrm{2H^+ + 2e^- \to H_2}$: $E^\circ = 0$ V (reference).

- $\mathrm{Fe^{2+} + 2e^- \to Fe}$: $E^\circ = -0.44$ V.

- $\mathrm{Zn^{2+} + 2e^- \to Zn}$: $E^\circ = -0.76$ V.

- $\mathrm{Mg^{2+} + 2e^- \to Mg}$: $E^\circ = -2.37$ V (very active).

The half-reaction with the higher $E^\circ$ proceeds spontaneously as written (reduction); the one with the lower $E^\circ$ runs in reverse (oxidation). The cell potential of the coupled reaction is $E_{cell} = E_cath - E_anode$; a positive value means the corrosion is spontaneous.

The **Nernst equation** corrects $E^\circ$ for non-standard activities:

$$
E = E^\circ - \frac{RT}{nF}\ln Q = E^\circ - \frac{0.0592}{n}\log_{10} Q  (at 25^\circC)
$$

where $Q$ is the reaction quotient, $n$ is the number of electrons transferred, $R$ is the gas constant, $F$ is the Faraday constant ($96{,}485$ C/mol).
```


### Pourbaix Diagrams

```{note}
**The Map of Stability vs. pH and Potential**
A **Pourbaix diagram** plots electrochemical potential $E$ vs. pH on a 2-D map, with regions labeled by the thermodynamically stable phase: bare metal, a soluble ionic species (corrosion), or an insoluble oxide/hydroxide (passivation).


- **Immune** region: metal is stable; corrosion is thermodynamically impossible.

- **Active** region: soluble ion is stable; metal corrodes.

- **Passive** region: insoluble oxide/hydroxide film forms, isolating metal from solution; *kinetic* barrier to corrosion (very slow rate even though dissolution is thermodynamically favorable).

The iron Pourbaix diagram has a passive region centered around pH 9–13 (where Fe(OH)$_3$ or Fe$_3$O$_4$ films form) and an active region at low pH (acid attack) and high pH for amphoteric metals.

**Engineering use:** given a process fluid's pH and the metal's natural rest potential, locate yourself on the Pourbaix diagram. Land in the passive region $\to$ corrosion is slow. Land in the active region $\to$ alternative metallurgy or pH adjustment is needed. Land in immune $\to$ unlimited service.
```


### Kinetics: The Tafel Equation and Corrosion Current

```{important}
**Mixed-Potential Theory and the Tafel Equation**
At the freely-corroding (open-circuit) potential, both anodic and cathodic reactions proceed at the same current density $i_{corr}$, the **corrosion current density**. The corrosion rate is directly proportional to $i_{corr}$ by Faraday's law:

$$
r_{corr} = \frac{i_{corr}M}{nF\rho}
$$

where $M$ is the metal's molar mass, $n$ is the electron-transfer number, and $\rho$ is the metal density. Units of $r_{corr}$: m/s (penetration rate); often converted to mm/yr or mpy (mils per year).

The activation polarization of each half-reaction is described by the **Tafel equation**:

$$
\eta = a + b\log_{10}(i/i_0)
$$

where $\eta$ is the overpotential (deviation from equilibrium potential), $i$ is the current density, and $a$, $b$ are Tafel constants. Extrapolating both Tafel lines to their intersection gives the corrosion potential and corrosion current density — the **Tafel-extrapolation method** of corrosion-rate measurement.
```


### Faraday's Law and Corrosion Rate

```{important}
**Penetration Rate in Engineering Units**
For a uniformly corroding flat surface, the penetration rate (depth lost per year) from a current density measurement is, in convenient engineering units:

$$
CR[mpy] = \frac{0.129i(eq.wt.)}{\rho}
$$

with $i$ in $\mu$A/cm$^2$, equivalent weight in g/eq, $\rho$ in g/cm$^3$. “mpy” is mils per year ($1$ mil $= 0.001$ in).

From weight-loss measurements (standard coupon test):

$$
CR[mpy] = \frac{534W}{\rhoAt}
$$

with $W$ = mass loss [mg], $\rho$ = density [g/cm$^3$], $A$ = exposed area [in$^2$], $t$ = exposure time [hr].

**Acceptance criteria (rule of thumb):**


- CR $<$ 5 mpy: *acceptable* for long service with a modest corrosion allowance.

- CR 5–20 mpy: *marginal*; acceptable if frequent inspection is planned.

- CR $>$ 50 mpy: *unacceptable* for long service; specify a different alloy.

Conversion: $1$ mm/yr $\approx 39.4$ mpy.
```


### Worked Example: Coupon Corrosion Rate

```{prf:example} 304 SS Coupon in Sulfuric Acid Service
A 304 SS coupon ($\rho = 7.9$ g/cm$^3$) of exposed area $A = 8$ in$^2$ is immersed in dilute H$_2$SO$_4$ at process conditions for $t = 720$ hours and loses $W = 120$ mg. Compute the corrosion rate in mpy. Decide whether 304 SS is acceptable for a 20-year service life.
```


```{dropdown} Solution Steps
- **Apply the weight-loss formula.**

$$
CR = \frac{534W}{\rhoAt} = \frac{534 \times 120}{7.9 \times 8 \times 720} = \frac{64{,}080}{45{,}504} = 1.41mpy
$$

- **Apply the acceptance rule of thumb.** CR = 1.41 mpy $<$ 5 mpy: *acceptable*.


- **Compute the 20-year metal loss to verify corrosion-allowance budget.**

$$
Loss_{20 yr} = 1.41mpy \times 20yr = 28mils = 0.71mm
$$

    This must be added as a corrosion allowance on top of the pressure-design wall thickness. Standard CA values: 1/16 in (1.6 mm), 1/8 in (3.2 mm), 1/4 in (6.4 mm). The 20-year loss (0.7 mm) easily fits inside a 1/16-in CA.


- **Important caveats.**


- *Concentration and temperature matter strongly.* For 304 SS in H$_2$SO$_4$, the corrosion rate rises sharply above $\sim$50$^\circ$C or at concentrations above $\sim$80 wt%. The 1.41 mpy assumes the coupon-test conditions match the design conditions.

- *Uniform-corrosion rule fails for localized attack.* If the coupon shows pitting, crevice corrosion, or intergranular attack, the uniform-rate calculation grossly underestimates the failure risk. Always inspect the coupon visually for localized damage.

- *Sensitization risk.* 304 SS in the 425–870$^\circ$C range can sensitize (chromium carbide precipitation at grain boundaries), drastically increasing intergranular corrosion. Use 304L or stabilized 321/347 grades if welding will occur near these temperatures.



- **Verification.** The corrosion rate is well below the acceptable threshold, and the projected wall loss fits comfortably inside a standard corrosion allowance. *Subject to the caveats*, 304 SS is acceptable for the service.
```


```{note}
**Exam Tips — Corrosion Thermodynamics**
- Anode = oxidation = metal dissolution. Cathode = reduction = O$_2$ or H$^+$ consumption.

- Galvanic series: more-active (negative $E^\circ$) metal corrodes preferentially when coupled.

- Pourbaix region: immune $\to$ no corrosion; active $\to$ corrosion; passive $\to$ kinetically slow.

- Corrosion rate calculation: $CR_mpy = 534W/(\rho A t)$ from coupon loss. Below 5 mpy acceptable; below 20 marginal.
```


## Corrosion Mechanisms: The Eight Forms
Fontana and Greene's classic textbook categorizes aqueous corrosion into eight forms. Each has characteristic damage morphology, susceptible alloy classes, and engineering defenses. The PE exam tests recognition (“what corrosion type matches this description?”) and selection (“what alloy avoids it?”).

### 1. Uniform (General) Corrosion

```{note}
**Mechanism.** Anodic and cathodic reactions are uniformly distributed over the surface; the metal thins evenly.

**Recognition.** Even thickness reduction; entire surface affected.

**Examples.** Carbon steel in dilute aerated water; copper in mildly acidic solutions.

**Defense.** Most predictable form — design with a **corrosion allowance** (1/16 to 1/4 in extra wall thickness) based on the measured rate. Standard approach to non-corrosion-rate-limited services.
```


### 2. Pitting Corrosion

```{note}
**Mechanism.** Localized breakdown of a passive film at discrete sites, leading to deep penetrations (pits) while the surrounding surface remains intact. An autocatalytic process: chloride or other aggressive ions accumulate in the pit, lowering pH and accelerating dissolution.

**Recognition.** Small, deep holes; the surface looks fine on visual inspection but a leak through a tube wall occurs at a single pit.

**Examples.** 304 SS in chloride-bearing waters above $\sim$60$^\circ$C; aluminum in chloride solutions.

**Defense.**


- Specify **Mo-containing alloys**: 316 (2–3% Mo) is the standard upgrade from 304; duplex 2205 (2.5–3.5% Mo, 22% Cr) for tougher service; Hastelloy C-276 (15–17% Mo) for the harshest.

- The **Pitting Resistance Equivalent Number (PREN)** quantifies pitting resistance:

$$
PREN = %Cr + 3.3 \times %Mo + 16 \times %N
$$

    304: PREN $\approx 19$. 316: $\approx 25$. 2205: $\approx 35$. SAF 2507 super-duplex: $\approx 42$. Higher PREN = better pitting resistance.
```


### 3. Crevice Corrosion

```{note}
**Mechanism.** Stagnant solution in a confined geometry (under gaskets, in lap joints, in O-ring grooves) experiences oxygen depletion, pH drop, and chloride concentration — producing the same conditions as inside a pit, but at a pre-existing geometric feature instead of a random breakdown site.

**Recognition.** Corrosion under flanges, gaskets, threaded joints, deposit films. The surface away from the crevice is intact.

**Defense.** Same materials defense as pitting (Mo-bearing alloys, high PREN). Also: design out crevices — use full-penetration welds instead of threaded joints, eliminate lap joints, specify smooth-bore fittings.
```


### 4. Galvanic Corrosion

```{note}
**Mechanism.** When two dissimilar metals are electrically connected in an electrolyte, the more-active (anodic) one corrodes preferentially while the more-noble (cathodic) one is protected. The rate is amplified by an unfavorable area ratio (small anode, large cathode $\to$ very high anode current density).

**Recognition.** Corrosion concentrated at the joint between two materials.

**Galvanic series in seawater (most active to most noble):** Mg, Zn, Al, mild steel, cast iron, 304 SS (active), low-alloy steel, brass, copper, 304 SS (passive), Ti, graphite, gold.

**Defense.**


- Electrically isolate the dissimilar metals (insulating gaskets, sleeves).

- Use materials close together in the galvanic series.

- Avoid *small-anode/large-cathode* configurations (a copper bolt in a steel plate is catastrophic; a steel bolt in a copper plate is much milder).

- Apply **cathodic protection**: connect the structure to a sacrificial more-active anode (Mg or Zn) that corrodes preferentially, or impress a DC current to drive the structure to a cathodic potential. Standard for buried pipelines and ship hulls.
```


### 5. Intergranular Corrosion (Sensitization in Stainless Steel)

```{note}
**Mechanism.** Preferential attack at grain boundaries due to compositional variation between grain interior and boundary. In austenitic stainless steel, heating in the 425–870$^\circ$C range precipitates chromium carbides (Cr$_{23}$C$_6$) at grain boundaries, locally depleting the boundary of chromium below the $\sim$12% needed for passivity — “**sensitization**.” Subsequent service in even mildly corrosive media attacks the depleted boundary regions.

**Recognition.** Falls apart at grain boundaries; the affected region looks granular rather than smooth.

**Examples.** Weld heat-affected zone in 304 SS exposed to acid; “weld-decay” fissures running parallel to a weld bead at a 1–5 mm offset.

**Defense.**


- Use **low-carbon (L) grades:** 304L, 316L (carbon $< 0.03$%) prevent significant Cr-carbide precipitation.

- Use **stabilized grades:** 321 (Ti-stabilized) or 347 (Nb-stabilized); the Ti or Nb preferentially forms carbides, leaving Cr in solid solution.

- Apply **solution annealing** (heat to $\sim$1050$^\circ$C, quench) after welding to dissolve any precipitated carbides. Only practical for small parts.
```


### 6. Stress-Corrosion Cracking (SCC)

```{note}
**Mechanism.** Simultaneous tensile stress (applied or residual from welding) and a specific corrosive environment cause brittle cracking through a normally ductile material. Three conditions must coexist: susceptible alloy, specific environment, tensile stress.

**Classic alloy-environment pairs:**


- Austenitic SS (304, 316) + hot chloride solutions ($> 60^\circ$C, $> 10$ ppm chloride).

- Carbon steel + hot caustic (NaOH); “caustic embrittlement.”

- Brass + ammonia.

- High-strength steels + H$_2$S (“sulfide stress cracking,” covered by NACE MR0175).

**Recognition.** Brittle, branched cracks through a ductile alloy; failure under static load with no warning; often initiate at stress concentrators (welds, attachments).

**Defense.**


- Switch alloy class: austenitic $\to$ ferritic or duplex SS for chloride SCC; carbon steel $\to$ Alloy 400 (Monel) for caustic SCC.

- Relieve residual stress by post-weld heat treatment (PWHT).

- Reduce environment severity: lower temperature, lower chloride, add inhibitors.
```


### 7. Erosion-Corrosion

```{note}
**Mechanism.** High-velocity fluid (especially when carrying entrained particles, bubbles, or two-phase flow) mechanically strips the passive film from the metal surface, exposing fresh metal to corrosion. The corrosion and erosion are mutually accelerating.

**Recognition.** Grooves, gullies, smooth-bottomed pits aligned with flow direction. Pump impellers, elbows, sharp directional changes are typical sites.

**Defense.**


- Reduce velocity; use larger pipe size at constrictions.

- Use hard alloys: Cu-Ni 70/30, Monel, Stellite hardfacing on pump-impeller leading edges.

- Eliminate two-phase flow where possible (avoid flashing across letdown valves).
```


### 8. Hydrogen Embrittlement

```{note}
**Mechanism.** Atomic hydrogen produced by corrosion or by cathodic protection diffuses into the metal lattice, embrittling high-strength steels by interfering with dislocation motion or by accumulating at internal defects. Failure is brittle, often catastrophic.

**Susceptible:** high-strength carbon and low-alloy steels ($\sigma_y > 700$ MPa); high-strength bolts; weldments not properly preheated/post-weld-heat-treated.

**Defense.**


- Use lower-strength steels (NACE MR0175: $\sigma_y \leq 620$ MPa hardness $\leq 22$ HRC for sour service).

- PWHT to relieve residual stress.

- Switch to nickel-based alloys (Inconel, Hastelloy) for severe sour service.

- Outgas the metal by low-temperature bake-out (200–300$^\circ$C for several hours) before service.
```


```{note}
**Exam Tips — Corrosion Forms**
- Memorize the eight forms and one defense each.

- “Chloride + austenitic SS” = SCC. Switch to duplex 2205.

- “Sensitization of 304” = use 304L or stabilized 321/347.

- “Galvanic couple in salt water” = sacrificial anode of zinc or magnesium.

- “Pitting in chloride water” = add Mo (316 or higher PREN).

- “Sour service” (H$_2$S) = NACE MR0175 compliance.
```


## Alloy Selection Catalogue for Chemical-Plant Service
A consolidated catalogue of the alloys used in process plants, with service envelopes and price tiers. The PE exam tests recognition (“which alloy fits this service?”) and rough cost-tier comparison.

### The Carbon-Steel Family

```{tip}
**Carbon and Low-Alloy Steels**
- **A516-70:** the workhorse plate for pressure vessels. Service: $-29$ to $+425^\circ$C, non-corrosive service.

- **A106-B:** seamless pipe for hydrocarbon service.

- **A350 LF2 / A203:** low-temperature qualified versions; usable to $-45^\circ$C (LF2) or $-100^\circ$C (A203 9% Ni).

- **Cr-Mo alloy steels (1.25Cr, 2.25Cr, 5Cr, 9Cr):** hydrogen service, elevated temperature ($425$–$650^\circ$C). The Nelson curves (API RP 941) govern hydrogen-attack design.

- **9% Ni steel (A553):** LNG service, down to $-195^\circ$C.

Cost benchmark: A516-70 plate is the cheapest pressure-vessel material; everything else is quoted as a multiple. Aluminum is similar to CS on a per-pound basis but cheaper per unit volume.
```


### The Stainless-Steel Family

```{tip}
**Stainless Steels**
- **304/304L:** 18% Cr, 8% Ni austenitic. Workhorse SS. Food, pharma, mild oxidizers. Avoid chlorides above 50 ppm at $T > 60^\circ$C (SCC). 304L (low-C) is the welding-safe variant.

- **316/316L:** 16% Cr, 10% Ni, 2% Mo. Mo adds pitting resistance. Dilute H$_2$SO$_4$, seawater (cold), most organic acids.

- **321 / 347:** Ti- and Nb-stabilized 304-class. Prevent sensitization in high-temperature service (refineries, ammonia plants).

- **Duplex 2205:** 22% Cr, 5% Ni, 3% Mo + N. Ferrite + austenite microstructure. Resists chloride SCC and pitting better than 316. Offshore, geothermal, FGD service. About 25% more expensive than 316.

- **Super-duplex 2507:** 25% Cr, 7% Ni, 4% Mo + N. Marine, chlorinated chemical service. PREN $> 40$.

- **Ferritic SS (430, 444):** 17% Cr, no Ni. Cheaper than austenitic; resistant to chloride SCC but less ductile and harder to weld.

Cost: 304 is roughly 3$\times$ A516-70; 316 is 4$\times$; duplex 2205 is 5$\times$; super-duplex 2507 is 8$\times$.
```


### Nickel and Cobalt Alloys

```{tip}
**High-Nickel Alloys**
- **Monel 400 (Ni-Cu 67/30):** hydrofluoric acid service, hot caustic, marine. The HF industry's standard alloy.

- **Inconel 600/625 (Ni-Cr or Ni-Cr-Mo):** high-temperature corrosion (sulfidation, hydrogen, hot mixed acids). Inconel 600 in nuclear-steam-generator tubing; Inconel 625 in flue-gas desulfurization (FGD).

- **Incoloy 800/800H:** reformer tubes, ethylene-cracker furnaces, high-temperature service to 1100$^\circ$C.

- **Hastelloy C-276:** the “universal” acid alloy. Hot HCl, mixed acids, FGD. Cost: $\sim$15$\times$ CS.

- **Hastelloy B-3:** non-oxidizing acids (HCl, concentrated H$_2$SO$_4$ without oxidizers). Cannot handle Fe$^{3+}$ or Cu$^{2+}$ contaminants.
```


### Reactive and Refractory Metals

```{tip}
**Specialty Alloys**
- **Titanium Gr 2 / Gr 12:** wet chlorine, hypochlorite, oxidizing chlorides, seawater (excellent), nitric acid. *Catastrophic* in dry chlorine, HF, or red fuming nitric acid.

- **Zirconium 702:** hot strong sulfuric ($> 70%$), hot HCl, hot HNO$_3$. Very expensive; used as plate or as lining/cladding.

- **Tantalum:** hot strong acids of all kinds; the “universal” acid material. Extremely expensive; used as heat-exchanger tubing or thin lining only.

- **Glass-lined steel:** hot HCl, dilute sulfuric below 70$^\circ$C, fine chemicals. Subject to thermal-shock cracking; limited size.

- **PTFE-lined steel:** broad acid resistance, low cost relative to exotic alloys. Limited to $\sim$200$^\circ$C and moderate pressures.
```


### The Alloy Upgrade Ladder

```{note}
**The Standard Escalation Path**
When a baseline material is found inadequate, the standard “upgrade ladder” for corrosion-driven decisions is:


- Carbon steel $\to$ 304 SS (add 18%Cr + 8%Ni for general oxidizing resistance).

- 304 $\to$ 316 (add Mo for pitting in chloride service).

- 316 $\to$ duplex 2205 (better SCC and pitting resistance with comparable cost premium).

- 2205 $\to$ Hastelloy C-276 / Inconel 625 (severe oxidizing or hot mixed-acid service).

- Inconel / Hastelloy $\to$ Ti, Zr, or Ta (extreme acid service).

- Ti / Zr / Ta $\to$ glass-lined or PTFE-lined CS (when the chemistry is too aggressive even for exotic metallurgy).

Each step roughly doubles the alloy cost. The economic optimum is the cheapest material that meets the service envelope with appropriate corrosion allowance and inspection budget.
```


```{note}
**Exam Tips — Alloy Selection**
- HF service $\to$ Monel.

- Hot wet chloride $\to$ duplex 2205 or Hastelloy.

- Hot caustic $\to$ Alloy 400 (Monel) or nickel-clad steel.

- Sour service ($H_2$S) $\to$ NACE MR0175-compliant low-strength steels or nickel-based alloys.

- LNG / cryogenic $\to$ 9% Ni steel or 304 SS or aluminum.

- Hot strong acid $\to$ Hastelloy, Zr, Ta, or glass/PTFE lining.

- Cost ladder: CS $\to$ 304 ($3\times$) $\to$ 316 ($4\times$) $\to$ duplex ($5\times$) $\to$ Hastelloy ($15\times$) $\to$ Ti/Zr ($20$–$50\times$) $\to$ Ta ($> 100\times$).
```


## Welding and Post-Weld Considerations
Most chemical-plant equipment is fabricated by welding. The weld is the weakest link — it has different microstructure, residual stresses, and possible defects compared to the parent metal. The PE exam tests basic weld-procedure concepts, code-required nondestructive examination (NDE), and post-weld heat treatment (PWHT).

### The Weld Joint and Its Microstructure

```{note}
**Three Zones of a Weld**
A fusion weld has three distinct microstructural zones:


- **Weld metal (fusion zone):** melted and resolidified; columnar grain structure; composition is parent metal + filler metal.

- **Heat-affected zone (HAZ):** parent metal that was heated below the melting point but high enough to alter its microstructure. Hardness peak; site of most service failures.

- **Parent (base) metal:** unaffected by the welding heat.

The HAZ is the high-risk zone: it often has the highest residual stress, the most distorted microstructure, and (in carbon steels) the highest hardness — all of which compound to make it the preferred site for SCC, fatigue cracking, and hydrogen-induced cracking.
```


### Joint Efficiency $E$ and Code Requirements

```{note}
**Why ASME Specifies Joint Efficiency**
The ASME Section VIII Div. 1 design formulas include a joint efficiency $E$ that derates the allowable stress at welds:


- **$E = 1.00$**: fully radiographed butt welds. The full code allowable stress is usable in the design equation.

- **$E = 0.85$**: spot-radiographed welds. Reduces allowable stress by 15%.

- **$E = 0.70$**: no radiography. Reduces by 30%.

- Other values for non-butt joints (fillet welds, single welds, etc.).

The choice trades **NDE cost** against **plate cost**: $E = 1.0$ requires costly radiography but lets you use a thinner wall; $E = 0.7$ saves NDE cost but forces a thicker (heavier, more expensive) wall. The economic optimum depends on vessel size and plate alloy.
```


### Post-Weld Heat Treatment (PWHT)

```{note}
**When PWHT Is Required**
ASME Sec. VIII Div. 1 Table UCS-56 mandates PWHT when wall thickness exceeds material-specific thresholds (e.g. 1.5 in for P-No. 1 carbon steel). The PWHT cycle:


- Heat to a specified temperature (typically 590–690$^\circ$C for carbon steel).

- Hold for 1 hour per inch of thickness (minimum).

- Cool slowly in still air or controlled furnace.

Purposes:


- Relieve residual stresses (typically reduces to 10–20% of yield).

- Temper hard HAZ microstructures (martensite in C-Mn steel HAZ).

- Drive off any trapped hydrogen.

PWHT is also required by NACE MR0175 for sour service, and is good practice for caustic service to avoid caustic SCC.
```


### Nondestructive Examination (NDE)

```{tip}
**Standard NDE Methods**
- **Visual (VT):** the cheapest; trained inspector checks for surface defects.

- **Liquid Penetrant (PT):** surface-breaking defects only; dye + developer.

- **Magnetic Particle (MT):** ferromagnetic materials only; surface and near-surface defects.

- **Radiographic (RT):** X-ray or gamma-ray imaging; volumetric defects (porosity, slag, lack of fusion); the ASME standard for full-radiography butt welds.

- **Ultrasonic (UT):** sound pulses; volumetric defects, very sensitive to planar defects (cracks). Increasingly used in place of RT (no radiation exposure, automated scanning).

- **Eddy current (ET):** tubing inspection; detects pits, cracks, wall thinning in heat-exchanger tubes.

NDE is required by code, by company specification, and by jurisdictional authorities (e.g. ABS for marine, US Coast Guard, foreign equivalents).
```


```{note}
**Exam Tips — Welding and NDE**
- ASME joint efficiency $E$: 1.00 (full RT), 0.85 (spot), 0.70 (none). Affects wall thickness.

- HAZ is the failure-prone zone in most weld-related service failures.

- PWHT required for thick sections, for sour service, and for caustic service.

- NDE methods: VT, PT, MT (surface); RT, UT (volumetric); ET (tubes).
```


## Worked Example: Integrating Materials Selection for a Process Vessel

```{prf:example} Materials Selection for a Reactor Pressure Vessel
A continuous stirred-tank reactor (CSTR) is being designed:


- Capacity: 50 m$^3$, 3-m ID cylindrical vessel.

- Design pressure 12 barg; design temperature 200$^\circ$C.

- Process side: dilute aqueous HCl (3 wt%) at 90$^\circ$C with trace H$_2$O$_2$ as oxidizer.

- Required service life: 20 years.

Select the wall material and the corrosion allowance. Compute the required wall thickness.
```


```{dropdown} Solution Steps
- **Apply the materials-selection algorithm.**

    **Step 1.1 — Temperature.** 200$^\circ$C design (90$^\circ$C process); within CS continuous-service envelope ($< 425^\circ$C).

    **Step 1.2 — Chemistry screening.**


- Dilute HCl: carbon steel attacked rapidly — reject CS.

- 304 SS: HCl is reducing-acid service; the chloride content drives both general corrosion and pitting — reject 304 SS.

- 316 SS: better than 304 but the trace H$_2$O$_2$ creates oxidizing-acid conditions that can still cause pitting. Marginal at best — reject as the primary material.

- Hastelloy C-276: handles hot HCl with oxidizing contaminants; routine FGD service. *Candidate.*

- Glass-lined CS: handles dilute HCl below 70$^\circ$C without issues; at 90$^\circ$C marginal; thermal-shock risk in a stirred reactor. Possible but not preferred.

- Titanium Gr 2: rapidly attacked by reducing HCl — reject.


    **Step 1.3 — Cost.** Hastelloy C-276 solid plate is very expensive (15–20$\times$ CS). **Cladded construction** (CS base + 3 mm C-276 cladding on the process side) cuts cost to $\sim$7–10$\times$ CS while preserving the C-276 corrosion resistance.

    **Selection: Hastelloy C-276 clad on A516-70 CS plate.**


- **Corrosion allowance.** The clad layer is the corrosion barrier; the CS substrate is structural. A 3 mm clad gives a corrosion allowance of 3 mm specifically on the clad layer. If C-276 corrodes at $< 2$ mpy (0.05 mm/yr) in this service, the 3 mm clad lasts $> 60$ years — comfortably beyond the 20-year requirement. **Inspection schedule:** verify clad integrity every 5 years via UT or visual entry.
```


```{dropdown} Solution Steps
- **Wall thickness from ASME Sec. VIII Div. 1.** The structural CS substrate must withstand the design pressure. At 200$^\circ$C, A516-70 has $S = 19{,}800$ psi (from ASME Sec. II Part D table; the room-temp value 25{,}000 psi is reduced at elevated temp).

    Convert design pressure: 12 barg $= 174$ psig. ID $= 3$ m $= 118$ in, so $R = 59$ in.

    Check thin-wall: $P/(SE)$ with $E = 1.0$ (fully radiographed weld assumed):

$$
\frac{174}{19{,}800 \times 1.0} = 0.0088 \ll 0.385  \checkmark
$$

    Hoop equation governs:

$$
t_{pressure} = \frac{P R}{S E - 0.6 P} = \frac{(174)(59)}{(19{,}800)(1.0) - (0.6)(174)} = \frac{10{,}266}{19{,}696} = 0.521in
$$

- **Add the clad layer.** The cladding does not contribute structural strength but its thickness is included in the total wall:

$$
t_{total} = t_{pressure} + t_{clad} = 0.521 + 0.118 = 0.639in(clad = 3  mm = 0.118  in)
$$

    Some codes also require a corrosion allowance on the structural CS substrate in case the clad fails locally; conservative practice adds 1/16 in (0.0625 in) for this:

$$
t_{final} = 0.521 + 0.0625 + 0.118 = 0.702in
$$

- **Round up to standard plate.** Next standard gauge above 0.702 in is **3/4 in (0.750 in)**. The fabrication spec: 3/4-in A516-70 plate clad with 1/8-in (3.2 mm) Hastelloy C-276 on the process side.


- **Verification.** Hoop stress at the chosen wall (using structural thickness 0.750 - 0.118 - 0.0625 = 0.5695 in):

$$
\sigma_h = \frac{PR}{t_{struct}} = \frac{(174)(59)}{0.5695} = 18{,}030psi < S = 19{,}800psi\checkmark
$$

    The selection satisfies all constraints: pressure (Sec. VIII), corrosion (Hastelloy in dilute oxidizing HCl), cost (cladded construction saves $\sim$60% over solid C-276), and service life (60+ years on the clad layer for a 20-year requirement).
```


```{note}
**Exam Tips — Integrated Material Selection**
- Always combine chemical-compatibility screening with mechanical (pressure, temperature) design.

- Cladded construction is the standard cost-saver for large vessels in aggressive service.

- Wall thickness = pressure-design thickness + clad thickness + corrosion allowance.

- Verify the structural-layer hoop stress against the code allowable at the design temperature.
```


## Summary: Materials Decision Tree and Reference Sheet

```{note}
**Materials Selection Algorithm**
- **Compute mechanical loads.** Pressure, temperature, dead-weight, dynamic, fatigue, thermal-cycling.

- **Compute applied stress.** For pressure vessels, hoop stress $\sigma_h = PR/t$ governs.

- **Screen by mechanical envelope.** Material $\sigma_y > $ applied $\sigma$ at design temperature, with safety factor.

- **Screen by chemistry.** Eliminate candidates that fail in the process chemistry (corrosion, SCC, embrittlement).

- **Compute or measure corrosion rate.** Use coupon tests or published rates. Apply corrosion-allowance rules.

- **Compare candidates by lifetime cost.** Capital + corrosion-driven maintenance + inspection + downtime cost.

- **Specify the material, weld procedure, NDE level, and PWHT requirements.**
```


```{tip}
**One-Page Formula Reference**
**Stress and strain:**
$\sigma = F/A_0$ (engineering); $\sigma_{true} = F/A_i$.
$\varepsilon = (L_i - L_0)/L_0$ (engineering); $\varepsilon_{true} = \ln(1 + \varepsilon)$.

**Hooke's law:**
$\sigma = E\varepsilon$ (elastic only). $\Delta L = \sigma L_0 / E = FL_0/(A_0 E)$.

**Resilience and toughness:**
$U_r = \sigma_y^2/(2E)$. Toughness $= $ area under entire $\sigma$-$\varepsilon$ curve.

**Yield criteria (multi-axial):**
Tresca: $\sigma_1 - \sigma_3 = \sigma_y$.
von Mises: $\sigma_{vM} = \sqrt{\tfrac{1}{2}[(\sigma_1-\sigma_2)^2 + (\sigma_2-\sigma_3)^2 + (\sigma_3-\sigma_1)^2]} = \sigma_y$.

**Hall-Petch:** $\sigma_y = \sigma_0 + k_yd^{-1/2}$.

**Creep:** $\varepsilon_s = A\sigma^n e^{-Q/RT}$. LMP $= T(C + \log t_r)$, $C \approx 20$ for steels.

**Fatigue:** S-N curve. Endurance limit $S_e \approx 0.5\sigma_u$ (steel). Modified Goodman: $S_a/S_e + \sigma_m/\sigma_u = 1/N$.

**Corrosion rate (coupon):** CR[mpy] $= 534W/(\rho A t)$. Acceptable $< 5$, marginal 5–20, reject $> 50$ mpy.

**PREN:** $= %Cr + 3.3%Mo + 16%N$. 304 $\approx 19$; 316 $\approx 25$; 2205 $\approx 35$; 2507 $\approx 42$.

**Pressure vessel (ASME VIII):**
Hoop: $t = PR/(SE - 0.6P)$; longitudinal $t = PR/(2SE + 0.4P)$.
Joint efficiency $E$: 1.00 (full RT), 0.85 (spot), 0.70 (none).

**Galvanic series (active $\to$ noble, seawater):** Mg, Zn, Al, steel, 304 (active), brass, Cu, 304 (passive), Ti, graphite, Au.

**Alloy upgrade ladder:** CS $\to$ 304 $\to$ 316 $\to$ duplex 2205 $\to$ Hastelloy C-276 / Inconel 625 $\to$ Ti/Zr $\to$ Ta or glass/PTFE-lined CS.
```


```{note}
**Common PE-Exam Mistakes**
- Confusing strength ($\sigma_y$) with stiffness ($E$) — they govern different failure modes.

- Using engineering vs. true stress inconsistently. Design always uses engineering.

- Forgetting Hall-Petch $d^{-1/2}$ scaling (not $d^{-1}$).

- Using room-temperature $\sigma_y$ at high service temperature — always look up $S$ at the actual design temperature.

- Selecting 304 SS for chloride service above 60$^\circ$C (SCC trap).

- Selecting 304 SS for welded service without specifying 304L or 321/347 (sensitization trap).

- Forgetting joint efficiency $E$ in ASME wall-thickness calculation.

- Using small-anode/large-cathode galvanic coupling (catastrophic).

- Ignoring fatigue at welds (the most common failure site in cyclic-load service).
```
