---
title: "Chemical and Phase Equilibria Study Guide"
author: "PE Study Guide"
date: "2025"
---

# Chemical and Phase Equilibria

## Quick Reference: Key Equations

| Topic | Formula | Notes |
|-------|---------|-------|
| Standard $\Delta G^\circ$ | $\Delta G^\circ_T = \sum_i \nu_i \Delta G^\circ_{f,i}$ | Products minus reactants |
| Equilibrium constant | $K_a = \exp(-\Delta G^\circ/RT)$ | Thermodynamic $K$ |
| $K_y$ (ideal gas) | $K_a = K_y \cdot P^{\sum\nu_i}$ | $K_y = \prod y_i^{\nu_i}$ |
| Van't Hoff | $d\ln K/dT = \Delta H^\circ_{rxn}/RT^2$ | Temperature effect on $K$ |
| Raoult's Law | $y_i P = x_i P_i^{sat}$ | Ideal VLE |
| Modified Raoult's | $y_i P = \gamma_i x_i P_i^{sat}$ | Non-ideal liquid |
| Antoine equation | $\log_{10}P^{sat} = A - B/(T+C)$ | $P$ in mmHg or bar |
| Henry's Law | $p_A = H_A\,x_A$ | Dilute solutions |
| Bubble point | $\sum x_i K_i = 1$, $K_i = P_i^{sat}/P$ | Find $T$ or $P$ |
| Dew point | $\sum y_i/K_i = 1$ | Find $T$ or $P$ |
| Flash (Rachford-Rice) | $\sum_i (z_i(K_i-1))/(1+\psi(K_i-1)) = 0$ | $\psi=V/F$, vapor fraction |
| Clausius-Clapeyron | $\ln(P_2/P_1) = (\Delta H_{vap}/R)(1/T_1 - 1/T_2)$ | Approx. for vapor pressure |
| Activity coefficient | $\ln\gamma_i$ from Margules, van Laar, or NRTL | Non-ideal liquid |
| Fugacity (liquid) | $f_i^L = \gamma_i x_i P_i^{sat}$ | Modified Raoult basis |

---

This study guide covers the principles of chemical equilibrium for gas-phase reactions. These calculations determine the final state of a system, representing the maximum possible conversion. It is important to note that equilibrium does not predict the reaction kinetics, which is the speed at which the reaction reaches equilibrium.

## Gas-Phase Chemical Equilibrium

This section introduces the key thermodynamic equations used to describe and calculate chemical equilibrium for gas-phase reactions.

### Gibbs Free Energy of Reaction

The spontaneity of a reaction and its equilibrium position are fundamentally linked to the change in Gibbs Free Energy.

```{note}
The Standard Gibbs Free Energy of Reaction ($\Delta G^\circ_T$) is the change in Gibbs energy for a process in which reactants in their standard states are converted to products in their standard states.

For gases, the standard state is the ideal gas state at a pressure of 1 bar. It is calculated by summing the standard Gibbs free energies of formation for all species, weighted by their stoichiometric coefficients.
```

```{admonition} Term Definitions
:class: tip
- **$\Delta G^\circ_T$**: Standard Gibbs free energy change of reaction at absolute temperature $T$ [J/mol or kJ/mol].
- **$\nu_i$**: Stoichiometric coefficient for component $i$. It is positive for products, negative for reactants, and dimensionless.
- **$\Delta G^\circ_{f,i}$**: Standard Gibbs free energy of formation for component $i$ at temperature $T$.
```

```{important}
The standard Gibbs free energy change of reaction is calculated as:

$$

\Delta G^\circ_T = \sum_i \nu_i \Delta G^\circ_{f,i} \quad \text{(Equation 1)}

$$

```

### The Thermodynamic Equilibrium Constant ($K_a$)

The standard Gibbs free energy change is directly related to the thermodynamic equilibrium constant, $K_a$.

```{note}
The thermodynamic equilibrium constant ($K_a$) is a dimensionless quantity that relates the activities of products and reactants at equilibrium.

A value of $K_a > 1$ indicates that the formation of products is favored at equilibrium. A value of $K_a < 1$ indicates that reactants are favored.
```

```{admonition} Term Definitions
:class: tip
- **$K_a$**: The dimensionless thermodynamic equilibrium constant.
- **$R$**: The ideal gas constant, $8.314 \, \text{J/(mol}\cdot\text{K)}$.
- **$T$**: The absolute temperature of the system in Kelvin [K].
```

```{important}
The relationship between the equilibrium constant and Gibbs free energy is:

$$

K_a = \exp\left(-\frac{\Delta G^\circ_T}{RT}\right) \quad \text{(Equation 2)}

$$

```

### Equilibrium for Ideal Gas Mixtures

For reactions involving ideal gases, the equilibrium constant can be expressed in terms of mole fractions and total pressure.

```{note}
For an ideal gas mixture, the activity of a component is its partial pressure expressed in bar.

The equilibrium constant $K_a$ can therefore be written as a function of the mole fractions of the components and the total system pressure. The term $\sum \nu_i$ determines how the total pressure affects the equilibrium position.
```

```{admonition} Term Definitions
:class: tip
- **$y_i$**: Mole fraction of component $i$ in the gas mixture at equilibrium.
- **$P$**: Total pressure of the system [bar].
- **$P^\circ$**: Standard state pressure, defined as $1$ bar.
- **$\nu_i$**: Stoichiometric coefficient for component $i$.
```

```{important}
The general form for the equilibrium constant in terms of activities is $K_a = \prod_i \hat{a}_i^{\nu_i}$.

For ideal gases, the activity $\hat{a}_i = y_i P / P^\circ$. This leads to:

$$

K_a = \prod_i (y_i)^{\nu_i} \left(\frac{P}{P^\circ}\right)^{\sum_i \nu_i} \quad \text{(Equation 3)}

$$

Since $P^\circ = 1$ bar, this is often simplified to $K_a = \left( \prod_i y_i^{\nu_i} \right) P^{\sum_i \nu_i}$.
```

### Effect of Temperature (Van't Hoff Equation)

The Van't Hoff equation describes how the equilibrium constant changes with temperature.

```{note}
The **Van't Hoff equation** shows that for an **endothermic reaction** ($\Delta H^\circ_{rxn} > 0$), the equilibrium constant increases with increasing temperature.

For an **exothermic reaction** ($\Delta H^\circ_{rxn} < 0$), the equilibrium constant decreases with increasing temperature. This is a quantitative expression of Le Châtelier's Principle.
```

```{admonition} Term Definitions
:class: tip
- **$\Delta H^\circ_{rxn}$**: The standard enthalpy change (heat of reaction) at temperature $T$ [J/mol].
- **$K_1, K_2$**: Equilibrium constants at absolute temperatures $T_1$ and $T_2$.
```

```{important}
The differential and integrated forms of the Van't Hoff equation are given below. The integrated form assumes that the standard heat of reaction, $\Delta H^\circ_{rxn}$, is constant over the temperature range from $T_1$ to $T_2$.

$$

\frac{d(\ln K_a)}{dT} = \frac{\Delta H^\circ_{rxn}}{RT^2} \quad \text{(Equation 4a - Differential Form)}

$$

$$

\ln\left(\frac{K_2}{K_1}\right) = -\frac{\Delta H^\circ_{rxn}}{R} \left(\frac{1}{T_2} - \frac{1}{T_1}\right) \quad \text{(Equation 4b - Integrated Form)}

$$

```

### Example Problems

```{prf:example} Methanol Reforming for Hydrogen Production
Hydrogen for a fuel cell can be formed by the reaction:

$$

\text{CH}_3\text{OH(g)} + \text{H}_2\text{O(g)} \rightleftharpoons \text{CO}_2\text{(g)} + 3\text{H}_2\text{(g)}

$$

The reactor feed is at 2.0 bar and the water/methanol ratio is 1.5. What is the equilibrium conversion of methanol at $80^\circ\text{C}$ (353.15 K) and 2.0 bar? Assume ideal gas behavior.
```

```{dropdown} Solution Steps
**Step 1: Gather Data and Calculate $\Delta G^\circ_{298}$ and $\Delta H^\circ_{298}$**

First, list the standard formation data at $25^\circ\text{C}$ (298.15 K).

| Component | $\Delta H^\circ_f$ (kJ/mol) | $\Delta G^\circ_f$ (kJ/mol) |
| :--- | :---: | :---: |
| $\text{CH}_3\text{OH(g)}$ | -201.2 | -162.3 |
| $\text{H}_2\text{O(g)}$ | -241.8 | -228.6 |
| $\text{CO}_2\text{(g)}$ | -393.5 | -394.4 |
| $\text{H}_2\text{(g)}$ | 0 | 0 |

The stoichiometric coefficients ($\nu_i$) are: $\nu_{\text{CO}_2} = 1$, $\nu_{\text{H}_2} = 3$, $\nu_{\text{CH}_3\text{OH}} = -1$, $\nu_{\text{H}_2\text{O}} = -1$.

$$

\Delta G^\circ_{298} = [1(-394.4) + 3(0)] - [1(-162.3) + 1(-228.6)] = -3.5 \, \text{kJ/mol}

$$

$$

\Delta H^\circ_{298} = [1(-393.5) + 3(0)] - [1(-201.2) + 1(-241.8)] = +49.5 \, \text{kJ/mol}

$$

The reaction is endothermic since $\Delta H^\circ > 0$.

**Step 2: Calculate Equilibrium Constant $K_{298}$ at $25^\circ\text{C}$**

Using Equation 2 with $T_1 = 298.15$ K and $R = 8.314$ J/(mol$\cdot$K).

$$

K_{298} = \exp\left(-\frac{\Delta G^\circ_{298}}{RT_1}\right) = \exp\left(-\frac{-3500 \, \text{J/mol}}{8.314 \, \frac{\text{J}}{\text{mol}\cdot\text{K}} \times 298.15 \, \text{K}}\right) = \exp(1.412) \approx 4.10

$$

**Step 3: Calculate Equilibrium Constant $K_{353}$ at $80^\circ\text{C}$**

Using the integrated Van't Hoff equation (4b) with $T_1 = 298.15$ K and $T_2 = 353.15$ K.

$$

\ln\left(\frac{K_{353}}{K_{298}}\right) = -\frac{\Delta H^\circ_{rxn}}{R} \left(\frac{1}{T_2} - \frac{1}{T_1}\right)

$$

$$

\ln\left(\frac{K_{353}}{4.10}\right) = -\frac{49500 \, \text{J/mol}}{8.314 \, \frac{\text{J}}{\text{mol}\cdot\text{K}}} \left(\frac{1}{353.15 \, \text{K}} - \frac{1}{298.15 \, \text{K}}\right)

$$

$$

\ln\left(\frac{K_{353}}{4.10}\right) = -5954.8 \times (0.0028316 - 0.0033540) = -5954.8 \times (-0.0005224) = 3.111

$$

$$

K_{353} = 4.10 \times e^{3.111} = 4.10 \times 22.44 \approx 92.0

$$

**Step 4: Set up Stoichiometry Table and Solve for Conversion**

Let $\xi$ be the extent of reaction. Basis: 1 mole of $\text{CH}_3\text{OH}$ and 1.5 moles of $\text{H}_2\text{O}$ are fed.

| Species | Initial (mol) | Equilibrium (mol) | Mole Fraction ($y_i$) |
| :--- | :---: | :---: | :---: |
| $\text{CH}_3\text{OH}$ | 1 | $1 - \xi$ | $(1 - \xi) / n_{total}$ |
| $\text{H}_2\text{O}$ | 1.5 | $1.5 - \xi$ | $(1.5 - \xi) / n_{total}$ |
| $\text{CO}_2$ | 0 | $\xi$ | $\xi / n_{total}$ |
| $\text{H}_2$ | 0 | $3\xi$ | $3\xi / n_{total}$ |
| **Total** | 2.5 | $n_{total} = 2.5 + 2\xi$ | 1.0 |

The change in moles is $\sum \nu_i = (1+3) - (1+1) = 2$.

Using Equation 3:

$$

K_a = \frac{y_{\text{CO}_2} y_{\text{H}_2}^3}{y_{\text{CH}_3\text{OH}} y_{\text{H}_2\text{O}}} P^2 = \frac{(\frac{\xi}{n_{total}})(\frac{3\xi}{n_{total}})^3}{(\frac{1-\xi}{n_{total}})(\frac{1.5-\xi}{n_{total}})} P^2 = \frac{27\xi^4}{(1-\xi)(1.5-\xi)} \frac{P^2}{n_{total}^2}

$$

Substitute $K_a = 92.0$, $P=2.0$ bar, and $n_{total} = 2.5 + 2\xi$:

$$

92.0 = \frac{27\xi^4}{(1-\xi)(1.5-\xi)} \frac{(2.0)^2}{(2.5 + 2\xi)^2}

$$

This non-linear equation can be solved numerically. Solving yields $\xi \approx 0.923$ mol.

**Step 5: Final Answer**

The conversion of methanol (the limiting reactant) is defined as moles reacted per mole fed.

$$

\text{Conversion} = X = \frac{\xi}{\text{initial moles of } \text{CH}_3\text{OH}} = \frac{0.923}{1.0} = 0.923

$$

The equilibrium conversion is **92.3\%**.
```

```{prf:example} Dehydrogenation of Butene
The catalytic reaction $\text{C}_4\text{H}_8\text{(g)} \rightleftharpoons \text{C}_4\text{H}_6\text{(g)} + \text{H}_2\text{(g)}$ takes place at $900^\circ\text{C}$ and 1.0 bar. The feed contains steam and $\text{C}_4\text{H}_8$ in a 10:1 ratio. At this temperature, $K_a = 0.329$.

What is the equilibrium conversion with steam present? Does equilibrium conversion increase or decrease if steam is not fed to the system? Explain why.
```

```{dropdown} Solution Steps
**Step 1: Calculate Conversion with Steam**

The change in moles is $\sum \nu_i = (1+1) - 1 = 1$. The equilibrium expression is:

$$

K_a = \frac{y_{\text{C}_4\text{H}_6} y_{\text{H}_2}}{y_{\text{C}_4\text{H}_8}} \left(\frac{P}{P^\circ}\right)^1 = \frac{y_{\text{C}_4\text{H}_6} y_{\text{H}_2}}{y_{\text{C}_4\text{H}_8}}

$$

Let $x$ be the extent of reaction. Basis: 1 mole of $\text{C}_4\text{H}_8$ and 10 moles of inert steam.

| Species | Initial (mol) | Equilibrium (mol) |
| :--- | :---: | :---: |
| $\text{C}_4\text{H}_8$ | 1 | $1 - x$ |
| $\text{C}_4\text{H}_6$ | 0 | $x$ |
| $\text{H}_2$ | 0 | $x$ |
| $\text{H}_2\text{O}$ (inert) | 10 | 10 |
| **Total** | 11 | $n_{total} = 11 + x$ |

Substitute mole fractions $y_i = n_i / n_{total}$ into the equilibrium expression:

$$

0.329 = \frac{(\frac{x}{11+x})(\frac{x}{11+x})}{(\frac{1-x}{11+x})} = \frac{x^2}{(1-x)(11+x)}

$$

This simplifies to the quadratic equation $1.329x^2 + 3.29x - 3.619 = 0$. Solving for the positive root:

$$

x = \frac{-3.29 + \sqrt{(3.29)^2 - 4(1.329)(-3.619)}}{2(1.329)} \approx 0.825

$$

The conversion is $x/1.0 = 0.825$, or **82.5\%**.

**Step 2: Calculate Conversion without Steam**

The stoichiometry table simplifies with $n_{total} = 1+x$.

$$

K_a = 0.329 = \frac{(\frac{x}{1+x})(\frac{x}{1+x})}{(\frac{1-x}{1+x})} = \frac{x^2}{1-x^2}

$$

Solving for $x$: $0.329(1-x^2) = x^2 \implies 1.329x^2 = 0.329 \implies x = \sqrt{0.329/1.329} \approx 0.498$.

Without steam, the equilibrium conversion is **49.8\%**.
```

## Thermal Effects in Chemical Reactions

This section introduces the fundamental equations that govern thermal effects in reactors, including the temperature dependence of equilibrium and energy balances for adiabatic and isothermal systems.

### Temperature Dependence of the Equilibrium Constant

```{note}
The **Van't Hoff Equation** quantitatively describes how the equilibrium constant ($K_e$) changes with temperature.

For an exothermic reaction ($\Delta H < 0$), $K_e$ decreases as temperature increases.

For an endothermic reaction ($\Delta H > 0$), $K_e$ increases as temperature increases. This relationship is crucial for determining the optimal operating temperature for reversible reactions.
```

```{admonition} Term Definitions
:class: tip
- **$K_e, K_m$**: Dimensionless equilibrium constants at temperatures $T$ and $T_m$, respectively.
- **$\Delta H$**: The heat of reaction, assumed constant [J/mol or cal/mol].
- **$R$**: The ideal gas constant [$8.314 \, \text{J/(mol}\cdot\text{K)}$ or $1.987 \, \text{cal/(mol}\cdot\text{K)}$].
- **$T, T_m$**: Absolute temperatures in Kelvin [K].
```

```{important}
The integrated Van't Hoff equation is:

$$

K_e = K_m \exp\left[ \left(\frac{\Delta H}{R}\right) \left(\frac{1}{T_m} - \frac{1}{T}\right) \right] \quad \text{(Equation 1)}

$$

```

### Equilibrium Conversion for A $\rightleftharpoons$ B

```{note}
For a simple reversible reaction, **the equilibrium conversion ($X_e$)** is the maximum possible conversion that can be achieved at a given temperature and pressure. It is determined directly by the value of the equilibrium constant, $K_e$. At equilibrium, the forward and reverse reaction rates are equal.
```

```{important}
For the elementary reversible reaction A $\rightleftharpoons$ B, the relationship is:

$$

X_e = \frac{K_e}{1 + K_e} \quad \text{(Equation 2)}

$$

This is derived from $K_e = \frac{C_B}{C_A} = \frac{C_{A0}X_e}{C_{A0}(1-X_e)}$.
```

### Energy Balance: Adiabatic vs. Isothermal Reactors

```{note}
The reactor energy balance relates the conversion achieved to the thermal conditions.

- **Adiabatic Reactor**: No heat is exchanged with the surroundings ($\dot{Q}=0$). The temperature changes as a function of conversion due to the heat of reaction.
- **Isothermal Reactor**: The temperature is held constant. This requires active heat transfer ($\dot{Q} \neq 0$) to compensate for the heat of reaction.
```

```{admonition} Term Definitions
:class: tip
- **$X, X_e$**: Fractional conversion and equilibrium fractional conversion.
- **$C_{PA}, C_{PI}$**: Molar heat capacities of reactant A and inert I.
- **$\alpha$**: Molar ratio of inerts to reactant A in the feed ($F_{I0} / F_{A0}$).
- **$T, T_{feed}$**: Reactor temperature and feed temperature.
- **$\dot{Q}$**: Rate of heat transfer [W or J/s].
- **$F_{A0}$**: Molar feed rate of reactant A [mol/s].
```

```{important}
For a simple reaction A $\rightleftharpoons$ B with constant heat capacities ($C_{PA} = C_{PB}$):

$$

\text{Adiabatic:} \quad X_{energy} = \frac{(C_{PA} + \alpha C_{PI})(T - T_{feed})}{-\Delta H_{rxn}} \quad \text{(Equation 3a)}

$$

$$

\text{Isothermal:} \quad \dot{Q} = X F_{A0} (-\Delta H_{rxn}) \quad \text{(Equation 3b)}

$$

```

### Example Problems

```{prf:example} Adiabatic Equilibrium Temperature and Conversion
For the reversible, liquid-phase reaction, A $\leftrightarrow$ B, determine the adiabatic equilibrium temperature and conversion when pure A is fed to the reactor at 300 K.

- $C_{PA} = C_{PB} = 50$ cal/(mol K)
- $K_e = 1.0 \times 10^5$ at 298 K
- $\Delta H_{rxn} = -2.0 \times 10^4$ cal/mol
```

```{dropdown} Solution Steps
**Step 1: Formulate the Equilibrium Conversion ($X_e$) Equation**

The equilibrium conversion $X_e$ depends on the equilibrium constant $K_e$, which in turn depends on temperature via the Van't Hoff equation (Eq. 1). Combining with Eq. 2:

$$

X_e(T) = \frac{K_e(T)}{1 + K_e(T)}

$$

where

$$

K_e(T) = (1.0 \times 10^5) \exp\left[ \frac{-20000 \, \text{cal/mol}}{1.987 \, \text{cal/(mol K)}} \left(\frac{1}{298 \text{ K}} - \frac{1}{T}\right) \right]

$$

This equation defines the S-shaped equilibrium curve. Since the reaction is exothermic ($\Delta H_{rxn} < 0$), $X_e$ decreases as $T$ increases.

**Step 2: Formulate the Energy Balance ($X_{energy}$) Equation**

For an adiabatic reactor with pure A feed ($\alpha = 0$), the energy balance (Eq. 3a) gives a linear relationship between conversion and temperature:

$$

X_{energy} = \frac{C_{PA}(T - T_{feed})}{-\Delta H_{rxn}} = \frac{50 \, \text{cal/(mol K)} \times (T - 300 \text{ K})}{20000 \, \text{cal/mol}} = \frac{T - 300}{400}

$$

This is the straight energy balance line, which starts at $X=0$ for $T=300$ K.

**Step 3: Solve for the Intersection**

We set $X_e = X_{energy}$ and solve for the common point $(T, X)$. This system of equations is typically solved graphically or with a numerical solver. The intersection of the equilibrium curve and the energy balance line yields the unique adiabatic operating point. The simultaneous solution of the two equations gives the final state of the reactor:

- **Adiabatic Equilibrium Temperature: $T \approx 460$ K**
- **Adiabatic Equilibrium Conversion: $X \approx 0.40$ (or 40\%)**
```

```{prf:example} Heat Duty for an Isothermal Reactor
100 mol/h of $\text{N}_2$ and 300 mol/h of $\text{H}_2$ are fed to an isothermal reactor at $350^\circ\text{C}$ to carry out the ammonia synthesis reaction:

$$

\text{N}_2(g) + 3\text{H}_2(g) \rightarrow 2\text{NH}_3(g)

$$

How much heat must be removed to maintain the reactor temperature if the conversion of $\text{N}_2$ is 75\%?

- $C_P(\text{N}_2) = C_P(\text{H}_2) = 29\ \text{J/(mol}\cdot\text{K)}$
- $C_P(\text{NH}_3) = 36\ \text{J/(mol}\cdot\text{K)}$
- $\Delta H^\circ_{f, \text{NH}_3} = -46\ \text{kJ/mol at } 25^\circ\text{C}$
```

```{dropdown} Solution Steps
We calculate the total enthalpy change ($\Delta H_{\text{total}}$) from inlet to outlet using a hypothetical path with a reference temperature of $25^\circ\text{C}$ (298.15 K). The heat to be removed is $\dot{Q} = -\Delta H_{\text{total}}$.

**Step 1: Determine Outlet Molar Flow Rates**

The feed is stoichiometric. For 75\% conversion of $\text{N}_2$ (the limiting reactant):

- $\text{N}_2$ reacted: $100\ \text{mol/h} \times 0.75 = 75\ \text{mol/h}$
- $\text{H}_2$ reacted: $75 \times 3 = 225\ \text{mol/h}$
- $\text{NH}_3$ produced: $75 \times 2 = 150\ \text{mol/h}$

The resulting outlet molar flow rates ($F_{\text{out},i}$) are:

- $F_{\text{N}_2,\ \text{out}} = 100 - 75 = 25\ \text{mol/h}$
- $F_{\text{H}_2,\ \text{out}} = 300 - 225 = 75\ \text{mol/h}$
- $F_{\text{NH}_3,\ \text{out}} = 0 + 150 = 150\ \text{mol/h}$

**Step 2: Path Segment 1: Cool Reactants to $25^\circ\text{C}$**

Calculate the enthalpy change ($\Delta H_1$) for cooling the feed stream from $350^\circ\text{C}$ (623.15 K) to $25^\circ\text{C}$ (298.15 K). Here, $\Delta T = -325$ K.

$$

\Delta H_1 = \sum F_{\text{in},i} C_{P,i} \Delta T = \left(100 \times 29 + 300 \times 29\right)\ \text{J/(h$\cdot$K)} \times (-325\ \text{K})

$$

$$

\Delta H_1 = 11600 \times (-325) = -3,770,000\ \text{J/h} = -3770\ \text{kJ/h}

$$

**Step 3: Path Segment 2: Reaction at $25^\circ\text{C}$**

Calculate the enthalpy change from the reaction ($\Delta H_2$) at the reference temperature. First, find the standard heat of reaction per mole of $\text{N}_2$.

$$

\Delta H_{\text{rxn},298} = \sum \nu_i \Delta H^\circ_{f,i} = \left[2(-46)\right] - \left[1(0) + 3(0)\right] = -92\ \text{kJ/mol of }\text{N}_2

$$

The total enthalpy change for reacting 75 mol/h of $\text{N}_2$ is:

$$

\Delta H_2 = 75\ \text{mol/h} \times (-92\ \text{kJ/mol}) = -6900\ \text{kJ/h}

$$

**Step 4: Path Segment 3: Heat Products to $350^\circ\text{C}$**

Calculate the enthalpy change ($\Delta H_3$) for heating the outlet mixture from $25^\circ\text{C}$ to $350^\circ\text{C}$. Here, $\Delta T = +325$ K.

$$

\Delta H_3 = \sum F_{\text{out},i} C_{P,i} \Delta T

$$

$$

\Delta H_3 = \left(25 \times 29 + 75 \times 29 + 150 \times 36\right)\ \text{J/(h$\cdot$K)} \times 325\ \text{K}

$$

$$

\Delta H_3 = \left(725 + 2175 + 5400\right) \times 325 = 8300 \times 325 = 2,697,500\ \text{J/h} = 2697.5\ \text{kJ/h}

$$

**Step 5: Calculate Total Heat Duty ($\dot{Q}$)**

Sum the enthalpy changes along the hypothetical path to find the total enthalpy change:

$$

\Delta H_{\text{total}} = \Delta H_1 + \Delta H_2 + \Delta H_3 = -3770 + (-6900) + 2697.5 = -7972.5\ \text{kJ/h}

$$

The heat that must be removed from the reactor is $\dot{Q} = -\Delta H_{\text{total}}$:

$$

\dot{Q} = -(-7972.5\ \text{kJ/h}) = 7972.5\ \text{kJ/h}

$$

Converting to kW (1 kW = 3600 kJ/h):

$$

\dot{Q} = 7972.5\ \text{kJ/h} \times \frac{1\ \text{kW}}{3600\ \text{kJ/h}} \approx 2.21\ \text{kW}

$$

**Step 6: Final Answer**

Approximately **2.2 kW** of heat must be removed to maintain the reactor at an isothermal temperature of $350^\circ\text{C}$.
```

## Chemical Equilibrium for Multiple Reactions

When multiple chemical reactions occur simultaneously, the system's final equilibrium composition cannot be determined by a single equilibrium constant. This guide covers the method of Gibbs free energy minimization, a robust technique for solving complex reaction equilibria.

### Gibbs Free Energy and Chemical Potential

```{note}
At constant temperature and pressure, a chemical system will spontaneously evolve towards the state with the minimum possible total Gibbs free energy. The equilibrium composition corresponds to this global minimum. The key quantity for this calculation is the **chemical potential** of each species $i$, which is equivalent to its partial molar Gibbs free energy ($\bar{G}_i$) in the mixture.
```

```{admonition} Term Definitions
:class: tip
- **$\bar{G}_i$**: Partial molar Gibbs free energy (chemical potential) of component $i$ in the mixture [J/mol].
- **$\Delta G^\circ_{f,i}$**: Standard Gibbs free energy of formation of component $i$ at temperature $T$ [J/mol].
- **$y_i$**: Mole fraction of component $i$ in the mixture.
- **$n_i$**: Number of moles of component $i$.
- **$n$**: Total number of moles in the mixture.
- **$G$**: Gibbs free energy per mole of the mixture.
- **$P$**: Total pressure of the system [bar].
- **$P^\circ$**: Standard-state pressure, 1 bar.
- **$R$**: Ideal gas constant [$8.314 \, \text{J/(mol}\cdot\text{K)}$].
- **$T$**: Absolute temperature [K].
```

```{important}
For an ideal gas, the partial molar Gibbs free energy of component $i$ is:

$$

\bar{G}_i = \Delta G^\circ_{f,i} + RT \ln\left(\frac{P}{P^\circ}\right) + RT \ln(y_i) \quad \text{(Equation 1)}

$$

The total Gibbs free energy of the mixture is the sum over all species:

$$

nG = \sum_i n_i \bar{G}_i = \sum_i n_i \left[ \Delta G^\circ_{f,i} + RT \ln\left(\frac{y_i P}{P^\circ}\right) \right] \quad \text{(Equation 2)}

$$

This is the objective function to be minimized.
```

### Constraints: Atomic Balances

```{note}
The minimization of Gibbs free energy is not unconstrained. It is subject to the fundamental law of conservation of mass, applied as **atomic balances**. The total number of atoms of each element (e.g., C, H, O) in the system must remain constant from the initial feed to the final equilibrium composition.
```

```{important}
For each element $j$ present in the system, a constraint equation must be satisfied:

$$

(\text{Total moles of atoms of element } j)_{\text{in}} = (\text{Total moles of atoms of element } j)_{\text{out}}

$$

$$

\sum_i n_{i,\text{in}} a_{ij} = \sum_i n_{i,\text{out}} a_{ij} \quad \text{(Equation 3)}

$$

where $a_{ij}$ is the number of atoms of element $j$ in one molecule of species $i$.
```

### Temperature-Dependent Thermodynamics

```{note}
To perform Gibbs minimization at a specific temperature $T$, the standard Gibbs free energies of formation ($\Delta G^\circ_{f,i}$) for every species must be known at that temperature. These values are calculated by integrating heat capacity ($C_P$) data from a known reference state (usually 298.15 K).
```

```{important}
The heat capacity is often expressed as a polynomial in temperature:

$$

C_{P,i} = A_i + B_i T + C_i T^2 + D_i T^3

$$

For a reaction, the change in heat capacity is $\Delta C_P = \sum_i \nu_i C_{P,i}$. This allows us to find the heat of reaction ($\Delta H^\circ_T$) at any temperature $T$ by integration from a reference temperature $T_R$:

$$

\Delta H^\circ_T = \Delta H^\circ_R + \int_{T_R}^T \Delta C_P \,dT

$$

This integrates to a compact form using a constant of integration, $J$:

$$

\Delta H^\circ_T = J + \Delta A T + \frac{\Delta B}{2} T^2 + \frac{\Delta C}{3} T^3 + \frac{\Delta D}{4} T^4

$$

where $J = \Delta H^\circ_R - \Delta A T_R - \frac{\Delta B}{2} T_R^2 - \frac{\Delta C}{3} T_R^3 - \frac{\Delta D}{4} T_R^4$.

The Gibbs free energy of reaction is then found by integrating the Van't Hoff equation:

$$

\frac{\Delta G^\circ_T}{RT} - \frac{\Delta G^\circ_R}{RT_R} = \int_{T_R}^T -\frac{\Delta H^\circ_T}{RT^2} \,dT

$$

This also integrates to a compact form using a second constant of integration, $I$:

$$

\frac{\Delta G^\circ_T}{RT} = I - \frac{J}{RT} + \frac{\Delta A}{R}\ln T + \frac{\Delta B}{2R} T + \frac{\Delta C}{6R} T^2 + \frac{\Delta D}{12R} T^3

$$

where $I = \frac{1}{R} [ \frac{\Delta G^\circ_R}{T_R} - \frac{J}{T_R} + \Delta A \ln T_R - \frac{\Delta B}{2} T_R - \frac{\Delta C}{6} T_R^2 - \frac{\Delta D}{12} T_R^3 ]$.

These equations are applied to formation reactions to find each $\Delta G^\circ_{f,i}$ at the desired temperature.
```

### Example Problems

```{prf:example} Water-Gas Shift Reaction
Calculate the equilibrium composition at 750 K and 1 bar for the water-gas shift reaction for a feed of 2 mol/s CO and 2 mol/s H$_{2}$O. Use both the extent of reaction method and Gibbs minimization with temperature-dependent data.

$$

\text{CO(g)} + \text{H}_2\text{O(g)} \rightleftharpoons \text{H}_2\text{(g)} + \text{CO}_2\text{(g)}

$$

```

```{dropdown} Solution Steps
This method uses the reaction stoichiometry and a calculated equilibrium constant.

**Step 1: Set up Stoichiometry Table**

Let $\xi$ be the extent of reaction.

| Species | Initial Moles | Equilibrium Moles |
| :--- | :--- | :--- |
| CO | 2 | $2 - \xi$ |
| H$_{2}$O | 2 | $2 - \xi$ |
| H$_{2}$ | 0 | $\xi$ |
| CO$_{2}$ | 0 | $\xi$ |
| **Total** | 4 | $n_{T} = (2-\xi) + (2-\xi) + \xi + \xi = 4$ |

**Step 2: Calculate Equilibrium Constant ($K_{eq}$)**

First, calculate the standard Gibbs free energy of reaction at 750 K using the temperature-dependent equations. This yields $\Delta G^\circ_{rxn, 750K} = -11,210 \, \text{J/mol}$.

$$

K_{eq} = \exp\left(-\frac{\Delta G^\circ_{rxn}}{RT}\right) = \exp\left(-\frac{-11210}{8.314 \times 750}\right) = \exp(1.799) \approx 6.04

$$

**Step 3: Solve for Extent of Reaction ($\xi$)**

Since the total moles and pressure terms cancel ($\Delta \nu = 0$), $K_{eq}$ is a ratio of mole numbers.

$$

K_{eq} = \frac{n_{H_2} n_{CO_2}}{n_{CO} n_{H_2O}} \implies 6.04 = \frac{(\xi)(\xi)}{(2-\xi)(2-\xi)} = \left(\frac{\xi}{2-\xi}\right)^2

$$

Taking the square root:

$$

\sqrt{6.04} = 2.458 = \frac{\xi}{2-\xi} \implies 4.916 - 2.458\xi = \xi \implies \xi = \frac{4.916}{3.458} \approx 1.422 \, \text{mol}

$$

**Step 4: Determine Final Composition**

Moles CO = Moles H$_{2}$O = $2 - 1.422 = \mathbf{0.578}$ mol.

Moles H$_{2}$ = Moles CO$_{2}$ = $\xi = \mathbf{1.422}$ mol.
```

```{prf:example} Methane Steam Reforming (Multiple Reactions)
Calculate the equilibrium composition at 950 K and 3.0 bar for a feed of 1.0 mol/s CH$_{4}$ and 1.0 mol/s H$_{2}$O. The possible products are CO, CO$_{2}$, and H$_{2}$. Use the Gibbs minimization method.
```

```{dropdown} Solution Steps
**Step 1: Define the System**

**Species:** CH$_4$, H$_2$O, CO, CO$_2$, H$_2$
**Conditions:** $T = 950\ \text{K}$, $P = 3.0\ \text{bar}$

**Step 2: Set up the Minimization Problem**

**Variables:** Final mole numbers to be determined: $n_{CH_4}, n_{H_2O}, n_{CO}, n_{CO_2}, n_{H_2}$.

**Objective Function:** Minimize total Gibbs free energy of the mixture:

$$

nG = \sum_{i=1}^{5} n_i \left[ \Delta G^\circ_{f,i,\ 950K} + RT \ln\left(y_i \frac{P}{P^\circ}\right) \right]

$$

**Constraints (Atomic Balances):**

$$

\begin{align}
&\text{Carbon:} && n_{CH_4} + n_{CO} + n_{CO_2} = 1.0 \\
&\text{Hydrogen:} && 4n_{CH_4} + 2n_{H_2O} + 2n_{H_2} = 6.0 \\
&\text{Oxygen:} && n_{H_2O} + n_{CO} + 2n_{CO_2} = 1.0 \\
&\text{Non-negativity:} && n_i \ge 0\quad \text{for all species}
\end{align}

$$

**Step 3: Solve and State Results**

This constrained minimization is solved numerically. The calculation yields the following equilibrium composition:

| Species | Equilibrium Moles | Mole Fraction ($y_i$) |
| :--- | :---: | :---: |
| CH$_{4}$ | 0.052 | 0.017 |
| H$_{2}$O | 0.170 | 0.056 |
| CO | 0.730 | 0.240 |
| CO$_{2}$ | 0.218 | 0.072 |
| H$_{2}$ | 1.839 | 0.605 |
| **Total Moles** | **3.009** | **1.000** |

**Step 4: Conclusion**

At 950 K and 3.0 bar, the methane is almost completely converted. The results show that the Gibbs minimization method robustly handles complex systems without needing to define or solve for multiple reaction extents and equilibrium constants.
```

## Chemical Equilibrium and Le Châtelier's Principle

This guide explores Le Châtelier's Principle, a qualitative tool for predicting how a system at equilibrium responds to external changes. We will use the industrially significant Haber-Bosch process for ammonia synthesis as a running example to illustrate these concepts.

```{note}
Le Châtelier's Principle states that when a system at equilibrium is subjected to a change in conditions (a "stress"), the system will shift its equilibrium position to partially counteract the effect of the change. The primary stresses include changes in:
- Temperature
- Pressure
- Concentration (or moles) of a reacting species
```

### The Ammonia Synthesis Reaction (Haber-Bosch Process)

```{note}
The Haber-Bosch process is a reversible, gas-phase reaction that synthesizes ammonia from nitrogen and hydrogen.
- It is an *exothermic* reaction, meaning it releases heat as it proceeds in the forward direction.
- The change in the number of moles of gas is negative, which is a critical feature for analyzing the effect of pressure.
```

```{important}
The balanced chemical equation is:

$$

\text{N}_2\text{(g)} + 3\text{H}_2\text{(g)} \rightleftharpoons 2\text{NH}_3\text{(g)} \quad\quad \Delta H < 0

$$

The change in moles of gas is:

$$

\Delta \nu = (\text{moles of gas products}) - (\text{moles of gas reactants}) = 2 - (1 + 3) = -2

$$

```

### The Equilibrium Constant Expression

```{admonition} Term Definitions
:class: tip
The following variables are used to quantitatively describe the equilibrium state:
- **$K_a$**: The thermodynamic equilibrium constant. It is dimensionless and depends only on temperature.
- **$y_i$**: The mole fraction of component $i$ (e.g., $y_{NH_3}$) at equilibrium.
- **$P$**: The total pressure of the system (e.g., in bar).
- **$P^\circ$**: The standard-state pressure (defined as 1 bar).
- **$K_y$**: A parameter representing the ratio of mole fractions at equilibrium. For a given temperature, $K_y$ will change if the pressure changes.
```

```{important}
The thermodynamic equilibrium constant, $K_a$, is defined using the activities ($a_i$) of the species. For an ideal gas, $a_i = y_i P / P^\circ$.

$$

K_a = \frac{(a_{NH_3})^2}{(a_{N_2})(a_{H_2})^3} = \frac{(y_{NH_3}P/P^\circ)^2}{(y_{N_2}P/P^\circ)(y_{H_2}P/P^\circ)^3}

$$

This expression can be separated into a mole fraction term ($K_y$) and a pressure term:

$$

K_a = \left( \frac{y_{NH_3}^2}{y_{N_2} y_{H_2}^3} \right) \left( \frac{P}{P^\circ} \right)^{2 - (1+3)} = K_y \left( \frac{P}{P^\circ} \right)^{-2}

$$

This equation quantitatively governs the equilibrium position and is the basis for understanding the effects of pressure changes.
```

### Applying Le Châtelier's Principle to Ammonia Synthesis

#### 1. Effect of Temperature

```{note}
According to Le Châtelier's principle, changing the temperature of a system at equilibrium will cause a shift in the direction that counteracts the temperature change.
- *Increasing Temperature*: Favors the endothermic (heat-absorbing) direction.
- *Decreasing Temperature*: Favors the exothermic (heat-releasing) direction.
```

```{admonition} Term Definitions
:class: tip
Application to the Haber-Bosch process ($\Delta H < 0$, exothermic):
- **Prediction**: If temperature is increased, the system will try to "cool down" by shifting in the endothermic (reverse) direction. This means the equilibrium shifts to the left, consuming NH$_{3}$ and producing more N$_{2}$ and H$_{2}$.
- **Result**: A higher temperature leads to a lower equilibrium conversion and a smaller yield of ammonia.
- **Conclusion**: To maximize the equilibrium yield, a low temperature is thermodynamically favorable. However, reaction rates are slow at low temperatures, so a compromise temperature (e.g., 400-450$^\circ$C) is used in practice.
```

```{important}
This effect is quantified by the Van't Hoff Equation. Since $\Delta H^\circ_{rxn}$ is negative for this reaction:

$$

\frac{d(\ln K_a)}{dT} = \frac{\Delta H^\circ_{rxn}}{RT^2} < 0

$$

This shows that as temperature ($T$) increases, $\ln(K_a)$ must decrease, meaning the equilibrium constant $K_a$ itself decreases. A smaller $K_a$ signifies a lower equilibrium yield of products.
```

#### 2. Effect of Pressure

```{note}
Changing the total pressure on a gaseous system at equilibrium will cause a shift in the direction that reduces the number of gas molecules.
- *Increasing Pressure*: Favors the side of the reaction with fewer moles of gas.
- *Decreasing Pressure*: Favors the side of the reaction with more moles of gas.
```

```{admonition} Term Definitions
:class: tip
Application to the Haber-Bosch process (4 moles of gas $\rightleftharpoons$ 2 moles of gas):
- **Prediction**: The forward reaction reduces the number of gas molecules from 4 to 2. Therefore, increasing the total pressure will shift the equilibrium to the right to counteract the pressure increase.
- **Result**: Higher pressure leads to a higher equilibrium conversion and a greater yield of ammonia.
- **Conclusion**: Industrial reactors are operated at very high pressures (e.g., 150-250 bar) to maximize the yield.
```

```{important}
The quantitative reason is found in the equilibrium expression:

$$

K_a = K_y \left( \frac{P}{P^\circ} \right)^{-2} \quad \implies \quad K_y = K_a \left( \frac{P}{P^\circ} \right)^{2}

$$

At a constant temperature, $K_a$ is a constant. The equation shows that if the total pressure $P$ is increased, the mole fraction term $K_y$ must also increase to maintain the equality. A larger $K_y$ means the ratio of product mole fractions to reactant mole fractions has increased, which corresponds to a shift to the right.
```

#### 3. Effect of Changing Moles (Concentration)

```{note}
Adding or removing a chemical species involved in the equilibrium will cause a shift that consumes the added species or replenishes the removed species. This is often analyzed using the reaction quotient, $Q$.
- If $Q < K_a$: The ratio of products to reactants is too low. The reaction shifts to the right (products).
- If $Q > K_a$: The ratio of products to reactants is too high. The reaction shifts to the left (reactants).
- If $Q = K_a$: The system is at equilibrium.
```

```{admonition} Term Definitions
:class: tip
Application to the Haber-Bosch process:
- **Adding Reactants (N$_{2}$ or H$_{2}$)**: This decreases the denominator of the reaction quotient $Q$, making $Q < K_a$. The equilibrium shifts to the right to consume the added reactants and form more ammonia.
- **Removing Product (NH$_{3}$)**: This decreases the numerator of $Q$, making $Q < K_a$. The equilibrium shifts to the right to replenish the ammonia that was removed. This is a common industrial strategy to drive a reaction to completion.
- **Adding an Inert Gas**: At constant volume, adding an inert gas increases total pressure but does not change partial pressures, so there is no shift. At constant total pressure, adding an inert gas decreases the partial pressures of all reacting species, which is equivalent to a pressure decrease, shifting the equilibrium to the side with more moles (left).
```

# Phase Equilibria: Ideal Systems

This guide covers vapor-liquid equilibrium (VLE) for ideal systems, where interactions between molecules are uniform. The behavior of these systems is described by Raoult's Law, which provides a simple and direct relationship between the liquid phase composition, vapor phase composition, and system pressure at a given temperature.

## Saturation Pressure and the Antoine Equation

```{note}
The *saturation pressure* ($P_i^{sat}$) of a pure component is the pressure at which it boils at a given temperature. It is a fundamental property in VLE and is highly sensitive to temperature. The Antoine equation is a widely used semi-empirical correlation that accurately relates saturation pressure to temperature.
```

```{admonition} Term Definitions
:class: tip
The following variables are used in the Antoine equation:
- **$P_i^{sat}$**: Saturation pressure of pure component $i$. Units can be kPa, bar, mmHg, etc.
- **$T$**: System temperature. The required units (K or $^\circ$C) depend on the constants.
- **$A_i, B_i, C_i$**: Component-specific Antoine constants obtained from experimental data.
```

```{important}
A common form of the Antoine equation is:

$$

\log_{10}(P_i^{sat}) = A_i - \frac{B_i}{C_i + T}

$$

Another form uses the natural logarithm, which requires a different set of constants:

$$

\ln(P_i^{sat}) = A_i - \frac{B_i}{C_i + T}

$$

It is critical to use the correct temperature units and logarithm base associated with the published constants.
```

## Raoult's Law for Ideal Solutions

```{note}
Raoult's Law is the cornerstone of ideal VLE. It states that the partial pressure of a component in the vapor phase is equal to its mole fraction in the liquid phase multiplied by its pure-component saturation pressure at the system temperature. This law assumes both the liquid and vapor phases behave ideally.
```

```{admonition} Term Definitions
:class: tip
The variables involved in Raoult's Law are:
- **$y_i$**: Mole fraction of component $i$ in the vapor phase.
- **$x_i$**: Mole fraction of component $i$ in the liquid phase.
- **$P$**: Total pressure of the system.
- **$P_i$**: Partial pressure of component $i$ in the vapor phase ($P_i = y_i P$).
- **$P_i^{sat}$**: Saturation pressure of pure component $i$ at the system temperature $T$.
```

```{important}
The mathematical statement of Raoult's Law is:

$$

y_i P = x_i P_i^{sat} \quad \text{(for each component } i \text{)}

$$

```

## Bubble and Dew Point Calculations

```{note}
For a binary mixture, Raoult's Law allows us to define two critical types of VLE calculations:
- **Bubble Point**: Given a liquid of known composition ($x_i$), the bubble point is the state (T or P) where the first bubble of vapor forms. At this point, the sum of the partial pressures equals the total pressure.
- **Dew Point**: Given a vapor of known composition ($y_i$), the dew point is the state (T or P) where the first drop of liquid forms. At this point, the liquid mole fractions calculated from the vapor must sum to one.
```

```{important}
The governing equations for a binary system (components 1 and 2) are:
- **Bubble Pressure Equation**: Used when liquid composition ($x_1, x_2$) is known.
  
  $$

  P = x_1 P_1^{sat} + x_2 P_2^{sat}

  $$

- **Dew Pressure Equation**: Used when vapor composition ($y_1, y_2$) is known.
  
  $$

  P = \frac{1}{\frac{y_1}{P_1^{sat}} + \frac{y_2}{P_2^{sat}}}

  $$

When temperature is the unknown, these equations must be solved iteratively.
```

## Example Problems

```{prf:example} Bubble Temperature Calculation
Calculate the bubble temperature at 85 kPa for an ideal binary liquid solution with a composition of $x_1 = 0.40$. The saturation pressures are given by the following Antoine equations, where T is in $^\circ$C and P is in kPa:

$$

\ln(P_1^{sat}) = 14.3 - \frac{2945}{T + 224}

$$

$$

\ln(P_2^{sat}) = 14.2 - \frac{2943}{T + 209}

$$

```

```{dropdown} Solution Steps
**Step 1: Define the Goal and Governing Equation**

This is a **bubble temperature** calculation. We are given the total pressure ($P=85$ kPa) and the liquid composition ($x_1=0.40$, $x_2=0.60$). We need to find the temperature $T$ that satisfies the bubble pressure equation:

$$

P = x_1 P_1^{sat}(T) + x_2 P_2^{sat}(T)

$$

Since $T$ is inside the exponential functions for $P^{sat}$, this equation is non-linear and requires an iterative solution.

**Step 2: Set Up the Iterative Solution**

We need to find the root of the following function $f(T) = 0$:

$$

f(T) = x_1 P_1^{sat}(T) + x_2 P_2^{sat}(T) - P = 0

$$

Substituting the known values and expressions:

$$

0.40 \exp\left(14.3 - \frac{2945}{T + 224}\right) + 0.60 \exp\left(14.2 - \frac{2943}{T + 209}\right) - 85 = 0

$$

The solution process involves:
- Guess a temperature, $T_{guess}$.
- Calculate $P_1^{sat}$ and $P_2^{sat}$ at $T_{guess}$.
- Calculate the total pressure, $P_{calc} = x_1 P_1^{sat} + x_2 P_2^{sat}$.
- If $P_{calc} > P_{actual}$ (85 kPa), the guess is too high. If $P_{calc} < P_{actual}$, the guess is too low. Adjust $T_{guess}$ and repeat until $P_{calc} \approx P_{actual}$.

**Step 3: Final Answer**

**Bubble Temperature: $T = 84.4^\circ$C**
```

```{prf:example} Isothermal Flash Calculation
A fixed-volume tank initially contains 1.0 mol of pure component A as a vapor at 1.9 bar. The saturation pressure of A at the tank temperature is $P_A^{sat} = 2.0$ bar. Then, 1.0 mol of liquid component B, with a saturation pressure of $P_B^{sat} = 1.0$ bar, is added to the tank. After the system reaches equilibrium at the same temperature, the final pressure is 1.44 bar. Assuming ideal behavior, determine the phases present, their compositions, and the number of moles of each phase.
```

```{dropdown} Solution Steps
**Step 1: Analyze the System State**
- **Initial State**: Component A is at $P = 1.9$ bar, which is below its saturation pressure of $P_A^{sat} = 2.0$ bar. Therefore, it exists as a single-phase superheated vapor.
- **Final State**: The final mixture has a pressure of $P = 1.44$ bar. Since this pressure lies between the saturation pressures of the two pure components ($P_B^{sat} < P < P_A^{sat}$), the system at equilibrium must consist of a **vapor-liquid mixture**. If the final pressure were greater than $P_A^{sat}$, it would be a subcooled liquid. If it were less than $P_B^{sat}$, it would be a superheated vapor.

**Step 2: Determine Equilibrium Compositions ($x_A$, $y_A$)**

Since two phases are present at a known total pressure, we can use the bubble pressure form of Raoult's Law to find the liquid phase composition, $x_A$.

$$

P = x_A P_A^{sat} + x_B P_B^{sat}

$$

Substitute $x_B = 1 - x_A$:

$$

1.44 = x_A(2.0) + (1 - x_A)(1.0)

$$

$$

1.44 = 2.0 x_A + 1.0 - 1.0 x_A \implies 0.44 = x_A

$$

The liquid phase composition is **$x_A = 0.44$** and **$x_B = 0.56$**.

Next, find the vapor phase composition, $y_A$, using Raoult's Law:

$$

y_A = \frac{x_A P_A^{sat}}{P} = \frac{0.44 \times 2.0}{1.44} = 0.611

$$

The vapor phase composition is **$y_A = 0.611$** and **$y_B = 0.389$**.

**Step 3: Determine Moles of Liquid (L) and Vapor (V)**

This calculation, often called a "flash," uses overall mole balances.
- Total moles in system, $N = N_A + N_B = 1.0 + 1.0 = 2.0$ mol.
- Overall mole fraction of A, $z_A = N_A / N = 1.0 / 2.0 = 0.5$.

We can write two balance equations:
- **Overall Mole Balance**: The total moles are split between the liquid and vapor phases.

$$

L + V = N = 2.0

$$

- **Component A Mole Balance**: The total moles of A are distributed between the two phases.

$$

x_A L + y_A V = z_A N

$$

Now we solve this system of two linear equations. Substitute $V = 2.0 - L$ into the component balance:

$$

(0.44)L + (0.611)(2.0 - L) = (0.5)(2.0)

$$

$$

0.44L + 1.222 - 0.611L = 1.0

$$

$$

-0.171L = 1.0 - 1.222

$$

$$

-0.171L = -0.222 \implies L = \frac{0.222}{0.171} = 1.298 \, \text{mol}

$$

Then, find the moles of vapor:

$$

V = 2.0 - L = 2.0 - 1.298 = 0.702 \, \text{mol}

$$

**Step 4: Final Summary of Results**

The final state of the system is a two-phase mixture with the following properties:
- **Phases Present**: Vapor and Liquid.
- **Liquid Phase**: Amount = **1.30 mol**, Composition = **$x_A=0.44, x_B=0.56$**.
- **Vapor Phase**: Amount = **0.70 mol**, Composition = **$y_A=0.61, y_B=0.39$**.
```

## Absorption and Henry's Law

This guide covers phase equilibrium for systems where a component is sparingly soluble in a liquid, forming a dilute solution. In these cases, the ideal solution model (Raoult's Law) is inaccurate for the solute. Instead, we use Henry's Law, an empirical relationship crucial for modeling gas absorption and stripping processes.

### Henry's Law

```{note}
Henry's Law provides a linear relationship for the equilibrium of a dilute species between a liquid and a gas phase. It states that the partial pressure of a sparingly soluble component in the vapor phase is directly proportional to its mole fraction in the liquid phase.
- This law is most accurate at low concentrations (typically $x_i < 0.01$).
- The solvent (the component in high concentration) is still modeled using Raoult's Law.
```

```{admonition} Term Definitions
:class: tip
The variables used in the primary form of Henry's Law are:
- **$H_i$**: Henry's constant for solute $i$ in a specific solvent. The units are pressure (e.g., bar, Pa, atm).
- **$x_i$**: Mole fraction of solute $i$ in the liquid phase.
- **$y_i$**: Mole fraction of solute $i$ in the gas phase.
- **$P$**: Total pressure of the system.
```

```{important}
The form of Henry's Law analogous to Raoult's Law is:

$$

y_i P = x_i H_i

$$

Here, $H_i$ can be viewed as a "pseudo-saturation-pressure" for a species that may not be able to exist as a pure liquid at the system's temperature and pressure.
```

### Temperature Dependence of Henry's Constant

```{note}
The proportionality "constant" in Henry's Law, $H_i$, is not a true constant; it is highly dependent on temperature. Generally, the solubility of gases in liquids decreases as temperature increases, which corresponds to an increase in the value of $H_i$.
```

```{important}
A common empirical equation to model the temperature dependence of Henry's constant is:

$$

H = \frac{1}{\exp(A + B/T + C \ln T + D T)}

$$

Where $A$, $B$, $C$, and $D$ are constants specific to the solute-solvent pair, and $T$ is the absolute temperature (in Kelvin).
```

### Alternative Forms of Henry's Law

```{note}
It is critical to be aware that Henry's Law is used in many different forms, distinguished by the units of the Henry's constant. Always check the definition and units of a given $H_i$ before use.
```

```{admonition} Term Definitions
:class: tip
Additional variables used in alternative forms:
- **$C_i$**: Molar concentration of species $i$ in the liquid [mol/L].
- **$C_{i,gas}$**: Molar concentration of species $i$ in the gas [mol/L].
```

```{important}
Some common alternative definitions of Henry's Law are:
- **Volatility form**: $H_i = \frac{y_i P}{x_i}$ [Units of pressure]
- **Solubility form 1**: $H_i = \frac{C_i}{y_i P}$ [Units of mol/(Volume·Pressure)]
- **Solubility form 2**: $H_i = \frac{x_i}{y_i P}$ [Units of 1/Pressure]
- **Dimensionless form**: $H_i = \frac{C_i}{C_{i,gas}}$ [Dimensionless]
```

### Example Problem

```{prf:example} Single-Stage Stripping Process
A stream of dry air at 5 bar and 20$^\circ$C is used to strip a volatile organic compound (VOC) from a wastewater stream. The process occurs in a single equilibrium stage. The Henry's constant for the VOC in water at this temperature is 2.5 bar. The inlet water contains the VOC at a mole fraction of 0.0005. What flow rate of air (in moles per mole of water) is needed to remove 95\% of the VOC from the water?
```

```{dropdown} Solution Steps
**Step 1: Define System, Basis, and Goal**

**System:** A single-stage stripper where a VOC (component C) is transferred from a liquid water stream (W) to a gaseous air stream (A). The outlet streams are in equilibrium.

**Basis:** 1.0 mole of water entering the stripper ($n_{W,in} = 1.0$ mol).
**Goal:** Find the required molar flow rate of air, $n_A$.
**Given Data:**
Total Pressure: $P = 5$ bar
Henry's Constant: $H_C = 2.5$ bar
Inlet VOC mole fraction in liquid: $x_{C,in} = 0.0005$
Removal efficiency: 95\%

**Step 2: State Simplifying Assumptions**

Since the system is very dilute with respect to the VOC, we assume:

**Assumption 1:** The total molar flow rate of the liquid stream is approximately constant. VOC content is negligible, so $n_{L,out} \approx n_{W,in} = 1.0$ mol.
**Assumption 2:** The total molar flow rate of the vapor stream is approximately constant and equal to the inlet air flow. VOC and water vapor are negligible compared to air, so $n_{V,out} \approx n_{A,in}$.

**Step 3: Perform Contaminant Mole Balance**

Track the VOC (C) moles through the system:

Moles of VOC in (liquid):

$$

n_{C,in} = x_{C,in} \times n_{L,in} = 0.0005 \times 1.0 = 5 \times 10^{-4}\ \text{mol}

$$

Moles of VOC out (liquid):

$$

n_{C,out,L} = 0.05 \times n_{C,in} = 0.05 \times (5 \times 10^{-4}) = 2.5 \times 10^{-5}\ \text{mol}

$$

Moles of VOC out (vapor):

$$

n_{C,out,V} = 0.95 \times n_{C,in} = 0.95 \times (5 \times 10^{-4}) = 4.75 \times 10^{-4}\ \text{mol}

$$

**Step 4: Apply Henry's Law at the Outlet**

The outlet liquid and vapor streams are in equilibrium. We can relate their compositions using Henry's Law.

$$

y_{C,out} P = x_{C,out} H_C

$$

First, we calculate the mole fraction of the VOC in the outlet liquid stream using Assumption 1 ($n_{L,out} \approx 1.0$ mol).

$$

x_{C,out} = \frac{n_{C,out,L}}{n_{L,out}} \approx \frac{2.5 \times 10^{-5} \, \text{mol}}{1.0 \, \text{mol}} = 2.5 \times 10^{-5}

$$

Now, we can solve for the mole fraction of the VOC in the outlet vapor stream.

$$

y_{C,out} = \frac{x_{C,out} H_C}{P} = \frac{(2.5 \times 10^{-5})(2.5 \, \text{bar})}{5 \, \text{bar}} = 1.25 \times 10^{-5}

$$

This is the maximum mole fraction of the VOC that the air can contain at equilibrium with the outlet water.

**Step 5: Calculate the Required Air Flow Rate**

The moles of VOC in the outlet vapor can also be defined by its mole fraction and the total molar flow rate of the vapor stream.

$$

n_{C,out,V} = y_{C,out} \times n_{V,out}

$$

Using our calculated values and Assumption 2 ($n_{V,out} \approx n_{A,in}$), we can solve for the required inlet air flow rate, $n_{A,in}$.

$$

4.75 \times 10^{-4} \, \text{mol} = (1.25 \times 10^{-5}) \times n_{A,in}

$$

$$

n_{A,in} = \frac{4.75 \times 10^{-4}}{1.25 \times 10^{-5}} = 38 \, \text{mol}

$$

The result indicates that to achieve the desired stripping, we need **38 moles of air for every 1 mole of water**.

**Step 6: Evaluate the Simplifying Assumptions**

A rigorous solution would account for the water that evaporates into the air stream. We can check if this amount was truly negligible. The solvent (water) is nearly pure, so we can use Raoult's Law for it.

- **Water Saturation Pressure**: At 20$^\circ$C, the saturation pressure of water is $P_W^{sat} \approx 0.0234$ bar.
- **Water Mole Fraction in Outlet Liquid**: The outlet liquid is almost pure water, so $x_{W,out} \approx 1$.
- **Calculate Water Mole Fraction in Outlet Vapor**: Using Raoult's Law for the water component:

  $$

  y_{W,out} P = x_{W,out} P_W^{sat}

  $$

  $$

  y_{W,out} = \frac{(1.0)(0.0234 \, \text{bar})}{5 \, \text{bar}} \approx 0.0047

  $$

- **Calculate Moles of Evaporated Water**: The total moles of vapor leaving is the sum of the air, the stripped VOC, and the evaporated water ($n_{V,out} = n_A + n_{C,out,V} + n_{W,evap}$). The amount of VOC is tiny, so $n_{V,out} \approx n_A + n_{W,evap}$.

  $$

  n_{W,evap} = y_{W,out} \times n_{V,out} \approx y_{W,out} \times (n_A + n_{W,evap})

  $$

  Since $n_{W,evap}$ will be small compared to $n_A$, we can approximate $n_{V,out} \approx n_A = 38$ mol.

  $$

  n_{W,evap} \approx 0.0047 \times 38 = 0.178 \, \text{mol}

  $$

**Conclusion on Assumptions**:
- The amount of evaporated water (0.18 mol) is only about 0.5\% of the total air flow (38 mol). Thus, the assumption that $n_{V,out} \approx n_{A,in}$ was excellent.
- The amount of evaporated water is about 18\% of the liquid water feed (1 mol). This is more significant, but since our primary goal was to find the air-to-water ratio, and the air flow is by far the largest stream, the effect on the final answer is minor. A fully rigorous iterative solution would yield a nearly identical result of ~38 mol air/mol water. Our simplifying assumptions were justified.
```

## Phase Transitions: Clapeyron, Clausius-Clapeyron, and Antoine Equations

This guide covers the thermodynamic relationships that describe the equilibrium between different phases of a pure substance. We will derive the exact Clapeyron equation, explore its useful approximation (the Clausius-Clapeyron equation), and discuss the practical, empirical Antoine equation.

### The Clapeyron Equation

```{note}
The Clapeyron equation provides an exact thermodynamic relationship for the slope of a phase boundary line on a pressure-temperature (P-T) diagram (e.g., the boiling curve). It is derived from the fundamental condition that the molar Gibbs free energies of two phases must be equal for them to coexist in equilibrium.
```

```{important}
**Forms of the Clapeyron Equation**

The Clapeyron equation is general and applies to any phase transition. The pressure $P$ is the saturation pressure, $P^{sat}$, for transitions involving a vapor phase.

- **Vapor-Liquid Equilibrium (Vaporization)**
  
  $$

  \frac{dP^{sat}}{dT} = \frac{\Delta H^{vap}}{T(V^V - V^L)}

  $$

- **Vapor-Solid Equilibrium (Sublimation)**
  
  $$

  \frac{dP^{sat}}{dT} = \frac{\Delta H^{sub}}{T(V^V - V^S)}

  $$

- **Liquid-Solid Equilibrium (Fusion/Melting)**
  
  $$

  \frac{dP}{dT} = \frac{\Delta H^{fus}}{T(V^L - V^S)}

  $$

```

```{important}
**Derivation of the Clapeyron Equation**

The derivation proceeds in the following steps:
- Start with the fundamental relation for Gibbs free energy ($G$):
  
  $$

  dG = VdP - SdT

  $$

- State the condition for phase equilibrium between two phases (e.g., Liquid and Vapor):
  
  $$

  G^L = G^V

  $$

- If we move along the equilibrium line, the changes in Gibbs free energy for each phase must be equal to maintain equilibrium:
  
  $$

  dG^L = dG^V

  $$

- Substitute the fundamental relation into the equality:
  
  $$

  V^L dP - S^L dT = V^V dP - S^V dT

  $$

- Rearrange the terms to solve for the slope of the phase boundary, $\frac{dP}{dT}$:
  
  $$

  (S^V - S^L) dT = (V^V - V^L) dP

  $$
  
  $$

  \frac{dP}{dT} = \frac{S^V - S^L}{V^V - V^L} = \frac{\Delta S_{vap}}{\Delta V_{vap}}

  $$

- At equilibrium, the Gibbs free energy of vaporization is zero ($\Delta G_{vap} = 0$). From the definition $\Delta G = \Delta H - T\Delta S$, we find that the entropy of vaporization is $\Delta S_{vap} = \frac{\Delta H_{vap}}{T}$.
- Substitute this into the slope equation to arrive at the final form of the Clapeyron equation:
  
  $$

  \frac{dP}{dT} = \frac{\Delta H_{vap}}{T \Delta V_{vap}}

  $$

```

### The Clausius-Clapeyron Equation

```{note}
The Clausius-Clapeyron equation is a simplified, approximate form of the Clapeyron equation that is valid for vapor-liquid and vapor-solid equilibria under specific conditions. It is derived using two key assumptions:
- The molar volume of the condensed phase (liquid or solid) is negligible compared to the molar volume of the vapor phase ($V^V \gg V^L$ or $V^V \gg V^S$). Therefore, $\Delta V \approx V^V$.
- The vapor phase behaves as an ideal gas, allowing the use of the ideal gas law: $V^V = \frac{RT}{P^{sat}}$.
```

```{important}
**Derivation and Forms of the Clausius-Clapeyron Equation**

- Substitute the assumptions into the Clapeyron equation for vaporization:
  
  $$

  \frac{dP^{sat}}{dT} = \frac{\Delta H^{vap}}{T(V^V)} \approx \frac{\Delta H^{vap}}{T(RT/P^{sat})} = \frac{P^{sat}\Delta H^{vap}}{RT^2}

  $$

- Rearrange to a common differential form:
  
  $$

  \frac{1}{P^{sat}}\frac{dP^{sat}}{dT} = \frac{\Delta H^{vap}}{RT^2} \implies \frac{d(\ln P^{sat})}{dT} = \frac{\Delta H^{vap}}{RT^2}

  $$

- A second useful differential form shows that a plot of $\ln(P^{sat})$ versus $1/T$ is a straight line with a slope of $-\frac{\Delta H^{vap}}{R}$:
  
  $$

  d(\ln P^{sat}) = -\frac{\Delta H^{vap}}{R} d\left(\frac{1}{T}\right)

  $$

```

```{note}
To integrate the Clausius-Clapeyron equation, a third assumption is required:
- The heat of vaporization, $\Delta H^{vap}$, is constant over the temperature range of integration.
```

```{important}
**Integrated Clausius-Clapeyron Equation**

Integrating the differential form between two states $(T_1, P^{sat}_1)$ and $(T_2, P^{sat}_2)$ yields:

$$

\ln\left(\frac{P^{sat}_2}{P^{sat}_1}\right) = -\frac{\Delta H^{vap}}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right)

$$

This equation is very useful for estimating vapor pressures or heats of vaporization from limited data.
```

### The Antoine Equation

```{note}
While the Clausius-Clapeyron equation is derived from theory, the Antoine equation is a practical, semi-empirical correlation that provides a more accurate fit for experimental vapor pressure data over a wider temperature range.
```

```{important}
**Antoine Equation**

$$

\log_{10} P^{sat} = A - \frac{B}{T + C}

$$

The constants $A, B,$ and $C$ are specific to each substance and depend on the units used for pressure ($P^{sat}$) and temperature ($T$).
```

### Example Problems

```{prf:example} Melting Point of Ice under Pressure
The molar heat of fusion of ice is 335 J/g. The densities of liquid water and ice at 0$^\circ$C are 1.00 g/cm$^3$ and 0.915 g/cm$^3$, respectively. Calculate the melting temperature of ice when the system pressure is 110 MPa.
```

```{dropdown} Solution Steps
**Step 1: Identify Strategy and Convert to Molar SI Units**

We must use the Clapeyron equation for liquid-solid equilibrium. It is an exact relation, which is necessary because the pressure change is large. First, we convert all given quantities to a consistent molar basis using the molecular weight of water (18.015 g/mol).

- **Molar Heat of Fusion ($\Delta H^{fus}$)**:
  
  $$

  \Delta H^{fus} = 335 \frac{\text{J}}{\text{g}} \times 18.015 \frac{\text{g}}{\text{mol}} = 6035 \frac{\text{J}}{\text{mol}}

  $$

- **Molar Volume of Liquid ($V^L$)**:
  
  $$

  \rho_L = 1.00 \frac{\text{g}}{\text{cm}^3} \times \frac{10^6 \text{ cm}^3}{1 \text{ m}^3} \times \frac{1 \text{ kg}}{1000 \text{ g}} = 1000 \frac{\text{kg}}{\text{m}^3}

  $$
  
  $$

  V^L = \frac{MW}{\rho_L} = \frac{18.015 \times 10^{-3} \text{ kg/mol}}{1000 \text{ kg/m}^3} = 1.8015 \times 10^{-5} \frac{\text{m}^3}{\text{mol}}

  $$

- **Molar Volume of Solid ($V^S$)**:
  
  $$

  \rho_S = 0.915 \frac{\text{g}}{\text{cm}^3} = 915 \frac{\text{kg}}{\text{m}^3}

  $$
  
  $$

  V^S = \frac{MW}{\rho_S} = \frac{18.015 \times 10^{-3} \text{ kg/mol}}{915 \text{ kg/m}^3} = 1.9688 \times 10^{-5} \frac{\text{m}^3}{\text{mol}}

  $$

**Step 2: Apply the Clapeyron Equation**

The governing equation for the solid-liquid boundary is:

$$

\frac{dP}{dT} = \frac{\Delta H^{fus}}{T(V^L - V^S)}

$$

The term $\frac{\Delta H^{fus}}{V^L - V^S}$ can be treated as approximately constant. Let's calculate its value.

$$

\Delta V^{fus} = V^L - V^S = (1.8015 - 1.9688) \times 10^{-5} = -1.673 \times 10^{-6} \frac{\text{m}^3}{\text{mol}}

$$

Note that for water, $\Delta V^{fus}$ is negative because ice is less dense than liquid water.

$$

\frac{\Delta H^{fus}}{\Delta V^{fus}} = \frac{6035 \text{ J/mol}}{-1.673 \times 10^{-6} \text{ m}^3/\text{mol}} = -3.607 \times 10^9 \frac{\text{J}}{\text{m}^3} = -3.607 \times 10^9 \text{ Pa}

$$

The differential equation simplifies to:

$$

\frac{dP}{dT} \approx \frac{-3.607 \times 10^9 \text{ Pa}}{T}

$$

**Step 3: Integrate the Equation**

We separate variables and integrate from a known reference point (State 1) to the desired final state (State 2).

- **State 1 (Normal Melting Point)**: $P_1 = 0.1013 \text{ MPa} = 1.013 \times 10^5 \text{ Pa}$, $T_1 = 273.15$ K
- **State 2**: $P_2 = 110 \text{ MPa} = 1.1 \times 10^8 \text{ Pa}$, $T_2 = ?$

$$

\int_{P_1}^{P_2} dP = (-3.607 \times 10^9 \text{ Pa}) \int_{T_1}^{T_2} \frac{dT}{T}

$$

$$

P_2 - P_1 = (-3.607 \times 10^9) \ln\left(\frac{T_2}{T_1}\right)

$$

$$

(1.1 \times 10^8 - 1.013 \times 10^5) = (-3.607 \times 10^9) \ln\left(\frac{T_2}{273.15}\right)

$$

$$

1.099 \times 10^8 = (-3.607 \times 10^9) \ln\left(\frac{T_2}{273.15}\right)

$$

$$

\ln\left(\frac{T_2}{273.15}\right) = \frac{1.099 \times 10^8}{-3.607 \times 10^9} = -0.03047

$$

$$

\frac{T_2}{273.15} = e^{-0.03047} = 0.96998

$$

$$

T_2 = 0.96998 \times 273.15 = 264.95 \text{ K}

$$

```

```{prf:example} Estimate $\Delta H_{vap}$ from the Antoine Equation
Given the Antoine equation for benzene, $\log_{10}P^{sat} = 6.90 - 1211/(220.8 + T)$, where $P^{sat}$ is in torr and $T$ is in $^\circ$C, estimate the heat of vaporization of benzene at 60$^\circ$C.
```

```{dropdown} Solution Steps
**Step 1: Identify Strategy**

The Clausius-Clapeyron equation relates the heat of vaporization to the slope of a $\ln(P^{sat})$ vs. $1/T$ plot: $\frac{d(\ln P^{sat})}{d(1/T)} = -\frac{\Delta H_{vap}}{R}$. We can use the given Antoine equation to approximate this derivative at 60$^\circ$C using a finite difference method. We will calculate $P^{sat}$ at two temperatures bracketing 60$^\circ$C (e.g., 55$^\circ$C and 65$^\circ$C) and use the slope between these two points.

**Step 2: Generate Data Points from Antoine Equation**

First, calculate $P^{sat}$ at $T_1 = 55^\circ$C and $T_2 = 65^\circ$C. Then convert all values to absolute units (K, ln(P)).

- **At T$_1$ = 55$^\circ$C (328.15 K)**:
  
  $$

  \log_{10} P^{sat}_{1} = 6.90 - \frac{1211}{220.8 + 55} = 2.509 \implies P^{sat}_{1} = 10^{2.509} = 322.8 \text{ torr}

  $$
  
  $$

  \ln(P^{sat}_{1}) = \ln(322.8) = 5.777

  $$
  
  $$

  1/T_1 = 1/328.15 = 0.0030474 \text{ K}^{-1}

  $$

- **At T$_2$ = 65$^\circ$C (338.15 K)**:
  
  $$

  \log_{10} P^{sat}_{2} = 6.90 - \frac{1211}{220.8 + 65} = 2.663 \implies P^{sat}_{2} = 10^{2.663} = 460.2 \text{ torr}

  $$
  
  $$

  \ln(P^{sat}_{2}) = \ln(460.2) = 6.132

  $$
  
  $$

  1/T_2 = 1/338.15 = 0.0029573 \text{ K}^{-1}

  $$

**Step 3: Calculate the Slope and $\Delta H_{vap}$**

Approximate the slope using the two-point finite difference formula:

$$

-\frac{\Delta H_{vap}}{R} \approx \frac{\Delta(\ln P^{sat})}{\Delta(1/T)} = \frac{\ln(P^{sat}_{2}) - \ln(P^{sat}_{1})}{1/T_{2} - 1/T_{1}}

$$

$$

-\frac{\Delta H_{vap}}{R} = \frac{6.132 - 5.777}{0.0029573 - 0.0030474} = \frac{0.355}{-0.0000901} = -3940 \text{ K}

$$

Now, solve for $\Delta H_{vap}$ using $R = 8.314$ J/(mol·K):

$$

\Delta H_{vap} = (3940 \text{ K}) \times R = 3940 \text{ K} \times 8.314 \frac{\text{J}}{\text{mol·K}} = 32755 \frac{\text{J}}{\text{mol}}

$$

```

## Vapor-Liquid Equilibrium: Non-Ideal Solutions

This guide addresses vapor-liquid equilibrium (VLE) in real mixtures where molecular interactions cause deviations from ideal behavior. We introduce the activity coefficient ($\gamma$) as a correction factor to Raoult's Law to accurately model these non-ideal liquid solutions.

```{note}
In non-ideal solutions, the intermolecular forces between unlike molecules (A-B) differ from those between like molecules (A-A and B-B). The liquid-phase activity coefficient, $\gamma_i$, quantifies this deviation for each component $i$.
- **Positive Deviation ($\gamma_i > 1$)**: Occurs when A-B attractions are weaker than A-A and B-B attractions (molecules "repel" each other). This leads to a higher-than-ideal total vapor pressure.
- **Negative Deviation ($\gamma_i < 1$)**: Occurs when A-B attractions are stronger than A-A and B-B attractions (molecules "prefer" to stay in the liquid). This leads to a lower-than-ideal total vapor pressure.
- **Ideal Solution ($\gamma_i = 1$)**: The system follows Raoult's Law.
```

### Modified Raoult's Law

```{note}
Modified Raoult's Law is the fundamental equation for VLE in non-ideal systems. It incorporates the activity coefficient to correct the liquid-phase contribution to the partial pressure of a component.
```

```{admonition} Term Definitions
:class: tip
The key variables for non-ideal VLE are:
- **$\gamma_i$**: The activity coefficient of component $i$ in the liquid phase (dimensionless).
- **$x_i, y_i$**: Mole fractions of component $i$ in the liquid and vapor phases.
- **$P, P_i^{sat}$**: Total system pressure and saturation pressure of pure component $i$.
```

```{important}
The mathematical statement of Modified Raoult's Law is:

$$

y_i P = x_i \gamma_i P_i^{sat}

$$

```

### Activity Coefficient Models

```{note}
Activity coefficients are functions of composition and sometimes temperature. They must be calculated using a thermodynamic model derived from expressions for the excess Gibbs free energy ($G^E$). These models use empirical parameters fit to experimental VLE data.
```

```{important}
**Common Activity Coefficient Models**

- **One-Parameter Margules Equation**: A simple symmetric model for binary systems. The parameter $A$ is constant.
  
  $$

  \ln \gamma_1 = A x_2^2 \quad \text{and} \quad \ln \gamma_2 = A x_1^2

  $$

- **Van Laar Equation**: A more flexible two-parameter model for binary systems. The parameters are $A_{12}$ and $A_{21}$.
  
  $$

  \ln \gamma_1 = A_{12} \left( \frac{A_{21} x_2}{A_{12} x_1 + A_{21} x_2} \right)^2

  $$
  
  $$

  \ln \gamma_2 = A_{21} \left( \frac{A_{12} x_1}{A_{12} x_1 + A_{21} x_2} \right)^2

  $$

```

### Non-Ideal VLE Calculation Equations

```{important}
**Bubble and Dew Point Equations for Non-Ideal Systems**

- **Bubble Pressure Equation (given $x_i$)**:
  
  $$

  P = \sum_i x_i \gamma_i P_i^{sat} = x_1 \gamma_1 P_1^{sat} + x_2 \gamma_2 P_2^{sat}

  $$

- **Dew Pressure Equation (given $y_i$)**:
  
  $$

  P = \frac{1}{\sum_i \frac{y_i}{\gamma_i P_i^{sat}}} = \frac{1}{\frac{y_1}{\gamma_1 P_1^{sat}} + \frac{y_2}{\gamma_2 P_2^{sat}}}

  $$

```

### Example Problems

```{prf:example} Bubble Pressure using the Margules Equation
A vapor-phase mixture containing 30 mol\% component 1 and 70 mol\% component 2 is compressed at a fixed temperature until it is completely liquefied. The saturation pressures are $P_1^{sat} = 0.82$ bar and $P_2^{sat} = 1.93$ bar. Experimental data shows that the bubble pressure of a 50:50 mixture of these components is 1.08 bar.

- a) Assuming the one-parameter Margules equation applies, estimate the pressure required to completely liquefy the 30:70 mixture.
- b) Would the required pressure be higher or lower if the components formed an ideal solution? Explain.
```

```{dropdown} Solution Steps
**Step 1: Find the Margules Parameter, A**

The pressure to completely liquefy a vapor is its **bubble pressure**. We are given one data point: for a liquid with $x_1=0.5$ and $x_2=0.5$, the bubble pressure is $P=1.08$ bar. We use this point to find the parameter $A$.

- Start with the bubble pressure equation:
  
  $$

  P = x_1 \gamma_1 P_1^{sat} + x_2 \gamma_2 P_2^{sat}

  $$

- Substitute the Margules expressions for $\gamma_1 = \exp(A x_2^2)$ and $\gamma_2 = \exp(A x_1^2)$:
  
  $$

  1.08 = (0.5) \exp(A (0.5)^2) (0.82) + (0.5) \exp(A (0.5)^2) (1.93)

  $$

- Since the composition is symmetric ($x_1=x_2=0.5$), the activity coefficients are equal: $\gamma_1 = \gamma_2 = \exp(0.25A)$. Factor this term out:
  
  $$

  1.08 = \exp(0.25A) [ (0.5)(0.82) + (0.5)(1.93) ]

  $$
  
  $$

  1.08 = \exp(0.25A) [ 0.41 + 0.965 ] = \exp(0.25A) [ 1.375 ]

  $$

- Solve for the exponential term:
  
  $$

  \exp(0.25A) = \frac{1.08}{1.375} = 0.78545

  $$

- Take the natural logarithm to solve for A:
  
  $$

  0.25A = \ln(0.78545) = -0.2415

  $$
  
  $$

  A = \frac{-0.2415}{0.25} = -0.966

  $$

**Step 2: Calculate the Bubble Pressure of the 30:70 Mixture**

Now we use the determined parameter $A=-0.966$ to find the bubble pressure for the target liquid composition: $x_1=0.30$ and $x_2=0.70$.

- First, calculate the activity coefficients at this new composition:
  
  $$

  \ln \gamma_1 = A x_2^2 = (-0.966) (0.70)^2 = -0.4733 \implies \gamma_1 = e^{-0.4733} = 0.623

  $$
  
  $$

  \ln \gamma_2 = A x_1^2 = (-0.966) (0.30)^2 = -0.0869 \implies \gamma_2 = e^{-0.0869} = 0.917

  $$

- Now, use these values in the bubble pressure equation:
  
  $$

  P = x_1 \gamma_1 P_1^{sat} + x_2 \gamma_2 P_2^{sat}

  $$
  
  $$

  P = (0.30)(0.623)(0.82) + (0.70)(0.917)(1.93)

  $$
  
  $$

  P = 0.1533 + 1.2372 = 1.3905 \, \text{bar}

  $$

The pressure required to completely liquefy the mixture is **1.39 bar**.

**Step 3: Comparison with Ideal Solution**

- **Analysis of Non-Ideality**: We found that the Margules parameter $A$ is negative. This means that for all compositions, $\ln \gamma_i$ will be negative, and therefore the activity coefficients $\gamma_i$ will be less than 1. This signifies a **negative deviation** from Raoult's Law.
- **Molecular Interpretation**: A negative deviation implies that the attractive forces between unlike molecules (1-2) are stronger than the average attractive forces between like molecules (1-1 and 2-2). This strong attraction holds molecules in the liquid phase more effectively, resulting in a lower total vapor pressure compared to an ideal solution at the same composition.
- **Conclusion**: Since the real solution exhibits a lower vapor pressure, it requires less external pressure to be fully condensed. Therefore, the required pressure for an ideal solution would be **higher** than for the real solution.
- **Verification Calculation**: For an ideal solution, $\gamma_1=\gamma_2=1$.
  
  $$

  P_{ideal} = x_1 P_1^{sat} + x_2 P_2^{sat} = (0.30)(0.82) + (0.70)(1.93) = 0.246 + 1.351 = 1.597 \, \text{bar}

  $$

As predicted, the ideal pressure (1.60 bar) is significantly higher than the real pressure (1.39 bar).
```

```{prf:example} Bubble Temperature using the Van Laar Equation
Calculate the bubble temperature and the equilibrium vapor composition for a binary system with a liquid mole fraction of $x_1 = 0.40$ at a total pressure of 70 kPa. The system is non-ideal and is described by the two-parameter Van Laar model with $A_{12}=1.2$ and $A_{21}=0.8$. The saturation pressures are given by the Antoine equations (T in $^\circ$C, P in kPa):

$$

\ln(P_1^{sat}) = 14.3 - \frac{2940}{T + 224} \quad \text{and} \quad \ln(P_2^{sat}) = 14.2 - \frac{2975}{T + 209}

$$

```

```{dropdown} Solution Steps
**Step 1: Identify the Strategy**

This is a bubble temperature calculation for a non-ideal system. We need to find the temperature $T$ and the vapor composition ($y_1, y_2$) that satisfy the VLE conditions simultaneously. This problem involves multiple non-linear equations and must be solved with a numerical tool (e.g., POLYMATH, Aspen Plus, MATLAB, or a Python script).

**Step 2: List the Unknowns and Governing Equations**

For a numerical solver, we must define all variables and the equations that constrain them. The knowns are $P=70$ kPa, $x_1=0.40$, $x_2=0.60$, $A_{12}=1.2$, and $A_{21}=0.8$.

- **Unknowns (7)**: $T, y_1, y_2, P_1^{sat}, P_2^{sat}, \gamma_1, \gamma_2$
- **Equations (7)**:
  1. $y_1 P = x_1 \gamma_1 P_1^{sat}$ *(Modified Raoult's Law, Comp 1)*
  2. $y_2 P = x_2 \gamma_2 P_2^{sat}$ *(Modified Raoult's Law, Comp 2)*
  3. $P_1^{sat} = \exp(14.3 - 2940 / (T + 224))$ *(Antoine Equation, Comp 1)*
  4. $P_2^{sat} = \exp(14.2 - 2975 / (T + 209))$ *(Antoine Equation, Comp 2)*
  5. $\ln \gamma_1 = A_{12} \left( \frac{A_{21} x_2}{A_{12} x_1 + A_{21} x_2} \right)^2$ *(Van Laar Equation, Comp 1)*
  6. $\ln \gamma_2 = A_{21} \left( \frac{A_{12} x_1}{A_{12} x_1 + A_{21} x_2} \right)^2$ *(Van Laar Equation, Comp 2)*
  7. $y_1 + y_2 = 1$ *(Summation Constraint)*

**Step 3: Solver Results and Interpretation**

Inputting this system of equations into a numerical solver provides the solution.
- **Bubble Temperature**: $T \approx 84.1^\circ\text{C}$
- **Vapor Composition**: $y_1 \approx 0.69$, $y_2 \approx 0.31$
- **Activity Coefficients**: $\gamma_1 \approx 1.34$, $\gamma_2 \approx 1.15$
- **Saturation Pressures**: $P_1^{sat} \approx 89.9$ kPa, $P_2^{sat} \approx 47.9$ kPa
```

# Fugacity of Mixtures

This guide introduces fugacity, a thermodynamic property that represents the "escaping tendency" of a substance from a phase. It can be thought of as a corrected or effective pressure that accounts for non-ideal behavior. The most fundamental principle of phase and chemical equilibrium is based on this property.

```{note}
The condition for equilibrium in a multi-component, multi-phase system is that for any given component, its fugacity must be equal in all phases where it is present. This principle supersedes all other rules like Raoult's Law or Henry's Law, which are simply special cases of this universal criterion.
```

```{important}
For a system with phases A, B, C, ..., the equilibrium criterion for component $i$ is:

$$

\hat{f}_i^A = \hat{f}_i^B = \hat{f}_i^C \dots

$$

The hat symbol, $\hat{f}$, denotes the fugacity of a component within a mixture. Matter spontaneously moves from a region of higher fugacity to a region of lower fugacity until equilibrium (equal fugacity) is reached.
```

## Calculating Fugacity in a Liquid Mixture

```{note}
The method for calculating the fugacity of a component in a liquid mixture depends on the ideality of the solution and the system pressure. The equations build upon each other, adding correction factors for increasing complexity.
```

```{admonition} Term Definitions
:class: tip
The key variables for calculating liquid-phase fugacity are:
- **$\hat{f}_i$**: Fugacity of component $i$ in the liquid mixture [Pressure].
- **$x_i$**: Mole fraction of component $i$ in the liquid.
- **$\gamma_i$**: Activity coefficient of component $i$ (accounts for liquid-phase non-ideality).
- **$P_i^{sat}$**: Saturation (vapor) pressure of pure component $i$ at the system temperature.
- **$\phi_i^{sat}$**: Fugacity coefficient of pure saturated $i$ (accounts for vapor-phase non-ideality at $P_i^{sat}$).
- **$V_i^L$**: Molar volume of pure liquid component $i$.
- **$P$**: Total system pressure.
```

```{important}
**Fugacity Calculation Equations**

The following equations are used to calculate the fugacity of component $i$ in a liquid mixture. They are presented in order of increasing rigor.

- **Ideal Liquid Solution (Low Pressure)**: This is equivalent to Raoult's Law.
  
  $$

  \hat{f}_i = x_i P_i^{sat}

  $$

- **Non-Ideal Liquid Solution (Low Pressure)**: This is equivalent to Modified Raoult's Law.
  
  $$

  \hat{f}_i = x_i \gamma_i P_i^{sat}

  $$

- **Rigorous Equation (High Pressure)**: This form includes corrections for vapor-phase non-ideality and the effect of pressure on the liquid phase.
  
  $$

  \hat{f}_i = x_i \gamma_i \phi_i^{sat} P_i^{sat} \exp\left[\frac{V_i^L(P - P_i^{sat})}{RT}\right]

  $$
  
  The exponential term is known as the *Poynting correction factor*. It is typically close to 1 unless the pressure $P$ is very high.
```

## Conceptual Examples of Fugacity

```{prf:example} Fugacity in a Binary VLE System
A binary liquid mixture containing 70 mol\% component A and 30 mol\% component B is in equilibrium with its vapor. The partial pressures in the vapor phase are measured to be $P_A = 0.2$ bar and $P_B = 0.8$ bar. Which component has the higher fugacity in the liquid phase?
```

```{dropdown} Solution Steps
**Step 1: Apply the Fundamental Rule of Equilibrium**

The system is at equilibrium, which means the fugacity of each component must be the same in the liquid (L) and vapor (V) phases.

$$

\hat{f}_A^L = \hat{f}_A^V \quad \text{and} \quad \hat{f}_B^L = \hat{f}_B^V

$$

**Step 2: Calculate Fugacity in the Vapor Phase**

At the low pressures given (total P = 1.0 bar), the vapor phase can be assumed to behave as an ideal gas mixture. For an ideal gas, the fugacity of a component is equal to its partial pressure.

$$

\hat{f}_A^V \approx P_A = 0.2 \, \text{bar}

$$

$$

\hat{f}_B^V \approx P_B = 0.8 \, \text{bar}

$$

**Step 3: Determine Fugacity in the Liquid Phase and Conclude**

Because of the equilibrium condition, the fugacities in the liquid phase must be equal to those in the vapor phase.

$$

\hat{f}_A^L = 0.2 \, \text{bar}

$$

$$

\hat{f}_B^L = 0.8 \, \text{bar}

$$

**Conclusion**: Component B has the higher fugacity in the liquid ($\hat{f}_B^L > \hat{f}_A^L$), even though it is the minority component by mole fraction ($x_B < x_A$). This indicates component B is much more volatile than component A.
```

```{prf:example} Fugacity of Salt in Water
Sufficient NaCl is added to water at 25$^\circ$C so that a saturated solution is formed, with solid salt crystals present at the bottom. Does the water or the salt have a higher fugacity in the liquid solution?
```

```{dropdown} Solution Steps
**Step 1: Estimate the Fugacity of Water**

The fugacity of water in the salt solution, $\hat{f}_{H_2O}^L$, is equal to the fugacity of water in the vapor phase it's in equilibrium with. We can estimate this using Modified Raoult's Law. At 25$^\circ$C, $P_{H_2O}^{sat} \approx 0.0317$ bar.

$$

\hat{f}_{H_2O}^L \approx x_{H_2O} \gamma_{H_2O} P_{H_2O}^{sat}

$$

In a saturated salt solution, $x_{H_2O}$ is less than 1 but still high (e.g., $\sim$0.9). The activity coefficient will also be near 1. Therefore, the fugacity of water is on the order of 0.02-0.03 bar.

**Step 2: Estimate the Fugacity of Salt**

The system contains solid salt in equilibrium with the dissolved salt. Therefore, the fugacity of the dissolved salt must equal the fugacity of the solid salt. Salt (NaCl) is a non-volatile solid, meaning its tendency to enter the vapor phase is extremely low. Its vapor pressure at 25$^\circ$C is infinitesimally small. Thus, its fugacity is practically zero.

**Step 3: Conclusion**

The fugacity of water ($\sim$0.03 bar) is many orders of magnitude greater than the fugacity of the dissolved salt ($\sim$0 bar).
```

## Fugacity in Everyday Phenomena

```{note}
The principle that matter spontaneously moves from a state of higher fugacity to a state of lower fugacity is a powerful tool for explaining a wide range of physical and chemical processes.
```

```{admonition} Term Definitions
:class: tip
**Examples of Fugacity at Work**

- **Opening a Soda Can**: The high pressure in the can creates a very high fugacity for the dissolved CO$_{2}$. When opened, this fugacity is much higher than that of CO$_{2}$ in the atmosphere. To reach equilibrium, CO$_{2}$ rapidly escapes the liquid.
- **Saturated Sugar in Iced Tea**: When solid sugar is present, the system is at equilibrium. This means the fugacity of sugar in the solid crystals is equal to the fugacity of the sugar dissolved in the tea. If you add more tea (pure water), the sugar fugacity in the liquid drops, so more solid sugar dissolves to restore equilibrium.
- **Reverse Osmosis**: High mechanical pressure is applied to a salt water solution. This pressure greatly increases the fugacity of the water in that solution (via the Poynting correction). When the fugacity of water in the salt solution exceeds the fugacity of pure water on the other side of a membrane, water is forced to move "backwards" against the concentration gradient.
- **A Carrot in Salt Water**: A carrot contains mostly fresh water, which has a high fugacity. The salt in the surrounding water lowers the fugacity of the water in the solution. Because the fugacity of water inside the carrot is now higher than that outside, water spontaneously moves out of the carrot, causing it to shrivel.
- **Melting Ice with Salt**: At 0$^\circ$C, pure solid ice and pure liquid water are in equilibrium, so $f_{ice} = f_{liquid}$. When salt is added, it dissolves in the liquid water and lowers the fugacity of the water in that phase ($f_{new\_liquid} < f_{liquid}$). Now, the fugacity of the solid ice is higher than the fugacity of the saltwater ($f_{ice} > f_{new\_liquid}$). To restore equilibrium, the ice melts, moving from a state of high fugacity to low fugacity.
- **Gas Mask Filter**: A gas mask filter contains an adsorbent material like activated carbon. The fugacity of a contaminant molecule is much lower when it is adsorbed onto the carbon surface than when it is in the air. This large fugacity difference drives the harmful molecules from the air onto the filter, purifying the air that is breathed.
```

## Phase Diagrams for Partially-Miscible Liquids

This guide explores the behavior of liquid mixtures that exhibit partial miscibility, leading to the formation of two distinct liquid phases. This phenomenon, known as liquid-liquid equilibrium (LLE), occurs when positive deviations from Raoult's Law are large, indicating significant repulsive forces between unlike molecules.

```{note}
When the repulsive forces between unlike molecules (A-B) are much stronger than the attractive forces between like molecules (A-A and B-B), a single liquid phase becomes unstable over a certain composition range. The mixture spontaneously separates into two immiscible liquid phases, often denoted $\alpha$ and $\beta$, which are in equilibrium with each other.
- The $\alpha$ phase is rich in one component (e.g., A) and contains a small amount of the other.
- The $\beta$ phase is rich in the other component (e.g., B) and contains a small amount of the first.
```

### Key Equations for Multi-Phase Equilibrium

```{note}
The fundamental principles of phase equilibrium still apply to partially-miscible systems, but the equations must now account for the existence of multiple liquid phases in addition to a vapor phase.
```

```{admonition} Term Definitions
:class: tip
**Gibbs Phase Rule**
The Gibbs Phase Rule determines the number of independent intensive variables that can be changed while maintaining the number of phases at equilibrium.
- **$F$**: Degrees of freedom.
- **$C$**: Number of chemical components.
- **$P$**: Number of phases in equilibrium.
```

```{important}
For a non-reactive system, the Gibbs Phase Rule is:

$$

F = C - P + 2

$$

```

```{important}
**Equilibrium Condition for LLE**

For two liquid phases, $\alpha$ and $\beta$, to be in equilibrium, the fugacity of each component $i$ must be the same in both phases.

$$

\hat{f}_i^\alpha = \hat{f}_i^\beta

$$

Using the activity coefficient model for fugacity ($\hat{f}_i = x_i \gamma_i P_i^{sat}$), this becomes:

$$

x_i^\alpha \gamma_i^\alpha P_i^{sat} = x_i^\beta \gamma_i^\beta P_i^{sat}

$$

The saturation pressure, $P_i^{sat}$, cancels, leading to the fundamental LLE condition that the *activity* of each component must be equal in the two equilibrium liquid phases:

$$

x_i^\alpha \gamma_i^\alpha = x_i^\beta \gamma_i^\beta

$$

```

### Interpreting the Temperature-Composition (T-x-y) Diagram

```{note}
A T-x-y diagram for a binary, partially-miscible system at constant pressure shows the phase behavior as a function of temperature and overall composition. It features a vapor phase at high temperatures, single-phase liquid regions, a two-phase liquid-liquid region (the "miscibility gap"), and a unique horizontal line where three phases coexist.
```

```{admonition} Term Definitions
:class: tip
**Regions of the T-x-y Diagram**

- **Single-Phase Regions (V, L$_\alpha$, L$_\beta$)**: At high T, a single vapor phase (V) exists. At lower T and compositions rich in one component, a single liquid phase exists, either rich in component A (L$_\alpha$) or rich in component B (L$_\beta$).
- **Two-Phase Regions (V+L, L+L)**: Any overall composition falling within these regions will separate into two phases. The compositions of the equilibrium phases are given by the endpoints of a horizontal tie line passing through the point. The lever rule can be used to find the relative amounts of each phase.
- **Three-Phase Equilibrium Line (V+L$_\alpha$+L$_\beta$)**: This is a horizontal line at a specific temperature, $T_{3\phi}$.
    - **Degrees of Freedom**: For a binary system ($C=2$) with three phases ($P=3$) at a fixed external pressure, the Gibbs Phase Rule gives:
      
      $$

      F = C-P+2 = 2-3+2=1

      $$
      
      However, since the entire diagram is already constructed at a fixed pressure, this one degree of freedom is used. There are **zero** remaining degrees of freedom.
    - **Implication**: The three phases can only coexist at a **single, unique temperature** for that given pressure. As heat is added or removed at this temperature, the amounts of the phases change, but the temperature and compositions of all three phases remain constant until one phase is completely consumed.
```

### Example Problems

```{prf:example} Three-Phase Mass Balance
One mole of a liquid mixture containing 25 mol\% component A and 75 mol\% component B is heated at constant pressure. When 0.05 moles of vapor have formed, the system is found to be at the three-phase equilibrium temperature. At this temperature, the compositions of the coexisting phases are:
- Liquid $\alpha$ phase: $x_A = 0.73, x_B = 0.27$
- Liquid $\beta$ phase: $x_A = 0.17, x_B = 0.83$
- Vapor phase: $y_A = 0.40, y_B = 0.60$

Determine the number of moles of each phase present.
```

```{dropdown} Solution Steps
**Step 1: Identify the State of the System**

The problem states that vapor has begun to form from a liquid mixture and that the system is at the three-phase equilibrium temperature. This confirms that all three phases (Vapor, Liquid $\alpha$, Liquid $\beta$) must be present and coexisting in equilibrium.

**Step 2: List Phases, Compositions, and Amounts**

We can summarize the knowns and unknowns for the system. Let $V$, $L_\alpha$, and $L_\beta$ be the mole amounts of each phase.

- **Phase 1: Vapor (V)**
    - Amount: $V = 0.05$ mol (given)
    - Composition: $y_B = 0.60$
- **Phase 2: Liquid $\alpha$ (L$_\alpha$)**
    - Amount: $L_\alpha = ?$
    - Composition: $x_{B,\alpha} = 0.27$
- **Phase 3: Liquid $\beta$ (L$_\beta$)**
    - Amount: $L_\beta = ?$
    - Composition: $x_{B,\beta} = 0.83$

**Step 3: Set up and Solve Mole Balances**

We can solve for the two unknown amounts, $L_\alpha$ and $L_\beta$, by writing two independent mole balances.

- **Overall Mole Balance**: The sum of the moles of the three phases must equal the total moles in the system, which is 1.0 mol.
  
  $$

  V + L_\alpha + L_\beta = 1.0

  $$
  
  $$

  0.05 + L_\alpha + L_\beta = 1.0 \implies L_\alpha + L_\beta = 0.95

  $$

- **Component B Mole Balance**: The moles of component B distributed among the three phases must equal the total moles of B fed to the system (0.75 mol).
  
  $$

  y_B V + x_{B,\alpha} L_\alpha + x_{B,\beta} L_\beta = 0.75

  $$
  
  $$

  (0.60)(0.05) + (0.27) L_\alpha + (0.83) L_\beta = 0.75

  $$
  
  $$

  0.03 + 0.27 L_\alpha + 0.83 L_\beta = 0.75 \implies 0.27 L_\alpha + 0.83 L_\beta = 0.72

  $$

Now we solve the system of two linear equations:
a) $L_\alpha + L_\beta = 0.95$
b) $0.27 L_\alpha + 0.83 L_\beta = 0.72$

From equation (a), express $L_\alpha$ in terms of $L_\beta$: $L_\alpha = 0.95 - L_\beta$. Substitute this into equation (b):

$$

0.27(0.95 - L_\beta) + 0.83 L_\beta = 0.72

$$

$$

0.2565 - 0.27 L_\beta + 0.83 L_\beta = 0.72

$$

$$

0.56 L_\beta = 0.72 - 0.2565 = 0.4635

$$

$$

L_\beta = \frac{0.4635}{0.56} \approx 0.828 \, \text{mol}

$$

Now solve for $L_\alpha$:

$$

L_\alpha = 0.95 - 0.828 = 0.122 \, \text{mol}

$$

**Step 4: Final Answer**

The system contains three phases with the following amounts and compositions:
- **Vapor**: 0.05 mol, with composition $y_B=0.60$.
- **Liquid $\alpha$**: 0.12 mol, with composition $x_B=0.27$.
- **Liquid $\beta$**: 0.83 mol, with composition $x_B=0.83$.
```

```{prf:example} Effect of Cooling from a Three-Phase State
A cyclohexane-water system is at equilibrium at 50$^\circ$C and a fixed pressure. The system contains three phases: a vapor phase, a water-rich liquid phase, and a cyclohexane-rich liquid phase. If the temperature is now decreased to 45$^\circ$C while keeping the pressure constant, what change will occur in the system?
```

```{dropdown} Solution Steps
**Step 1: Analyze the System using the Gibbs Phase Rule**

The Gibbs Phase Rule provides a rigorous way to understand the constraints on the system.
- **Components**: $C = 2$ (cyclohexane, water).
- **Initial Phases**: $P = 3$ (vapor, liquid $\alpha$, liquid $\beta$).
- **Initial Degrees of Freedom**: $F = C - P + 2 = 2 - 3 + 2 = 1$.
- **Constraint**: The problem states the pressure is held constant. This uses up the single available degree of freedom.
- **Interpretation**: This means that for the given pressure, the three phases can only coexist at a single, unique temperature (50$^\circ$C). It is thermodynamically impossible for the system to remain in a three-phase state if the temperature is changed.

**Step 2: Predict the Change**

To exist at the new temperature of 45$^\circ$C, the system must change in a way that increases its degrees of freedom. This requires a reduction in the number of phases. Since the temperature is being lowered (energy is being removed), the highest-energy phase is the most likely to disappear. In a vapor-liquid system, the vapor phase is the highest-energy phase.

**Step 3: Visualize on a Phase Diagram**

On a T-x-y diagram for this type of system, the three-phase equilibrium exists as a single horizontal line. The region directly below this line is the two-phase liquid-liquid region (L$_\alpha$ + L$_\beta$). Cooling the system from the three-phase line means moving vertically downward into this L+L region. This transition corresponds to the complete condensation of the vapor.

**Step 4: Conclusion**

Decreasing the temperature from the three-phase equilibrium point at constant pressure will cause the **vapor phase to condense entirely**. The system will transition from having three phases (V + L$_\alpha$ + L$_\beta$) to having only two phases (L$_\alpha$ + L$_\beta$).
```

## Phase Diagrams for Immiscible Liquids

This guide focuses on the vapor-liquid equilibrium (VLE) of immiscible liquids, such as oil and water. Immiscibility represents the extreme case of positive deviation from Raoult's Law, where repulsive forces between unlike molecules are so strong that the liquids do not mix. This leads to unique and simplified VLE behavior.

### Core Principles of Immiscible VLE

```{note}
When two immiscible liquids are mixed, they form separate, distinct liquid layers. Each pure liquid is unaware of the other's presence and behaves as if it were in the container alone. This has two major consequences for their phase equilibrium.
```

```{admonition} Term Definitions
:class: tip
**Key Principles**

- **Independent Vapor Pressures**: Each pure liquid in the mixture exerts its full saturation pressure ($P^{sat}$) at the given system temperature. The partial pressure of a component in the vapor phase is equal to its saturation pressure, as long as some of that component is present as a liquid.
    - If liquid A is present, its partial pressure is $P_A = P_A^{sat}$.
    - If liquid B is present, its partial pressure is $P_B = P_B^{sat}$.
- **Boiling Point of the Mixture**: The immiscible mixture will boil when the *sum* of the individual saturation pressures equals the total external pressure.
    - A significant consequence is that an immiscible mixture always boils at a temperature *lower* than the boiling point of either pure component. This is because the saturation pressures add together to reach the external pressure sooner. This principle is the basis for steam distillation.
- **Vapor Phase Composition**: At the boiling point, the composition of the vapor phase is fixed and determined by the ratio of the individual saturation pressures.
```

```{important}
**Governing Equations for Immiscible VLE**

When both immiscible liquids (A and B) are present and in equilibrium with a vapor phase:
- **Boiling Condition**:
  
  $$

  P_{total} = P_A^{sat}(T) + P_B^{sat}(T)

  $$

- **Vapor Phase Composition**:
  
  $$

  y_A = \frac{P_A}{P_{total}} = \frac{P_A^{sat}}{P_A^{sat} + P_B^{sat}}

  $$
  
  $$

  y_B = \frac{P_B}{P_{total}} = \frac{P_B^{sat}}{P_A^{sat} + P_B^{sat}}

  $$

```

### Example Problems

```{prf:example} Condensation of an Immiscible System
A gas mixture containing 75 mol\% component A and 25 mol\% component B is compressed isothermally. At a total pressure of 1.6 bar, liquid A begins to condense. As the pressure is increased further, liquid B begins to condense at a total pressure of 2.4 bar. What are the saturation pressures of pure A and pure B at this temperature?
```

```{dropdown} Solution Steps
**Step 1: Analyze the First Condensation Point (P = 1.6 bar)**

At this pressure, the first drop of liquid A forms at the dew point. The vapor phase composition remains $y_A=0.75, y_B=0.25$.

Calculate partial pressures using Dalton's Law:

$$

P_A = y_A P_{total} = 0.75 \times 1.6 \, \text{bar} = 1.2 \, \text{bar}

$$

$$

P_B = y_B P_{total} = 0.25 \times 1.6 \, \text{bar} = 0.4 \, \text{bar}

$$

Since liquid A is just beginning to condense, its partial pressure equals its saturation pressure:

$$

P_A = P_A^{sat} \implies P_A^{sat} = 1.2 \, \text{bar}

$$

**Step 2: Analyze the Second Condensation Point (P = 2.4 bar)**

At 2.4 bar, the system contains vapor and liquid A phases, and liquid B begins to condense. Since liquid A is present, the partial pressure of A remains fixed at its saturation pressure:

$$

P_A = P_A^{sat} = 1.2 \, \text{bar}

$$

Find the partial pressure of B by subtraction:

$$

P_B = P_{total} - P_A = 2.4 \, \text{bar} - 1.2 \, \text{bar} = 1.2 \, \text{bar}

$$

Since component B is just beginning to condense:

$$

P_B = P_B^{sat} \implies P_B^{sat} = 1.2 \, \text{bar}

$$

```

```{prf:example} Identifying Phases in an Immiscible System
A closed system contains 6 mol of component A and 4 mol of component B. The system is at equilibrium at 100$^\circ$C and a total pressure of 2.0 atm. A and B are completely immiscible in the liquid phase. Their saturation pressures at 100$^\circ$C are known to be $P_A^{sat} = 2.0$ atm and $P_B^{sat} = 0.5$ atm. Determine the phases present at equilibrium.
```

```{dropdown} Solution Steps
**Step 1: State the Strategy**

We must determine which combination of phases (Vapor, Liquid A, Liquid B) is thermodynamically consistent with the given total pressure and saturation pressures. We will test each plausible hypothesis.

**Step 2: Hypothesis 1: Two Liquids (A+B) and Vapor are Present**

- **Condition**: If both liquid A and liquid B were present, the total pressure of the system would be fixed at the sum of their saturation pressures.
- **Check**:
  
  $$

  P_{required} = P_A^{sat} + P_B^{sat} = 2.0 \, \text{atm} + 0.5 \, \text{atm} = 2.5 \, \text{atm}

  $$

- **Conclusion**: The actual system pressure is 2.0 atm. Since $P_{actual} \neq P_{required}$, it is impossible for both liquids to be present. This hypothesis is **incorrect**.

**Step 3: Hypothesis 2: Only Liquid A and Vapor are Present**

- **Condition**: If liquid A is present, its partial pressure in the vapor phase must be equal to its saturation pressure: $P_A = P_A^{sat} = 2.0$ atm.
- **Check**: If $P_A = 2.0$ atm, then for the total pressure to be 2.0 atm, the partial pressure of B would have to be zero:
  
  $$

  P_B = P_{total} - P_A = 2.0 \, \text{atm} - 2.0 \, \text{atm} = 0 \, \text{atm}

  $$

- **Conclusion**: This is impossible because we know the system contains 4 moles of component B. This hypothesis is **incorrect**.

**Step 4: Hypothesis 3: Only Vapor is Present**

- **Condition**: If the system is a single vapor phase, the partial pressures are determined by the overall mole fractions.
- **Check**: First, find the overall mole fractions.
  
  $$

  y_A = \frac{6}{6+4} = 0.6 \quad \text{and} \quad y_B = \frac{4}{6+4} = 0.4

  $$
  
  Next, calculate the corresponding partial pressures at $P_{total} = 2.0$ atm.
  
  $$

  P_A = y_A P_{total} = 0.6 \times 2.0 \, \text{atm} = 1.2 \, \text{atm}

  $$
  
  $$

  P_B = y_B P_{total} = 0.4 \times 2.0 \, \text{atm} = 0.8 \, \text{atm}

  $$
  
  Now, check for physical consistency. A component's partial pressure cannot exceed its saturation pressure. Here, the calculated $P_B$ (0.8 atm) is *greater than* its saturation pressure ($P_B^{sat} = 0.5$ atm).
- **Conclusion**: This is physically impossible. If the partial pressure of B reached 0.5 atm, it would begin to condense, preventing the partial pressure from rising further. Therefore, the system cannot be all vapor. This hypothesis is **incorrect**.

**Step 5: Hypothesis 4: Only Liquid B and Vapor are Present**

- **Condition**: This is the only remaining possibility. Let's test it. If liquid B is present, its partial pressure is fixed at its saturation pressure: $P_B = P_B^{sat} = 0.5$ atm.
- **Check**: The partial pressure of A would then be:
  
  $$

  P_A = P_{total} - P_B = 2.0 \, \text{atm} - 0.5 \, \text{atm} = 1.5 \, \text{atm}

  $$
  
  Is this state possible? Yes, because this partial pressure ($P_A = 1.5$ atm) is *less than* the saturation pressure of A ($P_A^{sat} = 2.0$ atm). Component A can exist as a vapor with this partial pressure without condensing.
- **Conclusion**: This state is thermodynamically consistent.

**Step 6: Final Answer**

The phases present at equilibrium are **liquid B coexisting with a vapor mixture** of A and B.
```

## Vapor-Liquid Equilibrium: Bubble Point Calculations

This guide covers bubble point calculations, a fundamental process in chemical engineering used to determine the conditions at which a liquid mixture of known composition begins to boil. This is essential for designing separation equipment like distillation columns and flash drums.

```{note}
A *bubble point* calculation determines the temperature (at a given pressure) or the pressure (at a given temperature) where the first infinitesimal bubble of vapor forms from a liquid mixture. The key principle is that at this point, the sum of the partial pressures exerted by the components in the liquid equals the total system pressure, and consequently, the mole fractions of the components in the first bubble of vapor must sum to one.
```

```{important}
**Governing Equations for Bubble Point Calculations**

The calculation is based on two fundamental principles for an ideal solution:
- **Raoult's Law**: Defines the composition of the vapor bubble in equilibrium with the liquid.
  
  $$

  y_i = \frac{x_i P_i^{sat}(T)}{P}

  $$

- **Summation Constraint**: The mole fractions in the vapor phase must sum to unity.
  
  $$

  \sum_{i} y_i = 1

  $$

Combining these gives the single governing equation that must be solved:

$$

\sum_{i} \frac{x_i P_i^{sat}(T)}{P} = 1

$$

Since the saturation pressure, $P_i^{sat}$, is a strong, non-linear function of temperature $T$ (often given by the Antoine equation), finding a bubble temperature requires an iterative solution method.
```

```{dropdown} Solution Steps
**Strategy for Iterative Bubble Temperature Calculation**

A numerical solver, such as Excel's Solver tool, is an efficient way to perform a bubble temperature calculation. The procedure is as follows:

**Step 1: Setup Spreadsheet**: Designate cells for the known variables: liquid mole fractions ($x_1, x_2, \dots$) and the total system pressure ($P$). Create another cell for the temperature, $T$, and enter an initial guess.

**Step 2: Enter Formulas**:
- In separate cells, calculate the saturation pressure, $P_i^{sat}$, for each component using its Antoine equation, referencing the cell with the guessed temperature $T$.
- In other cells, calculate the vapor mole fraction, $y_i$, for each component using Raoult's Law: $y_i = (x_i \times P_i^{sat}) / P$.

**Step 3: Define Target Cell**: Create a cell that calculates the sum of the vapor mole fractions, $\sum y_i$. This cell's value will be used to check for convergence.

**Step 4: Configure Solver Tool**:
- **Set Objective**: The target cell containing $\sum y_i$.
- **To**: A value of **1**.
- **By Changing Variable Cells**: The cell containing the temperature guess, $T$.

**Step 5: Run Solver**: The solver will iteratively adjust the temperature until it finds the value where the sum of the vapor mole fractions is exactly 1. For a specific system, this might yield a result like **$84.4^\circ$C**, which would be the bubble point temperature.
```

## Flash Separations

Flash separation, also known as flash distillation, is a single-stage separation process widely used in the chemical industry. It is designed to separate components in a liquid mixture based on differences in their volatilities.

```{note}
The process involves three main steps:
1. A pressurized liquid feed stream is heated.
2. The stream is passed through a throttling device (like a valve) into a vessel at a lower pressure.
3. The sudden pressure drop causes a fraction of the liquid to rapidly vaporize, or "flash". The resulting vapor and liquid phases are allowed to reach equilibrium inside the vessel (the "flash drum") and are then drawn off as separate product streams.

The vapor product is enriched in the more volatile components, while the liquid product is enriched in the less volatile components.
```

### Governing Equations for Flash Separations

The analysis of a flash separation requires the simultaneous application of material balances, phase equilibrium relationships, and, for adiabatic cases, an energy balance.

```{admonition} Term Definitions
:class: tip
**Key Variables**
- **$F, V, L$**: Total molar flow rates of the Feed, Vapor product, and Liquid product.
- **$z_i, y_i, x_i$**: Mole fractions of component $i$ in the Feed, Vapor, and Liquid streams.
- **$K_i$**: The vapor-liquid equilibrium ratio (K-factor) for component $i$.
- **$H_F, H_V, H_L$**: Molar enthalpies of the Feed, Vapor, and Liquid streams.
```

```{important}
**Material Balance Equations**

- **Overall Material Balance**:
  
  $$

  F = V + L

  $$

- **Component Material Balance** (for each component $i$):
  
  $$

  z_i F = y_i V + x_i L

  $$

```

```{important}
**Phase Equilibrium Equations**

- **K-factor Definition**: The K-factor relates the equilibrium compositions of the vapor and liquid phases.
  
  $$

  K_i = \frac{y_i}{x_i}

  $$

- **K-factor for Ideal Systems**: For systems that follow Raoult's Law, the K-factor is a function of saturation pressure ($P_i^{sat}$) and total system pressure ($P$).
  
  $$

  K_i = \frac{P_i^{sat}}{P}

  $$

```

```{important}
**The Rachford-Rice Flash Equation**

By combining the material balance and equilibrium equations, a single powerful equation can be derived to solve for the fraction of the feed that is vaporized ($V/F$).

- The liquid and vapor mole fractions can be expressed in terms of the feed composition and K-factors:
  
  $$

  x_i = \frac{z_i}{1 + \frac{V}{F}(K_i - 1)} \quad \text{and} \quad y_i = \frac{z_i K_i}{1 + \frac{V}{F}(K_i - 1)}

  $$

- Since $\sum y_i - \sum x_i = 0$, we can subtract the expressions to get the Rachford-Rice equation, which is typically solved numerically for the term $V/F$:
  
  $$

  \sum_{i} \frac{z_i (K_i - 1)}{1 + \frac{V}{F}(K_i - 1)} = 0

  $$

```

```{important}
**Adiabatic Energy Balance**

For an adiabatic flash process (no external heat exchange), the enthalpy is conserved:

$$

F H_F = V H_V + L H_L

$$

```

### Example Problems

```{prf:example} Flash with Known Vaporized Fraction
A 50/50 molar liquid mixture of benzene(1) and toluene(2) is flashed to a drum operating at 1.4 bar. At the resulting equilibrium temperature, it is known that 25\% of the feed vaporizes. The saturation pressure of benzene at this temperature is $P_1^{sat} = 2.0$ bar. Assuming an ideal solution, what is the composition of the vapor leaving the drum?
```

```{dropdown} Solution Steps
**Step 1: Identify Knowns and Goal**

Feed composition: $z_1 = 0.50$ (benzene), $z_2 = 0.50$ (toluene).
Drum pressure: $P = 1.4$ bar. Saturation pressure: $P_1^{sat} = 2.0$ bar. Vaporized fraction: $V/F = 0.25$.
Goal: Find the vapor composition, $y_1$.

**Step 2: Calculate the K-factor for Benzene ($K_1$)**

For an ideal solution, the K-factor is the ratio of the saturation pressure to the total pressure.

$$

K_1 = \frac{P_1^{sat}}{P} = \frac{2.0 \, \text{bar}}{1.4 \, \text{bar}} \approx 1.4286

$$

**Step 3: Calculate the Liquid Mole Fraction of Benzene ($x_1$)**

Use the rearranged form of the flash equation:

$$

x_1 = \frac{z_1}{1 + \frac{V}{F}(K_1 - 1)}

$$

$$

x_1 = \frac{0.50}{1 + 0.25(1.4286 - 1)} = \frac{0.50}{1 + 0.25(0.4286)} = \frac{0.50}{1.10715} \approx 0.4516

$$

**Step 4: Calculate the Vapor Mole Fraction of Benzene ($y_1$)**

Use the K-factor definition ($K_1 = y_1/x_1$):

$$

y_1 = K_1 \times x_1 = 1.4286 \times 0.4516 \approx 0.6451

$$

**Step 5: Final Answer**

The vapor composition is approximately **64.5\% benzene** ($y_1 = 0.645$) and 35.5\% toluene.
```

```{prf:example} Isothermal Flash Calculation
A liquid feed containing 60 mol\% component 1 and 40 mol\% component 2 is flashed to an outlet condition of 150$^\circ$C and 1210 kPa. The system behaves as an ideal solution. The saturation pressures (in kPa) are given by the Antoine equations, where T is in $^\circ$C:

$$

\ln(P_1^{sat}) = 15 - \frac{3010}{T + 250} \quad \text{and} \quad \ln(P_2^{sat}) = 14 - \frac{2700}{T + 205}

$$

Calculate the fraction of the feed that leaves as liquid ($L/F$) and the compositions of the equilibrium liquid ($x_1$) and vapor ($y_1$) phases.
```

```{dropdown} Solution Steps
**Step 1: Strategy: Isothermal Flash**

In an isothermal flash, the temperature and pressure in the drum are known. This means the K-factors are fixed. The first step is to determine the compositions of the liquid and vapor phases that can coexist at these conditions. Then, a material balance is used to find the relative amounts of the two phases.

**Step 2: Calculate Saturation Pressures and K-factors at 150$^\circ$C**

Substitute $T=150^\circ$C into the given Antoine equations.

$$

\ln(P_1^{sat}) = 15 - \frac{3010}{150 + 250} = 15 - 7.525 = 7.475 \implies P_1^{sat} = e^{7.475} \approx 1763.4 \, \text{kPa}

$$

$$

\ln(P_2^{sat}) = 14 - \frac{2700}{150 + 205} = 14 - 7.606 = 6.394 \implies P_2^{sat} = e^{6.394} \approx 598.2 \, \text{kPa}

$$

Now, calculate the K-factors at the drum pressure $P = 1210$ kPa.

$$

K_1 = \frac{P_1^{sat}}{P} = \frac{1763.4}{1210} \approx 1.457

$$

$$

K_2 = \frac{P_2^{sat}}{P} = \frac{598.2}{1210} \approx 0.494

$$

**Step 3: Solve the Rachford-Rice Equation (Iteratively)**

We must now find the value of $V/F$ that solves the Rachford-Rice equation.

$$

f(V/F) = \sum_{i} \frac{z_i (K_i - 1)}{1 + \frac{V}{F}(K_i - 1)} = \frac{0.6(1.457-1)}{1+\frac{V}{F}(1.457-1)} + \frac{0.4(0.494-1)}{1+\frac{V}{F}(0.494-1)} = 0

$$

$$

\frac{0.2742}{1+0.457(V/F)} + \frac{-0.2024}{1-0.506(V/F)} = 0

$$

Solving this non-linear equation for $V/F$ using a numerical solver (e.g., Excel Solver, Python's `fsolve`) yields:

$$

\frac{V}{F} \approx 0.3125

$$

**Step 4: Determine the Liquid Fraction ($L/F$)**

The liquid fraction is simply one minus the vapor fraction.

$$

\frac{L}{F} = 1 - \frac{V}{F} = 1 - 0.3125 = 0.6875

$$

**Step 5: Determine the Liquid and Vapor Compositions**

Now that we know $V/F$, we can use the composition formulas from the Rachford-Rice derivation.
- **Liquid Composition ($x_i$)**:
  
  $$

  x_1 = \frac{z_1}{1 + \frac{V}{F}(K_1 - 1)} = \frac{0.6}{1 + 0.3125(1.457 - 1)} = \frac{0.6}{1.1428} \approx 0.525

  $$
  
  $$

  x_2 = 1 - x_1 = 1 - 0.525 = 0.475

  $$

- **Vapor Composition ($y_i$)**:
  
  $$

  y_1 = K_1 x_1 = 1.457 \times 0.525 \approx 0.765

  $$
  
  $$

  y_2 = K_2 x_2 = 0.494 \times 0.475 \approx 0.235

  $$
  
  (As a check, the vapor mole fractions sum to $0.765 + 0.235 = 1.0$).

**Step 6: Final Answer**

The results of the isothermal flash calculation are:
- The fraction of the effluent that is liquid is **68.8\%** ($L/F = 0.688$).
- **Liquid Phase Composition**: 52.5\% component 1 ($x_1 = 0.525$).
- **Vapor Phase Composition**: 76.5\% component 1 ($y_1 = 0.765$).
```

## Solid-Liquid Equilibrium: Solubility

This section focuses on the equilibrium between a solid solute and a liquid solvent, which is governed by the solute's solubility. This is the basis for designing crystallization and dissolution processes.

```{note}
Solubility describes the maximum amount of a solute that can dissolve in a solvent at a given temperature to form a stable solution.
- **Saturated Solution**: A solution in equilibrium with undissolved solid solute. It contains the maximum possible amount of dissolved solute at that temperature.
- **Supersaturated Solution**: An unstable state where the solution contains more dissolved solute than its equilibrium solubility. Given time or a seed crystal, the excess solute will precipitate.
- **Kinetics vs. Equilibrium**: Solubility diagrams describe the final equilibrium state, not the rate (kinetics) at which dissolution or crystallization occurs.
```

### Using Solubility Diagrams for Material Balances

```{note}
Solubility diagrams, which plot solubility versus temperature, are essential tools for performing material balances on crystallizer systems. It is critical to interpret the units of solubility correctly.
```

```{important}
**Converting Solubility to Mass Fraction**

Solubility is often reported as a mass ratio. To use it in a mass balance, it must be converted to a mass fraction of the solute in the saturated solution.

- **Common Unit**: Solubility = $\frac{\text{grams of solute}}{100 \text{ grams of solvent}}$
- **Conversion Formula**:
  
  $$

  \text{Mass Fraction }(x) = \frac{\text{mass of solute}}{\text{mass of solute} + \text{mass of solvent}}

  $$

For example, if the solubility of NaCl is 40 g NaCl / 100 g H$_2$O, the mass fraction is:

$$

x_{NaCl} = \frac{40}{40 + 100} = \frac{40}{140} \approx 0.286

$$

```

```{prf:example} Crystallizer Material Balance
A saturated aqueous solution of potassium dichromate (K$_2$Cr$_2$O$_7$) at 60$^\circ$C is fed to a crystallizer that operates at 20$^\circ$C. The outlet slurry is filtered, yielding 200 kg of solid K$_2$Cr$_2$O$_7$ crystals and 400 kg of saturated solution at 20$^\circ$C. How much water was evaporated in the crystallizer?
```

```{dropdown} Solution Steps
**Step 1: Find Compositions from Solubility Data**

We use a standard solubility chart for K$_2$Cr$_2$O$_7$ to find the compositions of the inlet and outlet solutions.
- **Inlet (60$^\circ$C)**: Solubility $\approx$ 38 g K$_2$Cr$_2$O$_7$ / 100 g H$_2$O.
  
  $$

  x_{in} = \frac{38}{38+100} = \frac{38}{138} = 0.2754

  $$

- **Outlet Solution (20$^\circ$C)**: Solubility $\approx$ 12 g K$_2$Cr$_2$O$_7$ / 100 g H$_2$O.
  
  $$

  x_{out,sol} = \frac{12}{12+100} = \frac{12}{112} = 0.1071

  $$

**Step 2: Draw and Label a Process Flow Diagram**

- **Inlet**: One stream, the feed ($m_{feed}$), with a K$_2$Cr$_2$O$_7$ mass fraction of $x_{in}=0.2754$.
- **Outlets**: Three streams.
    a) Evaporated pure water ($m_{evap}$).
    b) Solid crystals ($m_{crys} = 200$ kg), which are pure K$_2$Cr$_2$O$_7$ (mass fraction = 1).
    c) Saturated solution ($m_{sol} = 400$ kg) with a K$_2$Cr$_2$O$_7$ mass fraction of $x_{out,sol}=0.1071$.

**Step 3: Set up Material Balances**

We have two unknown flow rates ($m_{feed}$ and $m_{evap}$), so we need to set up two independent balance equations.

- **Overall Mass Balance** (Mass In = Mass Out):
  
  $$

  m_{feed} = m_{evap} + m_{crys} + m_{sol}

  $$
  
  $$

  m_{feed} = m_{evap} + 200 + 400 \implies m_{feed} = m_{evap} + 600

  $$

- **Water Balance** (Water In = Water Out):
  
  $$

  (\text{Water in feed}) = (\text{Water evaporated}) + (\text{Water in solution})

  $$
  
  $$

  m_{feed} \times (1 - x_{in}) = m_{evap} + m_{sol} \times (1 - x_{out,sol})

  $$
  
  $$

  m_{feed} \times (1 - 0.2754) = m_{evap} + 400 \times (1 - 0.1071)

  $$
  
  $$

  0.7246 \cdot m_{feed} = m_{evap} + (400 \times 0.8929)

  $$
  
  $$

  0.7246 \cdot m_{feed} = m_{evap} + 357.16

  $$

**Step 4: Solve the System of Equations**

Substitute the expression for $m_{feed}$ from the overall balance into the water balance.

$$

0.7246 (m_{evap} + 600) = m_{evap} + 357.16

$$

$$

0.7246 \cdot m_{evap} + 434.76 = m_{evap} + 357.16

$$

Rearrange to solve for $m_{evap}$:

$$

434.76 - 357.16 = m_{evap} - 0.7246 \cdot m_{evap}

$$

$$

77.6 = 0.2754 \cdot m_{evap}

$$

$$

m_{evap} = \frac{77.6}{0.2754} \approx 281.8 \, \text{kg}

$$

**Step 5: Final Answer**

Approximately **282 kg** of water must be evaporated in the crystallizer.
```

---

## PE Exam Practice Problems

```{prf:example} Practice Problem 1 — Bubble Point Calculation (Raoult's Law)

A liquid mixture of 30 mol% benzene (1) and 70 mol% toluene (2) is at 1 atm total pressure. Use Raoult's Law to find the bubble point temperature and vapor composition.

Antoine constants ($\log_{10} P^{sat}$ in mmHg, $T$ in °C):
- Benzene: $A = 6.905$, $B = 1211$, $C = 220.8$
- Toluene: $A = 6.953$, $B = 1344$, $C = 219.5$

$P_{total} = 760$ mmHg.
```

```{dropdown} Solution

**Step 1: Bubble point condition**

At bubble point, the first vapor bubble forms. The condition is:

$$\sum x_i K_i = 1 \quad \text{where} \quad K_i = P_i^{sat}(T)/P$$

**Step 2: Iterate on temperature**

Try $T = 95°C$:

$$P_1^{sat} = 10^{6.905 - 1211/(95+220.8)} = 10^{6.905 - 3.835} = 10^{3.070} = 1175 \text{ mmHg}$$

$$P_2^{sat} = 10^{6.953 - 1344/(95+219.5)} = 10^{6.953 - 4.275} = 10^{2.678} = 476 \text{ mmHg}$$

$$\sum x_i P_i^{sat}/P = (0.30 \times 1175 + 0.70 \times 476)/760 = (352.5 + 333.2)/760 = 685.7/760 = 0.902 < 1$$

Temperature too low. Try $T = 100°C$:

$$P_1^{sat} = 10^{6.905 - 1211/320.8} = 10^{3.130} = 1349 \text{ mmHg}$$

$$P_2^{sat} = 10^{6.953 - 1344/319.5} = 10^{2.742} = 552 \text{ mmHg}$$

$$\sum x_i K_i = (0.30 \times 1349 + 0.70 \times 552)/760 = (404.7 + 386.4)/760 = 1.041 > 1$$

Interpolating: $T_{bubble} \approx 95 + 5 \times (1 - 0.902)/(1.041 - 0.902) \approx 95 + 3.5 = \mathbf{98.5°C}$

**Step 3: Vapor composition at bubble point** (use $T \approx 98.5°C$, $K_i = P_i^{sat}/P$)

$$y_1 = x_1 K_1 = 0.30 \times (1349/760) \approx 0.532 \quad y_2 = 0.468$$
```

---

```{prf:example} Practice Problem 2 — Chemical Equilibrium: $K$ and Conversion

The gas-phase reaction $\text{N}_2\text{O}_4(g) \rightleftharpoons 2\,\text{NO}_2(g)$ has $\Delta G^\circ_{298} = +4.7$ kJ/mol and $\Delta H^\circ_{rxn} = +57.2$ kJ/mol.

**(a)** What is $K_a$ at 298 K?

**(b)** Is equilibrium conversion higher or lower at 400 K? Calculate $K_a$ at 400 K.

**(c)** Does increasing total pressure favor products or reactants?
```

```{dropdown} Solution

**Part (a): $K_a$ at 298 K**

$$K_a = \exp\!\left(-\frac{\Delta G^\circ}{RT}\right) = \exp\!\left(-\frac{4700}{8.314 \times 298}\right) = \exp(-1.897) = \mathbf{0.150}$$

$K_a < 1$ means reactants are favored at 298 K.

**Part (b): $K_a$ at 400 K (Van't Hoff)**

$$\ln\frac{K_2}{K_1} = \frac{\Delta H^\circ}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right) = \frac{57200}{8.314}\left(\frac{1}{298} - \frac{1}{400}\right)$$

$$= 6880 \times (3.356\times10^{-3} - 2.500\times10^{-3}) = 6880 \times 8.56\times10^{-4} = 5.89$$

$$K_2 = 0.150 \times e^{5.89} = 0.150 \times 361.7 = \mathbf{54.3}$$

At 400 K, $K_a = 54.3 \gg 1$ — products (NO₂) are strongly favored. Higher temperature **increases** conversion for this endothermic reaction.

**Part (c): Pressure effect**

$\sum\nu_i = 2 - 1 = +1$ (reaction increases moles). Higher total pressure shifts equilibrium **toward reactants** (Le Châtelier's principle — the system compresses by favoring fewer moles). Increasing pressure **decreases** NO₂ yield.
```

```{caution}
**PE Exam Traps — Chemical and Phase Equilibria**

- **$K_a$ is dimensionless but $K_y$ is not.** The thermodynamic equilibrium constant $K_a = K_y \cdot P^{\sum\nu_i}$ (with $P$ in bar). If $\sum\nu_i \neq 0$, changing pressure changes $K_y$ even though $K_a$ is fixed by temperature alone. Forgetting the pressure factor in gas-phase equilibrium is extremely common.
- **Van't Hoff direction:** For exothermic reactions ($\Delta H^\circ < 0$), increasing $T$ decreases $K$. For endothermic ($\Delta H^\circ > 0$), increasing $T$ increases $K$. Le Châtelier's principle and Van't Hoff must be consistent — always check the sign of $\Delta H^\circ$ before stating whether higher $T$ helps or hurts yield.
- **Bubble vs. dew point:** At the **bubble point**, you know the liquid composition ($x_i$) and the condition $\sum x_i K_i = 1$. At the **dew point**, you know the vapor composition ($y_i$) and the condition $\sum y_i/K_i = 1$. Mixing these up inverts the problem entirely.
- **Raoult's Law requires ideal liquid AND ideal vapor.** If activity coefficients are given ($\gamma_i \neq 1$), use modified Raoult's: $y_i P = \gamma_i x_i P_i^{sat}$. Neglecting $\gamma_i$ when it's provided leads to wrong bubble/dew point temperatures.
- **Flash calculation: $\psi$ is the vapor fraction, not liquid fraction.** In the Rachford-Rice equation, $\psi = V/F$ varies between 0 (all liquid, bubble point) and 1 (all vapor, dew point). If your answer gives $\psi$ outside $[0,1]$, the feed is either entirely liquid or entirely vapor at those conditions — not a two-phase flash.
```

## Phase Behavior Near the Critical Point

```{note}
The critical point represents the terminus of the vapor-liquid equilibrium curve on a phase diagram. Beyond this point, the distinction between liquid and vapor phases ceases to exist, and the substance enters the supercritical fluid phase, which has unique properties combining those of liquids and gases.
```

```{admonition} Term Definitions
:class: tip
**Key Definitions**
- **Critical Point**: The specific temperature ($T_c$) and pressure ($P_c$) for a substance at which the liquid and vapor phases become identical and indistinguishable.
- **Supercritical Fluid**: A substance at a temperature and pressure above its critical point ($T > T_c$ and $P > P_c$). It has a density similar to a liquid but the viscosity and diffusivity of a gas.
```

```{note}
**Phenomena at the Critical Point**
The transition into and out of the supercritical state involves unique and observable phenomena.
- **Heating to the Critical Point**: Imagine a sealed container holding a liquid and its vapor, with the overall density being exactly the critical density. As the system is heated towards the critical temperature, the liquid expands (density decreases) and the vapor is compressed (density increases). The properties of the two phases converge. The meniscus—the visible boundary between the liquid and vapor—becomes progressively fainter and then vanishes completely at the critical point, as the system becomes one uniform, homogeneous supercritical fluid.
- **Cooling from the Supercritical State**: If a supercritical fluid is cooled back down through its critical point, it exhibits a phenomenon called **critical opalescence**. At the instant of passing through the critical point, large-scale density fluctuations form spontaneously throughout the fluid. These fluctuations have a size comparable to the wavelength of visible light, causing them to scatter light intensely. This makes the fluid, for a moment, appear milky, cloudy, or opaque. Immediately after this flash of opalescence, the fluid separates back into distinct liquid and vapor phases.
```