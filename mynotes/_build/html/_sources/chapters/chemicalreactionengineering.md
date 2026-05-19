---
title: "Chemical Reaction Engineering Study Guide"
author: "PE Study Guide"
date: "2025"
---

# Chemical Reaction Engineering

## Quick Reference: Key Equations

| Topic | Formula | Notes |
|-------|---------|-------|
| 1st-order integrated | $[A] = [A]_0 e^{-kt}$ | Batch, 1st order |
| 2nd-order integrated | $1/[A] = 1/[A]_0 + kt$ | Batch, 2nd order |
| Half-life (1st order) | $t_{1/2} = \ln 2/k = 0.693/k$ | Independent of $[A]_0$ |
| Half-life (2nd order) | $t_{1/2} = 1/(k[A]_0)$ | Depends on $[A]_0$ |
| Arrhenius | $k = A\,e^{-E_a/RT}$ | $T$ in K |
| Batch reactor | $t = C_{A0}\int_0^X dX/(-r_A)$ | Design equation |
| CSTR design | $V = F_{A0}\,X/(-r_A)$ | Evaluated at exit |
| PFR design | $V = F_{A0}\int_0^X dX/(-r_A)$ | Integrated over $X$ |
| Space time | $\tau = V/v_0 = C_{A0}/(-r_A)$ | CSTR at SS |
| Levenspiel plot | Rectangular area ($\approx$ CSTR) vs. integral ($\approx$ PFR) | Graphical sizing |
| Adiabatic $T$ rise | $T = T_0 + (-\Delta H_{rxn}/\rho C_p)(C_{A0} X)$ | Adiabatic batch/PFR |
| Energy balance (CSTR) | $\dot{Q} - \dot{W}_s = F_{A0}[\Delta H_{rxn}X + \sum\Theta_i C_{p,i}(T-T_0)]$ | General |
| Selectivity | $S_{D/U} = r_D/r_U$ | Point selectivity |
| Yield | $Y = $ moles desired product / moles fed to reactor | Overall |

---

## First-Order Reaction Kinetics

First-order reactions are chemical reactions where the rate of reaction is directly proportional to the concentration of only one of the reactants. Understanding their behavior is crucial for reactor design and analysis.

```{note}
**Half-Life:** The **half-life** ($t_{1/2}$) of a reaction is the time it takes for the concentration of a reactant to be reduced to half of its initial value. For a first-order reaction, the half-life is constant and does not depend on the initial concentration. This means that in every half-life interval, the amount of reactant will decrease by 50%. This property is unique to first-order processes and provides a powerful conceptual tool for quick estimations.
```

### Visualizing Half-Life

```{prf:example} Visualizing Half-Life in a First-Order Reaction
**Question:** A first-order reaction, $A \rightarrow B$, starts with 16 molecules of reactant A. After 100 seconds, 8 molecules of A remain and 8 molecules of B have been formed. What will the mixture look like at 300 seconds?
```

```{dropdown} Solution Steps
**Step 1: Analyze the Initial Data and Define Knowns:**

Initial molecules of A at $t=0$ s: $N_{A0} = 16$.
Molecules of A at $t=100$ s: $N_A = 8$.

We observe that exactly half of the initial reactant A has been consumed in the first 100 seconds.

**Step 2: Identify the Half-Life ($t_{1/2}$):**

Since the reactant amount dropped by exactly 50% in 100 seconds: $t_{1/2} = 100 \, \text{s} $

**Step 3: Calculate Reactant Population at Each Half-Life Interval:**

Track the population of A by repeatedly halving it for each 100 s interval:

- At $t=0$ s: $N_A = 16$.
- At $t=100$ s (1 half-life): $N_A = 8$.
- At $t=200$ s (2 half-lives): $N_A = 4$.
- At $t=300$ s (3 half-lives): $N_A = 2$.

**Step 4: Determine Final Composition:**

The total number of molecules is conserved: $N_A + N_B = 16$.
Molecules of A remaining at 300 s: $N_A = 2$.
Molecules of B formed at 300 s: $N_B = 16 - 2 = 14$.
```

## Quantitative Analysis of First-Order Reactions

While the half-life concept is useful for estimations, precise calculations require the integrated first-order rate law. This section covers the key equations and their application.

```{admonition} Term Definitions
:class: tip
- $[A]$: Concentration of reactant A at time $t$ ($\text{mol/L}$).
- $[A]_0$: Initial concentration of reactant A at $t=0$ ($\text{mol/L}$).
- $k$: First-order rate constant, temperature-dependent ($\text{s}^{-1}$, $\text{min}^{-1}$, etc.).
- $t$: Elapsed time.
```

```{important}
**First-Order Integrated Rate Law**
The relationship between concentration and time for a first-order process is given by:

$$

[A] = [A]_0 e^{-kt} \quad \text{(Equation 1)}

$$

This equation can be rearranged into a linear form by taking the natural logarithm:

$$

\ln\left(\frac{[A]}{[A]_0}\right) = -kt

$$

```

### Relating Half-Life and the Rate Constant

A crucial relationship can be derived by substituting the definition of half-life ($t = t_{1/2}$, $[A] = 0.5[A]_0$) into the integrated rate law.

```{important}
**Half-Life and Rate Constant Relationship**

$$

0.5[A]_0 = [A]_0 e^{-kt_{1/2}}


0.5 = e^{-kt_{1/2}}


\ln(0.5) = -kt_{1/2}

$$

Since $\ln(0.5) = -\ln(2)$, we arrive at the simple and important result:

$$

k = \frac{\ln(2)}{t_{1/2}} \quad \text{(Equation 2)}

$$

Note that the initial concentration $[A]_0$ does not appear in the final equation.
```

### First-Order Kinetics Calculation

```{prf:example} First-Order Kinetics Calculations
**Question:** The decomposition of dimethyl ether is a first-order process with a half-life of 2165 seconds at $450^\circ\text{C}$. The reaction occurs in a constant volume container with an initial dimethyl ether concentration of 2.0 M.
(a) What is the concentration of dimethyl ether after one hour?
(b) How much time is required for the concentration to become 0.2 M?
```

```{dropdown} Solution Steps
**Solution (Part a): Concentration after one hour**

**Step 1: Identify Knowns and Goal:**
- Initial Concentration, $[A]_0 = 2.0 \, \text{M}$
- Half-life, $t_{1/2} = 2165 \, \text{s}$
- Time, $t = 1 \, \text{hour} = 3600 \, \text{s}$
- **Goal:** Find final concentration, $[A]$, at $t=3600$ s.

**Step 2: Calculate the Rate Constant (k):**
Using Equation 2, we find the rate constant from the given half-life. It is critical to use consistent units.

$$

k = \frac{\ln(2)}{t_{1/2}} = \frac{0.6931}{2165 \, \text{s}} = 0.0003201 \, \text{s}^{-1}

$$

**Step 3: Apply the First-Order Rate Equation:**
Using Equation 1, substitute the known values to find the concentration $[A]$.

$$

[A] = [A]_0 e^{-kt}


[A] = (2.0 \, \text{M}) \exp\left(-(0.0003201 \, \text{s}^{-1})(3600 \, \text{s})\right)


[A] = (2.0 \, \text{M}) \exp(-1.15236)


[A] = (2.0 \, \text{M}) \times (0.3159) = 0.6318 \, \text{M}

$$

**Step 4: Conclusion for Part (a):**
After one hour, the concentration of dimethyl ether will be approximately **0.63 M**.
```

```{dropdown} Solution Steps
**Solution (Part b): Time to reach 0.2 M**

**Step 1: Identify Knowns and Goal:**
- Initial Concentration, $[A]_0 = 2.0 \, \text{M}$
- Final Concentration, $[A] = 0.2 \, \text{M}$
- Rate Constant, $k = 0.0003201 \, \text{s}^{-1}$ (from Part a)
- **Goal:** Find the time required, $t$.

**Step 2: Apply and Rearrange the First-Order Rate Equation:**
We start with Equation 1 again, but this time we solve for the unknown time, $t$.

$$

[A] = [A]_0 e^{-kt}


\frac{[A]}{[A]_0} = e^{-kt}

$$

Take the natural logarithm of both sides to solve for the exponent:

$$

\ln\left(\frac{[A]}{[A]_0}\right) = -kt


t = -\frac{1}{k} \ln\left(\frac{[A]}{[A]_0}\right)

$$

**Step 3: Substitute Values and Calculate Time:**

$$

t = -\frac{1}{0.0003201 \, \text{s}^{-1}} \ln\left(\frac{0.2 \, \text{M}}{2.0 \, \text{M}}\right)


t = -\frac{1}{0.0003201 \, \text{s}^{-1}} \ln(0.1)


t = -\frac{1}{0.0003201 \, \text{s}^{-1}} (-2.3026)


t = 7193.4 \, \text{s}

$$

**Step 4: Conclusion for Part (b):**
It will take approximately **7193 seconds** (or about 2.0 hours) for the concentration to drop to 0.2 M.
```

## Temperature Dependence and Reactor Design

The rate of reaction is highly sensitive to temperature. The **Arrhenius equation** describes this relationship, which is fundamental for designing reactors that operate at different temperatures.

```{admonition} Term Definitions
:class: tip
- $k$: The rate constant (temperature-dependent).
- $A$: The pre-exponential or frequency factor (same units as $k$). Assumed constant.
- $E_a$: The activation energy, the minimum energy barrier for reaction ($\text{J/mol}$ or $\text{kcal/mol}$).
- $R$: The ideal gas constant ($8.314 \, \frac{\text{J}}{\text{mol} \cdot \text{K}}$ or $1.987 \times 10^{-3} \, \frac{\text{kcal}}{\text{mol} \cdot \text{K}}$).
- $T$: Absolute temperature in Kelvin (K).
```

```{important}
**The Arrhenius Equation**
The temperature dependence of the rate constant is given by:

$$

k = A e^{-E_a / (RT)} \quad \text{(Equation 3)}

$$

To determine $E_a$ from experimental data, a linearized form is used by taking the natural logarithm:

$$

\ln(k) = \ln(A) - \frac{E_a}{R} \left(\frac{1}{T}\right)

$$

This equation is in the form of a straight line, $y = b + mx$, where a plot of $\ln(k)$ versus $1/T$ yields a slope of $m = -E_a/R$.
```

### Activation Energy Calculation

```{prf:example} Activation Energy and Temperature Effects
**Question:** For a reaction $A \rightarrow \text{Products}$, a plot of $\ln(k)$ versus $1/T$ (where T is in Kelvin) yields a straight line with a slope of $-18000$ K.
(a) What is the activation energy ($E_a$) for this reaction? Use $R \approx 1.99 \times 10^{-3}$ kcal/(mol·K).
(b) Given $k_1 = 2.15 \, \text{s}^{-1}$ at $T_1 = 600$ K, calculate the rate constant $k_2$ at $T_2 = 700$ K.
```

```{dropdown} Solution Steps
**Solution (Part a): Activation Energy**

**Step 1: Relate Slope to Activation Energy:**
From the linearized Arrhenius equation:

$$

\text{Slope} = -\frac{E_a}{R}

$$

**Step 2: Substitute Known Values and Solve for $E_a$:**

$$

-18000 \, \text{K} = -\frac{E_a}{1.99 \times 10^{-3} \, \text{kcal/(mol}\cdot\text{K)}}


E_a = (18000 \, \text{K}) \times (1.99 \times 10^{-3} \, \text{kcal/(mol}\cdot\text{K)}) = 35.82 \, \text{kcal/mol}

$$

**Step 3: Conclusion for Part (a):**
The activation energy is approximately **36 kcal/mol**.
```

```{dropdown} Solution Steps
**Solution (Part b): Rate Constant at New Temperature**

**Step 1: Select the Appropriate Equation Form:**
Use the two-point form of the Arrhenius equation:

$$

\ln\left(\frac{k_2}{k_1}\right) = \frac{E_a}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)

$$

**Step 2: Substitute Known Values:**
From Part (a): $\frac{E_a}{R} = 18000 \, \text{K}$. Using $T_1 = 600$ K, $T_2 = 700$ K, $k_1 = 2.15 \, \text{s}^{-1}$:

$$

\ln\left(\frac{k_2}{2.15 \, \text{s}^{-1}}\right) = (18000 \, \text{K}) \left(\frac{1}{600 \, \text{K}} - \frac{1}{700 \, \text{K}}\right)


\ln\left(\frac{k_2}{2.15}\right) = 18000 (0.0002381) = 4.2857

$$

**Step 3: Solve for the New Rate Constant, $k_2$:**

$$

\frac{k_2}{2.15} = e^{4.2857} \approx 72.65


k_2 = 72.65 \times 2.15 \, \text{s}^{-1} \approx 156.2 \, \text{s}^{-1}

$$

**Step 4: Conclusion for Part (b):**
The rate constant at 700 K is approximately **156 s$^{-1}$**.
```

## CSTR Design Application

The principles of reaction kinetics are applied directly to design chemical reactors, such as the Continuous Stirred-Tank Reactor (CSTR).

```{note}
**CSTR Steady-State Material Balance:** For a CSTR operating at steady-state, conditions inside the reactor are uniform and constant. The material balance simplifies to an algebraic equation. The general balance is: Input - Output + Generation = Accumulation. At steady state, Accumulation is zero.

$$

F_{A0} - F_A + r_A V = 0

$$

Where $r_A$ is the rate of **formation** of A. For a reactant, $r_A$ is negative. For a first-order reaction, the rate of **consumption** is $-r_A = k C_A$, so the rate of formation is $r_A = -k C_A$.
```

```{admonition} Term Definitions
:class: tip
- $F_{A0}$: Molar flow rate of A **into** the reactor ($\text{mol/s}$).
- $F_A$: Molar flow rate of A **out of** the reactor ($\text{mol/s}$).
- $V$: Volume of the reactor ($\text{L}$).
- $v_0$: Volumetric flow rate of the feed ($\text{L/s}$).
- $C_A$: Concentration of A in the reactor and in the outlet stream ($\text{mol/L}$).
- $Da$: Damköhler number (dimensionless), $Da = k\tau = kV/v_0$. Represents the ratio of reaction rate to convection rate.
```

```{important}
**CSTR Design Equation for a First-Order Reaction**
Substituting $r_A = -k C_A$ and $F_A = C_A v_0$ into the general balance gives:

$$

F_{A0} - F_A - k \left(\frac{F_A}{v_0}\right) V = 0

$$

Solving for the outlet molar flow rate, $F_A$:

$$

F_A = \frac{F_{A0}}{1 + \frac{kV}{v_0}} = \frac{F_{A0}}{1 + Da} \quad \text{(Equation 4)}

$$

```

### Example: Evaluating CSTR Performance

```{prf:example} Evaluating CSTR Performance
**Question:** An existing 50 L CSTR is used for the liquid-phase reaction A $\rightarrow$ Products. The reactor operates isothermally at 600 K, where $k = 2.15 \, \text{s}^{-1}$. The feed enters at $v_0 = 500$ L/s with $C_{A0} = 0.4$ mol/L. To be suitable, the molar flow rate of A exiting the reactor ($F_A$) must be less than 5 mol/s. Is the reactor suitable?
```

```{dropdown} Solution Steps
**Step 1: List Knowns and Goal:**
- Reactor Volume, $V = 50$ L
- Rate Constant, $k = 2.15 \, \text{s}^{-1}$ (at 600 K)
- Volumetric Flow Rate, $v_0 = 500$ L/s
- Inlet Concentration, $C_{A0} = 0.4$ mol/L
- Performance Target: $F_A < 5$ mol/s
- **Goal:** Calculate outlet flow rate $F_A$ and compare it to the target.

**Step 2: Calculate the Inlet Molar Flow Rate ($F_{A0}$):**

$$

F_{A0} = C_{A0} \times v_0 = (0.4 \, \text{mol/L}) \times (500 \, \text{L/s}) = 200 \, \text{mol/s}

$$

**Step 3: Calculate the Damköhler Number (Da):**
The Damköhler number is a key dimensionless group for reactor analysis.

$$

Da = \frac{kV}{v_0} = \frac{(2.15 \, \text{s}^{-1})(50 \, \text{L})}{500 \, \text{L/s}} = \frac{107.5}{500} = 0.215

$$

A small Da number ($Da \ll 1$) suggests that the residence time is short compared to the reaction time, leading to low conversion.

**Step 4: Apply the CSTR Design Equation (Eq. 4) to Find $F_A$:**

$$

F_A = \frac{F_{A0}}{1 + Da} = \frac{200 \, \text{mol/s}}{1 + 0.215} = \frac{200 \, \text{mol/s}}{1.215} \approx 164.6 \, \text{mol/s}

$$

**Step 5: Compare Result to Requirement and Conclude:**
The calculated outlet flow rate is $F_A \approx 165$ mol/s. The requirement is $F_A < 5$ mol/s. Since $165 \, \text{mol/s} \gg 5 \, \text{mol/s}$, the reactor is **not suitable**. The conversion is far too low for the given process requirements. To meet the goal, the Damköhler number would need to be significantly increased, for example by increasing reactor volume $V$ or decreasing volumetric flow rate $v_0$.
```

## Conversion with Levenspiel Plots

This section explores reactor performance analysis using a **Levenspiel plot**, a powerful graphical method for sizing and comparing different reactor types and configurations for a specific reaction at constant temperature.

```{note}
**The Levenspiel Plot:** A Levenspiel plot is a graphical tool used in chemical reaction engineering to determine reactor volume. It plots a function related to the inverse reaction rate against the fractional conversion of a reactant. The area on this plot has units of volume, allowing for graphical calculation of reactor sizes.
```

```{admonition} Term Definitions
:class: tip
- $X$: The fractional conversion of the limiting reactant A, defined as $X = \frac{F_{A0} - F_A}{F_{A0}}$. It is a dimensionless quantity ranging from 0 to 1.
- $r_A$: The rate of formation of reactant A (e.g., in $\text{mol/(L}\cdot\text{s)}$). Since A is a reactant being consumed, this value is negative. The rate of reaction is therefore expressed as $-r_A$, which is a positive quantity.
- $F_{A0}$: The molar feed rate of reactant A into the reactor (e.g., in $\text{mol/s}$).
- $\frac{F_{A0}}{-r_A}$: The y-axis of a standard Levenspiel plot. This group has units of volume: $\frac{\text{mol/s}}{\text{mol/(L}\cdot\text{s)}} = \text{L}$.
```

### Graphical Interpretation of Reactor Design Equations

The design equations for CSTRs and PFRs correspond to distinct areas on a Levenspiel plot.

```{important}
**CSTR Design Equation and Graphical Area**
The algebraic design equation for a CSTR is rearranged to isolate the reactor volume, $V$:

$$

V = \frac{F_{A0} X}{-r_A}

$$

This can be interpreted graphically as the area of a rectangle on the Levenspiel plot:

$$

V = X \times \left(\frac{F_{A0}}{-r_A}\right)_{\text{at exit conversion X}}

$$

- **Height**: The value of $\frac{F_{A0}}{-r_A}$ evaluated at the final (exit) conversion, $X$.
- **Width**: The total conversion achieved, $X$.
```

```{important}
**PFR Design Equation and Graphical Area**
The differential design equation for a PFR is integrated to find the required volume, $V$:

$$

V = F_{A0} \int_{0}^{X} \frac{dX}{-r_A}

$$

This corresponds to the **area under the curve** of the Levenspiel plot, integrated from an initial conversion (usually 0) to the final conversion, $X$.

$$

V = \int_{0}^{X} \left(\frac{F_{A0}}{-r_A}\right) dX

$$

```

### Example: Reactor Sizing with a Levenspiel Plot

```{prf:example} Reactor Sizing with a Levenspiel Plot
**Question:** Given a Levenspiel plot for a reaction where the y-value, $\frac{F_{A0}}{-r_A}$, is 50 L for conversions between $X=0.1$ and $X=0.5$. We have three available reactors: a 20 L PFR, a 15 L CSTR, and a 25 L CSTR.
(a) What single reactor results in the largest conversion, and what is that conversion?
(b) If you use two reactors in series, which two and in what order maximizes overall conversion?
```

```{dropdown} Solution Steps
**Solution (Part a): Single Reactor Performance**

**Step 1: Analyze the 15 L CSTR:**
We find the conversion $X$ where the CSTR rectangle area equals 15 L. The height of the rectangle is the y-value at the exit conversion. Assume the y-value is 50 L in the relevant range.

$$

V_{\text{CSTR}} = X \times \left(\frac{F_{A0}}{-r_A}\right)_{\text{exit}}


15 \, \text{L} = X \times (50 \, \text{L}) \implies X = \frac{15}{50} = 0.3

$$

The 15 L CSTR achieves a conversion of **30%**.

**Step 2: Analyze the 25 L CSTR:**
Following the same procedure for the 25 L CSTR:

$$

V_{\text{CSTR}} = X \times \left(\frac{F_{A0}}{-r_A}\right)_{\text{exit}}


25 \, \text{L} = X \times (50 \, \text{L}) \implies X = \frac{25}{50} = 0.5

$$

The 25 L CSTR achieves a conversion of **50%**.

**Step 3: Analyze the 20 L PFR:**
The PFR volume is the area under the curve. The source problem provides a calculation for the area up to a certain conversion, implying a more complex shape than a simple rectangle. Using the given value from the problem source:

$$

V_{\text{PFR}} = \text{Area under curve up to X} = 20 \, \text{L} \quad (\text{given to correspond to } X = 0.3)

$$

Therefore, the 20 L PFR achieves a conversion of **30%**.

**Step 4: Conclusion for Part (a):**
Comparing the maximum conversion from each available reactor:
- 15 L CSTR $\rightarrow$ 30% conversion
- 20 L PFR $\rightarrow$ 30% conversion
- **25 L CSTR $\rightarrow$ 50% conversion**

The **25 L CSTR** provides the highest single-reactor conversion.
```

```{dropdown} Solution Steps
**Solution (Part b): Reactors in Series**

**Step 1: Recall the Reactor Selection Heuristic:**
The optimal reactor choice depends on the shape of the Levenspiel plot, which reflects how the reaction rate changes with conversion.
- **PFR is better** where the curve is **rising** (rate is decreasing). A PFR minimizes the required volume in this region.
- **CSTR is better** where the curve is **falling** (rate is increasing, e.g., in autocatalytic or some adiabatic reactions). A CSTR minimizes the required volume in this region.

**Step 2: Determine the Optimal Sequence:**
The goal is to arrange two reactors to maximize the total area "captured" on the Levenspiel plot.
- **First Reactor:** The problem implies the reaction rate is higher at intermediate conversions (the curve dips), making a CSTR more efficient for the first stage of conversion. The 25 L CSTR is the best single reactor, taking us to an initial conversion of $X=0.5$.
- **Second Reactor:** After the CSTR, the feed to the second reactor is already at 50% conversion. For conversions beyond this point, the Levenspiel curve is typically rising (rate is decreasing). In this region, a PFR is more efficient. Therefore, we should place the 20 L PFR after the CSTR.

**Step 3: Conclusion for Part (b):**
To maximize overall conversion, the optimal arrangement is the **25 L CSTR followed by the 20 L PFR**. This sequence uses each reactor type in the conversion range where it is most volumetrically efficient.
```

## Isothermal Batch Reactors

Batch reactors are simple, closed systems used extensively in the chemical industry, especially for small-scale production, high-value products, and processes requiring flexibility. This section covers their fundamental principles, design considerations, and the material balances required for their analysis.

### Introduction and Key Concepts

A batch reactor is essentially a stirred tank that operates as a closed system. Reactants are charged into the vessel at the beginning of the process, and the products are removed only after the reaction has run for a specific amount of time.

```{note}
**Key Characteristics of a Batch Reactor**
- **Closed System:** No mass is added or removed during the reaction phase. The total mass inside the reactor remains constant.
- **Well-Mixed:** A critical assumption is that the reactor contents are perfectly mixed due to efficient stirring. This means there are no spatial gradients within the reactor volume at any given moment. Concentrations and temperature are uniform throughout.
- **Unsteady-State Operation:** While spatially uniform, the properties of the system (e.g., concentrations of each species) change with time as the reaction proceeds.
```

```{admonition} Term Definitions
:class: tip
**Common Applications and Use Cases**
Batch reactors are favored in situations where continuous flow processes are impractical or uneconomical.
- Small-scale production runs.
- Manufacturing of high-value products like pharmaceuticals or specialty chemicals.
- Processes with very long reaction times (e.g., hours or days).
- Fermentation processes, where preventing contamination is critical.
- Multi-product plants where the same reactor can be used to make different products sequentially.
```

### Heat Transfer and Scale-Up Considerations

Managing the heat of reaction is a critical design challenge, especially when scaling a process from the lab to production.

```{note}
**The Challenge of Scale-Up**
The primary difficulty in scaling up a reactor arises from the relationship between reactor volume (which determines production capacity) and the available heat transfer area.
- **Volume** scales with the cube of a characteristic dimension (e.g., diameter, $D$).
- **Heat Transfer Area** (the vessel surface) scales with the square of that dimension.

This means that as a reactor gets larger, its volume increases much faster than its surface area. The ratio of area to volume decreases, making it progressively harder to add or remove heat.
```

```{important}
**Geometric Scaling Relationships**

$$

\text{Volume: } V \propto D^3


\text{Area: } A \propto D^2


\frac{\text{Heat Transfer Area}}{\text{Volume}} = \frac{A}{V} \propto \frac{D^2}{D^3} = \frac{1}{D}

$$

```

```{admonition} Term Definitions
:class: tip
**Other Scale-Up Issues**
- **Mixing:** Achieving uniform mixing is more difficult and energy-intensive in a large vessel. Dead zones with poor mixing can lead to non-uniform temperatures and concentrations.
- **Startup Time:** Heating, cooling, and charging a large reactor takes significantly longer, reducing overall productivity.
- **Materials of Construction:** Lab reactors are often glass, while industrial reactors are metal. The metal surface can have unintended catalytic or inhibitory effects on the reaction chemistry.
```

### Material Balances on Tank Reactors

To model the behavior of a reactor, we perform a mole balance on each chemical species.

```{note}
**The General Mole Balance Principle**
The fundamental principle for any species in any control volume is:

$$

\text{Rate of Accumulation} = \text{Rate of Inflow} - \text{Rate of Outflow} + \text{Rate of Generation by Reaction}

$$

```

```{admonition} Term Definitions
:class: tip
- $N_i$: The number of moles of component $i$ within the reactor volume.
- $F_{i0}, F_i$: Molar flow rates of component $i$ *in* and *out* of the reactor (moles/time).
- $r_i$: The rate of formation of component $i$ per unit volume (moles/(volume$\cdot$time)). A negative value indicates consumption.
- $V$: The volume of the reacting mixture in the reactor.
- $C_i$: The concentration of component $i$ ($N_i/V$).
- $X$: The fractional conversion of a reactant.
```

```{important}
**General Mole Balance Equation**
For any component A, the mole balance is written as a differential equation:

$$

\frac{dN_A}{dt} = F_{A0} - F_A + r_A V \quad \text{(Equation 1)}

$$

This general equation is simplified for different reactor types based on their flow characteristics.
```

```{important}
**Batch Reactor Mole Balance**
In a batch reactor, there is no inflow or outflow during the reaction, so $F_{A0} = 0$ and $F_A = 0$. The general mole balance (Equation 1) simplifies to:

$$

\frac{dN_A}{dt} = r_A V

$$

For liquid-phase reactions with constant volume, we can write this in terms of concentration ($N_A = C_A V$):

$$

\frac{dC_A}{dt} = r_A

$$

```

### Example: Batch Reactor with Multiple Reactions

```{prf:example} Mole Balances for a Multi-Reaction System
**Question:** Consider an isothermal batch reactor where the following three liquid-phase reactions occur. The rates of reaction ($r_1, r_2, r_3$) are given in moles per liter per second. Write the mole balance equation for each species (A, B, C, D, E).

$$

\begin{align*}
    \text{Reaction 1:} \quad & A + B \xrightarrow{k_1} C & r_1 &= k_1 C_A C_B \\
    \text{Reaction 2:} \quad & C \xrightarrow{k_2} 2E & r_2 &= k_2 C_C \\
    \text{Reaction 3:} \quad & 2A \xrightarrow{k_3} D & r_3 &= k_3 C_A^2
\end{align*}

$$

```

```{dropdown} Solution Steps
We apply the batch reactor mole balance, $\frac{dN_i}{dt} = r_i V$, to each component. The net rate of formation for a species, $r_i$, is the sum of its rates of formation in every reaction, accounting for stoichiometry ($\nu_{ij}$, which is negative for reactants and positive for products). The general form is $r_i = \sum_{j} \nu_{ij} r_j$.

**Step 1: Mole Balance on A:**
Component A is consumed in Reaction 1 ($\nu_{A1} = -1$) and Reaction 3 ($\nu_{A3} = -2$).

$$

r_A = (-1)r_1 + (-2)r_3 = -k_1 C_A C_B - 2k_3 C_A^2


\frac{dN_A}{dt} = r_A V = (-k_1 C_A C_B - 2k_3 C_A^2) V

$$

**Step 2: Mole Balance on B:**
Component B is consumed only in Reaction 1 ($\nu_{B1} = -1$).

$$

r_B = (-1)r_1 = -k_1 C_A C_B


\frac{dN_B}{dt} = r_B V = (-k_1 C_A C_B) V

$$

**Step 3: Mole Balance on C:**
Component C is formed in Reaction 1 ($\nu_{C1} = +1$) and consumed in Reaction 2 ($\nu_{C2} = -1$).

$$

r_C = (+1)r_1 + (-1)r_2 = k_1 C_A C_B - k_2 C_C


\frac{dN_C}{dt} = r_C V = (k_1 C_A C_B - k_2 C_C) V

$$

**Step 4: Mole Balance on D:**
Component D is formed only in Reaction 3 ($\nu_{D3} = +1$).

$$

r_D = (+1)r_3 = k_3 C_A^2


\frac{dN_D}{dt} = r_D V = (k_3 C_A^2) V

$$

**Step 5: Mole Balance on E:**
Component E is formed only in Reaction 2 ($\nu_{E2} = +2$).

$$

r_E = (+2)r_2 = 2k_2 C_C


\frac{dN_E}{dt} = r_E V = (2k_2 C_C) V

$$

**Step 6: Solving the System:**
This gives a system of five coupled ordinary differential equations (ODEs). To find the number of moles of each species over time, this system must be solved numerically using software. The required inputs are the initial number of moles of each species ($N_{A0}, N_{B0}, N_{C0}, \dots$), the constant reactor volume ($V$), and the values of the rate constants ($k_1, k_2, k_3$) at the isothermal operating temperature.
```

### Example: Copolymerization in a Batch Reactor

```{prf:example} Copolymerization of Styrene and Butadiene
**Question:** Styrene (S) and butadiene (B) are copolymerized in an isothermal batch reactor. The $27 \, \text{m}^3$ reactor was charged with $2,200 \, \text{kg}$ of styrene and $5,000 \, \text{kg}$ of butadiene. The polymerization is first order in S and first order in B, and the rate constant is $k = 0.036 \, \text{m}^3\text{/(kmol}\cdot\text{h)}$. The reaction is $S + 3.2 B \rightarrow \text{polymer}$, and constant density is assumed. What are the concentrations of S and B after 10 h?
```

```{dropdown} Solution Steps
**Step 1: Analyze the Problem and Define the Goal:**
The core task is to model a second-order reaction ($r = -kC_SC_B$) in a constant-volume batch reactor. This requires solving a system of coupled ordinary differential equations (ODEs) that describe the change in concentration of each reactant over time. The goal is to find the concentrations $C_S$ and $C_B$ at $t = 10$ h.

**Step 2: Calculate Initial Moles and Concentrations:**
To solve the ODEs, we first need the initial conditions ($C_{S0}$, $C_{B0}$) at $t=0$.
Molecular Weight of Styrene (S, $C_8H_8$): $104.15 \, \text{kg/kmol}$. Molecular Weight of Butadiene (B, $C_4H_6$): $54.09 \, \text{kg/kmol}$.

**Initial Molar Amounts**

$$

N_{S0} = \frac{2200 \, \text{kg}}{104.15 \, \text{kg/kmol}} = 21.12 \, \text{kmol}


N_{B0} = \frac{5000 \, \text{kg}}{54.09 \, \text{kg/kmol}} = 92.44 \, \text{kmol}

$$

**Initial Concentrations**

$$

C_{S0} = \frac{N_{S0}}{V} = \frac{21.12 \, \text{kmol}}{27 \, \text{m}^3} = \textbf{0.782 kmol/m}^3


C_{B0} = \frac{N_{B0}}{V} = \frac{92.44 \, \text{kmol}}{27 \, \text{m}^3} = \textbf{3.424 kmol/m}^3

$$

**Step 3: Formulate the Mole Balance Equations:**
For a constant-volume batch reactor, the mole balance for any species $i$ simplifies to $\frac{dC_i}{dt} = r_i$.
The rate of formation of Styrene is $r_S = -k C_S C_B$.
From the stoichiometry, 3.2 moles of B are consumed for every mole of S. Therefore, the rate of formation of Butadiene is $r_B = -3.2 (k C_S C_B)$.
This gives us the system of ODEs to solve:

**System of Differential Equations**

$$

\frac{dC_S}{dt} = -k C_S C_B


\frac{dC_B}{dt} = -3.2 k C_S C_B

$$

**Step 4: Define the Solution Approach:**
The problem is now fully defined as an initial value problem. We must solve the system of ODEs with the known rate constant and initial concentrations over the specified time interval.

**Summary for Numerical Solver**
Equations to Solve:

$$

\begin{align*}
    \frac{dC_S}{dt} &= -0.036 \cdot C_S \cdot C_B \\
    \frac{dC_B}{dt} &= -3.2 \cdot (0.036) \cdot C_S \cdot C_B = -0.1152 \cdot C_S \cdot C_B
\end{align*}

$$

Initial Conditions (at $t=0$):

$$

\begin{align*}
    C_S(0) &= 0.782 \, \text{kmol/m}^3 \\
    C_B(0) &= 3.424 \, \text{kmol/m}^3
\end{align*}

$$

Integration Interval: from $t=0$ to $t=10$ h.

This system would be integrated using a numerical solver (e.g., in MATLAB, Python, or Polymath) to find the final concentrations $C_S(10)$ and $C_B(10)$.
```

### Example: Pseudo-First-Order Reaction

```{prf:example} Hydration with a Component in Large Excess
**Question:** The elementary, irreversible liquid-phase hydration of butylene oxide (A) produces butylene glycol (C): $C_4H_8O \text{ (A)} + H_2O \text{ (B)} \rightarrow C_4H_{10}O_2 \text{ (C)}$. The reaction is conducted using water (B) as the solvent, so it is in large excess. The initial concentration of butylene oxide is $C_{A0} = 0.25$ mol/L. The rate constant is $k' = 8.3 \times 10^{-4}$ L/(mol·min) at 323 K. A batch reactor is used.
(a) Determine the final concentration of butylene oxide after 45 min.
(b) A consultant suggests enhancing the rate by continuously feeding water at 25 L/min into the initial 500 L volume. Will this proposal increase, decrease, or have no effect on the time required to reach a given conversion?
```

```{dropdown} Solution Steps
**Solution (Part a): Final Concentration Calculation**

**Step 1: Simplify the Rate Law via Pseudo-First-Order Approximation:**
When a second-order reaction ($r = -k'C_AC_B$) involves one reactant (B) in large excess (e.g., a solvent), its concentration $C_B$ remains essentially constant throughout the reaction. We can combine the true rate constant $k'$ and the constant concentration $C_B$ into a new, "pseudo-first-order" rate constant, $k$.
Molar density of water: $C_B \approx \frac{1000 \, \text{g/L}}{18.015 \, \text{g/mol}} \approx 55.5$ mol/L.
Since $C_B \gg C_{A0}$ ($55.5 \gg 0.25$), the assumption is valid.

$$

r_A = -k' C_A C_B \approx -(k' C_B) C_A = -k C_A


k = k' C_B = (8.3 \times 10^{-4} \, \frac{\text{L}}{\text{mol}\cdot\text{min}}) \cdot (55.5 \, \frac{\text{mol}}{\text{L}}) = 0.046065 \, \text{min}^{-1}

$$

**Step 2: Apply the First-Order Integrated Rate Law:**
For a first-order reaction in a constant-volume batch reactor:

$$

\ln\left(\frac{C_{A0}}{C_A}\right) = k t

$$

Solving for the final concentration, $C_A$, after $t = 45$ min:

$$

\ln\left(\frac{0.25 \, \text{mol/L}}{C_A}\right) = (0.046065 \, \text{min}^{-1}) \cdot (45 \, \text{min}) = 2.073


\frac{0.25}{C_A} = e^{2.073} \approx 7.948


C_A = \frac{0.25}{7.948} \approx \textbf{0.0315 mol/L}

$$

```

```{dropdown} Solution Steps
**Solution (Part b): Effect of Adding More Solvent**

**Step 1: Analyze the Proposal using a Mole Basis:**
The proposal involves changing the volume, so analyzing concentrations can be misleading. The fundamental measure of reaction progress is the number of **moles** converted. Let's write the mole balance for the product, C. This is now a semi-batch reactor, but the core principle holds.

$$

\frac{dN_C}{dt} = r_C V

$$

**Step 2: Examine the Rate of Molar Production:**
The rate of formation of product C per unit volume is $r_C = k' C_A C_B$. Substituting this into the mole balance gives:

$$

\frac{dN_C}{dt} = (k' C_A C_B) V

$$

Now, express the concentration of A in terms of moles and the changing volume, $C_A = N_A/V$.

**Molar Rate of Production**

$$

\frac{dN_C}{dt} = \left(k' \frac{N_A}{V} C_B\right) V = k' C_B N_A

$$

Using the pseudo-first-order constant $k = k'C_B$:

$$

\frac{dN_C}{dt} = k N_A

$$

**Step 3: Conclusion:**
The final equation is the key insight. The rate at which **moles of product C are formed** depends only on the number of moles of reactant A present ($N_A$) and the pseudo-rate constant ($k$). It is **independent of the total reactor volume $V$**.
- When adding more water, the concentration of A ($C_A = N_A/V$) decreases because the volume $V$ increases. This *lowers* the volumetric reaction rate ($r_C$).
- At the same time, the total reactor volume $V$ is increasing.

As the mole balance explicitly shows, these two effects exactly cancel each other out. The rate of conversion of moles of A is unchanged. Therefore, the consultant's proposal will have **no effect** on the time required to reach a specific conversion (i.e., to convert a specific number of moles of A).
```

## Isothermal Semibatch Reactors

A semibatch reactor is a variation of a batch reactor where one or more reactants are added to the reactor, or products are removed from the reactor, during the course of the reaction. This mode of operation provides additional control over concentration and temperature, making it a versatile tool for chemical synthesis.

### Fundamental Equations

The dynamic behavior of a semibatch reactor is described by a set of simultaneous ordinary differential equations derived from mole and volume balances.

```{admonition} Term Definitions
:class: tip
- $N_i$: Moles of component $i$ in the reactor at time $t$.
- $F_{i0}, F_i$: Molar flow rates of $i$ entering and leaving the reactor (mol/s).
- $v_0, v$: Volumetric flow rates into and out of the reactor (L/s).
- $V$: Volume of the reactor contents at time $t$ (L).
- $k$: Reaction rate constant.
- $C_i$: Molar concentration of component $i$ in the reactor, $C_i = N_i/V$ (mol/L).
```

```{important}
**General Mole and Volume Balances**
For an irreversible reaction $A + B \rightarrow 2C$ with a rate law of $r = k C_A^n C_B^m$:
- **Mole Balances (moles):**
  
  $$

  \begin{align*}
      \frac{dN_A}{dt} &= F_{A0} - F_A - kC_A^n C_B^m V \\
      \frac{dN_B}{dt} &= F_{B0} - F_B - kC_A^n C_B^m V \\
      \frac{dN_C}{dt} &= F_{C0} - F_C + 2kC_A^n C_B^m V
  \end{align*}

  $$

- **Volume Balance (liquid phase):**
  
  $$

  \frac{dV}{dt} = v_0 - v

  $$

To solve this system, initial conditions ($N_{A0}, N_{B0}, N_{C0}, V_0$) at $t=0$ are required.
```

### Conceptual Overview and Applications

Semibatch reactors are typically stirred tanks operating in a non-steady-state, open-system mode, primarily used for liquid-phase reactions.

```{note}
**Key Applications of Semibatch Reactors**
This reactor type is chosen to exert specific control over the reaction environment.
1. **Selectivity Control:** By adding one reactant (A) slowly to another (B), the concentration of A can be kept low. This is advantageous if an undesired side reaction has a higher reaction order with respect to A than the desired reaction.
2. **Sequential Reactions:** To prevent side reactions between reactants of different steps (e.g., B and D in $A+B\rightarrow C; C+D\rightarrow E$), one can react A and B to completion first, then add D.
3. **Heat Transfer and Safety:** For highly exothermic reactions, adding a reactant slowly controls the reaction rate, and thus the rate of heat generation. This prevents dangerous temperature spikes (thermal runaway).
4. **Shifting Equilibrium:** If a reaction is reversible ($A+B \leftrightarrow C+D$) and a product (D) is a gas, continuously removing D from the liquid phase will shift the equilibrium to the right, increasing yield.
5. **Sparingly Soluble Reactants:** Gaseous reactants like H$_2$ or O$_2$ have low solubility in liquids. They must be continuously bubbled (fed) through the reactor to maintain their concentration in the liquid phase.
```

### Example: Gas-Liquid Hydrogenation

```{prf:example} Hydrogenation in a Semibatch Reactor
**Question:** In an isothermal semibatch reactor, a liquid-phase reactant A is hydrogenated to produce a liquid product P: $A(\text{liq}) + H_2(\text{g}) \rightarrow P(\text{liq})$. The reactor initially contains $N_{A0} = 150$ mol of A. Hydrogen gas is fed from a cylinder to maintain a constant reactor pressure of 3 bar. The rate law is $-r_A = k C_A P_{H_2}$, where $k = 0.0074$ bar$^{-1}$min$^{-1}$. Assume the volume of the liquid phase is constant.
(a) Determine the time required to reach 80% conversion of A.
(b) Derive an expression for the molar flow rate of hydrogen into the reactor as a function of time.
```

```{dropdown} Solution Steps
**Solution (Part a): Time to Reach 80% Conversion**

**Step 1: Mole Balance on A:**
Reactant A is only present in the liquid phase and is not fed or removed. Therefore, its mole balance is identical to that of a batch reactor. Let $V_L$ be the constant liquid volume.

$$

\frac{dN_A}{dt} = r_A V_L = (-k C_A P_{H_2}) V_L

$$

Since $V_L$ is constant, we can use $N_A = C_A V_L$ and simplify to a concentration basis:

$$

\frac{dC_A}{dt} = -k C_A P_{H_2}

$$

**Step 2: Integrate the Rate Law:**
The key simplification is that hydrogen is supplied to maintain a constant pressure, so $P_{H_2} = 3$ bar is constant throughout the reaction. The rate law simplifies to a pseudo-first-order form, $r_A = -k'C_A$, where the new constant is $k' = k \cdot P_{H_2}$. We can now separate variables and integrate the simplified rate law:

$$

\int_{C_{A0}}^{C_A} \frac{dC_A}{C_A} = \int_0^t -k P_{H_2} dt \implies \ln\left(\frac{C_A}{C_{A0}}\right) = -k P_{H_2} t

$$

**Step 3: Solve for Time:**
The target is 80% conversion ($X_A=0.8$). At this point, the final concentration is $C_A = C_{A0}(1-X_A) = 0.2 C_{A0}$. The concentration ratio is $C_A/C_{A0} = 0.2$.

$$

\ln(0.2) = -(0.0074 \, \text{bar}^{-1}\text{min}^{-1}) \cdot (3 \, \text{bar}) \cdot t


-1.6094 = -0.0222 \cdot t


t = \frac{1.6094}{0.0222} = \textbf{72.5 min}

$$

```

```{dropdown} Solution Steps
**Solution (Part b): Hydrogen Flow Rate vs. Time**

**Step 1: Mole Balance on Gaseous H$_2$:**
Hydrogen is fed into the reactor ($F_{H_2,in}$) and consumed by the reaction. From the 1:1 stoichiometry, its rate of formation is $r_{H_2} = r_A = -k C_A P_{H_2}$.

$$

\frac{dN_{H_2}}{dt} = F_{H_2,in} + r_{H_2} V_L = F_{H_2,in} - k C_A P_{H_2} V_L

$$

**Step 2: Apply Simplification for Constant Gas Moles:**
The problem states that the reactor pressure, temperature, and volume are constant. According to the ideal gas law ($PV=nRT$), if P, V, and T are constant for the gas phase, then the number of moles of hydrogen gas in the reactor headspace, $N_{H_2}$, must also be constant. Therefore, the accumulation term is zero:

$$

\frac{dN_{H_2}}{dt} = 0

$$

**Step 3: Derive the Flow Rate Expression:**
The mole balance simplifies to an algebraic equation for the inlet flow rate:

$$

0 = F_{H_2,in} - k C_A P_{H_2} V_L \implies F_{H_2,in} = k P_{H_2} V_L C_A

$$

To get the flow rate as a function of time, we need the expression for $C_A(t)$ from Part (a):

$$

C_A(t) = C_{A0} e^{-k P_{H_2} t}

$$

Substituting this in and recognizing that $C_{A0} V_L = N_{A0}$ (the initial moles of A):

**Hydrogen Feed Rate as a Function of Time**

$$

F_{H_2,in}(t) = k P_{H_2} N_{A0} e^{-k P_{H_2} t}

$$

This result shows that the hydrogen flow rate required is highest at $t=0$ when the concentration of A is highest, and it decays exponentially as reactant A is consumed.
```

### Example: Catalytic Semibatch Reaction

```{prf:example} Semibatch Reaction with Changing Volume
**Question:** A catalytic reaction, $A \rightarrow C$, takes place in the liquid phase of an isothermal semibatch reactor. The rate law is $r_A = -k C_A C_B$, with $k = 0.25$ L/(mol·min), where B is the catalyst. Initially, the reactor contains 2700 L of a solution with $C_{A0} = 20.0$ mol/L. The initial concentration of catalyst B is zero. Starting at $t=0$, a solution containing 0.05 mol/L of B is fed to the reactor at a flow rate of 12.5 L/min. How many moles of product C are in the reactor after 200 min?
```

```{dropdown} Solution Steps
**Step 1: Strategy and Initial Conditions:**
This system involves changing volume and coupled concentrations, requiring a numerical solution. We first define all initial conditions and constant feed rates.
Initial Conditions ($t=0$): $V(0) = 2700$ L, $N_A(0) = C_{A0} V(0) = (20.0 \, \text{mol/L}) \cdot (2700 \, \text{L}) = 54,000$ mol, $N_B(0) = 0$ mol (Catalyst is not present initially), $N_C(0) = 0$ mol (Product is not present initially).
Feed Stream ($t > 0$): Volumetric flow rate in: $v_0 = 12.5$ L/min.
Molar feed rate of B: $F_{B0} = v_0 C_{B,in} = (12.5 \, \text{L/min}) (0.05 \, \text{mol/L}) = 0.625$ mol/min.
Molar feed rates of A and C are zero: $F_{A0} = 0, F_{C0} = 0$.

**Step 2: Formulate the System of Differential Equations:**
We need mole balances for A, B, and C, and a volume balance. The concentrations $C_A=N_A/V$ and $C_B=N_B/V$ must be calculated at each time step.

Volume Balance: Flow in only.
$\frac{dV}{dt} = v_0 = 12.5$

Mole Balance on A (Reactant): No flow, only consumption.
$\frac{dN_A}{dt} = r_A V = -k C_A C_B V$

Mole Balance on B (Catalyst): Flow in, no consumption.
$\frac{dN_B}{dt} = F_{B0} = 0.625$

Mole Balance on C (Product): No flow, only formation.
$\frac{dN_C}{dt} = r_C V = -r_A V = k C_A C_B V$

**Step 3: Summarize for Numerical Solution:**
The complete system of ODEs and initial conditions is prepared for a numerical solver.

**System for Numerical Solver**
Differential Equations:

$$

\begin{align*}
    \frac{dV}{dt} &= 12.5 \\
    \frac{dN_A}{dt} &= -0.25 \left(\frac{N_A}{V}\right) \left(\frac{N_B}{V}\right) V = -0.25 \frac{N_A N_B}{V} \\
    \frac{dN_B}{dt} &= 0.625 \\
    \frac{dN_C}{dt} &= 0.25 \left(\frac{N_A}{V}\right) \left(\frac{N_B}{V}\right) V = 0.25 \frac{N_A N_B}{V}
\end{align*}

$$

Initial Conditions (at $t=0$): $V=2700$, $N_A=54000$, $N_B=0$, $N_C=0$.
Integration Interval: from $t=0$ to $t=200$ min.

**Step 4: Final Result:**
Solving this system with a numerical package (such as POLYMATH, MATLAB, or Python) yields the number of moles of each component at $t=200$ min. The result for product C is:

$$

N_C(200 \text{ min}) \approx \textbf{28,000 moles}

$$

```

## Isothermal Continuous Stirred Tank Reactors (CSTRs)

The Continuous Stirred-Tank Reactor (CSTR) is a common type of reactor used in industrial processing. In its ideal form, it operates at steady state with perfect mixing. This key assumption implies that the concentration and temperature of the effluent stream are the same as the conditions everywhere inside the reactor. This section focuses on the analysis of isothermal CSTRs.

### Fundamental Equations

The design of a CSTR is based on a steady-state mole balance, which results in an algebraic equation rather than a differential equation.

```{admonition} Term Definitions
:class: tip
- $F_{i0}, F_i$: Molar flow rates of component $i$ entering and leaving the reactor (mol/s).
- $V$: Volume of the reactor contents (L).
- $v_0$ or $v$: Volumetric flow rate (L/s). For liquid-phase systems, this is often assumed constant ($v_0 = v$).
- $k$: Reaction rate constant.
- $C_i$: Molar concentration of component $i$ in the reactor and in the exit stream (mol/L).
- $X_A$: Fractional conversion of reactant A.
```

```{important}
**CSTR Steady-State Mole Balance**
The general form is: $\text{Inflow} - \text{Outflow} + \text{Generation by Reaction} = 0$.
For a reaction $A \rightarrow \text{Products}$ with rate law $-r_A = k C_A^n$:

$$

F_{A0} - F_A + r_A V = 0

$$

Substituting $r_A = -kC_A^n$ and $F_A = vC_A$ (for constant liquid density):

$$

v C_{A0} - v C_A - kC_A^n V = 0

$$

This algebraic equation must be solved for the unknown outlet concentration, $C_A$.
```

```{important}
**Key CSTR Relationships (Constant Density)**
- **Space Time ($\tau$):** The average time a fluid element spends in the reactor.
  
  $$

  \tau = \frac{V}{v}

  $$

- **Conversion ($X_A$):** The fraction of reactant A that has been converted.
  
  $$

  X_A = \frac{F_{A0} - F_A}{F_{A0}} = \frac{v C_{A0} - v C_A}{v C_{A0}} = \frac{C_{A0} - C_A}{C_{A0}}

  $$

- **Concentration from Conversion:**
  
  $$

  C_A = C_{A0}(1-X_A)

  $$

```

### Example: Second-Order Reaction in a CSTR

```{prf:example} Second-Order Hydrolysis in a CSTR
**Question:** The hydrolysis of acetic anhydride (A) to form acetic acid is carried out in a 1250-L CSTR. The feed contains 2.5 mol/L acetic anhydride and 50.0 mol/L of water (W). The reaction, $(CH_3CO)_2O + H_2O \rightarrow 2CH_3COOH$, is first order in acetic anhydride and first order in water. At the reactor temperature, the rate constant is $k = 0.075$ L/(mol·s). The feed flow rate is 15 L/s. What is the conversion of acetic anhydride?
```

```{dropdown} Solution Steps
**Step 1: Formulate the Steady-State Mole Balances:**
We must solve the steady-state mole balances for both reactants, acetic anhydride (A) and water (W).
Rate Law: $-r_A = k C_A C_W$. Stoichiometry: A and W react in a 1:1 ratio, so their rates of formation are equal: $r_A = r_W$.
The general mole balance for species $i$ is $F_{i0} - F_i + r_i V = 0$.
Assuming constant volumetric flow rate $v$:

$$

\begin{align*}
    v C_{A0} - v C_A + r_A V = 0 &\implies v(C_{A0} - C_A) - k C_A C_W V = 0 \\
    v C_{W0} - v C_W + r_W V = 0 &\implies v(C_{W0} - C_W) - k C_A C_W V = 0
\end{align*}

$$

**Step 2: Substitute Known Values to Form a System of Equations:**
We have a system of two algebraic equations with two unknowns: the outlet concentrations $C_A$ and $C_W$.
Given: $v = 15$ L/s, $V = 1250$ L, $C_{A0} = 2.5$ mol/L, $C_{W0} = 50.0$ mol/L, $k = 0.075$ L/(mol·s).

**System of Algebraic Equations**
Substituting the values:

$$

\begin{align*}
    15(2.5 - C_A) - (0.075) C_A C_W (1250) &= 0 \\
    15(50.0 - C_W) - (0.075) C_A C_W (1250) &= 0
\end{align*}

$$

Simplifying:

$$

\begin{align*}
    37.5 - 15 C_A - 93.75 C_A C_W &= 0 \\
    750 - 15 C_W - 93.75 C_A C_W &= 0
\end{align*}

$$

**Step 3: Solve the System of Equations:**
This system of non-linear equations must be solved simultaneously. While analytical substitution is possible, a numerical solver is a more robust approach for complex systems.
Based on the provided solution from such a solver:

$$

C_A = 0.081 \, \text{mol/L} \quad \text{and} \quad C_W = 47.58 \, \text{mol/L}

$$

**Step 4: Calculate the Final Conversion:**
The conversion of acetic anhydride (A) is calculated from the inlet and outlet concentrations.

$$

X_A = \frac{C_{A0} - C_A}{C_{A0}} = \frac{2.5 - 0.081}{2.5} = \frac{2.419}{2.5} = 0.9676

$$

The conversion is **97%**.
```

### Example: Reversible Reaction in a CSTR

```{prf:example} Reversible Reaction with a Change in Flow Rate
**Question:** The liquid-phase, reversible reaction $A + B \rightleftharpoons 2C$ occurs in an isothermal CSTR. The feed contains equimolar amounts of A and B. The conversion of A is measured to be 60.0%. The equilibrium conversion under the same feed conditions is 80.0%. If the volumetric flow rate is increased by 50.0%, what is the new conversion of A? The forward reaction is first order in A and B; the reverse reaction is second order in C.
```

```{dropdown} Solution Steps
**Solution (Part 1 of 3): Use Equilibrium Data**
This problem is solved by finding a key dimensionless group that characterizes the reactor system and then using it to predict performance under new conditions.

**Step 1: Relate Rate Constants using Equilibrium Conversion ($X_e$):**
The net rate of reaction for A is $-r_A = k_1 C_A C_B - k_2 C_C^2$.
At equilibrium, the net rate is zero ($-r_A = 0$) and the conversion is $X_e = 0.80$.

$$

k_1 C_{A,e} C_{B,e} = k_2 C_{C,e}^2

$$

We express the equilibrium concentrations in terms of the initial concentration $C_{A0}$ and $X_e$. Since the feed is equimolar, $C_{B0} = C_{A0}$.
- $C_{A,e} = C_{A0}(1-X_e) = C_{A0}(1-0.80) = 0.2 C_{A0}$
- $C_{B,e} = C_{A0}(1-X_e) = 0.2 C_{A0}$
- $C_{C,e} = 2 C_{A0} X_e = 2 C_{A0}(0.80) = 1.6 C_{A0}$

Substituting these into the equilibrium expression allows us to find the ratio of rate constants:

$$

k_1 (0.2 C_{A0})(0.2 C_{A0}) = k_2 (1.6 C_{A0})^2


k_1 (0.04 C_{A0}^2) = k_2 (2.56 C_{A0}^2)

$$

**Relationship Between Rate Constants**

$$

k_1 = \frac{2.56}{0.04} k_2 \implies k_1 = 64 k_2

$$

```

```{dropdown} Solution Steps
**Solution (Part 2 of 3): Characterize the Initial Reactor State**

**Step 1: Use Initial Operating Data to Find a Reactor Constant Group:**
For the initial case (Case 1), the conversion is $X_1 = 0.60$ at a flow rate $v_1$. We use the CSTR mole balance:

$$

v_1(C_{A0} - C_{A1}) + r_{A1} V = 0 \implies v_1 C_{A0} X_1 = -r_{A1} V

$$

First, find the concentrations at $X_1 = 0.60$:
- $C_{A1} = C_{A0}(1-X_1) = 0.4 C_{A0}$
- $C_{B1} = C_{A0}(1-X_1) = 0.4 C_{A0}$
- $C_{C1} = 2 C_{A0} X_1 = 1.2 C_{A0}$

Now, substitute these into the rate law, using $k_1=64k_2$:

$$

-r_{A1} = k_1 C_{A1} C_{B1} - k_2 C_{C1}^2 = 64k_2(0.4C_{A0})^2 - k_2(1.2C_{A0})^2


-r_{A1} = k_2 C_{A0}^2 [64(0.16) - 1.44] = k_2 C_{A0}^2 [10.24 - 1.44] = 8.8 k_2 C_{A0}^2

$$

Substitute this rate back into the mole balance:

$$

v_1 C_{A0} (0.60) = (8.8 k_2 C_{A0}^2) V

$$

Rearranging gives us a key dimensionless group that combines all the unknown system parameters:

**Dimensionless Reactor Group**

$$

\frac{k_2 C_{A0} V}{v_1} = \frac{0.60}{8.8} \approx 0.06818

$$

```

```{dropdown} Solution Steps
**Solution (Part 3 of 3): Solve for the New Conversion**

**Step 1: Set up the Mole Balance for the New Condition:**
The flow rate is increased by 50%, so the new flow rate is $v_2 = 1.5 v_1$. We seek the new conversion, $X_2$. The CSTR design equation for this new case (Case 2) is:

$$

v_2 C_{A0} X_2 = -r_{A2} V

$$

The rate law $-r_{A2}$ can be expressed in terms of the new conversion $X_2$:

$$

-r_{A2} = k_1 C_{A2}C_{B2} - k_2 C_{C2}^2 = k_2 C_{A0}^2 [64(1-X_2)^2 - 4X_2^2]

$$

Substitute this into the design equation:

$$

(1.5 v_1) C_{A0} X_2 = k_2 C_{A0}^2 [64(1-X_2)^2 - 4X_2^2] V

$$

Rearrange the equation to isolate the dimensionless group we found in the previous step:

$$

X_2 = \left(\frac{k_2 C_{A0} V}{v_1}\right) \frac{[64(1-X_2)^2 - 4X_2^2]}{1.5}

$$

**Step 2: Solve for the New Conversion $X_2$:**
Substitute the value of the dimensionless group (0.06818) into the equation:

$$

X_2 = (0.06818) \frac{64(1-2X_2+X_2^2) - 4X_2^2}{1.5}


1.5 X_2 = 0.06818 [64 - 128X_2 + 64X_2^2 - 4X_2^2]


1.5 X_2 = 0.06818 [60X_2^2 - 128X_2 + 64]

$$

Multiplying and rearranging gives a quadratic equation:

$$

22.0 X_2 = 60X_2^2 - 128X_2 + 64

$$

**Final Quadratic Equation for Conversion**

$$

60X_2^2 - 150X_2 + 64 = 0

$$

Solving this using the quadratic formula yields two roots: $X_2 \approx 1.95$ and $X_2 \approx 0.546$. Since conversion cannot be greater than 1, the only physically meaningful answer is $X_2=0.546$.

The new conversion is **55%**. This result is logical, as increasing the flow rate decreases the reactor's space time, leading to a lower conversion.
```

## Isothermal Plug Flow Reactors (PFRs)

The Plug Flow Reactor (PFR) model is used to describe chemical reactions in continuous, flowing systems, typically within a tube or pipe. It is a cornerstone of chemical reaction engineering, particularly for large-scale, continuous processes where reactants are converted as they flow along the length of the reactor.

### Fundamental Equations

The design of a PFR is based on a differential mole balance taken over a differential segment of the reactor volume. For an irreversible reaction $A \rightarrow 2B$ with a rate law of $-r_A = k C_A^n$:

```{admonition} Term Definitions
:class: tip
- $F_i$: Molar flow rate of component $i$ at a specific point in the reactor (mol/s).
- $V$: Cumulative reactor volume from the inlet to a specific point (L). $V_T$ is the total reactor volume.
- $z, L$: Distance down the reactor and total reactor length (m).
- $A_c$: The cross-sectional area of the tubular reactor (m$^2$).
- $k$: Reaction rate constant.
- $C_A$: Molar concentration of A (mol/L).
- $v, v_0$: Volumetric flow rate at a point in the reactor and at the inlet (L/s).
- $F_T$: Total molar flow rate (mol/s).
- $P, T, R$: Absolute pressure (bar), absolute temperature (K), and the ideal gas constant.
- $X_A$: Fractional conversion of component A.
```

```{important}
**PFR Differential Mole Balances (Volume Basis)**
The change in molar flow rate with respect to reactor volume is:

$$

\begin{align*}
    \frac{dF_A}{dV} &= r_A = -kC_A^n \\
    \frac{dF_B}{dV} &= -2r_A = 2kC_A^n
\end{align*}

$$

```

### Conceptual Model of a PFR

The PFR model simplifies the complex fluid dynamics within a tubular reactor by making several key assumptions.

```{note}
**The Ideal Plug Flow Model**
- **Plug Flow:** The fluid is assumed to flow in discrete "plugs," as if separated by invisible pistons.
- **No Axial Mixing:** There is no mixing or diffusion in the direction of flow. Material in one plug does not mix with the material in the plugs ahead of or behind it.
- **Perfect Radial Mixing:** Within each plug (radially, across the tube's diameter), properties like concentration and temperature are assumed to be uniform. This is an idealization; real flows often have velocity and temperature profiles.
- **Batch Reactor Analogy:** Each plug moving through the PFR can be viewed as a tiny, isolated batch reactor that reacts for a specific amount of time equal to its residence time in that segment.
- **Uniform Residence Time:** A key consequence of the model is that all molecules spend the exact same amount of time in the reactor. This is fundamentally different from a CSTR, which exhibits a wide distribution of residence times.
```

### Mole Balance Derivation for a PFR

The PFR design equation is derived by performing a mole balance on a differential slice of the reactor volume, $dV$, at steady state. For a component A, the general mole balance on the differential volume $dV$ is:

```{important}
**General Mole Balance:**

$$

(\text{Rate of Accumulation}) = (\text{Rate In}) - (\text{Rate Out}) + (\text{Rate of Generation})

$$

```

At steady state, the accumulation term is zero. The balance becomes:

```{important}
**Steady-State Mole Balance:**

$$

0 = F_A\big|_V - F_A\big|_{V+dV} + r_A \cdot dV

$$

```

Here, $r_A$ is the rate of formation of A per unit volume, and $F_A\big|_{V+dV}$ can be expressed using a Taylor series as $F_A\big|_{V+dV} \approx F_A\big|_V + \frac{dF_A}{dV}dV$. The balance simplifies to:

```{important}
**Simplified PFR Design Equation:**

$$

0 = F_A\big|_V - \left(F_A\big|_V + \frac{dF_A}{dV}dV\right) + r_A dV \implies -\frac{dF_A}{dV}dV + r_A dV = 0

$$

```

```{important}
**PFR Design Equations**
Rearranging gives the fundamental **differential form** of the PFR design equation:

$$

\frac{dF_A}{dV} = r_A

$$

To find the total reactor volume $V$ required for a certain conversion, this equation is integrated. By relating molar flow to conversion ($F_A = F_{A0}(1-X_A) \implies dF_A = -F_{A0}dX_A$), we get the **integral form**:

$$

V = F_{A0} \int_0^{X_A} \frac{dX_A}{-r_A}

$$

```

### Accounting for Gas-Phase Reactions

For liquid-phase reactions, density and volumetric flow rate ($v$) are typically assumed to be constant. For **gas-phase reactions**, this assumption is often invalid.

```{note}
**Causes of Volumetric Flow Rate Change in Gas-Phase PFRs**
The volumetric flow rate, $v$, can change along the length of the reactor due to:
1. **Change in Moles:** If a reaction changes the total number of moles (e.g., $A(g) \rightarrow 2B(g)$), the gas will expand or contract.
2. **Change in Temperature (T):** In non-isothermal reactors, temperature changes affect gas density ($v \propto T$).
3. **Change in Pressure (P):** Pressure drop through a packed bed or due to friction causes the gas to expand ($v \propto 1/P$).
```

Because $v$ can change, we cannot simply use $F_A = vC_A$ with a constant $v$. Instead, we must express the concentration, $C_A$, in terms of the variables we are integrating ($F_i, P, T$).

```{important}
**Concentration in Gas-Phase Systems (Ideal Gas)**
Using the ideal gas law, concentration can be written in terms of molar flow rates:

$$

C_A = \frac{P_A}{RT} = \frac{y_A P}{RT} = \left(\frac{F_A}{F_T}\right) \frac{P}{RT}

$$

Where $F_T = F_A + F_B + \dots + F_{\text{inerts}}$ is the total molar flow rate. This complete expression for $C_A$ is substituted into the rate law ($r_A$). This creates a system of coupled differential equations for the molar flow rates ($F_i$), temperature ($T$), and pressure ($P$) that must be solved simultaneously with numerical methods.
```

### Applications and Design Considerations

```{admonition} Term Definitions
:class: tip
**Typical PFR Applications**
PFRs are generally preferred for:
- **Large-scale production** in continuous, steady-state processes.
- **Fast reactions** that do not require long residence times.
- **Most heterogeneous catalytic reactions**, where the reactor is a tube packed with solid catalyst pellets.
- Situations where **high conversion** is desired, as a PFR is typically more volume-efficient than a CSTR for positive-order reactions.
```

```{note}
**Key PFR Design Concerns**
- **Poor Mixing:** PFRs have no moving parts for agitation. If reactants need to be mixed, static mixers can be installed within the tube.
- **Temperature Control and Hot Spots:** For highly exothermic reactions, the temperature can rise dangerously along the reactor, leading to thermal runaway or undesired side reactions. This is managed by using a **shell-and-tube reactor**. This design consists of many small-diameter tubes containing the catalyst, all housed within a larger shell. A coolant flows through the shell to remove heat effectively from the large surface area provided by the tubes.
```

### Example: Gas-Phase Reaction with Changing Mole Number

```{prf:example} Gas-Phase PFR with Changing Volumetric Flow
**Question:** Develop the equations required to determine the plug flow reactor volume needed to achieve 50% conversion of reactant A. The gas-phase reaction, $A + 2B \rightarrow 2D$, is carried out in an isothermal PFR at 5.0 atm and 55°C. The feed volumetric flow rate is 50 L/min. The rate law is $r_A = -2.5 C_A^{0.5} C_B$ mol/(L·min). The feed consists of mole fractions $y_A = 0.2$, $y_B = 0.5$, and $y_C = 0.3$, where C is an inert.
```

```{dropdown} Solution Steps
**Step 1: Strategy:**
This is a gas-phase reaction where the total number of moles changes (1 mole of A + 2 moles of B $\rightarrow$ 2 moles of D, a net change of -1 mole of gas per mole of A reacted). Even at constant temperature and pressure, this change in moles will cause the volumetric flow rate, $v$, to change along the reactor. Therefore, we cannot solve a simple integral in terms of concentration. We must solve a system of differential equations in terms of molar flow rates ($F_i$).

**Step 2: Calculate Initial Conditions (at V=0):**
First, we need the initial molar flow rate of each species. This requires finding the total molar feed rate, $F_{T0}$, using the ideal gas law.
- Temperature: $T = 55 + 273.15 = 328.15$ K.
- Pressure: $P = 5.0$ atm.
- Gas Constant: $R = 0.08206$ L·atm/(mol·K).

**Initial Molar Flow Rates**
Total Molar Feed Rate:

$$

F_{T0} = \frac{P v_0}{R T} = \frac{(5.0 \, \text{atm})(50 \, \text{L/min})}{(0.08206 \, \frac{\text{L}\cdot\text{atm}}{\text{mol}\cdot\text{K}})(328.15 \, \text{K})} = 9.29 \, \text{mol/min}

$$

Individual Molar Feed Rates:

$$

\begin{align*}
    F_{A0} &= y_{A0} F_{T0} = 0.2 \cdot (9.29) = \textbf{1.858 mol/min} \\
    F_{B0} &= y_{B0} F_{T0} = 0.5 \cdot (9.29) = \textbf{4.645 mol/min} \\
    F_{C0} &= y_{C0} F_{T0} = 0.3 \cdot (9.29) = \textbf{2.787 mol/min} \\
    F_{D0} &= 0
\end{align*}

$$

**Step 3: Formulate the System of Differential Equations:**
We write the PFR design equation, $\frac{dF_i}{dV} = r_i$, for each species.
- **Reactant A:** $\frac{dF_A}{dV} = r_A = -2.5 C_A^{0.5} C_B$
- **Reactant B:** The stoichiometry is 2 moles of B per 1 mole of A, so $r_B = 2r_A$.
  
  $$

  \frac{dF_B}{dV} = 2r_A = -5.0 C_A^{0.5} C_B

  $$

- **Product D:** The stoichiometry is 2 moles of D formed per 1 mole of A reacted, so $r_D = -2r_A$.
  
  $$

  \frac{dF_D}{dV} = -2r_A = 5.0 C_A^{0.5} C_B

  $$

- **Inert C:** The inert does not react, so $\frac{dF_C}{dV} = 0$. This means $F_C = F_{C0}$ throughout the reactor.

**Step 4: Define Algebraic Relationships and Stopping Condition:**
The rate laws depend on concentrations, which must be related to the molar flow rates.
- **Algebraic Equations:**
  
  $$

  \begin{align*}
      F_T &= F_A + F_B + F_C + F_D \quad (\text{Total molar flow rate}) \\
      v &= v_0 \left(\frac{F_T}{F_{T0}}\right) \quad (\text{Volumetric flow rate, since P and T are constant}) \\
      C_A &= \frac{F_A}{v} \quad (\text{Concentration of A}) \\
      C_B &= \frac{F_B}{v} \quad (\text{Concentration of B})
  \end{align*}

  $$

- **Differential Equations:**
  
  $$

  \begin{align*}
       \frac{dF_A}{dV} &= -2.5 C_A^{0.5} C_B \\
       \frac{dF_B}{dV} &= -5.0 C_A^{0.5} C_B \\
       \frac{dF_D}{dV} &= 5.0 C_A^{0.5} C_B
  \end{align*}

  $$

- **Initial Conditions:** Use the $F_{i0}$ values from Step 2 at $V=0$.
- **Stopping Condition:** Integrate with respect to $V$ until conversion $X_A = \frac{F_{A0} - F_A}{F_{A0}}$ reaches 0.50.

**Step 5: Final Result:**
Solving this system with a numerical package provides the reactor volume $V$ at which the stopping condition is met. The result is:

$$

V \approx \textbf{28.8 L}

$$

```

### Example: Gas-to-Solid Reaction

```{prf:example} PFR with a Phase Change
**Question:** An isothermal plug flow reactor is used for the reaction $10A(g) \rightarrow B(s)$. The rate law is first order in A, with a rate expression $r_A = -10kC_A$, where the intrinsic rate constant is $k=0.30$ L/(mol·min). Small solid particles of product B are entrained in the gas flow. The solid is assumed to occupy a negligible volume compared to the gas. The feed of pure A is at a pressure of 10 bar, a temperature of 450 K, and a molar flow rate of 120 mol/min. The reactor volume is 100 L. Determine the exit conversion.
```

```{dropdown} Solution Steps
**Step 1: Strategy and Key Insight:**
**Constant Concentration due to Phase Change:** The crucial point in this problem is that 10 moles of gaseous reactant A are consumed and removed from the gas phase, and replaced by a negligible volume of solid B. The feed is pure A, and since only A is removed from the gas phase, the remaining gas is also pure A. Because the temperature and pressure are constant, the concentration of the pure gas A must also be constant throughout the reactor.

**Step 2: Calculate the Constant Gas-Phase Concentration ($C_{A0}$):**
Using the ideal gas law for the inlet conditions (which apply everywhere in the reactor):
- $P = 10$ bar
- $T = 450$ K
- $R = 0.08314$ L·bar/(mol·K)

$$

C_A = C_{A0} = \frac{P}{RT} = \frac{10 \, \text{bar}}{(0.08314 \, \frac{\text{L}\cdot\text{bar}}{\text{mol}\cdot\text{K}})(450 \, \text{K})} = \textbf{0.267 mol/L}

$$

**Step 3: Set up and Integrate the Mole Balance:**
The PFR design equation is $\frac{dF_A}{dV} = r_A$. The rate of reaction of A is given as $r_A = -10 k C_A$. Since we've established that $C_A$ is constant and equal to $C_{A0}$, the rate of reaction is also constant throughout the reactor.

$$

\frac{dF_A}{dV} = -10 \cdot k \cdot C_{A0} = \text{constant}

$$

We can integrate this simple differential equation directly from the inlet ($V=0, F_A=F_{A0}$) to the outlet ($V=V_T, F_A=F_{A,exit}$):

$$

\int_{F_{A0}}^{F_{A,exit}} dF_A = \int_0^{V_T} (-10 k C_{A0}) dV


F_{A,exit} - F_{A0} = -10 \cdot k \cdot C_{A0} \cdot V_T

$$

**Step 4: Calculate Conversion:**
The conversion $X_A$ is defined as $X_A = \frac{F_{A0} - F_{A,exit}}{F_{A0}}$. The term $F_{A0} - F_{A,exit}$ represents the total moles of A reacted per minute. From our integrated equation:

**Moles of A Reacted**

$$

\text{Moles Reacted} = F_{A0} - F_{A,exit} = 10 \cdot k \cdot C_{A0} \cdot V_T

$$

Now, substitute the known values:
- $k = 0.30$ L/(mol·min)
- $C_{A0} = 0.267$ mol/L
- $V_T = 100$ L

$$

\text{Moles Reacted} = 10 \cdot (0.30) \cdot (0.267) \cdot (100) = 80.1 \, \text{mol/min}

$$

The conversion is the ratio of moles reacted to moles fed ($F_{A0} = 120$ mol/min):

$$

X_A = \frac{80.1 \, \text{mol/min}}{120 \, \text{mol/min}} = 0.6675

$$

The exit conversion is **67%**.
```

## Comparing Reactors in Series

A fundamental task in chemical engineering is selecting the appropriate reactor type and configuration to achieve a desired conversion efficiently. This section uses a graphical method, the Levenspiel plot, to compare the performance and required volumes of Continuous Stirred-Tank Reactors (CSTRs) and Plug Flow Reactors (PFRs), both individually and in series.

### The Levenspiel Plot: A Graphical Tool for Reactor Design

For an isothermal reaction, the Levenspiel plot provides a powerful visual representation of reactor performance by plotting a function of the inverse reaction rate against conversion.

```{note}
**Understanding the Levenspiel Plot**
A Levenspiel plot graphs the term $\frac{F_{A0}}{-r_A}$ on the y-axis versus the conversion, $X_A$, on the x-axis.
- **Y-Axis ($\frac{F_{A0}}{-r_A}$):** This term has units of volume (e.g., L or m$^3$). A higher point on the y-axis signifies a slower reaction rate (since $-r_A$ is in the denominator).
- **X-Axis ($X_A$):** This axis represents the fractional conversion of reactant A, ranging from 0 to 1.

The area on this plot represents the reactor volume required to achieve a certain conversion, making it an excellent tool for visual comparison.
```

### Visualizing Single Reactor Volume

For a given conversion, the required volume for a CSTR and a PFR can be represented as distinct areas on the Levenspiel plot.

```{important}
**CSTR Design Equation and Graphical Area**
The design equation for a CSTR is an algebraic equation:

$$

V_{CSTR} = \frac{F_{A0} X_A}{(-r_A)_{\text{exit}}} \quad \text{or} \quad V_{CSTR} = \left(\frac{F_{A0}}{-r_A}\right)_{\text{at }X_A} \times X_A

$$

Graphically, this represents the area of a **rectangle**. The height of the rectangle is the value of $\frac{F_{A0}}{-r_A}$ at the final exit conversion (the slowest rate in the process), and the width is the total conversion $X_A$.
```

```{important}
**PFR Design Equation and Graphical Area**
The design equation for a PFR is an integral equation:

$$

V_{PFR} = F_{A0} \int_0^{X_A} \frac{dX_A}{-r_A} \quad \text{or} \quad V_{PFR} = \int_0^{X_A} \left(\frac{F_{A0}}{-r_A}\right) dX_A

$$

Graphically, this represents the **area under the curve** of the Levenspiel plot, integrated from zero conversion to the final conversion $X_A$.
```

```{admonition} Term Definitions
:class: tip
**Single Reactor Comparison**
For any reaction where the rate decreases as conversion increases (a typical nth-order reaction), the Levenspiel plot curve will be upward-sloping. In this common case, the rectangle representing the CSTR volume will always be larger than the area under the curve representing the PFR volume for the same final conversion.

**Conclusion:** To achieve the same conversion for a typical reaction, a **PFR requires a smaller volume than a CSTR**. This is because the entire CSTR must operate at the lowest reaction rate (corresponding to the final exit conditions), whereas the PFR takes advantage of the higher reaction rates that exist at lower conversions near the reactor inlet.
```

### Comparing Reactors in Series

The graphical method also provides clear insight into configuring multiple reactors in series to optimize total volume.

```{note}
**PFRs in Series**
The total volume required to achieve a final conversion $X_f$ using two PFRs in series is the sum of their individual volumes.

$$

V_{total} = V_1 + V_2 = \int_0^{X_1} \left(\frac{F_{A0}}{-r_A}\right) dX_A + \int_{X_1}^{X_f} \left(\frac{F_{A0}}{-r_A}\right) dX_A = \int_0^{X_f} \left(\frac{F_{A0}}{-r_A}\right) dX_A

$$

The total volume is exactly the same as the volume of a single PFR used to achieve the same final conversion $X_f$. Therefore, for an isothermal reaction, there is **no volumetric advantage or disadvantage** to using multiple PFRs in series instead of one larger PFR.
```

```{note}
**CSTRs in Series**
Using two or more CSTRs in series offers a significant advantage in reducing the total required volume compared to a single CSTR for the same final conversion.
- A single CSTR to reach high conversion must be very large, as its volume is defined by the large rectangle at the slowest reaction rate.
- If two CSTRs are used, the first operates to an intermediate conversion ($X_1$), and its volume is a smaller rectangle. The second reactor then operates from $X_1$ to the final conversion $X_f$. Its volume is also a rectangle, but its height is determined by the final, slowest rate.

The sum of the areas of the two smaller rectangles is significantly less than the area of the single large rectangle required for one CSTR.
```

```{admonition} Term Definitions
:class: tip
**Series Reactor Comparison Conclusion**
- For a given final conversion, the total volume required for **multiple CSTRs in series is less** than the volume of a single CSTR.
- The optimal arrangement for minimizing volume is an infinite number of infinitesimally small CSTRs in series, which is mathematically equivalent to a single PFR. This reinforces the conclusion that PFRs are more volume-efficient for typical reactions.
```

## Adiabatic Temperature and Energy Balances

For an adiabatic process, there is no heat exchange with the surroundings ($\Delta H = 0$). The heat generated or consumed by the reaction directly changes the temperature of the reactor contents. This section demonstrates how to calculate the final temperature (the adiabatic temperature) for a reaction with a given conversion.

### Example: Adiabatic Temperature Calculation

```{prf:example} Calculating Adiabatic Temperature Rise
**Question:** The reaction $NO + 0.5 O_2 \rightarrow NO_2$ occurs in an adiabatic reactor. The feed enters at 100°C and consists of 1 mole of NO and 0.5 moles of O$_2$. The heat of reaction at 25°C is $\Delta H_{rxn, 298K} = -57.0$ kJ/mol. The heat capacities ($C_p/R$) are given as:
- $C_p(\text{NO})/R = 3.5 + 0.001 T$
- $C_p(\text{O}_2)/R = 3.2 + 0.0018 T$
- $C_p(\text{NO}_2)/R = 4.2 + 0.0025 T$
where T is in Kelvin. Calculate the adiabatic temperature for 30% conversion of NO.
```

```{dropdown} Solution Steps
**Step 1: Strategy: Enthalpy as a State Function:**
Since enthalpy is a state function, the overall enthalpy change of a process is independent of the path taken. For an adiabatic process, the total enthalpy change is zero ($\Delta H_{total} = 0$). We can construct a convenient hypothetical three-step path from the initial state (reactants at 373 K) to the final state (product mixture at $T_f$) and set the sum of the enthalpy changes to zero.
(a) **$\Delta H_1$:** Cool the reactants from the feed temperature (373 K) to a reference temperature (298 K).
(b) **$\Delta H_2$:** Carry out the reaction at 298 K to the specified conversion (30%).
(c) **$\Delta H_3$:** Heat the final product mixture from 298 K to the unknown final adiabatic temperature, $T_f$.
The energy balance is: $\Delta H_1 + \Delta H_2 + \Delta H_3 = \Delta H_{total} = 0$.

**Step 2: Calculate $\Delta H_1$ (Cooling Reactants):**
This is the enthalpy change from cooling the initial 1 mole of NO and 0.5 moles of O$_2$.

$$

\Delta H_1 = \int_{373K}^{298K} \sum n_i C_{p,i} \, dT = \int_{373}^{298} R \left[ (1)(3.5 + 0.001T) + (0.5)(3.2 + 0.0018T) \right] dT


\Delta H_1 = R \int_{373}^{298} (5.1 + 0.0019T) dT = R \left[ 5.1T + \frac{0.0019}{2}T^2 \right]_{373}^{298}

$$

Plugging in the limits and $R = 8.314$ J/(mol·K):

$$

\Delta H_1 = 8.314 \left[ (5.1(298-373)) + (0.00095(298^2-373^2)) \right]


\Delta H_1 = 8.314 [-382.5 - 47.8] = -3578 \, \text{J} = \textbf{-3.58 kJ}

$$

The sign is negative because heat is removed during cooling.

**Step 3: Calculate $\Delta H_2$ (Heat of Reaction at 298 K):**
The reaction proceeds to 30% conversion, so 0.3 moles of the basis reactant (NO) react.

$$

\Delta H_2 = (\text{moles NO reacted}) \times (\Delta H_{rxn, 298K}) = (0.3 \, \text{mol}) \times (-57.0 \, \text{kJ/mol})


\Delta H_2 = \textbf{-17.1 kJ}

$$

**Step 4: Set up $\Delta H_3$ (Heating the Final Mixture):**
First, determine the composition of the final mixture based on 30% conversion of 1 mole of NO.
- Moles NO remaining: $1.0 - 0.3 = 0.7$ mol
- Moles O$_2$ remaining: $0.5 - (0.5 \times 0.3) = 0.35$ mol
- Moles NO$_2$ formed: $1 \times 0.3 = 0.3$ mol
Now, set up the integral for heating this final mixture from 298 K to $T_f$.

$$

\Delta H_3 = \int_{298K}^{T_f} \sum n_i C_{p,i} \, dT


\Delta H_3 = R \int_{298}^{T_f} \left[ (0.7)(3.5+0.001T) + (0.35)(3.2+0.0018T) + (0.3)(4.2+0.0025T) \right] dT


\Delta H_3 = R \int_{298}^{T_f} (2.45+0.0007T + 1.12+0.00063T + 1.26+0.00075T) dT


\Delta H_3 = R \int_{298}^{T_f} (4.83 + 0.00208T) dT

$$

Integrating this expression gives:

**Expression for $\Delta H_3$**

$$

\Delta H_3 = R \left[ 4.83T + \frac{0.00208}{2}T^2 \right]_{298}^{T_f}


\Delta H_3 (\text{in kJ}) = \frac{8.314}{1000} \left[ 4.83(T_f-298) + 0.00104(T_f^2 - 298^2) \right]

$$

**Step 5: Solve the Energy Balance for the Final Temperature ($T_f$):**
Set the sum of the enthalpies to zero: $\Delta H_1 + \Delta H_2 + \Delta H_3 = 0$.

$$

-3.58 \, \text{kJ} - 17.1 \, \text{kJ} + 0.008314 \left[ 4.83(T_f-298) + 0.00104(T_f^2 - 298^2) \right] = 0


-20.68 + 0.008314 [4.83 T_f - 1439.34 + 0.00104 T_f^2 - 92.1] = 0


-20.68 + 0.04017 T_f - 11.97 + 8.647 \times 10^{-6} T_f^2 - 0.766 = 0

$$

This simplifies to a quadratic equation for $T_f$:

**Final Quadratic Equation for Temperature**

$$

8.647 \times 10^{-6} T_f^2 + 0.04017 T_f - 33.416 = 0

$$

Solving this using the quadratic formula, $T_f = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$, yields two roots. Only the positive root is physically meaningful.

$$

T_f = \frac{-0.04017 + \sqrt{0.04017^2 - 4(8.647 \times 10^{-6})(-33.416)}}{2(8.647 \times 10^{-6})} \approx \textbf{720 K}

$$

The final adiabatic temperature is approximately 720 K (or 447°C).
```

### Example: Endothermic Reaction in an Adiabatic PBR

```{prf:example} Adiabatic PBR with Constant Heat Capacities
**Question:** An endothermic reaction occurs in an adiabatic packed bed reactor (PBR). The feed enters at 500 K, and the exit stream is at 487 K with 40% conversion. The heat capacities and heat of reaction are assumed to be constant.
(a) Is the reaction endothermic or exothermic?
(b) If the space time is doubled, causing the outlet temperature to drop to 482 K, what is the new conversion?
```

```{dropdown} Solution Steps
**Step 1: Part (a): Endothermic or Exothermic?**
In an adiabatic system, no heat is exchanged with the surroundings. Any temperature change is caused solely by the heat of reaction. If the temperature drops, the reaction must be consuming energy from the fluid (endothermic). If the temperature rises, the reaction must be releasing energy (exothermic). The reactor is adiabatic, and the temperature drops from 500 K to 487 K. Therefore, the reaction is **endothermic**.

**Step 2: Part (b): Calculating New Conversion via Proportionality:**
For an adiabatic reactor with constant heat capacities, the energy balance shows a direct linear relationship between conversion ($X$) and the change in temperature ($\Delta T = T_{out} - T_{in}$).

$$

X_A = \frac{\sum \Theta_i C_{p,i}}{-\Delta H_{rxn}}(T - T_{in}) = (\text{Constant}) \cdot (T_{out} - T_{in})

$$

We can solve for this constant using the initial set of conditions.
- Initial conversion: $X_1 = 0.40$
- Initial temperature change: $\Delta T_1 = 487 \, \text{K} - 500 \, \text{K} = -13 \, \text{K}$

$$

0.40 = \text{Constant} \cdot (-13 \, \text{K}) \implies \text{Constant} = \frac{0.40}{-13} \approx -0.03077 \, \text{K}^{-1}

$$

Now we use this constant to find the new conversion ($X_2$) for the new temperature change. Doubling the space time allows the reaction to proceed further, consuming more heat and dropping the temperature more.
- New temperature change: $\Delta T_2 = 482 \, \text{K} - 500 \, \text{K} = -18 \, \text{K}$

$$

X_2 = (\text{Constant}) \cdot (\Delta T_2) = (-0.03077 \, \text{K}^{-1}) \cdot (-18 \, \text{K}) = 0.554

$$

The new conversion is **55%**.
```

### Example: Initial Temperature Profile in a Heated PFR

```{prf:example} Initial Temperature Profile in a Heated PFR
**Question:** An endothermic, second-order reaction ($A \rightarrow \text{Products, } -r_A = k C_A^2$) takes place in a PFR with a diameter of 8 cm. The reactor is heated by a steam jacket that maintains a constant wall temperature of 300°C. The feed enters at 250°C. Other data includes: $\Delta H_{rxn} = 80$ kJ/mol, $k = 0.5$ L/(mol·min) at 250°C, and $U = 5000$ kJ/(m$^2\cdot$h$\cdot$K). Immediately downstream from the reactor inlet, will the fluid temperature increase, decrease, or stay the same?
```

```{dropdown} Solution Steps
**Step 1: Strategy: Analyze the Differential Energy Balance:**
**Comparing Heat Effects:** To determine the initial temperature trend, we must evaluate the sign of the temperature derivative with respect to reactor volume, $\frac{dT}{dV}$, at the inlet ($V=0$). This requires comparing the rate of heat consumption by the endothermic reaction with the rate of heat addition from the steam jacket at the reactor entrance.

The differential energy balance for a PFR with heat exchange is:

$$

\frac{dT}{dV} = \frac{Ua(T_a - T) + r_A(-\Delta H_{rxn})}{\sum F_i C_{p,i}}

$$

The sign of $\frac{dT}{dV}$ is determined by the sign of the numerator: $Ua(T_a - T) + r_A(-\Delta H_{rxn})$.

**Step 2: Evaluate Heat Transfer Term at the Inlet:**
This term represents heat addition from the steam jacket. The heat transfer area per unit volume is $a = 4/D$.
- $U = 5000 \, \frac{\text{kJ}}{\text{m}^2 \cdot \text{h} \cdot \text{K}} \times \frac{1 \text{ h}}{60 \text{ min}} = 83.33 \, \frac{\text{kJ}}{\text{m}^2 \cdot \text{min} \cdot \text{K}}$
- $D = 8 \, \text{cm} = 0.08 \, \text{m}$
- Temperature difference at inlet: $T_a - T = 300^\circ\text{C} - 250^\circ\text{C} = 50 \, \text{K}$

$$

\text{Heat Added} = U \left(\frac{4}{D}\right)(T_a - T) = (83.33) \left(\frac{4}{0.08}\right)(50) = 208,333 \, \frac{\text{kJ}}{\text{m}^3 \cdot \text{min}}


\text{Heat Added} = 208,333 \frac{\text{kJ}}{\text{m}^3\cdot\text{min}} \times \frac{1 \, \text{m}^3}{1000 \, \text{L}} = \textbf{208.3} \, \frac{\text{kJ}}{\text{L} \cdot \text{min}}

$$

**Step 3: Evaluate Heat Consumption Term at the Inlet:**
This term represents heat consumed by the endothermic reaction ($\Delta H_{rxn} > 0$).

$$

\text{Heat Consumed} = -r_A(\Delta H_{rxn}) = (k C_{A0}^2)(\Delta H_{rxn})


\text{Heat Consumed} = (0.5 \frac{\text{L}}{\text{mol}\cdot\text{min}} \cdot C_{A0}^2)(80 \frac{\text{kJ}}{\text{mol}}) = \textbf{40} \cdot C_{A0}^2 \, \frac{\text{kJ}}{\text{L} \cdot \text{min}}

$$

**Step 4: Compare Heat Effects and Conclude:**
The initial temperature trend depends on the sign of $(208.3 - 40 C_{A0}^2)$. The problem implies a realistic operating condition where the initial concentration is not excessively high. For any reasonable initial concentration (e.g., even if $C_{A0}$ were as high as 2 mol/L, the heat consumption term would be $40 \cdot 2^2 = 160$ kJ/(L·min)), the heat addition term dominates.

$$

\text{Heat Added (208.3)} > \text{Heat Consumed (e.g., 160)}

$$

Since the rate of heat addition from the steam jacket is greater than the rate of heat consumption by the reaction at the inlet, the numerator in the energy balance is positive. Therefore, $\frac{dT}{dV}$ is positive, and the temperature will **increase** immediately downstream from the inlet.
```

---

## PE Exam Practice Problems

```{prf:example} Practice Problem 1: CSTR vs. PFR Sizing

The liquid-phase reaction $A \rightarrow B$ follows second-order kinetics: $-r_A = k C_A^2$ with $k = 0.5$ L/mol·min.

Feed: $C_{A0} = 2$ mol/L, volumetric flow rate $v_0 = 10$ L/min. Desired conversion: $X = 0.80$.

**(a)** What volume CSTR is required?

**(b)** What volume PFR is required?

**(c)** Which is smaller, and why?
```

```{dropdown} Solution

**Part (a): CSTR volume**

Exit concentration: $C_A = C_{A0}(1-X) = 2(1-0.8) = 0.4$ mol/L

Exit rate: $-r_A = k C_A^2 = 0.5 \times (0.4)^2 = 0.08$ mol/L·min

$$V_{CSTR} = \frac{F_{A0}\,X}{-r_A\big|_{exit}} = \frac{v_0 C_{A0} X}{-r_A} = \frac{10 \times 2 \times 0.80}{0.08} = \mathbf{200 \text{ L}}$$

**Part (b): PFR volume**

$$V_{PFR} = F_{A0}\int_0^{0.8}\frac{dX}{-r_A} = v_0 C_{A0}\int_0^{0.8}\frac{dX}{k\,C_{A0}^2(1-X)^2}$$

$$= \frac{v_0}{k\,C_{A0}}\int_0^{0.8}\frac{dX}{(1-X)^2} = \frac{10}{0.5 \times 2}\left[\frac{1}{1-X}\right]_0^{0.8} = 10\left[\frac{1}{0.2} - 1\right] = 10 \times 4 = \mathbf{40 \text{ L}}$$

**Part (c): Comparison**

$V_{PFR} = 40$ L is **5× smaller** than $V_{CSTR} = 200$ L.

For positive-order reactions, the PFR is always more efficient because it operates at higher concentrations throughout (higher rate), while the CSTR operates entirely at the low exit concentration (lowest rate). For second-order kinetics, this difference is especially pronounced.
```

---

```{prf:example} Practice Problem 2: Arrhenius: Finding $E_a$ from Two Temperature Data Points

A first-order reaction has rate constants $k_1 = 0.012$ min⁻¹ at 300 K and $k_2 = 0.135$ min⁻¹ at 350 K.

**(a)** What is the activation energy $E_a$ (kJ/mol)?

**(b)** What is the rate constant at 325 K?
```

```{dropdown} Solution

**Part (a): Activation energy**

Taking the ratio of Arrhenius at two temperatures:

$$\ln\frac{k_2}{k_1} = \frac{E_a}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)$$

$$\ln\frac{0.135}{0.012} = \ln(11.25) = 2.420$$

$$\frac{1}{T_1} - \frac{1}{T_2} = \frac{1}{300} - \frac{1}{350} = 3.333\times10^{-3} - 2.857\times10^{-3} = 4.762\times10^{-4} \text{ K}^{-1}$$

$$E_a = \frac{R \ln(k_2/k_1)}{1/T_1 - 1/T_2} = \frac{8.314 \times 2.420}{4.762\times10^{-4}} = \mathbf{42{,}250 \text{ J/mol} \approx 42.3 \text{ kJ/mol}}$$

**Part (b): Rate constant at 325 K**

$$\ln\frac{k_{325}}{k_1} = \frac{E_a}{R}\left(\frac{1}{300} - \frac{1}{325}\right) = \frac{42{,}250}{8.314}\left(2.564\times10^{-4}\right) = 5083 \times 2.564\times10^{-4} = 1.303$$

$$k_{325} = 0.012 \times e^{1.303} = 0.012 \times 3.681 = \mathbf{0.0442 \text{ min}^{-1}}$$
```

```{caution}
**PE Exam Traps: Chemical Reaction Engineering**

- **CSTR uses exit conditions, PFR integrates.** The CSTR design equation evaluates $-r_A$ at the **exit** (lowest) concentration. Evaluating $-r_A$ at the feed concentration for a CSTR gives a dramatically undersized reactor. The PFR integrates from feed to exit concentration, naturally accounting for the changing rate.
- **Levenspiel plot area interpretation:** For a CSTR, volume = rectangle with width $X$ and height $F_{A0}/(-r_A)_{exit}$. For a PFR, volume = area under the $F_{A0}/(-r_A)$ curve from 0 to $X$. For a rate that increases with conversion (autocatalytic or unusual kinetics), a CSTR first + PFR second can be more efficient than PFR alone.
- **Arrhenius $T$ must be in Kelvin.** $E_a/(RT)$ requires absolute temperature. Using °C gives a nonsensical exponent. Also, the pre-exponential $A$ has the same units as $k$ (s⁻¹ for first-order, L/mol·s for second-order) - its units are often omitted but are essential for dimensional consistency.
- **Conversion $X$ is fraction reacted, not fraction remaining.** $C_A = C_{A0}(1-X)$, so at $X = 0.9$, only 10% of A remains. Writing $C_A = C_{A0}\,X$ is wrong and a very common slip.
- **Space time $\tau = V/v_0$ is not residence time for gas-phase reactions** with changing mole number, because the volumetric flow rate $v$ changes with conversion. Use $\tau = C_{A0}\int_0^X dX/(-r_A)$ consistently.
```