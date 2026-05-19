---
title: "Mass and Energy Balances"
author: "PE Study Guide"
date: "Process Fundamentals"
---

# Mass and Energy Balance

# Process Fundamentals Study Guide

## Introduction to Process Fundamentals

Welcome to your chemical engineering refresher for the Professional Engineering (PE) exam. This guide is designed to rebuild your knowledge from the ground up, starting with the most fundamental concepts. The core of chemical process analysis rests on the laws of conservation, primarily the conservation of mass and energy. We will begin by focusing on the material balance, the foundation upon which most other process calculations are built.

```{note}
A **system** is a specific region of space we are interested in (e.g., a reactor, a distillation column, a pipe). The boundary separating the system from its surroundings is called the **control volume**. The analysis of what crosses this boundary is the key to solving process problems.
```

---

## Quick Reference: Key Equations

| Formula | Equation | When to Use |
|---------|----------|-------------|
| General balance | $\text{Accum} = \dot{m}_{in} - \dot{m}_{out} + \text{Gen} - \text{Cons}$ | Any process |
| Steady-state overall | $\dot{m}_{in} = \dot{m}_{out}$ | No rxn, SS |
| Component balance | $F z_i = V y_i + L x_i$ | Separation units |
| Transient balance | $\frac{dM}{dt} = \dot{m}_{in} - \dot{m}_{out}$ | Filling/draining tanks |
| Extent of reaction | $\dot{n}_i = \dot{n}_{i,0} + \nu_i \xi$ | Reactive systems |
| % Excess air | $\frac{\dot{n}_{air,fed} - \dot{n}_{air,theo}}{\dot{n}_{air,theo}} \times 100\%$ | Combustion |
| Overall conversion | $X_{overall} = \frac{F_{A,0} - F_{A,f}}{F_{A,0}}$ | Recycle systems |
| Single-pass conversion | $X_{SP} = \frac{F_{A,m} - F_{A,out}}{F_{A,m}}$ | Reactor only |
| DoF | $\text{DoF} = \text{Unknowns} - \text{Indep. Equations}$ | Setup check |
| Energy balance (SS) | $\dot{Q} = \Delta\dot{H} = \dot{m}(\hat{h}_{out} - \hat{h}_{in})$ | Heat exchangers |
| Sensible heat | $\dot{Q}_s = \dot{m} c_p \Delta T$ | Temp change, no phase change |
| Latent heat | $\dot{Q}_L = \dot{n} \Delta H_{phase}$ | Phase change |
| Reactive energy balance | $\dot{Q} = \dot{\xi}\Delta\hat{H}_{rxn}^\circ + \sum_{out}\dot{n}_i\hat{h}_i - \sum_{in}\dot{n}_i\hat{h}_i$ | Reactors |
| $\Delta H^\circ_{rxn}$ | $\sum_{prod}|\nu_i|\Delta\hat{H}_{f,i}^\circ - \sum_{react}|\nu_i|\Delta\hat{H}_{f,i}^\circ$ | Standard state |

---

## Material Balances

The principle of mass conservation states that mass cannot be created or destroyed. When applied to a process system, this gives us the general material balance equation.

### The General Balance Equation

```{important}
**Conceptual Balance Equation:**

$$
\text{Accumulation} = \text{In} - \text{Out} + \text{Generation} - \text{Consumption}
$$
```

```{admonition} Term Definitions
:class: tip

- **Accumulation**: The change in the amount of the quantity within the system over time
- **In**: The rate at which the quantity enters the system through its boundaries
- **Out**: The rate at which the quantity leaves the system through its boundaries
- **Generation**: The rate at which the quantity is produced within the system (e.g., by chemical reaction)
- **Consumption**: The rate at which the quantity is consumed within the system (e.g., by chemical reaction)
```

```{note}
**Steady-State Systems**

A system is at **steady-state** if all process variables (temperature, pressure, flow rate, composition) are constant with respect to time. At steady-state, the **Accumulation** term is zero.
```

### Overall Steady-State Balance (No Reaction)

For a system at steady-state with no chemical reactions, the generation and consumption terms are also zero. The general balance equation simplifies dramatically.

```{note}
**Fundamental Principle**

**What goes in must come out.**
```

```{admonition} Variable Definitions
:class: tip

- $\dot{m}_{in}$: The total mass flow rate into the system per unit time (e.g., kg/s, lb/hr). The dot over the 'm' signifies a rate
- $\dot{m}_{out}$: The total mass flow rate out of the system per unit time (e.g., kg/s, lb/hr)
```

```{important}
**Overall Mass Balance**

$$
\dot{m}_{in} = \dot{m}_{out}
$$

This simple equation is the starting point for analyzing any non-reactive, steady-state process.
```

### Component Steady-State Balance (No Reaction)

While the overall balance is useful, we often need to track individual chemical species (components) through a system. This is especially true for separation processes like distillation, absorption, or flash separation.

```{note}
**Component Balance Principle**

The mass of a specific component entering the system must equal the mass of that same component leaving the system.
```

```{admonition} Standard Variable Definitions
:class: tip

- $F$: Total mass flow rate of the incoming **F**eed stream (kg/s)
- $V$: Total mass flow rate of the outgoing **V**apor stream (kg/s)
- $L$: Total mass flow rate of the outgoing **L**iquid stream (kg/s)
- $z_i$: The mass fraction of component $i$ in the feed stream
- $y_i$: The mass fraction of component $i$ in the vapor stream
- $x_i$: The mass fraction of component $i$ in the liquid stream
```

```{important}
**Component Balance Equation**

**Derivation:** Apply the "In = Out" principle to a single component, $i$:

$$
(\text{Mass of } i \text{ in}) = (\text{Mass of } i \text{ out})
$$

$$
F z_i = V y_i + L x_i
$$

This equation can be written for each component in the mixture.
```

```{prf:example} Flash Drum Separation

**Problem Statement:** A feed stream of 1000 kg/hr containing 40% ethanol and 60% water by mass enters a flash drum. The vapor stream leaving the top is found to contain 70% ethanol, and the liquid stream leaving the bottom contains 20% ethanol. The system is at steady-state. Calculate the mass flow rates of the vapor ($V$) and liquid ($L$) streams.
```

```{dropdown} Solution Steps

**Step 1: List Knowns and Define Basis**

Basis: 1 hour of operation

- Feed Flow ($F$) = 1000 kg/hr
- Feed ethanol fraction ($z_e$) = 0.40
- Vapor ethanol fraction ($y_e$) = 0.70
- Liquid ethanol fraction ($x_e$) = 0.20

**Step 2: Set up Material Balances**

Two unknowns ($V$ and $L$) require two equations:

**Overall Balance:** $F = V + L \Rightarrow 1000 = V + L$ (Eq. 1)

**Ethanol Balance:** $F z_e = V y_e + L x_e \Rightarrow 400 = 0.7V + 0.2L$ (Eq. 2)

**Step 3: Solve System of Equations**

From Eq. 1: $L = 1000 - V$. Substitute into Eq. 2:

$$
400 = 0.7V + 0.2(1000 - V) = 0.7V + 200 - 0.2V = 0.5V + 200
$$

$$
V = \frac{400-200}{0.5} = 400 \text{ kg/hr}
$$

$$
L = 1000 - 400 = 600 \text{ kg/hr}
$$

**Step 4: Verification**

**Water balance check:** $z_w=0.6$, $y_w=0.3$, $x_w=0.8$

In: $(1000)(0.6) = 600$ kg/hr

Out: $(400)(0.3) + (600)(0.8) = 600$ kg/hr
```

## Material Balances with Chemical Reactions

When a chemical reaction occurs, components are generated and consumed. This means the simple "In = Out" balance for components no longer holds. However, atoms are conserved.

### Atom Balances

```{note}
**Atomic Conservation Principle**

For any atom (e.g., Carbon, Hydrogen, Oxygen), the total number of moles of that atom entering the system must equal the total number of moles leaving the system. This method is powerful because it does not require calculating generation or consumption terms.
```

```{important}
**Atom Balance Equation**

For atom 'A':

$$
(\text{moles of A})_{in} = (\text{moles of A})_{out}
$$
```

```{prf:example} Methane Combustion

**Problem:** 100 mol/hr of methane ($CH_4$) is burned completely with 25% excess air. Calculate the molar flow rate and composition of the flue gas. Assume air is 21% $O_2$ and 79% $N_2$ by mole.
```

```{dropdown} Solution Steps

**Step 1: Basis and Reaction:** 100 mol/hr CH₄; CH₄ + 2O₂ → CO₂ + 2H₂O

**Step 2: Feed:** O₂ = 100 × 2 × 1.25 = 250 mol/hr; N₂ = 250 × 79/21 = 940.5 mol/hr

**Step 3: Products:** CO₂ = 100; H₂O = 200; N₂ = 940.5; O₂ (excess) = 50 mol/hr

**Step 4: Total Flow:** 100 + 200 + 940.5 + 50 = 1290.5 mol/hr

**Step 5: Mole %:** CO₂ = 7.75%, H₂O = 15.50%, N₂ = 72.88%, O₂ = 3.87%
```

## Transient (Unsteady-State) Material Balances

So far, we have focused on steady-state systems where process variables do not change over time. Now, we will examine transient processes, where the amount of material inside the system changes.

### Defining Process Types

```{admonition} Process Classifications
:class: tip

- **Steady-State**: Accumulation = 0, properties constant with time
- **Transient**: Accumulation $\neq$ 0, properties change with time
- **Batch**: No material enters or leaves during process
- **Continuous**: Material continuously flows in and out
- **Semi-Batch**: Combination of batch and continuous characteristics
```

### The General Balance with Accumulation

```{note}
**Transient Balance Principle**

The rate at which mass builds up or depletes within the system (accumulation) equals the rate of mass flowing in minus the rate flowing out.
```

```{admonition} Variable Definitions
:class: tip

- $M$: Total mass inside system (kg)
- $t$: Time (s)
- $\frac{dM}{dt}$: Rate of mass accumulation (kg/s)
- $\dot{m}_{in}$: Mass flow rate entering (kg/s)
- $\dot{m}_{out}$: Mass flow rate leaving (kg/s)
```

```{important}
**Transient Mass Balance**

For a non-reacting, transient system:

$$
\frac{dM}{dt} = \dot{m}_{in} - \dot{m}_{out}
$$
```

```{prf:example} Filling a Tank

**Problem:** A 2 m³ tank, initially half-full of water, is fed at 4 kg/s and withdrawn at 2 kg/s. How long to fill completely? ($\rho_{water} = 1000$ kg/m³)
```

```{dropdown} Solution Steps

**Step 1: Define System and Knowns**

Tank volume: 2 m³, Initial volume: 1 m³, Volume to fill: 1 m³

$\dot{m}_{in} = 4$ kg/s, $\dot{m}_{out} = 2$ kg/s, $\rho = 1000$ kg/m³

**Step 2: Apply Material Balance**

$\frac{dM}{dt} = 4 - 2 = 2$ kg/s (positive = accumulating)

**Step 3: Convert to Volumetric Rate**

$\frac{dV}{dt} = \frac{dM/dt}{\rho} = \frac{2}{1000} = 0.002$ m³/s

**Step 4: Calculate Fill Time**

$t = \frac{V_{fill}}{dV/dt} = \frac{1}{0.002} = 500$ seconds
```

## A Strategic Approach to Material Balances

With the fundamental balance equations established, we now focus on a systematic strategy for translating word problems into solvable systems of equations.

### Core Principles and Initial Analysis

```{note}
**The Golden Rule of Steady-State**

For any steady-state system, the total mass entering must equal the total mass leaving:

$$
\sum \dot{m}_{in} = \sum \dot{m}_{out}
$$

This holds regardless of reactions, phases, or compositions.
```

```{admonition} Problem-Solving Checklist
:class: tip

- **Identify the Goal**: What is the final answer needed?
- **Look for Keywords**: "overhead," "bottoms," "pure," "inert"
- **Check Assumptions**: If a substance enters, it must exit (unless consumed)
- **Mass Conservation**: Total mass in = total mass out (steady-state)
```

### Drawing and Labeling Process Flow Diagrams

```{note}
**Variable Naming Convention**

A consistent notation prevents confusion and errors in complex problems.
```

```{admonition} Recommended Notation
:class: tip

- **Flow Rates**: $\dot{m}$ (mass), $\dot{n}$ (molar), numbered by stream
- **Fractions**: $x$ (mass fraction), $y$ (mole fraction)
- **Combined**: $x_{B,1}$ = mass fraction of Benzene in stream 1
- **Pre-calculation**: Fill in simple unknowns immediately (fractions sum to 1)
```

### Setting Up Independent Balance Equations

```{important}
**Independent Equations Rule**

For a non-reactive system:

- Number of independent equations = Number of chemical species
- Can use $N$ component balances OR $(N-1)$ component + 1 overall balance
- Cannot use all $N+1$ equations as independent set
```

```{prf:example} Setting Up Balances for Mixing Column

**Problem:** Stream 1 (30% A, 70% B) and Stream 2 (40% A, 60% C) feed a column. Stream 3 is pure A. Stream 4 contains 20% B. Set up the independent mass balance equations.
```

```{dropdown} Solution Steps

**Step 1: Label Streams and Compositions**

Stream 1: $x_{A,1}=0.30$, $x_{B,1}=0.70$, $x_{C,1}=0$

Stream 2: $x_{A,2}=0.40$, $x_{B,2}=0$, $x_{C,2}=0.60$

Stream 3: $x_{A,3}=1.0$, $x_{B,3}=0$, $x_{C,3}=0$

Stream 4: $x_{B,4}=0.20$, $x_{A,4} + x_{C,4} = 0.80$

**Step 2: Write Component Balances**

**Component A:** $0.30\dot{m}_1 + 0.40\dot{m}_2 = 1.0\dot{m}_3 + x_{A,4}\dot{m}_4$

**Component B:** $0.70\dot{m}_1 = 0.20\dot{m}_4$

**Component C:** $0.60\dot{m}_2 = (0.80 - x_{A,4})\dot{m}_4$

**Step 3: Verify Overall Balance**

Sum of component balances gives: $\dot{m}_1 + \dot{m}_2 = \dot{m}_3 + \dot{m}_4$
```

### Degrees of Freedom Analysis

```{important}
**Degrees of Freedom Calculation**

$$
\text{DoF} = (\text{Number of Unknowns}) - (\text{Number of Independent Equations})
$$

- DoF = 0: Exactly determined (solvable)
- DoF $>$ 0: Underspecified (need more information)
- DoF $<$ 0: Overspecified (contradictory information)
```

```{note}
**Example DoF Analysis**

In the mixing column example:

- Unknowns: $\dot{m}_1, \dot{m}_2, \dot{m}_3, \dot{m}_4, x_{A,4}$ (5 total)
- Independent equations: 3 components = 3 equations
- DoF = 5 - 3 = 2 (underspecified)

Need 2 more pieces of information to solve!
```

```{caution}
**PE Exam Traps — Material Balances**

- **Over-counting equations:** The overall balance is NOT independent of component balances — it's the sum of all of them. Using all N components plus the overall gives N, not N+1, independent equations.
- **Mole vs. mass basis:** Mixing streams with different molecular weights? Convert to a consistent basis (all moles or all mass) before writing balances. Mixing mole fractions and mass fractions in one equation is a common error.
- **Recycle hides inerts:** An inert in a fresh feed will build up indefinitely without a purge stream. If the problem has an inert and no purge, re-read it — one must be implied.
- **Fractional conversion ≠ mole fraction in product:** Conversion refers to the fraction of the *reactant fed* that reacts, not the product concentration.
```

## Material Balances with Multiple Reactions

Chemical processes rarely involve a single, perfect reaction. Often, a primary reaction occurs alongside one or more side reactions. To analyze these systems, we can use two robust methods: balancing conserved atomic species or tracking the progress of each reaction individually using the extent of reaction.

```{note}
**Multiple Reaction Systems**

When multiple reactions occur simultaneously, we cannot simply use component balances because species are both generated and consumed. However, atoms are always conserved, providing a powerful analysis tool.
```

```{prf:example} Dehydrogenation of Ethane

**Problem:** 100 moles of ethane ($C_2H_6$) are fed to a reactor. The primary reaction is dehydrogenation to form ethylene ($C_2H_4$) and hydrogen ($H_2$). A side reaction occurs where ethylene reacts with ethane to form propylene ($C_3H_6$) and methane ($CH_4$). Given: fractional conversion of ethane = 0.7, selectivity of ethylene to propylene = 5. Find the molar composition of the product gas.

**Reactions:**

1. $C_2H_6 \longrightarrow C_2H_4 + H_2$
2. $C_2H_6 + C_2H_4 \longrightarrow C_3H_6 + CH_4$
```

```{admonition} Process Flow Information
:class: tip

- **Inlet**: 100 mol $C_2H_6$
- **Outlet**: Contains unreacted $C_2H_6$ and products $C_2H_4, H_2, C_3H_6, CH_4$
- **Unknowns**: 5 outlet molar flow rates
- **Available Info**: 2 atomic balances + conversion + selectivity + stoichiometric constraint
```

### Method 1: Atomic Species Balances

```{note}
**Atomic Conservation Principle**

For any atom, the total moles entering the system must equal the total moles leaving the system. This method works regardless of reaction complexity.
```

```{important}
**Atomic Balance Equation**

For any atom X:

$$
(\text{Moles of atom X})_{in} = (\text{Moles of atom X})_{out}
$$
```

```{dropdown} Solution Steps

**Step 1: Apply Given Constraints**

**Fractional Conversion:** $f = \frac{100 - \dot{n}_{C_2H_6}}{100} = 0.7 \Rightarrow \dot{n}_{C_2H_6} = 30$ mol

**Selectivity:** $S = \frac{\dot{n}_{C_2H_4}}{\dot{n}_{C_3H_6}} = 5 \Rightarrow \dot{n}_{C_2H_4} = 5\dot{n}_{C_3H_6}$

**Stoichiometry:** From Reaction 2: $\dot{n}_{C_3H_6} = \dot{n}_{CH_4}$

**Step 2: Carbon Balance**

C atoms in: $100 \times 2 = 200$ mol C

C atoms out: $(30 \times 2) + (5\dot{n}_{C_3H_6} \times 2) + (\dot{n}_{C_3H_6} \times 3) + (\dot{n}_{C_3H_6} \times 1)$

$200 = 60 + 14\dot{n}_{C_3H_6} \Rightarrow \dot{n}_{C_3H_6} = 10$ mol

**Step 3: Calculate Other Species**

$\dot{n}_{CH_4} = \dot{n}_{C_3H_6} = 10$ mol

$\dot{n}_{C_2H_4} = 5 \times 10 = 50$ mol

**Step 4: Hydrogen Balance**

H atoms in: $100 \times 6 = 600$ mol H

H atoms out: $(30 \times 6) + (50 \times 4) + (2\dot{n}_{H_2}) + (10 \times 6) + (10 \times 4)$

$600 = 480 + 2\dot{n}_{H_2} \Rightarrow \dot{n}_{H_2} = 60$ mol

**Step 5: Final Composition**

Total: $30 + 50 + 60 + 10 + 10 = 160$ mol

Mole fractions: $C_2H_6$: 18.75%, $C_2H_4$: 31.25%, $H_2$: 37.50%, $C_3H_6$: 6.25%, $CH_4$: 6.25%
```

### Method 2: Extent of Reaction

```{note}
**Extent of Reaction Concept**

The extent of reaction ($\xi$) tracks the progress of each individual reaction. It has units of moles and represents the "moles of reaction" that have occurred.
```

```{important}
**Species Balance with Extents**

For species $i$ involved in multiple reactions $j$:

$$
\dot{n}_i = \dot{n}_{i,in} + \sum_j \nu_{ij}\xi_j
$$

where $\nu_{ij}$ is the stoichiometric coefficient (negative for reactants, positive for products).
```

```{admonition} Species Balance Equations
:class: tip

- $\dot{n}_{C_2H_6} = 100 - \xi_1 - \xi_2$ (reactant in both reactions)
- $\dot{n}_{C_2H_4} = \xi_1 - \xi_2$ (product in Rxn 1, reactant in Rxn 2)
- $\dot{n}_{H_2} = \xi_1$ (product in Rxn 1 only)
- $\dot{n}_{C_3H_6} = \xi_2$ (product in Rxn 2 only)
- $\dot{n}_{CH_4} = \xi_2$ (product in Rxn 2 only)
```

```{dropdown} Solution Steps

**Step 1: Apply Conversion Constraint**

From $\dot{n}_{C_2H_6} = 30$: $30 = 100 - \xi_1 - \xi_2$

Therefore: $\xi_1 + \xi_2 = 70$ (Equation 1)

**Step 2: Apply Selectivity Constraint**

$S = \frac{\dot{n}_{C_2H_4}}{\dot{n}_{C_3H_6}} = \frac{\xi_1 - \xi_2}{\xi_2} = 5$

Therefore: $\xi_1 - \xi_2 = 5\xi_2 \Rightarrow \xi_1 = 6\xi_2$ (Equation 2)

**Step 3: Solve for Extents**

Substitute Eq. 2 into Eq. 1: $(6\xi_2) + \xi_2 = 70$

$7\xi_2 = 70 \Rightarrow \xi_2 = 10$ mol

$\xi_1 = 6 \times 10 = 60$ mol

**Step 4: Calculate Outlet Flows**

$\dot{n}_{C_2H_6} = 100 - 60 - 10 = 30$ mol

$\dot{n}_{C_2H_4} = 60 - 10 = 50$ mol

$\dot{n}_{H_2} = 60$ mol, $\dot{n}_{C_3H_6} = 10$ mol, $\dot{n}_{CH_4} = 10$ mol

**Step 5: Verify Results**

Same composition as Method 1
```

### Comparison of Methods

```{note}
**Method Selection Guidelines**

**Atomic Species Balance Method:**

- More direct when reaction stoichiometry is complex
- Requires fewer initial equations
- May lead to more complex algebraic systems

**Extent of Reaction Method:**

- Requires more setup (equation for every species)
- Often leads to simpler systems of equations
- Provides direct insight into individual reaction progress
- Preferred when tracking multiple reactions separately

Both methods produce identical results. Choose based on problem complexity and personal preference.
```

## Combustion Reactions

Combustion is a rapid reaction between a substance with an oxidant, usually oxygen, to produce heat and light. In chemical engineering, we are primarily concerned with the combustion of hydrocarbon fuels for analyzing furnaces, boilers, and reactors.

### Complete vs. Incomplete Combustion

```{note}
**Types of Combustion**

**Complete Combustion**: Sufficient oxygen for all carbon → $CO_2$ and all hydrogen → $H_2O$

**Incomplete Combustion**: Insufficient oxygen supply, carbon → $CO$ instead of $CO_2$
```

```{important}
**Combustion Reaction Examples**

**Complete Methane Combustion:**

$$
CH_4 + 2O_2 \longrightarrow CO_2 + 2H_2O
$$

**Incomplete Methane Combustion:**

$$
CH_4 + \frac{3}{2}O_2 \longrightarrow CO + 2H_2O
$$
```

### Key Terminology for Combustion

```{admonition} Critical Combustion Terms
:class: tip

- **Theoretical Oxygen**: Molar amount of $O_2$ required for complete combustion (from stoichiometry)
- **Theoretical Air**: Quantity of air containing the theoretical oxygen amount
- **Excess Air**: Air fed above theoretical requirement (prevents incomplete combustion)
```

```{important}
**Percent Excess Air**

$$
\% \text{ Excess Air} = \frac{(\text{moles of air})_{\text{fed}} - (\text{moles of air})_{\text{theoretical}}}{(\text{moles of air})_{\text{theoretical}}} \times 100\%
$$
```

```{prf:example} Complete Combustion of Methane

**Problem:** 100 moles of methane ($CH_4$) are burned with 25% excess air. The reaction proceeds to completion with no partial combustion. Find the moles of air fed and the composition of the stack gas. Assume air is 21% $O_2$ and 79% $N_2$ by mole.
```

```{dropdown} Solution Steps

**Step 1: Basis and Stoichiometry**

Basis: 100 moles $CH_4$ feed

Reaction: $CH_4 + 2O_2 \longrightarrow CO_2 + 2H_2O$

**Step 2: Calculate Theoretical Air**

Theoretical $O_2$: $100 \times 2 = 200$ mol $O_2$

Theoretical air: $\frac{200 \text{ mol } O_2}{0.21} = 952.4$ mol air

**Step 3: Calculate Fed Air**

With 25% excess: $(\text{moles air})_{\text{fed}} = 952.4 \times 1.25 = 1190.5$ mol air

**Step 4: Apply Extent of Reaction**

Complete conversion: $\xi = 100$ mol (all methane consumed)

Fed $O_2$: $1190.5 \times 0.21 = 250$ mol

Fed $N_2$: $1190.5 \times 0.79 = 940.5$ mol

**Step 5: Calculate Product Composition**

$\dot{n}_{CO_2} = 0 + (1)\xi = 100$ mol

$\dot{n}_{H_2O} = 0 + (2)\xi = 200$ mol

$\dot{n}_{O_2} = 250 + (-2)\xi = 50$ mol (excess)

$\dot{n}_{N_2} = 940.5$ mol (inert)

**Step 6: Final Results**

Air fed: **1190.5 mol**

Stack gas: $CO_2$: 100 mol, $H_2O$: 200 mol, $O_2$: 50 mol, $N_2$: 940.5 mol
```

## Material Balances with Recycle

In many chemical processes, a portion of the product stream is separated and fed back to the reactor inlet. This recycle stream increases overall conversion, recovers catalyst, or dilutes feed streams.

### Key Definitions for Recycle Systems

```{admonition} Recycle System Components
:class: tip

- **Fresh Feed**: Material entering the process from external source
- **Recycle Stream**: Stream returned from downstream separation to mix with fresh feed
- **Combined Feed**: Stream entering reactor (fresh feed + recycle mixture)
```

```{important}
**Recycle Ratio**

$$
R_R = \frac{F_{T,R}}{F_f}
$$

where $F_{T,R}$ = total flow rate of recycle stream, $F_f$ = total flow rate of fresh feed
```

### Overall Conversion vs. Single-Pass Conversion

```{note}
**Critical Distinction**

Understanding the difference between overall and single-pass conversion is essential for recycle system analysis and design optimization.
```

```{important}
**Conversion Definitions**

**Overall Conversion** (measures entire process performance):

$$
\text{Overall Conversion} = \frac{F_{A,0} - F_{A,f}}{F_{A,0}}
$$

**Single-Pass Conversion** (measures reactor performance only):

$$
\text{Single-Pass Conversion} = \frac{F_{A,m} - F_{A,outlet}}{F_{A,m}}
$$

where:

- $F_{A,0}$ = reactant A flow in fresh feed
- $F_{A,f}$ = reactant A flow in final outlet stream
- $F_{A,m}$ = reactant A flow in combined feed to reactor
- $F_{A,outlet}$ = reactant A flow leaving reactor
```

```{note}
**Recycle Strategy**

The goal of a recycle loop is to achieve high overall conversion even when single-pass conversion is relatively low. This allows:

- Smaller reactor volumes
- Better temperature control
- Higher overall process efficiency
- Economic optimization of conversion vs. separation costs
```

## Advanced Material Balance Examples

This section applies foundational material balance principles to complex systems involving recycle loops and multiple unit operations. These examples demonstrate how to break down complex processes into solvable parts by choosing appropriate system boundaries.

```{note}
**Complex System Analysis Strategy**

For multi-unit processes:

- Choose system boundaries strategically to isolate unknowns
- Start with overall system balances before subsystem analysis
- Use degrees of freedom analysis to verify solvability
- Internal recycle streams don't cross overall system boundaries
```

### Example 1: Evaporative Crystallization with Recycle

```{prf:example} Evaporative Crystallization with Recycle

**Problem:** A continuous process involves an evaporator and crystallizer. Fresh feed (400 kg/h, 15 wt% KCl) mixes with recycle, enters an evaporator where water is removed. The concentrated solution (38 wt% KCl) goes to a crystallizer/filter. Output is filter cake (solid KCl crystals + saturated solution at 28 wt% KCl). Crystals are 84% of filter cake mass. Remaining filtrate (28 wt% KCl) is recycled.

Find: (a) KCl crystal flow rate, (b) water vapor flow rate, (c) recycle flow rate.
```

```{admonition} Process Stream Definitions
:class: tip

- $\dot{m}_1$: Fresh feed = 400 kg/h, $x_1 = 0.15$
- $\dot{m}_2$: Water vapor from evaporator, $x_2 = 0$
- $\dot{m}_3$: Concentrated solution to crystallizer, $x_3 = 0.38$
- $\dot{m}_4$: Solid KCl crystals, $x_4 = 1.0$
- $\dot{m}_5$: Saturated solution with crystals, $x_5 = 0.28$
- $\dot{m}_6$: Recycle stream, $x_6 = 0.28$

**Given Constraint:** $\frac{\dot{m}_4}{\dot{m}_4 + \dot{m}_5} = 0.84$
```

```{note}
**Solution Strategy**

**Two-Step Approach:**

1. Overall system balance (excludes internal recycle)
2. Crystallizer/filter subsystem balance (includes recycle)
```

```{dropdown} Solution Steps

**Step 1: Overall System Analysis**

**DoF Check:** 3 unknowns ($\dot{m}_2, \dot{m}_4, \dot{m}_5$), 3 equations (overall mass, KCl balance, filter cake relation) → DoF = 0

**Filter Cake Relation:**
$\dot{m}_4 = 0.84(\dot{m}_4 + \dot{m}_5) \Rightarrow \dot{m}_5 = 0.1905\dot{m}_4$

**Step 2: Overall KCl Balance**

KCl In = KCl Out: $\dot{m}_1 x_1 = \dot{m}_4 x_4 + \dot{m}_5 x_5$

$(400)(0.15) = \dot{m}_4(1.0) + \dot{m}_5(0.28)$

$60 = \dot{m}_4 + 0.28(0.1905\dot{m}_4) = 1.05334\dot{m}_4$

$\dot{m}_4 = 56.96$ kg/h, $\dot{m}_5 = 10.85$ kg/h

**Step 3: Overall Mass Balance**

Total In = Total Out: $\dot{m}_1 = \dot{m}_2 + \dot{m}_4 + \dot{m}_5$

$400 = \dot{m}_2 + 56.96 + 10.85 \Rightarrow \dot{m}_2 = 332.19$ kg/h

**Step 4: Crystallizer/Filter Subsystem**

**DoF Check:** 2 unknowns ($\dot{m}_3, \dot{m}_6$), 2 equations → DoF = 0

**Mass Balance:** $\dot{m}_3 = (\dot{m}_4 + \dot{m}_5) + \dot{m}_6 = 67.81 + \dot{m}_6$

**KCl Balance:** $\dot{m}_3(0.38) = 56.96(1.0) + 10.85(0.28) + \dot{m}_6(0.28)$

$(67.81 + \dot{m}_6)(0.38) = 59.998 + 0.28\dot{m}_6$

$25.77 + 0.38\dot{m}_6 = 59.998 + 0.28\dot{m}_6$

$\dot{m}_6 = 342.28$ kg/h

**Step 5: Final Answers**

(a) KCl crystals: **57.0 kg/h**

(b) Water vapor: **332.2 kg/h**

(c) Recycle flow: **342.3 kg/h**
```

### Example 2: Distillation with Condenser and Reboiler

```{prf:example} Distillation Column Analysis

**Problem:** Feed to distillation column is 45 mol% n-pentane/55 mol% n-hexane. Vapor leaving top (98 mol% pentane) goes to total condenser. Half of condensate returns as reflux, half withdrawn as overhead product at 85 kmol/h. Overhead contains 95% of feed pentane. Bottom liquid goes to reboiler.

**Part A:** Find feed flow rate and bottoms composition.

**Part B:** Find vapor temperature at 1 atm and volumetric flow rates.
```

```{admonition} Given Information
:class: tip

- Feed: 45 mol% pentane, 55 mol% hexane
- Vapor from column: 98 mol% pentane
- Overhead product: 85 kmol/h (50% of condensate)
- Overhead contains 95% of feed pentane
- Operating pressure: 1 atm (760 mmHg)
```

```{dropdown} Solution Steps

**Step 1: Find Feed Flow Rate**

Pentane recovery relationship: $(N_{overhead})(y_{p,overhead}) = 0.95 \times (N_{feed})(x_{p,feed})$

$(85)(0.98) = 0.95 \times (N_{feed})(0.45)$

$83.3 = N_{feed} \times 0.4275 \Rightarrow N_{feed} = 194.85$ kmol/h

**Step 2: Find Bottoms Flow Rate**

Overall molar balance: $N_{feed} = N_{overhead} + N_{bottoms}$

$194.85 = 85 + N_{bottoms} \Rightarrow N_{bottoms} = 109.85$ kmol/h

**Step 3: Find Bottoms Composition**

Overall pentane balance: $N_{feed} \times 0.45 = (N_{overhead} \times 0.98) + (N_{bottoms} \times x_{p,bottoms})$

$194.85 \times 0.45 = 85 \times 0.98 + 109.85 \times x_{p,bottoms}$

$87.68 = 83.3 + 109.85 x_{p,bottoms} \Rightarrow x_{p,bottoms} = 0.040$

**Bottoms:** 4.0% pentane, 96.0% hexane
```

```{important}
**VLE and Volumetric Calculations**

**Dew Point Calculation (Raoult's Law):**

$$
\sum \frac{y_i P}{P_i^{sat}(T)} = 1
$$

**Antoine Equation:**

$$
P_i^{sat} = 10^{(A - \frac{B}{T+C})}
$$

**Liquid Volume:**

$$
\dot{V}_i = \frac{\dot{n}_i \times MW_i}{\rho_i}
$$
```

```{admonition} Antoine Constants and Properties
:class: tip

**Antoine Constants (T in °C, P in mmHg):**

n-Pentane: A = 6.85221, B = 1064.63, C = 232.0

n-Hexane: A = 6.87776, B = 1171.17, C = 224.41

**Physical Properties:**

Pentane: MW = 72.15 kg/kmol, $\rho$ = 621 kg/m³

Hexane: MW = 86.18 kg/kmol, $\rho$ = 659 kg/m³
```

```{dropdown} Solution Steps (Part B)

**Step 1: Apply dew point equation with Antoine constants:**

$$
\frac{0.98 \times 760}{10^{(6.85221 - \frac{1064.63}{T+232.0})}} + \frac{0.02 \times 760}{10^{(6.87776 - \frac{1171.17}{T+224.41})}} = 1
$$

Solving iteratively: $T = 37.3$ °C (310.45 K)

**Step 2: Vapor Volumetric Flow Rate**

Total vapor to condenser: $2 \times 85 = 170$ kmol/h (reflux + product)

$\dot{V}_{vapor} = \frac{(170)(0.08206)(310.45)}{1} = 4325$ m³/h

**Step 3: Liquid Product Volumetric Flow Rate**

**Pentane volume:** $\dot{V}_{p} = \frac{(85 \times 0.98)(72.15)}{621} = 9.68$ m³/h

**Hexane volume:** $\dot{V}_{h} = \frac{(85 \times 0.02)(86.18)}{659} = 0.22$ m³/h

**Total liquid:** $\dot{V}_{liquid} = 9.68 + 0.22 = 9.90$ m³/h

**Step 4: Part B Final Results**

Vapor temperature: **37.3°C** | Vapor flow rate: **4325 m³/h** | Liquid product flow rate: **9.90 m³/h**
```

### Example 3: Multi-Unit Crystallization with Recycle and Drying

```{prf:example} Multi-Unit Crystallization with Recycle and Drying

**Problem:** Potassium dichromate ($K_2Cr_2O_7$, KD) is recovered from a 25 wt% aqueous solution. Fresh feed joins recycle and feeds crystallizer/centrifuge where water evaporates causing crystallization. Saturated solution contains 15 wt% KD. Slurry split: 90% solution recycled, 10% leaves with crystals as filter cake (85 wt% solid KD, 15 wt% saturated solution). Filter cake goes to dryer where dry air evaporates remaining water, leaving pure KD. Air leaves dryer with 0.08 mole fraction water.

For 1000 kg/h pure KD production, find:

1. Water evaporated in crystallizer/centrifuge
2. Recycle stream mass flow rate
3. Molar flow rate of dry air to dryer
```

```{note}
**Solution Strategy**

Analyze different system boundaries strategically. Key insight: balances on non-reactive species (like KD) across boundaries where only one stream contains that species can directly solve for unknown flow rates.
```

```{admonition} Process Stream Analysis
:class: tip

- Fresh feed: 25 wt% KD aqueous solution
- Saturated solution: 15 wt% KD, 85 wt% water
- Filter cake: 85 wt% solid KD crystals, 15 wt% saturated solution
- Split ratio: 90% solution recycled, 10% with filter cake
- Final product: 1000 kg/h pure KD crystals
- Air outlet: 0.08 mole fraction water
```

```{dropdown} Solution Steps

**Step 1: Analyze Dryer - Find Filter Cake Flow Rate**

**Dryer KD Balance:** Only KD-containing streams are filter cake (in) and pure crystals (out)

KD in filter cake = (crystals) + (dissolved in solution)

$(\dot{m}_{cake} \times 0.85) + (\dot{m}_{cake} \times 0.15 \times 0.15) = 1000$ kg/h

$\dot{m}_{cake}(0.85 + 0.0225) = 1000 \Rightarrow \dot{m}_{cake} = \frac{1000}{0.8725} = 1146.1$ kg/h

**Step 2: Overall System Analysis - Find Fresh Feed Rate**

**Overall KD Balance:** Only KD enters in fresh feed, only leaves as final product

$\dot{m}_{feed} \times 0.25 = 1000 \Rightarrow \dot{m}_{feed} = 4000$ kg/h

**Step 3: Find Evaporated Water (Answer 1)**

**Mass Balance around Mixing Point + Crystallizer:**

Boundary includes feed mixing and crystallizer (recycle is internal)

Total Mass In = Total Mass Out: $\dot{m}_{feed} = \dot{m}_{evap} + \dot{m}_{cake}$

$4000 = \dot{m}_{evap} + 1146.1 \Rightarrow \dot{m}_{evap} = 2853.9$ kg/h

**Answer 1: 2854 kg/h**

**Step 4: Find Recycle Stream Rate (Answer 2)**

**Solution mass in filter cake:** $\dot{m}_{soln,cake} = 1146.1 \times 0.15 = 171.9$ kg/h

This is the 10% portion. Recycle is the 90% portion:

$\frac{\dot{m}_{recycle}}{\dot{m}_{soln,cake}} = \frac{90\%}{10\%} = 9$

$\dot{m}_{recycle} = 9 \times 171.9 = 1547.1$ kg/h

**Answer 2: 1547 kg/h**

**Step 5: Find Air Flow Rate to Dryer (Answer 3)**

**Water entering dryer:** $\dot{m}_{H_2O,in} = 171.9 \times 0.85 = 146.1$ kg/h

**Convert to molar:** $\dot{n}_{H_2O,out} = \frac{146.1}{18.015} = 8.11$ kmol/h

**Total outlet stream:** $\dot{n}_{total,out} = \frac{8.11}{0.08} = 101.38$ kmol/h

**Dry air flow:** $\dot{n}_{air,in} = 101.38 - 8.11 = 93.27$ kmol/h

**Answer 3: 93.3 kmol/h**
```

### Example 4: Leaching Process with Multiple Recycle Streams

```{prf:example} Coffee Decaffeination Process

**Problem:** 100 kg coffee beans (1.5 kg caffeine, 98.5 kg inert solids) fed to mixing tank. Decaffeinating solvent (DCS) extracts 90% of initial caffeine. Treated beans carry 20 kg DCS to dryer. Dryer recovers 90% of this DCS (recycled to mixer), 10% leaves with final beans.

Solvent-caffeine solution from mixer (88 wt% DCS) enters settling unit, splits into waste stream (5 wt% DCS) and cleaned solvent recycled to mixing point with fresh DCS. Combined solvent entering mixer contains 95 wt% DCS.

Find: (a) fresh DCS mass required per 100 kg beans, (b) composition of recycle from settling unit.
```

```{note}
**Solution Strategy**

Degree of Freedom analysis reveals overall system is solvable first. Work inward, solving for internal streams using systematic boundary selection.
```

```{admonition} Process Stream Information
:class: tip

- Coffee beans: 100 kg (1.5 kg caffeine, 98.5 kg solids)
- Caffeine removal: 90% of initial (1.35 kg removed)
- DCS to dryer: 20 kg
- DCS recovery from dryer: 90% (18 kg recycled)
- DCS in final beans: 10% (2 kg)
- Mixer outlet: 88 wt% DCS
- Waste stream: 5 wt% DCS
- Combined solvent to mixer: 95 wt% DCS
```

```{dropdown} Solution Steps (Part a)

**Step 1: Pre-calculations from Problem Statement**

**Caffeine removed:** $1.5 \times 0.90 = 1.35$ kg

**Caffeine in final beans:** $1.5 \times 0.10 = 0.15$ kg

**DCS recycled from dryer:** $20 \times 0.90 = 18$ kg

**DCS in final beans:** $20 \times 0.10 = 2$ kg

**Step 2: Overall System DoF Analysis**

**Boundary:** Fresh beans + Fresh DCS → Final beans + Waste solution

**Unknowns:** $\dot{m}_{fresh}$, $\dot{m}_{waste}$ (2 variables)

**Equations:** Caffeine balance, DCS balance (2 equations)

**DoF = 2 - 2 = 0** (solvable)

**Step 3: Overall Caffeine Balance**

Caffeine in beans = Caffeine in final beans + Caffeine in waste

Waste is 5% DCS, so 95% caffeine:

$1.5 = 0.15 + (\dot{m}_{waste} \times 0.95)$

$1.35 = 0.95\dot{m}_{waste} \Rightarrow \dot{m}_{waste} = 1.42$ kg

**Step 4: Overall DCS Balance (Answer a)**

DCS in fresh feed = DCS in final beans + DCS in waste

$\dot{m}_{fresh} = 2 + (1.42 \times 0.05) = 2 + 0.071 = 2.071$ kg

**Answer (a): 2.07 kg fresh DCS per 100 kg beans**
```

```{dropdown} Solution Steps (Part b)

**Step 5: Mixing Tank Balance Analysis**

**Boundary:** Around mixing tank only

**Unknowns:** $\dot{m}_{in,tank}$ (combined solvent in), $\dot{m}_{out,tank}$ (solution out)

**DoF:** 2 unknowns - 2 balances = 0

**Step 6: Caffeine Balance on Mixing Tank**

Caffeine in beans + Caffeine in solvent = Caffeine in solution + Caffeine with beans

$1.5 + (\dot{m}_{in,tank} \times 0.05) = (\dot{m}_{out,tank} \times 0.12) + 0.15$

**Step 7: DCS Balance on Mixing Tank**

DCS in solvent + DCS from dryer = DCS in solution + DCS with beans

$(\dot{m}_{in,tank} \times 0.95) + 18 = (\dot{m}_{out,tank} \times 0.88) + 20$

**Solving simultaneously:** $\dot{m}_{in,tank} = 20.4$ kg, $\dot{m}_{out,tank} = 19.75$ kg

**Step 8: Mixing Point Balance (Answer b)**

**Overall mass balance:** $\dot{m}_{fresh} + \dot{m}_{recycle} = \dot{m}_{in,tank}$

$2.071 + \dot{m}_{recycle} = 20.4 \Rightarrow \dot{m}_{recycle} = 18.33$ kg

**DCS balance:** $(\dot{m}_{fresh} \times 1.0) + (\dot{m}_{recycle} \times x_{DCS,recycle}) = (\dot{m}_{in,tank} \times 0.95)$

$(2.071 \times 1.0) + (18.33 \times x_{DCS,recycle}) = (20.4 \times 0.95)$

$2.071 + 18.33x_{DCS,recycle} = 19.38$

$x_{DCS,recycle} = \frac{17.309}{18.33} = 0.944$

**Answer (b): Recycle stream is 94.4% DCS, 5.6% caffeine**
```

```{important}
**Final Results**

**(a) Fresh DCS Required:** 2.07 kg per 100 kg coffee beans

**(b) Recycle Stream Composition:** 94.4 wt% DCS, 5.6 wt% caffeine
```

## Combustion Reactor with Product Recycle

```{prf:example} Butane Combustion with Product Recycle

**Problem:** Butane ($C_4H_{10}$) is burned with 25% excess oxygen. Combined feed to reactor: 100 mol/h butane. Single-pass conversion: 45%. Mole ratio $CO_2$:$CO$ in reactor outlet: 9:1. Stream from reactor goes to separator where 90% of unreacted butane and oxygen are recycled. Remaining 10% leaves as waste.

Find:

1. Molar composition of product gas from reactor
2. Molar flow rates of butane and oxygen in fresh feed
3. Overall conversion of butane in process
```

```{note}
**Solution Strategy**

Use reactor information to solve outlet stream first. Then analyze separator and mixing point for fresh feed and recycle rates. Since specific CO formation reaction isn't given, use atomic species balances.
```

```{admonition} Given Information
:class: tip

- Combined feed to reactor: 100 mol/h butane
- Excess oxygen: 25% above stoichiometric
- Single-pass conversion: 45%
- $CO_2$:$CO$ mole ratio: 9:1
- Separator recovery: 90% of unreacted gases recycled
- Complete combustion stoichiometry: $C_4H_{10} + 6.5O_2 \rightarrow 4CO_2 + 5H_2O$
```

```{dropdown} Solution Steps

**Step 1: Reactor Feed Analysis**

**Basis:** 100 mol/h butane to reactor

**Theoretical $O_2$:** $100 \times 6.5 = 650$ mol/h

**Actual $O_2$ fed:** $650 \times 1.25 = 812.5$ mol/h

**Step 2: Reactor Outlet - Unreacted Butane**

With 45% conversion: $\dot{n}_{C_4H_{10},out} = 100 \times (1-0.45) = 55$ mol/h

**Step 3: Hydrogen Balance Around Reactor**

H atoms in = H atoms out:

$(100 \times 10) = (55 \times 10) + (\dot{n}_{H_2O} \times 2)$

$1000 = 550 + 2\dot{n}_{H_2O} \Rightarrow \dot{n}_{H_2O} = 225$ mol/h

**Step 4: Carbon Balance with $CO$ and $CO_2$ Ratio**

C atoms in = C atoms out:

$(100 \times 4) = (55 \times 4) + \dot{n}_{CO_2} + \dot{n}_{CO}$

Given $\dot{n}_{CO_2} = 9\dot{n}_{CO}$:

$400 = 220 + 9\dot{n}_{CO} + \dot{n}_{CO} = 220 + 10\dot{n}_{CO}$

$\dot{n}_{CO} = 18$ mol/h, $\dot{n}_{CO_2} = 162$ mol/h

**Step 5: Oxygen Balance Around Reactor**

O atoms in = O atoms out:

$(812.5 \times 2) = (\dot{n}_{O_2,out} \times 2) + (162 \times 2) + (18 \times 1) + (225 \times 1)$

$1625 = 2\dot{n}_{O_2,out} + 567 \Rightarrow \dot{n}_{O_2,out} = 529$ mol/h
```

```{important}
**Answer 1: Reactor Outlet Composition**

Total moles out: $55 + 225 + 18 + 162 + 529 = 989$ mol/h

**Mole Fractions:**

- $y_{C_4H_{10}} = 55/989 = 5.6\%$
- $y_{H_2O} = 225/989 = 22.7\%$
- $y_{CO} = 18/989 = 1.8\%$
- $y_{CO_2} = 162/989 = 16.4\%$
- $y_{O_2} = 529/989 = 53.5\%$
```

```{dropdown} Solution Steps (Continued)

**Step 6: Separator Analysis**

**Recycle streams (90% of unreacted):**

$\dot{n}_{C_4H_{10},recycle} = 55 \times 0.90 = 49.5$ mol/h

$\dot{n}_{O_2,recycle} = 529 \times 0.90 = 476.1$ mol/h

**Waste streams (10% of unreacted):**

$\dot{n}_{C_4H_{10},waste} = 55 \times 0.10 = 5.5$ mol/h

**Step 7: Mixing Point Balance (Answer 2)**

Fresh feed + Recycle = Combined feed to reactor:

$\dot{n}_{C_4H_{10},fresh} + 49.5 = 100 \Rightarrow \dot{n}_{C_4H_{10},fresh} = 50.5$ mol/h

$\dot{n}_{O_2,fresh} + 476.1 = 812.5 \Rightarrow \dot{n}_{O_2,fresh} = 336.4$ mol/h

**Step 8: Overall Butane Conversion (Answer 3)**

$\text{Overall Conv.} = \frac{\dot{n}_{C_4H_{10},fresh} - \dot{n}_{C_4H_{10},waste}}{\dot{n}_{C_4H_{10},fresh}}$

$= \frac{50.5 - 5.5}{50.5} = \frac{45}{50.5} = 0.891 = 89.1\%$
```

```{note}
**Final Results Summary**

1. **Reactor outlet composition:** 5.6% $C_4H_{10}$, 22.7% $H_2O$, 1.8% $CO$, 16.4% $CO_2$, 53.5% $O_2$
2. **Fresh feed rates:** 50.5 mol/h butane, 336.4 mol/h oxygen
3. **Overall butane conversion:** 89.1%
```

## Methanol Synthesis with Recycle and Purge Stream

```{prf:example} Methanol Production with Recycle and Purge

**Problem:** Methanol ($CH_3OH$) produced by reacting CO and $H_2$ over catalyst. Fresh feed: 30 mol% CO, 60 mol% $H_2$, 10 mol% $N_2$ (inert). Feed mixes with recycle and goes to reactor. Reactor effluent goes to condenser separating pure liquid methanol. Remaining gases split: portion purged (prevent inert buildup), rest recycled. Recycle ratio: 3 moles recycled per 1 mole fresh feed. Recycle stream: 25 mol% $N_2$.

For 100 mol/h fresh feed, find:

1. Rate of methanol production
2. Rate and composition of purge gas
3. Overall and single-pass CO conversions
```

```{note}
**Solution Strategy**

DoF analysis shows overall system is solvable first. Inert species ($N_2$) provides key to unlocking system. Use extent of reaction method.
```

```{admonition} Process Information
:class: tip

- **Reaction:** $CO + 2H_2 \rightarrow CH_3OH$
- **Fresh feed:** 100 mol/h (30 mol/h CO, 60 mol/h $H_2$, 10 mol/h $N_2$)
- **Recycle ratio:** 3:1 (recycle:fresh feed)
- **Recycle composition:** 25 mol% $N_2$
- **Products:** Pure liquid methanol + purge gas
```

```{dropdown} Solution Steps

**Step 1: Basis and Overall System Boundary**

**Basis:** 100 mol/h fresh feed

Contains: 30 mol/h CO, 60 mol/h $H_2$, 10 mol/h $N_2$

**Boundary:** Fresh feed in → Methanol out + Purge out

**Step 2: Overall Nitrogen Balance**

$N_2$ is inert - only enters in fresh feed, only leaves in purge:

$(\text{$N_2$ In}) = (\text{$N_2$ Out})$

$10 = \dot{n}_{purge} \times y_{N_2,purge} = \dot{n}_{purge} \times 0.25$

$\dot{n}_{purge} = 40$ mol/h

**Step 3: Extent of Reaction from Reactant Balances**

For each reactant: In - Out = Reacted = $\nu_i \xi$

**CO balance:** $30 - (\dot{n}_{purge} \times y_{CO,purge}) = (1)\xi$

$30 - 40y_{CO,purge} = \xi$ ... (Eq. 1)

**$H_2$ balance:** $60 - (\dot{n}_{purge} \times y_{H_2,purge}) = (2)\xi$

$60 - 40y_{H_2,purge} = 2\xi$ ... (Eq. 2)

**Step 4: Solve for Purge Composition**

**Mole fraction constraint:** $y_{CO} + y_{H_2} + y_{N_2} = 1$

$y_{CO,purge} + y_{H_2,purge} + 0.25 = 1$ ... (Eq. 3)

From Eq. 2: $y_{H_2,purge} = \frac{60-2\xi}{40}$

From Eq. 1: $y_{CO,purge} = \frac{30-\xi}{40}$

Substitute into Eq. 3: $\frac{30-\xi}{40} + \frac{60-2\xi}{40} + 0.25 = 1$

$\frac{90-3\xi}{40} = 0.75 \Rightarrow 90-3\xi = 30 \Rightarrow \xi = 20$ mol/h

**Step 5: Calculate Final Compositions**

$y_{CO,purge} = \frac{30-20}{40} = 0.25$

$y_{H_2,purge} = \frac{60-40}{40} = 0.50$

$y_{N_2,purge} = 0.25$
```

```{important}
**Answers 1 & 2: Production and Purge**

**(1) Methanol Production Rate:** $\dot{n}_{methanol} = \xi = 20$ mol/h

**(2) Purge Gas:**

- Rate: 40 mol/h
- Composition: 25% CO, 50% $H_2$, 25% $N_2$
```

```{dropdown} Solution Steps (Continued)

**Step 6: Overall CO Conversion**

$\text{Overall Conv.} = \frac{\text{CO in fresh} - \text{CO in purge}}{\text{CO in fresh}}$

$= \frac{30 - (40 \times 0.25)}{30} = \frac{30-10}{30} = 0.667 = 66.7\%$

**Step 7: Single-Pass CO Conversion**

**Recycle rate:** $3 \times 100 = 300$ mol/h

**Total feed to reactor:** $100 + 300 = 400$ mol/h

**CO to reactor:** Fresh CO + Recycle CO

$= 30 + (300 \times y_{CO,recycle}) = 30 + (300 \times 0.25) = 105$ mol/h

**Single-pass conversion:** $\frac{\text{CO reacted}}{\text{CO to reactor}} = \frac{20}{105} = 0.190 = 19.0\%$
```

```{note}
**Answer 3: CO Conversions**

**Overall Conversion:** 66.7%

**Single-Pass Conversion:** 19.0%

This clearly demonstrates how recycle significantly increases overall process conversion above the low single-pass reactor conversion.
```

```{note}
**Key Insights: Recycle with Purge Systems**

**Critical Design Considerations:**

- Inert buildup necessitates purge stream to maintain steady operation
- Recycle dramatically improves overall conversion vs. single-pass
- Purge rate determined by inert material balance
- Higher recycle ratios increase overall conversion but also operating costs
- Optimal purge rate balances material recovery with inert removal
```

## Introduction to Reactor Systems with Recycle

Reactor systems with recycle streams are common in chemical processing to improve overall conversion and economic efficiency. However, when unreactive species (inerts) are present, a **purge stream** becomes necessary to prevent accumulation and maintain steady-state operation.

```{note}
A **purge stream** is a portion of a recycle stream that is withdrawn to prevent the buildup of materials that remain entirely in the recycle stream. Without a purge, inert species would accumulate indefinitely, preventing the system from reaching steady state.
```

The typical reactor system consists of four main components:

- **Mixing Point**: Where fresh feed combines with recycle stream
- **Reactor**: Where chemical reaction occurs with specified conversion
- **Separator**: Where products are separated from unreacted species
- **Splitting Point**: Where recycle stream is divided into purge and recycle portions

## Material Balance Equations

### Mixing Point Balances

At the mixing point, fresh feed (stream 1) combines with recycle (stream 7) to form reactor feed (stream 2).

```{important}
Total material balance:

$$
\dot{m}_2 = \dot{m}_1 + \dot{m}_7
$$

Component material balance (for each component i):

$$
x_{i,2}\dot{m}_2 = x_{i,1}\dot{m}_1 + x_{i,7}\dot{m}_7
$$
```

### Reactor Balances

For a reactor with fractional conversion X and stoichiometric feed:

```{important}
For reactants (component 1 is limiting reactant):

$$
x_{i,3}\dot{m}_3 = x_{i,2}\dot{m}_2 \cdot (1 - X)
$$

For products:

$$
x_{i,3}\dot{m}_3 = x_{1,2}\dot{m}_2 \cdot X \cdot a
$$

For unreactive species (inerts):

$$
x_{i,2}\dot{m}_2 = x_{i,3}\dot{m}_3
$$
```

### Separator Balances

The separator may not remove all reaction products and may also remove some feed species.

```{important}
Total material balance:

$$
\dot{m}_3 = \dot{m}_4 + \dot{m}_5
$$

Component material balance:

$$
x_{i,3}\dot{m}_3 = x_{i,4}\dot{m}_4 + x_{i,5}\dot{m}_5
$$
```

### Splitting Point Balances

At the splitting point, stream 5 is divided into purge (stream 6) and recycle (stream 7).

```{important}
Flow rate relationships:

$$
\dot{m}_5 = \dot{m}_6 + \dot{m}_7
$$

$$
\dot{m}_6 = \text{purge} \cdot \dot{m}_5
$$

$$
\dot{m}_7 = (1 - \text{purge}) \cdot \dot{m}_5
$$

Composition relationships:

$$
x_{i,5} = x_{i,6} = x_{i,7} \text{ (for each component i)}
$$
```

```{admonition} Key Variables & Notation
:class: tip

- $\dot{m}_j$ = total molar flow rate at location j (mol/s)
- $x_{i,j}$ = mole fraction of component i at location j (dimensionless)
- $X$ = fractional conversion of limiting reactant (dimensionless)
- $a$ = stoichiometric coefficient of product (dimensionless)
- $\text{purge}$ = fraction of stream 5 that is purged (dimensionless)
```

### Overall System Analysis

```{note}
**Degrees of Freedom Analysis:** For a system with n components and 4 units, the total number of unknowns equals the number of independent material balance equations. Additional specifications (conversion, purge fraction, separator efficiency) reduce the degrees of freedom to zero for a solvable system.
```

### Worked Examples

```{prf:example} Haber Process - Conceptual Analysis

The Haber process reaction: $\text{N}_2 + 3\text{H}_2 \rightarrow 2\text{NH}_3$

A fresh feed containing stoichiometric amounts of reactants plus inert gas combines with recycle. The reactor achieves 15% conversion of nitrogen. Products enter a separator that removes all ammonia. If reactor feed is 10 mol/s with 20% inert and remaining N₂ and H₂ in stoichiometric proportions, find the necessity for a purge stream.
```

```{dropdown} Solution Steps

**Step 1: Define basis and analyze reactor feed composition:**

Reactor feed = 10 mol/s total

Inert = 20% = 2 mol/s

Remaining 8 mol/s contains N₂ and H₂ in stoichiometric ratio (1:3)

Therefore: N₂ = 2 mol/s, H₂ = 6 mol/s

**Step 2: Calculate reactor outlet composition:**

With 15% conversion of N₂:

N₂ converted = $0.15 \times 2 = 0.3$ mol/s

N₂ remaining = $2 - 0.3 = 1.7$ mol/s

H₂ consumed = $3 \times 0.3 = 0.9$ mol/s

H₂ remaining = $6 - 0.9 = 5.1$ mol/s

NH₃ produced = $2 \times 0.3 = 0.6$ mol/s

Inert unchanged = 2 mol/s

**Step 3: Analyze steady-state feasibility without purge:**

After separator: NH₃ removed completely

Recycle stream contains: 1.7 mol/s N₂, 5.1 mol/s H₂, 2 mol/s inert

For steady state, fresh feed must contain zero inert to balance the system

However, problem states fresh feed contains inert gas

**Conclusion: System cannot reach steady state without purge**

**Step 4: Solution with purge stream:**

Adding a purge stream (e.g., 25% of separator outlet) allows:

- Removal of excess inert from the system
- Fresh feed can contain inert gas
- System achieves steady-state operation
```

```{prf:example} Haber Process – NH₃ Production

- Fresh feed: 74.775 mol/s H₂, 24.925 mol/s N₂, 0.30 mol/s Ar
- 40% of N₂ converted to NH₃
- Separator removes all NH₃; others exit unaltered
- 1% purge before recycle

**Find:** NH₃ production rate
```

```{dropdown} Solution Steps

**Step 1: Setup:** 17 unknowns (flow rates across 7 locations), 17 equations (mass balances + specs).

Given: $X = 0.40$, purge = 0.01

**Step 2: Mixer (1 + 7 → 2):**

$$
\dot{m}_{i,1} + \dot{m}_{i,7} = \dot{m}_{i,2}, \quad i = \mathrm{H_2, N_2, Ar}
$$

**Step 3: Reactor (2 → 3):**

$$
\begin{align}
\dot{m}_{NH_3,3} &= 2 \times 0.40 \times \dot{m}_{N_2,2} \\
\dot{m}_{N_2,3} &= 0.60 \times \dot{m}_{N_2,2} \\
\dot{m}_{H_2,3} &= \dot{m}_{H_2,2} - 3 \times 0.40 \times \dot{m}_{N_2,2} \\
\dot{m}_{Ar,3} &= \dot{m}_{Ar,2}
\end{align}
$$

**Step 4: Separator + Split:**

Stream 3 → NH₃ to 4, others to 5

Stream 5: 1% purge (6), 99% recycle (7)

**Step 5: Solution:**

Use Excel Solver or similar to solve 17 linear equations.

**Step 6: Result:** NH₃ production = **19.94 mol/s**

**Step 7: Check:** Atom balances: N, H (NH₃ + purge); Ar (purge only)
```

### Problem-Solving Strategy

```{note}
**Systematic Approach for Reactor-Recycle-Purge Systems:**

1. Draw complete process flow diagram with all streams labeled
2. Identify all unknown flow rates and compositions
3. Count degrees of freedom (unknowns vs. independent equations)
4. Write material balances for each unit operation
5. Apply process specifications (conversion, separation efficiency, purge fraction)
6. Solve system of equations (often requires computational tools for complex systems)
7. Verify solution using overall atomic balances
```

```{admonition} Common Mistakes to Avoid
:class: warning

- Forgetting that total material balances are not independent of component balances
- Not accounting for stoichiometric relationships in reactor balances
- Assuming equal compositions in recycle and purge streams at splitting points
- Neglecting the necessity of purge streams for inert species
- Using overall atomic balances as independent equations in the solution process
```

```{caution}
**PE Exam Traps — Combustion Calculations**

- **Excess air vs. excess oxygen:** Always compute theoretical O₂ first, then convert to air using 21 mol% O₂. Applying the excess percentage directly to O₂ moles is correct; applying it to air gives the same answer — but mixing these up when air composition is unusual (problem gives 20% O₂) is a trap.
- **Incomplete combustion products:** If the problem says "incomplete combustion" or gives a CO:CO₂ ratio, do NOT assume all C → CO₂. Use an atomic C balance instead.
- **Water phase in flue gas:** At stack conditions, water is typically vapor. Don't use liquid water properties in a combustion gas composition calculation.
```

## Introduction to Energy Balances

```{note}
While material balances track the flow of mass, **energy balances** track the flow of energy based on the **First Law of Thermodynamics**, which states that energy is conserved. For chemical engineers, this typically involves analyzing heat transfer and the energy changes associated with temperature changes or phase transitions.

The fundamental principle: Energy can neither be created nor destroyed, only converted from one form to another.
```

Energy balances are essential for:

- Sizing heating and cooling equipment
- Determining utility requirements (steam, cooling water)
- Analyzing heat exchanger performance
- Optimizing energy efficiency in processes
- Safety analysis and temperature control

## The First Law for Open, Steady-State Systems

For chemical engineering systems where material flows continuously in and out at steady rates, we apply the First Law of Thermodynamics in its most general form.

```{important}
**General Energy Balance for Open, Steady-State Systems:**

$$
\Delta \dot{H} + \Delta \dot{E}_k + \Delta \dot{E}_p = \dot{Q} - \dot{W}_s
$$

This equation states that the rate of energy accumulation in all forms equals the net rate of energy input to the system.
```

```{admonition} Energy Balance Terms
:class: tip

- $\Delta \dot{H}$ = Rate of enthalpy change $(\dot{H}_{out} - \dot{H}_{in})$ [kW or kJ/s]
- $\Delta \dot{E}_k$ = Rate of kinetic energy change [kW or kJ/s]
- $\Delta \dot{E}_p$ = Rate of potential energy change [kW or kJ/s]
- $\dot{Q}$ = Rate of heat transfer **to** the system [kW or kJ/s]
- $\dot{W}_s$ = Rate of shaft work done **by** the system [kW or kJ/s]
- $\hat{h}$ = Specific enthalpy (enthalpy per unit mass) [kJ/kg]
- $\dot{m}$ = Mass flow rate [kg/s]

**Sign Conventions:**

- $\dot{Q} > 0$: Heat added to system; $\dot{Q} < 0$: Heat removed from system
- $\dot{W}_s > 0$: Work done by system (turbine); $\dot{W}_s < 0$: Work done on system (pump)
```

### Simplified Energy Balance

For many common chemical engineering applications (heat exchangers, reactors, pipes), the kinetic and potential energy changes are negligible compared to enthalpy changes, and no shaft work is involved.

```{important}
**Simplified Energy Balance (Most Common Form):**

$$
\dot{Q} = \Delta \dot{H} = \dot{m}(\hat{h}_{out} - \hat{h}_{in})
$$

This form is applicable when:

- $\Delta \dot{E}_k \approx 0$ (low velocities)
- $\Delta \dot{E}_p \approx 0$ (small elevation changes)
- $\dot{W}_s = 0$ (no pumps, turbines, or compressors)
```

## Worked Example: Steam Heat Exchanger Analysis

```{prf:example} Energy Balance on Steam Heat Exchanger

**Problem:** Superheated steam at 10 bar and 200°C flows at 2.0 kg/s through a heat exchanger. Steam heats reactor feed, and 450 kJ/s (450 kW) of heat is removed from steam. Determine outlet temperature, phase, and final specific enthalpy.
```

```{dropdown} Solution Steps

**Step 1: Set Up Energy Balance**

System: Steam flowing through heat exchanger

Heat removed: $\dot{Q} = -450$ kW (negative because removed)

$\dot{Q} = \dot{m}(\hat{h}_{out} - \hat{h}_{in}) \Rightarrow -450 = (2.0)(\hat{h}_{out} - \hat{h}_{in})$

**Step 2: Find Inlet Specific Enthalpy**

From superheated steam tables at 10 bar and 200°C:

$\hat{h}_{in} = 2828$ kJ/kg

**Step 3: Calculate Outlet Specific Enthalpy**

$\hat{h}_{out} = \hat{h}_{in} + \frac{\dot{Q}}{\dot{m}} = 2828 + \frac{-450}{2.0} = 2828 - 225 = 2603$ kJ/kg

**Step 4: Determine Outlet Phase**

Compare $\hat{h}_{out}$ to saturation properties at 10 bar:

$\hat{h}_f = 762.5$ kJ/kg (saturated liquid)

$\hat{h}_g = 2777.1$ kJ/kg (saturated vapor)

Since $762.5 < 2603 < 2777.1$: **Two-phase mixture (wet steam)**

Temperature = saturation temperature at 10 bar = 179.9°C

**Step 5: Calculate Quality (Vapor Fraction)**

For two-phase mixture: $\hat{h}_{out} = x\hat{h}_g + (1-x)\hat{h}_f$

$2603 = x(2777.1) + (1-x)(762.5) = 2014.6x + 762.5$

$x = \frac{2603 - 762.5}{2014.6} = 0.914 = 91.4\%$ vapor
```

## Sensible and Latent Heat

Energy transfer in chemical processes can result in either temperature changes or phase changes, requiring different calculation approaches.

```{note}
**Two Types of Heat Transfer:**

- **Sensible Heat:** Causes temperature change with no phase change
- **Latent Heat:** Causes phase change at constant temperature

Understanding this distinction is crucial for accurate energy balance calculations, especially for systems involving boiling, condensation, melting, or freezing.
```

### Sensible Heat Calculations

```{important}
**Sensible Heat Transfer:**

$$
Q_s = mc_p\Delta T
$$

**For continuous processes:**

$$
\dot{Q}_s = \dot{m}c_p\Delta T
$$

where:

- $c_p$ = specific heat capacity at constant pressure [kJ/kg·K]
- $\Delta T$ = temperature change [K or °C]
- Note: $\Delta T$ in Kelvin equals $\Delta T$ in Celsius
```

### Latent Heat Calculations

```{important}
**Latent Heat Transfer (Phase Change):**

$$
Q_L = n\Delta H_{\text{phase change}}
$$

**For continuous processes:**

$$
\dot{Q}_L = \dot{n}\Delta H_{\text{phase change}}
$$

**Common Phase Changes:**

- Vaporization: $\Delta H_{vap} > 0$ (liquid → vapor)
- Condensation: $\Delta H_{cond} = -\Delta H_{vap} < 0$ (vapor → liquid)
- Fusion (melting): $\Delta H_{fus} > 0$ (solid → liquid)
- Freezing: $\Delta H_{freeze} = -\Delta H_{fus} < 0$ (liquid → solid)
```

```{admonition} Important Properties for Water
:class: tip

- $\Delta H_{vap}$ (water at 100°C) = 40.6 kJ/mol = 2257 kJ/kg
- $\Delta H_{fus}$ (water at 0°C) = 6.01 kJ/mol = 334 kJ/kg
- $c_{p,steam}$ = 2.01 kJ/kg·K
- $c_{p,water}$ = 4.184 kJ/kg·K
- $c_{p,ice}$ = 2.09 kJ/kg·K
- Molecular weight of water = 18.015 g/mol
```

## Multi-Step Energy Balance Example

```{prf:example} Cooling Steam to Ice

**Problem:** Calculate heat required to convert 45 g steam at 150°C to ice at -80°C.

**Given:**

- $\Delta H_{vap}$ (water) = 40.6 kJ/mol
- $\Delta H_{fus}$ (water) = 6.01 kJ/mol
- $c_{steam} = 2.01$ kJ/kg·K, $c_{water} = 4.184$ kJ/kg·K, $c_{ice} = 2.09$ kJ/kg·K
```

```{admonition} Process Path Analysis
:class: tip

1. Cool steam: 150°C → 100°C (sensible)
2. Condense steam → liquid at 100°C (latent)
3. Cool water: 100°C → 0°C (sensible)
4. Freeze water → ice at 0°C (latent)
5. Cool ice: 0°C → -80°C (sensible)

**Unit Conversions:**

- Mass: $m = 45$ g = 0.045 kg
- Moles: $n = 45/18.015 = 2.50$ mol
```

```{dropdown} Solution Steps

**Step 1: Calculate Each Heat Transfer Step**

$Q_{total} = Q_1 + Q_2 + Q_3 + Q_4 + Q_5$

**Step 2: Step 1: Cool Steam (150°C → 100°C)**

$Q_1 = mc_{steam}\Delta T = (0.045)(2.01)(100-150) = -4.52$ kJ

**Step 3: Step 2: Condense Steam at 100°C**

$Q_2 = n(-\Delta H_{vap}) = (2.50)(-40.6) = -101.5$ kJ

**Step 4: Step 3: Cool Water (100°C → 0°C)**

$Q_3 = mc_{water}\Delta T = (0.045)(4.184)(0-100) = -18.83$ kJ

**Step 5: Step 4: Freeze Water at 0°C**

$Q_4 = n(-\Delta H_{fus}) = (2.50)(-6.01) = -15.03$ kJ

**Step 6: Step 5: Cool Ice (0°C → -80°C)**

$Q_5 = mc_{ice}\Delta T = (0.045)(2.09)(-80-0) = -7.52$ kJ

**Step 7: Sum Total Heat Transfer**

$Q_{total} = -4.52 - 101.5 - 18.83 - 15.03 - 7.52 = -147.4$ kJ
```

```{note}
**Final Answer**

A total of **147.4 kJ** of heat must be removed to convert 45 g of steam at 150°C to ice at -80°C.

The negative sign indicates heat removal from the system.
```

## Energy Balances with Phase Change

Many industrial processes, such as condensation, evaporation, and distillation, involve phase changes. Calculating energy requirements for these processes requires accounting for both sensible heat (temperature change) and latent heat (phase change).

### State Functions and Hypothetical Paths

```{note}
**State Function Property**

Enthalpy ($\hat{H}$) is a **state function**, meaning the change in enthalpy ($\Delta \hat{H}$) between two states depends only on initial and final conditions, not on the path taken. This allows us to construct convenient, hypothetical paths to calculate $\Delta \hat{H}$ when direct calculation is difficult.
```

```{admonition} Hypothetical Path Strategy
:class: tip

Break complex processes into simpler steps:

1. Sensible heat change to saturation point (boiling/condensation)
2. Latent heat change for phase transition at constant temperature
3. Sensible heat change to final temperature

**Total Change:** $\Delta \hat{H}_{total} = \Delta \hat{H}_1 + \Delta \hat{H}_2 + \Delta \hat{H}_3 + \cdots$
```

### Calculating Enthalpy Changes

```{important}
**Enthalpy Change Calculations**

**Sensible Heat (Temperature Change):**

$$
\Delta \hat{H} = \int_{T_1}^{T_2} C_p(T) \,dT
$$

where $C_p$ is often given as: $C_p = A + BT + CT^2 + DT^3$

**Latent Heat (Phase Change):**

$$
\Delta \hat{H}_{\text{vaporization}} = -\Delta \hat{H}_{\text{condensation}}
$$
```

```{prf:example} Energy Balance on Acetone Condenser

**Problem:** Calculate cooling duty ($\dot{Q}$) to condense and cool 100 mol/s acetone from vapor at 100°C to liquid at 25°C at 1 atm.

**Given:**

- $\Delta \hat{H}_{vap}$ = 30.2 kJ/mol at normal boiling point (56°C)
- Acetone vapor: $C_p = 0.07196 + 20.10 \times 10^{-5}T - 12.78 \times 10^{-8}T^2 + 34.76 \times 10^{-12}T^3$
- Acetone liquid: $C_p = 0.123 + 18.6 \times 10^{-5}T$
- ($C_p$ in kJ/mol·°C, $T$ in °C)
```

```{note}
**Solution Strategy**

Construct three-step hypothetical path from initial state (vapor, 100°C) to final state (liquid, 25°C). Use energy balance: $\dot{Q} = \Delta \dot{H} = \dot{n} \Delta \hat{H}_{total}$
```

```{admonition} Hypothetical Path Definition
:class: tip

1. $\Delta \hat{H}_1$: Cool acetone vapor 100°C → 56°C (sensible)
2. $\Delta \hat{H}_2$: Condense vapor → liquid at 56°C (latent)
3. $\Delta \hat{H}_3$: Cool liquid 56°C → 25°C (sensible)
```

```{dropdown} Solution Steps

**Step 1: Calculate $\Delta \hat{H}_1$ (Vapor Cooling)**

$\Delta \hat{H}_1 = \int_{100}^{56} C_{p,vapor}(T) \,dT$

$= \int_{100}^{56} (0.07196 + 20.10 \times 10^{-5}T - 12.78 \times 10^{-8}T^2 + 34.76 \times 10^{-12}T^3) \,dT$

Evaluating the integral: $\Delta \hat{H}_1 = -3.82$ kJ/mol

**Step 2: Calculate $\Delta \hat{H}_2$ (Condensation)**

Condensation is opposite of vaporization:

$\Delta \hat{H}_2 = -\Delta \hat{H}_{vap} = -30.2$ kJ/mol

**Step 3: Calculate $\Delta \hat{H}_3$ (Liquid Cooling)**

$\Delta \hat{H}_3 = \int_{56}^{25} C_{p,liquid}(T) \,dT$

$= \int_{56}^{25} (0.123 + 18.6 \times 10^{-5}T) \,dT$

Evaluating the integral: $\Delta \hat{H}_3 = -4.06$ kJ/mol

**Step 4: Calculate Total Cooling Duty**

$\Delta \hat{H}_{total} = (-3.82) + (-30.2) + (-4.06) = -38.08$ kJ/mol

$\dot{Q} = \dot{n} \Delta \hat{H}_{total} = (100)(-38.08) = -3808$ kJ/s
```

```{important}
**Final Answer**

Required cooling duty: **3808 kW**

The negative sign confirms heat is being removed from the system.
```

```{caution}
**PE Exam Traps — Energy Balances**

- **Sign convention:** $\dot{Q} > 0$ means heat **added to** the system. If steam exits a heat exchanger cooler than it entered, $\dot{Q}$ for the steam side is **negative** — the steam is the hot fluid losing energy.
- **Steam tables vs. $c_p \Delta T$:** For water and steam, always prefer steam tables over $c_p \Delta T$ — $c_p$ for steam varies significantly with temperature and pressure. Only use $c_p \Delta T$ when steam tables are unavailable or for ideal gas approximations.
- **Two-phase region:** If $\hat{h}_f < \hat{h}_{out} < \hat{h}_g$, the outlet is a wet mixture — don't report a temperature as if it's superheated. Report the saturation temperature plus the quality $x$.
- **Sensible + latent sequencing:** When cooling a superheated gas through condensation to a subcooled liquid, you must use **three separate steps**: (1) sensible cool to dew point, (2) condense at constant T, (3) sensible cool liquid. Applying a single average $c_p$ across the phase transition gives a wrong answer.
```

## Energy Balances on Reactive Systems

When a chemical reaction occurs, energy is either released (exothermic reaction) or consumed (endothermic reaction). To determine the overall heating or cooling requirement for a reactor ($\dot{Q}$), we must account for both enthalpy changes due to temperature differences (sensible heat) and the enthalpy change from the reaction itself.

```{note}
**Reactive System Energy Balance Principle**

Reactive systems require accounting for two distinct energy effects:

1. Energy change from the chemical reaction itself
2. Sensible heat changes due to temperature differences between inlet and outlet streams

The total energy requirement is the sum of these effects.
```

### The Heat of Reaction Method

```{note}
**Heat of Reaction Method Strategy**

Separate the overall enthalpy change into two distinct parts:

1. Enthalpy change from chemical reaction at standard reference state
2. Sensible heat changes to bring reactants from inlet to reference state, and products from reference state to outlet conditions
```

```{important}
**Energy Balance for Steady-State Reactor**

$$
\dot{Q} = \Delta \dot{H} = \dot{\xi} \Delta \hat{H}_{rxn}^\circ + \sum_{\text{out}} \dot{n}_i \hat{h}_i - \sum_{\text{in}} \dot{n}_i \hat{h}_i
$$

**Reference State:** Molecular species at 25°C and 1 atm
```

```{admonition} Variable Definitions
:class: tip

- $\dot{Q}$: Rate of heat transfer to reactor (+) or from reactor (-)
- $\dot{\xi}$: Extent of reaction (mol/time) from material balance
- $\Delta \hat{H}_{rxn}^\circ$: Standard heat of reaction (kJ/mol) at reference state
- $\dot{n}_i$: Molar flow rate of species $i$ in inlet/outlet streams
- $\hat{h}_i$: Specific enthalpy of species $i$ relative to reference state
```

### Calculating Standard Heat of Reaction

```{important}
**Standard Heat of Reaction Calculation**

$$
\Delta \hat{H}_{rxn}^\circ = \sum_{\text{products}} |\nu_i| \Delta \hat{H}_{f,i}^\circ - \sum_{\text{reactants}} |\nu_i| \Delta \hat{H}_{f,i}^\circ
$$

where:

- $\nu_i$: Stoichiometric coefficient of species $i$
- $\Delta \hat{H}_{f,i}^\circ$: Standard heat of formation of species $i$
- $\Delta \hat{H}_{f}^\circ = 0$ for elemental species ($O_2$, $H_2$, $N_2$, C(graphite))
```

```{note}
**Standard Heat of Formation Definition**

The standard heat of formation ($\Delta \hat{H}_{f}^\circ$) is the enthalpy change when one mole of a substance is formed from its constituent elements in their standard state at 25°C and 1 atm.
```

```{prf:example} Water-Gas Shift Reactor Energy Balance

**Problem:** In the water-gas shift reaction, CO reacts with steam to produce $CO_2$ and $H_2$. Feed enters at 300°C, product exits at 500°C. Feed: 1.0 mol CO with 50% excess steam. CO conversion: 80%. Determine reactor heat duty ($\dot{Q}$).

**Reaction:** $CO(g) + H_2O(g) \rightarrow CO_2(g) + H_2(g)$
```

```{dropdown} Solution Steps

**Step 1: Material Balance - Find Extent of Reaction**

**Feed composition:**
- CO: 1.0 mol
- $H_2O$: Stoichiometric (1.0 mol) + 50% excess = 1.5 mol

**CO conversion:** $1.0 \times 0.80 = 0.8$ mol reacted

**Extent of reaction:** $\xi = 0.8$ mol (stoichiometric coefficient of CO = -1)

**Step 2: Calculate Outlet Molar Flow Rates**

Using $\dot{n}_{out} = \dot{n}_{in} + \nu\xi$:

$\dot{n}_{CO} = 1.0 - (1)(0.8) = 0.2$ mol

$\dot{n}_{H_2O} = 1.5 - (1)(0.8) = 0.7$ mol

$\dot{n}_{CO_2} = 0 + (1)(0.8) = 0.8$ mol

$\dot{n}_{H_2} = 0 + (1)(0.8) = 0.8$ mol

**Step 3: Compile Enthalpy Data**

Reference: Molecular species at 25°C, 1 atm. Specific enthalpies from ideal gas tables:

| Species | $\dot{n}_{in}$ (mol) | $\hat{h}_{in}$ (kJ/mol) at 300°C | $\dot{n}_{out}$ (mol) | $\hat{h}_{out}$ (kJ/mol) at 500°C |
|---------|---------------------|----------------------------------|----------------------|----------------------------------|
| CO | 1.0 | 8.17 | 0.2 | 14.38 |
| $H_2O$ | 1.5 | 9.57 | 0.7 | 17.01 |
| $CO_2$ | 0 | - | 0.8 | 21.34 |
| $H_2$ | 0 | - | 0.8 | 13.82 |

**Step 4: Calculate Standard Heat of Reaction**

**Standard heats of formation (kJ/mol):**
- $\Delta \hat{H}_{f,CO}^\circ = -110.53$
- $\Delta \hat{H}_{f,H_2O(g)}^\circ = -241.83$
- $\Delta \hat{H}_{f,CO_2}^\circ = -393.5$
- $\Delta \hat{H}_{f,H_2}^\circ = 0$

$\Delta \hat{H}_{rxn}^\circ = [\Delta \hat{H}_{f,CO_2}^\circ + \Delta \hat{H}_{f,H_2}^\circ] - [\Delta \hat{H}_{f,CO}^\circ + \Delta \hat{H}_{f,H_2O}^\circ]$

$= [-393.5 + 0] - [-110.53 + (-241.83)]$

$= -393.5 - (-352.36) = -41.14$ kJ/mol

**Step 5: Calculate Sensible Heat Terms**

$\sum_{\text{in}} \dot{n}_i \hat{h}_i = (1.0)(8.17) + (1.5)(9.57) = 8.17 + 14.36 = 22.53$ kJ

$\sum_{\text{out}} \dot{n}_i \hat{h}_i = (0.2)(14.38) + (0.7)(17.01) + (0.8)(21.34) + (0.8)(13.82)$

$= 2.88 + 11.91 + 17.07 + 11.06 = 42.92$ kJ

**Step 6: Calculate Total Heat Duty**

$Q = \xi \Delta \hat{H}_{rxn}^\circ + \sum_{\text{out}} \dot{n}_i \hat{h}_i - \sum_{\text{in}} \dot{n}_i \hat{h}_i$

$= (0.8)(-41.14) + (42.92) - (22.53)$

$= -32.91 + 20.39 = -12.52$ kJ
```

```{important}
**Final Answer**

**Reactor Heat Duty:** -12.5 kJ

The negative sign indicates the reaction is exothermic - this amount of heat must be removed to maintain the specified outlet temperature.
```

```{note}
**Key Reactive System Energy Balance Principles**

**Problem-Solving Strategy:**

1. Complete material balance first to find extent of reaction
2. Use standard reference state (25°C, 1 atm) for all enthalpy calculations
3. Calculate standard heat of reaction from heats of formation
4. Account for sensible heat changes separately from reaction enthalpy
5. Apply proper sign conventions: exothermic reactions have negative $\Delta \hat{H}_{rxn}^\circ$

**Sign Conventions:**

- Heat added to reactor: positive (+)
- Heat removed from reactor: negative (-)
- Exothermic reaction: negative $\Delta \hat{H}_{rxn}^\circ$
- Endothermic reaction: positive $\Delta \hat{H}_{rxn}^\circ$

**Critical Data Sources:**

- Standard heats of formation from thermodynamic tables
- Specific enthalpies from ideal gas property tables
- Reference state consistency is essential for accuracy
```

## Energy Balances on Reactive Systems (Continued)

In the previous section, we introduced the Heat of Reaction method. Here, we explore an alternative approach - the Heat of Formation method - which leads to identical results through a different conceptual path. We will also learn how to calculate heats of reaction at temperatures other than the standard 25°C.

### The Heat of Formation Method

```{note}
**Heat of Formation Method Principle**

This method calculates total enthalpy change by determining the absolute enthalpy of each component in inlet and outlet streams relative to a common baseline. The energy balance becomes a simple subtraction of total outlet and inlet enthalpies.
```

```{admonition} Reference State Definition
:class: tip

Constituent elements of each species in their standard form at 25°C and 1 atm:

- Carbon: C(s) - solid graphite
- Hydrogen: $H_2$(g) - gaseous hydrogen
- Oxygen: $O_2$(g) - gaseous oxygen
- Nitrogen: $N_2$(g) - gaseous nitrogen
```

```{important}
**Absolute Enthalpy Calculation**

$$
\hat{H}_i(T) = \Delta \hat{H}_{f,i}^\circ + \Delta \hat{h}_i = \Delta \hat{H}_{f,i}^\circ + \int_{25^\circ C}^{T} C_p(T) \,dT
$$

**Simplified Energy Balance:**

$$
\dot{Q} = \Delta \dot{H} = \sum_{\text{out}} \dot{n}_i \hat{H}_i - \sum_{\text{in}} \dot{n}_i \hat{H}_i
$$

The reaction term is implicitly included in the absolute enthalpies.
```

```{prf:example} Water-Gas Shift Reactor (Heat of Formation Method)

**Problem:** Re-solve the previous water-gas shift example using Heat of Formation method to demonstrate equivalency. CO and $H_2O$ enter at 300°C, products leave at 500°C. Feed: 1.0 mol CO, 1.5 mol $H_2O$. CO conversion: 80%.

**Reaction:** $CO(g) + H_2O(g) \rightarrow CO_2(g) + H_2(g)$
```

```{dropdown} Solution Steps

**Step 1: Material Balance (Identical to Previous Example)**

**Inlet streams:** 1.0 mol CO, 1.5 mol $H_2O$

**Outlet streams:** 0.2 mol CO, 0.7 mol $H_2O$, 0.8 mol $CO_2$, 0.8 mol $H_2$

**Step 2: Calculate Absolute Enthalpies**

Reference: C(s), $H_2$(g), $O_2$(g) at 25°C, 1 atm

Formula: $\hat{H} = \Delta \hat{H}_{f}^\circ + \Delta \hat{h}$

| Species | $\Delta \hat{H}_{f}^\circ$ (kJ/mol) | $\Delta \hat{h}_{in}$ (300°C) (kJ/mol) | $\hat{H}_{in}$ (total) (kJ/mol) | $\Delta \hat{h}_{out}$ (500°C) (kJ/mol) | $\hat{H}_{out}$ (total) (kJ/mol) |
|---------|-------------------------------------|----------------------------------------|--------------------------------|-----------------------------------------|----------------------------------|
| CO | -110.53 | 8.17 | -102.36 | 14.38 | -96.15 |
| $H_2O$ | -241.83 | 9.57 | -232.26 | 17.01 | -224.82 |
| $CO_2$ | -393.5 | - | - | 21.34 | -372.16 |
| $H_2$ | 0 | - | - | 13.82 | 13.82 |

**Step 3: Calculate Inlet Enthalpy Sum**

$\sum_{\text{in}} \dot{n}_i \hat{H}_i = (1.0)(-102.36) + (1.5)(-232.26)$

$= -102.36 - 348.39 = -450.75$ kJ

**Step 4: Calculate Outlet Enthalpy Sum**

$\sum_{\text{out}} \dot{n}_i \hat{H}_i = (0.2)(-96.15) + (0.7)(-224.82) + (0.8)(-372.16) + (0.8)(13.82)$

$= -19.23 - 157.37 - 297.73 + 11.06 = -463.27$ kJ

**Step 5: Calculate Heat Duty**

$Q = \sum_{\text{out}} \dot{n}_i \hat{H}_i - \sum_{\text{in}} \dot{n}_i \hat{H}_i$

$= (-463.27) - (-450.75) = -12.52$ kJ
```

```{important}
**Method Comparison Result**

**Heat Duty:** -12.5 kJ

This is identical to the Heat of Reaction method result, demonstrating that both approaches are mathematically equivalent.
```

### Effect of Temperature on Heat of Reaction

```{note}
**Temperature-Dependent Heat of Reaction**

The standard heat of reaction ($\Delta \hat{H}_{rxn}^\circ$) is defined at 25°C. To find the heat of reaction at different temperatures, we use a hypothetical path based on Hess's Law.
```

```{important}
**Temperature Correction for Heat of Reaction**

$$
\Delta \hat{H}_{rxn}(T) = \Delta \hat{H}_{rxn}^\circ (298K) + \int_{298K}^{T} \Delta C_p \,dT
$$

where $\Delta C_p$ is the change in heat capacity for the reaction:

$$
\Delta C_p = \sum_{\text{products}} |\nu_i| C_{p,i} - \sum_{\text{reactants}} |\nu_i| C_{p,i}
$$
```

```{prf:example} Heat of Reaction at Elevated Temperature

**Problem:** Calculate the heat of reaction at 600 K for hydrazine decomposition.

**Reaction:** $N_2H_4(g) \rightarrow N_2(g) + 2H_2(g)$

**Given:** $\Delta \hat{H}_{f,N_2H_4}^\circ = +95.35$ kJ/mol

Heat capacity: $C_P = A + BT + CT^2 + DT^3$ (J/mol·K)
```

```{dropdown} Solution Steps

**Step 1: Calculate Standard Heat of Reaction at 298 K**

$\Delta \hat{H}_{rxn}^\circ = [\Delta \hat{H}_{f,N_2}^\circ + 2\Delta \hat{H}_{f,H_2}^\circ] - [\Delta \hat{H}_{f,N_2H_4}^\circ]$

Since $N_2$ and $H_2$ are elements in standard state: $\Delta \hat{H}_{f}^\circ = 0$

$\Delta \hat{H}_{rxn}^\circ = [0 + 2(0)] - [95.35] = -95.35$ kJ/mol

**Step 2: Calculate $\Delta C_p$ as Function of Temperature**

$\Delta C_p = [C_{p,N_2} + 2C_{p,H_2}] - [C_{p,N_2H_4}]$

Substitute heat capacity polynomials for each species to get $\Delta C_p(T)$

**Step 3: Integrate $\Delta C_p$ for Temperature Correction**

$\int_{298K}^{600K} \Delta C_p \,dT$

Using spreadsheet integration or numerical methods:

$\int_{298K}^{600K} \Delta C_p \,dT \approx +6.65$ kJ/mol

**Step 4: Calculate Heat of Reaction at 600 K**

$\Delta \hat{H}_{rxn}(600K) = \Delta \hat{H}_{rxn}^\circ (298K) + \int_{298K}^{600K} \Delta C_p \,dT$

$= -95.35 + 6.65 = -88.7$ kJ/mol
```

```{important}
**Temperature Effect Result**

**Heat of Reaction at 600 K:** -88.7 kJ/mol

The reaction is slightly less exothermic at higher temperature due to the positive temperature correction.
```

```{note}
**Key Reactive System Energy Balance Methods**

**Method Comparison:**

**Heat of Reaction Method:**

- Uses standard heat of reaction plus sensible heat corrections
- Reference: molecular species at 25°C, 1 atm
- Separates reaction and temperature effects explicitly

**Heat of Formation Method:**

- Uses absolute enthalpies referenced to constituent elements
- Reference: elements in standard state at 25°C, 1 atm
- Reaction effects included implicitly in formation enthalpies

**Temperature Effects:**

- Heat of reaction varies with temperature due to different heat capacities
- Use Kirchhoff's equation with $\Delta C_p$ integration
- Generally small corrections unless temperature differences are large

Both methods yield identical results when applied correctly.
```

---

## PE Exam Practice Problems

The following problems are written in the style of NCEES PE exam questions. Try each problem before opening the solution.

---

```{prf:example} Practice Problem 1 — Flash Drum with Recycle (Material Balance)

A process feed of 500 kg/h containing 30 wt% toluene and 70 wt% benzene enters a flash drum. The overhead vapor is 80 wt% benzene and is completely condensed. Half of the condensate is returned to the drum as reflux; the other half is withdrawn as overhead product. The bottoms liquid from the drum is 15 wt% benzene.

**(a)** What is the overhead product flow rate (kg/h)?

**(b)** What is the bottoms flow rate (kg/h)?
```

```{dropdown} Solution

**Step 1: Define streams and unknowns**

Let:
- $F = 500$ kg/h (feed), $z_B = 0.30$ (toluene fraction in feed), so benzene in feed = 0.70
- $D$ = overhead product (kg/h), $B$ = bottoms (kg/h)
- Vapor overhead: $y_{benz} = 0.80$, so toluene fraction = 0.20
- Bottoms: $x_{benz} = 0.15$, toluene fraction = 0.85

Note: the reflux is internal to the drum — it does NOT cross the overall system boundary. So the overall balance only involves F, D, and B.

**Step 2: Overall mass balance**

$$F = D + B \implies 500 = D + B \quad (1)$$

**Step 3: Overall benzene balance**

$$F \cdot 0.70 = D \cdot 0.80 + B \cdot 0.15$$

$$350 = 0.80D + 0.15B \quad (2)$$

**Step 4: Solve simultaneously**

From (1): $B = 500 - D$. Substitute into (2):

$$350 = 0.80D + 0.15(500-D) = 0.80D + 75 - 0.15D = 0.65D + 75$$

$$D = \frac{275}{0.65} = 423.1 \text{ kg/h}$$

$$B = 500 - 423.1 = 76.9 \text{ kg/h}$$

**Answers:** (a) $D \approx \mathbf{423}$ **kg/h**, (b) $B \approx \mathbf{77}$ **kg/h**

**Verification (toluene balance):** In: $500 \times 0.30 = 150$ kg/h. Out: $423.1 \times 0.20 + 76.9 \times 0.85 = 84.6 + 65.4 = 150$ kg/h ✓
```

---

```{prf:example} Practice Problem 2 — Reactor with Purge (Material + Energy)

Ethylene oxide ($\text{C}_2\text{H}_4\text{O}$) is produced by partial oxidation of ethylene over a silver catalyst:

$$\text{C}_2\text{H}_4 + \tfrac{1}{2}\,\text{O}_2 \rightarrow \text{C}_2\text{H}_4\text{O} \qquad \Delta\hat{H}_{rxn}^\circ = -105 \text{ kJ/mol}$$

A side reaction also occurs:

$$\text{C}_2\text{H}_4 + 3\,\text{O}_2 \rightarrow 2\,\text{CO}_2 + 2\,\text{H}_2\text{O} \qquad \Delta\hat{H}_{rxn}^\circ = -1323 \text{ kJ/mol}$$

Fresh feed: 100 mol/h C₂H₄ and 150 mol/h O₂. Per pass through the reactor, 30% of C₂H₄ reacts; selectivity to ethylene oxide (moles EO produced per mole C₂H₄ converted) is 0.75.

**(a)** What is the molar production rate of ethylene oxide (mol/h)?

**(b)** What is the total heat that must be removed from the reactor (kW), assuming inlet and outlet are both at 25°C?
```

```{dropdown} Solution

**Step 1: Extent of each reaction**

Basis: 100 mol/h C₂H₄ feed to reactor (assume once-through for this problem, no recycle specified).

C₂H₄ converted per pass: $100 \times 0.30 = 30$ mol/h

Selectivity = 0.75, so:
- Moles EO produced: $30 \times 0.75 = 22.5$ mol/h → $\xi_1 = 22.5$ mol/h (main reaction)
- Moles via combustion: $30 \times 0.25 = 7.5$ mol/h → $\xi_2 = 7.5$ mol/h (side reaction)

**(a) Ethylene oxide production rate: $\mathbf{22.5}$ mol/h**

**Step 2: Heat removed from reactor (Part b)**

Since both inlet and outlet are at 25°C (standard state), only the heat of reaction contributes:

$$\dot{Q} = \xi_1 \Delta\hat{H}_{rxn,1}^\circ + \xi_2 \Delta\hat{H}_{rxn,2}^\circ$$

$$\dot{Q} = (22.5)(-105) + (7.5)(-1323)$$

$$\dot{Q} = -2362.5 + (-9922.5) = -12{,}285 \text{ kJ/h}$$

Convert to kW: $\dot{Q} = \frac{-12{,}285}{3600} = -3.41$ kW

**(b) Heat removed: $\mathbf{3.41}$ kW** (negative sign confirms heat must be removed — exothermic reactions)

**Key insight:** Even though the main reaction is only moderately exothermic, the side combustion reaction releases far more heat per mole. Always check the contribution of all reactions when sizing heat removal equipment.
```

---

```{caution}
**PE Exam Traps — Reactive Energy Balances**

- **Don't forget the side reactions:** If a problem gives two reactions and asks for reactor heat duty, include the heat of reaction for **each** reaction scaled by its own extent. Omitting the combustion side reaction in Example 2 above would underestimate heat removal by 80%.
- **Reference state consistency:** Standard heats of formation are at 25°C and 1 atm. If reactants enter at 300°C and products leave at 500°C, you must add sensible heat correction terms. The formula is: $\dot{Q} = \xi\Delta\hat{H}_{rxn}^\circ + \sum_{out}\dot{n}_i\hat{h}_i - \sum_{in}\dot{n}_i\hat{h}_i$.
- **Exothermic sign check:** For an exothermic reaction, $\Delta\hat{H}_{rxn}^\circ < 0$ and $\dot{Q} < 0$ (heat leaves the reactor). If you get a positive $\dot{Q}$ for a combustion reaction, check your sign convention.
- **Latent heats of formation:** Water formed by combustion is typically vapor at high temperature ($\Delta\hat{H}_{f,H_2O(g)}^\circ = -241.83$ kJ/mol). Using the liquid value ($-285.84$ kJ/mol) is wrong unless the product water is liquid.
```
