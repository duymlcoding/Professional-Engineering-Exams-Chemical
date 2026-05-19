---
author: PE Study Guide
date: "2025"
title: Mass Transfer Study Guide
---

# Mass Transfer

## Quick Reference: Key Equations

| Topic | Formula | Notes |
|-------|---------|-------|
| Fick's First Law | $J_A = -D_{AB}\,dC_A/dz$ | Steady-state molar flux [mol/m²·s] |
| Fick's Second Law | $\partial C_A/\partial t = D_{AB}\,\partial^2 C_A/\partial x^2$ | Unsteady diffusion |
| Error function soln. | $(C_A - C_{A0})/(C_{As}-C_{A0}) = 1 - \text{erf}(x/2\sqrt{D_{AB}t})$ | Semi-infinite solid |
| Mass transfer coeff. | $N_A = k_c(C_{As} - C_{A\infty})$ | Convective MT |
| Sherwood number | $Sh = k_c L/D_{AB}$ | Dimensionless $k_c$ |
| Schmidt number | $Sc = \mu/(\rho D_{AB}) = \nu/D_{AB}$ | Fluid property |
| Colburn analogy | $j_D = j_H$ | MT–HT analogy |
| Distillation: OB | $y = (L/V)x + (D/V)x_D$ | Above feed (rectifying) |
| Distillation: OB | $y = (L'/V')x - (B/V')x_B$ | Below feed (stripping) |
| Reflux ratio | $R = L/D$ | $L$ = liquid down, $D$ = distillate |
| Min. reflux (Fenske) | $R_{min}$ from pinch point on McCabe-Thiele | At infinite stages |
| Henry's Law | $p_A = H\,x_A$ | Dilute gas absorption |
| Absorption factor | $A = L/(mG)$ | $m$ = Henry slope; $A>1$ for feasible absorption |
| Rayleigh equation | $\ln(F/W) = \int_{x_W}^{x_F} dx/(y^*-x)$ | Batch distillation |

---

## Diffusion into a Solid

Diffusion is the net movement of a substance from a region of higher concentration to a region of lower concentration, driven by the random motion of particles. When this process occurs over time, it is known as **unsteady-state diffusion**, and it is crucial for many materials science and chemical engineering processes, such as hardening steel or doping semiconductors.

### The Governing Equation: Fick's Second Law

```{note}
Unsteady-state diffusion is described by **Fick's Second Law**, a partial differential equation that relates the change in concentration over time to the second derivative of concentration with respect to spatial position. It describes how the concentration profile evolves over time.
```

```{important}
For one-dimensional diffusion with a constant diffusion coefficient, the law is:

$$
\frac{\partial C_A}{\partial t} = D_{AB} \frac{\partial^2 C_A}{\partial x^2} \quad \text{(Equation 1)}
$$


```

```{admonition} Term Definitions
:class: tip
- $C_A$: Concentration of the diffusing substance A [mol/m$^3$ or wt\%].
- $t$: Time [s].
- $x$: Position or distance into the solid [m].
- $D_{AB}$: The diffusion coefficient (or diffusivity) of A in B [m$^2$/s].
```

### The Error Function Solution for a Semi-Infinite Solid

```{note}
A common scenario involves diffusion into a solid that is thick enough to be considered **semi-infinite**. The initial concentration is uniform, and at time $t=0$, the surface concentration is suddenly changed to a new, constant value. The analytical solution for this specific case uses the mathematical **error function (erf)**.
```

```{important}
The concentration profile is given by:

$$
\frac{C_A(x,t) - C_{A0}}{C_{As} - C_{A0}} = 1 - \text{erf}\left(\frac{x}{2\sqrt{D_{AB}t}}\right) \quad \text{(Equation 2)}
$$


```

```{admonition} Term Definitions
:class: tip
- $C_A(x,t)$: The concentration at position $x$ and time $t$.
- $C_{A0}$: The initial, uniform concentration in the solid at $t=0$.
- $C_{As}$: The constant concentration maintained at the surface ($x=0$) for all time $t>0$.
- $\text{erf}(z)$: The error function, whose values are found in tables or calculated by software.
```

### Example Problem: Carburization of a Steel Alloy

```{prf:example} Carburization of a Steel Alloy
A steel alloy initially has a uniform carbon concentration of 0.10 wt\%. To harden the surface, it is placed in a high-temperature furnace at 1000$^\circ$C where the carbon concentration at the surface is maintained at 1.5 wt\%. The diffusion coefficient of carbon in steel at this temperature is $D_{AB} = 2.0 \times 10^{-11}$ m$^2$/s. How long (in hours) will it take for the carbon concentration to reach 1.0 wt\% at a depth of 1.0 mm below the surface?
```

```{dropdown} Solution Steps
**Step 1: Identify Knowns and Strategy**
The problem describes diffusion into a semi-infinite solid with constant surface concentration, matching the conditions for the error function solution. We will solve Equation 2 for time, $t$.
- Target Concentration: $C_A(x,t) = 1.0$ wt\%
- Initial Concentration: $C_{A0} = 0.10$ wt\%
- Surface Concentration: $C_{As} = 1.5$ wt\%
- Depth: $x = 1.0 \, \text{mm} = 1.0 \times 10^{-3}$ m
- Diffusivity: $D_{AB} = 2.0 \times 10^{-11}$ m$^2$/s

**Step 2: Calculate the Concentration Ratio**
Substitute the known concentrations into the left-hand side of Equation 2.

$$
\frac{C_A(x,t) - C_{A0}}{C_{As} - C_{A0}} = \frac{1.0 - 0.10}{1.5 - 0.10} = \frac{0.9}{1.4} \approx 0.6429
$$

**Step 3: Solve for the Error Function Term**
Set the result equal to the right-hand side of Equation 2 and solve for erf(z).

$$
0.6429 = 1 - \text{erf}\left(\frac{x}{2\sqrt{D_{AB}t}}\right)
$$

$$
\text{erf}\left(\frac{x}{2\sqrt{D_{AB}t}}\right) = 1 - 0.6429 = 0.3571
$$

**Step 4: Find the Argument of the Error Function**
Using an error function table or calculator, find the value of $z$ for which $\text{erf}(z) = 0.3571$.

$$
z = \frac{x}{2\sqrt{D_{AB}t}} \approx 0.328
$$

**Step 5: Solve for Time ($t$)**
Rearrange the equation for $z$ to solve for the unknown time, $t$.

$$
\sqrt{t} = \frac{x}{2 \cdot (0.328) \cdot \sqrt{D_{AB}}}
$$

$$
t = \left( \frac{x}{2 \cdot (0.328) \cdot \sqrt{D_{AB}}} \right)^2 = \frac{x^2}{4 \cdot (0.328)^2 \cdot D_{AB}}
$$

$$
t = \frac{(1.0 \times 10^{-3} \, \text{m})^2}{4 \cdot (0.328)^2 \cdot (2.0 \times 10^{-11} \, \text{m}^2/\text{s})} = \frac{1.0 \times 10^{-6}}{8.60 \times 10^{-12}} \, \text{s} \approx 116,279 \, \text{s}
$$

**Step 6: Convert to Hours and Final Answer**
Convert the time from seconds to hours.

$$
t = 116,279 \, \text{s} \times \frac{1 \, \text{h}}{3600 \, \text{s}} \approx 32.3 \, \text{h}
$$

The process will take approximately **32.3 hours**.

```

## McCabe-Thiele Diagrams

The McCabe-Thiele method is a graphical technique used to determine the number of theoretical equilibrium stages required to separate a binary (two-component) mixture via distillation. It is a powerful visual tool that combines thermodynamic equilibrium data with material balances to model the distillation process. The entire method is built upon a key simplifying assumption.

```{note}
**Key Assumption: Constant Molar Overflow (CMO)**
The McCabe-Thiele method assumes **Constant Molar Overflow (CMO)**. This means that for every mole of vapor that condenses on a tray, one mole of liquid vaporizes. As a result, the molar flow rates of liquid ($L$) and vapor ($V$) are considered constant throughout each section of the column (i.e., above the feed and below the feed). This simplification is reasonably accurate for ideal mixtures where the molar heats of vaporization of the two components are nearly equal.
```

### Important Equations

The McCabe-Thiele diagram is constructed using several key lines, each derived from material balances around different sections of the distillation column.

```{important}
**Key Operating and Feed Lines**

**Rectifying Section Operating Line (TOL):**
This line describes the material balance in the section above the feed. In terms of the reflux ratio, $R$:

$$
y = \left(\frac{R}{R+1}\right)x + \left(\frac{1}{R+1}\right)x_D
$$

**Stripping Section Operating Line (BOL):**
This line describes the material balance in the section below the feed.

$$
y = \left(\frac{\bar{L}}{\bar{V}}\right)x - \left(\frac{B}{\bar{V}}\right)x_B
$$

**The q-Line (Feed Line):**
This line is determined by the thermal condition of the feed and represents the locus of intersection points for the TOL and BOL.

$$
y = \left(\frac{q}{q-1}\right)x - \left(\frac{z_F}{q-1}\right)
$$


```

```{admonition} Term Definitions
:class: tip
- $x, y$: Mole fraction of the more volatile component in the liquid and vapor phase, respectively.
- $x_D, x_B, z_F$: Mole fractions in the distillate, bottoms, and feed streams.
- $L, V$: Molar flow rates of liquid and vapor in the rectifying (top) section [mol/time].
- $\bar{L}, \bar{V}$: Molar flow rates of liquid and vapor in the stripping (bottom) section [mol/time].
- $D, B, F$: Molar flow rates of the distillate, bottoms, and feed streams.
- $R$: Reflux ratio, the ratio of liquid returned to the column to liquid taken as distillate ($R=L/D$).
- $q$: The thermal quality of the feed.
```

### The Conceptual Basis: Why "Stepping Off Stages" Works

```{note}
**Combining Balances and Equilibrium**
A distillation column achieves separation because of two distinct physical phenomena that are represented by the two main lines on the diagram:
1. **On a stage (tray):** The vapor and liquid phases are in intimate contact, allowing them to reach thermodynamic equilibrium. Their compositions ($x_n, y_n$) for a given stage $n$ are related by the **Vapor-Liquid Equilibrium (VLE) curve**. This is a thermodynamic relationship.
2. **Between stages:** A vapor stream ($y_{n+1}$) rising from one stage passes a liquid stream ($x_n$) descending from the stage above. Their compositions are related by a **material balance**. This relationship is described by the **operating line**.

The McCabe-Thiele "staircase" is a graphical method of alternating between these two relationships to count the number of stages needed to get from the reboiler composition to the distillate composition.
```

```{note}
**Visualizing the Stepping Process**
The graphical procedure for stepping off stages simulates the movement of components through the column:
1. **Start at the Distillate:** Begin at the top of the column. The liquid reflux returning to the first stage has the distillate composition, $x_D$. This is represented by the point ($x_D, x_D$) on the $y=x$ line.
2. **Find Vapor from Stage 1 (Material Balance):** To find the composition of the vapor ($y_1$) rising from stage 1, move vertically from the starting point to the **Top Operating Line (TOL)**. This represents the material balance between the condenser and stage 1.
3. **Find Liquid on Stage 1 (Equilibrium):** This vapor ($y_1$) is in equilibrium with the liquid on stage 1 ($x_1$). To find this liquid's composition, move horizontally from the point on the TOL to the **VLE curve**. The x-coordinate of this new point is $x_1$. This completes one "step," which represents one theoretical stage.
4. **Repeat Down the Column:** From the point on the VLE curve, move vertically down to the operating line to find the vapor composition from the next stage ($y_2$). Then move horizontally to the VLE curve to find the corresponding liquid composition ($x_2$). This process is repeated. When the steps cross the q-line, you must switch from using the TOL to using the BOL for the vertical movements. Continue until the liquid composition $x_n$ is less than or equal to the desired bottoms composition, $x_B$.
```

### The Role of the Feed: The q-Line

The condition of the feed stream when it enters the column has a significant impact on the internal liquid and vapor flow rates. The **q-line** is a graphical tool that accounts for the thermal condition and composition of the feed, and it correctly links the operating lines for the top and bottom sections of the column.

```{note}
**Definition of Feed Quality (q)**
The value of **q**, the feed quality, is defined as the fraction of the feed that becomes liquid in the stripping (bottom) section of the column. It can be thought of as the heat required to vaporize one mole of feed divided by the molar latent heat of vaporization of the feed.

$$
q = \frac{\text{Increase in liquid flow rate below the feed tray}}{\text{Total molar feed rate}} = \frac{\bar{L} - L}{F}
$$


```

```{admonition} Feed Quality (q) Classification
:class: tip
The value of $q$ precisely defines the thermal state of the feed, which in turn determines the slope of the q-line.
- **Subcooled Liquid ($q > 1$):** The feed is a cold liquid. It condenses some vapor rising from below, increasing the liquid flow rate in the stripping section by more than the feed rate. The q-line slope is positive and greater than 1.
- **Saturated Liquid ($q = 1$):** The feed is a liquid at its boiling point. All of the feed joins the liquid stream flowing down. The q-line is vertical.
- **Two-Phase Mixture ($0 < q < 1$):** The feed is a liquid-vapor mixture. The liquid fraction ($q$) flows down, and the vapor fraction ($1-q$) flows up. The q-line has a negative slope.
- **Saturated Vapor ($q = 0$):** The feed is a vapor at its dew point. All of the feed joins the vapor stream flowing up. The q-line is horizontal.
- **Superheated Vapor ($q < 0$):** The feed is a hot vapor. It vaporizes some of the liquid flowing down from above, resulting in less liquid in the stripping section. The q-line has a positive slope less than 1.
```

```{important}
**q-Line Properties**
The q-line is derived by finding the mathematical intersection of the TOL and BOL. Its equation is:

$$
y = \left(\frac{q}{q-1}\right)x - \left(\frac{z_F}{q-1}\right)
$$

This line has two critical properties that are used to draw it on the diagram:
- Its **slope** is determined by the feed quality: $m_q = \frac{q}{q-1}$.
- It always intersects the **$y=x$ line** at the feed composition, $z_F$.

To construct the diagram, one draws the q-line starting from the point $(z_F, z_F)$ on the $y=x$ line with the slope $m_q$. The intersection of this q-line with the TOL defines the point through which the BOL must pass.

```

### Comprehensive Example: Acetone-Ethanol Separation

```{prf:example} Acetone-Ethanol Separation
Acetone and ethanol are to be separated in a distillation column. The column has a **partial condenser** and a **partial reboiler**, which each function as an equilibrium stage. An equimolar ($z_F=0.5$), sub-cooled liquid feed enters at 100 kmol/hr. The feed is cold enough that it condenses 1 mole of vapor inside the column for every 6 moles of feed that enters. The desired separation is a distillate **vapor** product of 95 mol\% acetone ($y_D=0.95$) and a bottoms liquid product of 5 mol\% acetone ($x_B=0.05$). The reflux returned from the condenser is a saturated liquid. The column is operated with a liquid-to-vapor flow ratio in the rectifying section of $(L/V) = 1.4 \times (L/V)_{\text{min}}$. Assume Constant Molar Overflow.

**Tasks:**
1. Plot the operating lines for the rectifying and stripping sections and the feed line.
2. Determine the total number of equilibrium stages required and the number of trays needed.
3. Determine the optimal feed tray location.
4. Determine the molar flow rates of the distillate (D) and bottoms (B) products, as well as the internal flow rates in the rectifying (L, V) and stripping ($\bar{L}, \bar{V}$) sections.
```

```{dropdown} Solution Steps
**Step 1: Analyze the Problem and List Knowns**
Before beginning, it's crucial to identify all the given information and the goals.
- **Feed (F):** Rate = 100 kmol/hr, Composition $z_F = 0.5$.
- **Distillate (D):** Vapor product, Composition $y_D = 0.95$.
- **Bottoms (B):** Liquid product, Composition $x_B = 0.05$.
- **Column Type:** Partial condenser and partial reboiler.
- **Operating Condition:** $(L/V) = 1.4 \times (L/V)_{\text{min}}$.

Our task is to fully define the column's design and operation using the McCabe-Thiele method. We will start by defining the three key lines on the diagram: the q-line, the Top Operating Line (TOL), and the Bottom Operating Line (BOL).

**Solution Part 1: Constructing the McCabe-Thiele Diagram**

**Step 2: Determine the Feed Line (q-Line)**
The q-line's properties are determined by the thermal condition of the feed. The feed is a sub-cooled liquid, which means $q > 1$.
- The increase in liquid flow across the feed stage is the sum of the feed itself plus any vapor it condenses: $\bar{L} - L = F + \frac{1}{6}F = \frac{7}{6}F$.
- We can now calculate $q$:

  $$
  q = \frac{\bar{L} - L}{F} = \frac{(7/6)F}{F} = \frac{7}{6} \approx 1.167
  $$

The q-line is plotted by starting at the point $(z_F, z_F) = (0.5, 0.5)$ on the $y=x$ line and drawing a line with a slope of $m_q = q/(q-1) = (7/6)/(1/6) = 7$.

**Step 3: Clarify Distillate Composition and the Partial Condenser**
A partial condenser acts as one equilibrium stage. It takes vapor from the top tray and splits it into two streams that are in equilibrium: the final vapor product ($D$, with composition $y_D$) and the saturated liquid reflux ($L$, with composition $x_D$). To find $x_D$, we must use the VLE data to find the liquid composition in equilibrium with the vapor $y_D=0.95$. The Top Operating Line (TOL) must originate from the point $(x_D, x_D)$ on the $y=x$ line.
From VLE data for Acetone-Ethanol, a vapor of $y=0.95$ is in equilibrium with a liquid of approximately $x=0.91$. We will use $\mathbf{x_D = 0.91}$ for plotting our operating line.

**Step 4: Determine the Rectifying Operating Line (TOL)**
The operating liquid-to-vapor ratio is $(L/V) = 1.4 \times (L/V)_{\text{min}}$. First, we find the minimum ratio.
- The minimum TOL is the line drawn from $(x_D, x_D) = (0.91, 0.91)$ to the intersection of the **q-line** and the **VLE curve**.
- By drawing this line on the graph, its slope is measured to be approximately 0.62. So, $(L/V)_{\text{min}} \approx 0.62$.
- The actual operating ratio is: $(L/V)_{\text{actual}} = 1.4 \times 0.62 = 0.868 \approx 0.87$.
The TOL is plotted starting from $(x_D, x_D) = (0.91, 0.91)$ with a slope of 0.87.

**Step 5: Determine the Stripping Operating Line (BOL)**
The BOL is the straight line that connects two points: $(x_B, x_B) = (0.05, 0.05)$ and the intersection point of the TOL and the q-line. Drawing this line completes the diagram.

**Solution Part 2: Determining Stages and Feed Location**

**Step 6: Step Off Stages and Determine Feed Location**
Now we use the completed diagram to count the required equilibrium stages, starting from the top.
- **Stage 1 (Partial Condenser):** This is our first equilibrium stage, establishing the equilibrium between $y_D=0.95$ and $x_D=0.91$.
- **Stepping Procedure:** We begin counting trays at $(x_D, x_D)=(0.91, 0.91)$. We draw "stair steps" between the **TOL** and the VLE curve.
- **Feed Stage and Switch to BOL:** When a step crosses the q-line, we switch to using the **BOL**. The tray on which this crossover occurs is the optimal feed tray.
- **Final Stage (Partial Reboiler):** We continue stepping down on the BOL until we reach or pass $x_B=0.05$. The partial reboiler is the final equilibrium stage.

Following this procedure on the McCabe-Thiele graph yields the following results:
- Total equilibrium stages required $\approx \textbf{10.75}$.
- Number of trays = Total Stages - Condenser - Reboiler = $10.75 - 1 - 1 = 8.75$ trays. We round up to **9 trays**.
- The optimal feed tray is where the switch from TOL to BOL occurs, which is **Tray 7** (counting from the top).

**Solution Part 3: Calculating Molar Flow Rates**

**Step 7: Calculate Overall Product Flow Rates (D and B)**
We solve the overall material balances for the column.
- **Overall Total Balance:** $F = D + B \implies 100 = D + B$
- **Overall Component Balance (Acetone):** $F z_F = D y_D + B x_B$

  $$
  (100)(0.5) = D(0.95) + B(0.05)
  $$

Solving the system of two equations (by substituting $B = 100 - D$):

$$
50 = 0.95D + (100 - D)(0.05) \implies 45 = 0.90D \implies D = 50 \, \text{kmol/hr}
$$

$$
B = 100 - D = 50 \, \text{kmol/hr}
$$

**Step 8: Calculate Internal Column Flow Rates**
- **Rectifying Section (L, V):** From a balance around the partial condenser, $V = L + D$. We also know $L = 0.87V$.

  $$
  V = 0.87V + 50 \implies 0.13V = 50 \implies V \approx 385 \, \text{kmol/hr}
  $$

  $$
  L = 0.87 \times V = 0.87 \times 385 \approx 335 \, \text{kmol/hr}
  $$

- **Stripping Section ($\bar{L}, \bar{V}$):** We use the q-value to find $\bar{L}$.

  $$
  \bar{L} = L + qF = 335 + (7/6)(100) \approx 452 \, \text{kmol/hr}
  $$

  From a balance around the reboiler, $\bar{L} = \bar{V} + B$.

  $$
  \bar{V} = \bar{L} - B = 452 - 50 = 402 \, \text{kmol/hr}
  $$

**Final Answer Summary**
- **Total Equilibrium Stages:** 10.75 (Requires 1 partial condenser, 1 partial reboiler, and 9 trays).
- **Optimal Feed Location:** Tray 7 (from the top).
- **Product Flow Rates:** $D = 50$ kmol/hr, $B = 50$ kmol/hr.
- **Internal Flow Rates (Rectifying):** $L = 335$ kmol/hr, $V = 385$ kmol/hr.
- **Internal Flow Rates (Stripping):** $\bar{L} = 452$ kmol/hr, $\bar{V} = 402$ kmol/hr.

```

## Batch Column: Variable Reflux

An alternative operating mode for batch distillation is to maintain a __constant distillate composition__, $x_D$. To achieve this, the __reflux ratio, R__, must be continuously increased throughout the run. As the liquid in the reboiler becomes leaner in the more volatile component, more reflux (a higher $R$) is needed to achieve the required separation and keep the distillate product on-spec.

### Material Balances for Constant Distillate Composition

```{note}
When the distillate composition ($x_D$) is held constant, the complex Rayleigh integral is not needed. The process can be analyzed with simple overall and component mole balances, treating the entire process as a single system with initial and final states.
```

```{important}
The governing equations are the overall material balances:

$$
\text{Total Balance: } W_i = D + W_f \quad \text{(Equation 4)}
$$

$$
\text{Component Balance: } W_i x_{W,i} = D x_D + W_f x_{W,f} \quad \text{(Equation 5)}
$$

These two equations can be solved simultaneously for two unknowns (e.g., $D$ and $W_f$).

```

```{admonition} Term Definitions
:class: tip
- $W_i$, $W_f$: Initial and final moles of liquid in the reboiler.
- $D$: Total moles of distillate collected.
- $x_{W,i}$, $x_{W,f}$: Initial and final mole fraction in the reboiler.
- $x_D$: Constant mole fraction of the distillate.
```

### Example Problem: Variable Reflux Distillation

```{prf:example} Variable Reflux Distillation
A batch still is charged with 1000 moles of an ethanol-water mixture containing 30 mole \% ethanol ($x_{W,i}=0.3$). The column has 2 equilibrium stages (including the partial reboiler). The distillation is run with a constant distillate composition of $x_D=0.6$ until the reboiler composition drops to $x_{W,f}=0.09$. How much distillate is produced, and what is the range of reflux ratios used?
```

```{dropdown} Solution Steps
**Part 1: Calculate Amount of Distillate**

**Step 1: Set up Balances:**
Use the known values in Equations 4 and 5.
Given: $W_i = 1000$ mol, $x_{W,i} = 0.30$, $x_D = 0.60$ (constant), $x_{W,f} = 0.09$.
Total material balance:

$$
1000 = D + W_f \implies W_f = 1000 - D
$$

Component balance:

$$
(1000)(0.30) = D(0.60) + W_f(0.09)
$$

**Step 2: Solve for Distillate (D):** Substitute the expression for $W_f$ into the component balance.

$$
300 = 0.60 D + (1000 - D)(0.09)
$$

$$
300 = 0.60 D + 90 - 0.09 D
$$

$$
210 = 0.51 D
$$

$$
D = \frac{210}{0.51} \approx 411.8 \, \text{moles}
$$

**Final Answer (Part 1):**
The total amount of distillate produced is approximately **412 moles**.

```

```{dropdown} Solution Steps - Part 2
**Part 2: Determine the Range of Reflux Ratios**

**Step 1: Strategy:** The reflux ratio must be adjusted continuously. We find the required range by determining the reflux ratio needed at the start ($R_i$) and at the end ($R_f$) of the process using the McCabe-Thiele method. The slope of the operating line is $m = R/(R+1)$.

**Step 2: Calculate Initial Reflux Ratio ($R_i$):** At the start, $x_D = 0.6$ and $x_{W,i} = 0.3$. We find the operating line that connects the point ($0.6, 0.6$) on the $y=x$ line and allows for a bottoms composition of $0.3$ in exactly 2 stages. This requires a graphical trial-and-error process, which shows this corresponds to an operating line with a slope of 0.125.

$$
\text{slope} = \frac{R_i}{R_i+1} = 0.125
$$

$$
R_i = 0.125(R_i+1) \implies R_i = 0.125 R_i + 0.125
$$

$$
0.875 R_i = 0.125 \implies R_i = \frac{0.125}{0.875} \approx 0.143
$$

**Step 3: Calculate Final Reflux Ratio ($R_f$):** At the end, $x_D=0.6$ and $x_{W,f}=0.09$. We repeat the trial-and-error process. The operating line that connects ($0.6, 0.6$) to a bottoms composition of $0.09$ in 2 stages corresponds to a slope of 0.75.

$$
\text{slope} = \frac{R_f}{R_f+1} = 0.75
$$

$$
R_f = 0.75(R_f+1) \implies R_f = 0.75 R_f + 0.75
$$

$$
0.25 R_f = 0.75 \implies R_f = \frac{0.75}{0.25} = 3.0
$$

**Final Answer (Part 2):** The required reflux ratio increases from an initial value of **R = 0.14** to a final value of **R = 3.0**.

```

## Distillation – Side Stream Feed

Standard distillation columns have a single feed, creating a rectifying section (above the feed) and a stripping section (below). When a column has multiple feeds, such as a main feed and a secondary steam feed, additional operating sections are created. A column with two feeds will have three sections: top, middle, and bottom, each with a unique operating line on a McCabe-Thiele diagram.

### Constructing the Middle Operating Line

```{note}
For a column with two feeds, a **Middle Operating Line (MOL)** must be constructed. This line represents the material balance in the section between the two feed points. The MOL is the straight line that connects two specific intersection points on the McCabe-Thiele diagram:
1. The intersection of the **Top Operating Line (TOL)** with the **feed line for the upper feed**.
2. The intersection of the **Bottom Operating Line (BOL)** with the **feed line for the lower feed**.
```

### Example Problem: Column with Steam Injection

```{prf:example} Column with Steam Injection
An ethanol-water distillation column has a total condenser and a partial reboiler. It is fed with a main subcooled liquid feed and a secondary feed of pure saturated steam, which enters on the first stage above the reboiler. The Top Operating Line (TOL), Bottom Operating Line (BOL), and main feed line are plotted. Determine the optimal feed plate location for the main feed and the total number of equilibrium stages required.
```

```{dropdown} Solution Steps
**Step 1: Strategy:** The solution requires correctly constructing the Middle Operating Line (MOL). Once all three operating lines (TOL, MOL, BOL) are drawn, we can step off the stages from the bottom ($x_B$) to the top ($x_D$), switching operating lines as we cross the feed locations.

**Step 2: Construct the Steam Feed Line:** A feed line's properties are set by its composition ($z$) and thermal quality ($q$).
- **Composition ($z_s$):** The feed is pure steam (pure water), so its mole fraction of ethanol is zero. The feed line originates at ($z_s, z_s$) = (0, 0).
- **Quality ($q$):** The feed is a saturated vapor, for which $q=0$. The slope of the feed line is $\frac{q}{q-1} = \frac{0}{0-1} = 0$.

Therefore, the steam feed line is a **horizontal line at y=0** (the x-axis).

**Step 3: Construct the Middle Operating Line (MOL):** Following the rule from the Key Concept, we draw a straight line connecting the two intersection points:
- **Point 1:** Intersection of the given TOL and the main (upper) feed line.
- **Point 2:** Intersection of the given BOL and the steam (lower) feed line. This point lies on the x-axis.

**Step 4: Step Off the Stages:** We count stages from the bottom up.
- **Partial Reboiler:** The reboiler counts as Stage 0. Start at ($x_B, x_B$) on the y=x line. The first step goes from the equilibrium curve down to the **BOL**.
- **Stage 1 (Steam Feed):** The steam enters on Stage 1. This is the stage immediately above the reboiler. After stepping up from the reboiler, we have crossed the lower feed location. Therefore, all subsequent steps must use the next operating line up, which is the **MOL**.
- **Switch to TOL:** Continue stepping off stages using the MOL. When a stage step crosses the main feed line, switch to the **TOL** for all remaining stages until $x_D$ is reached.

**Step 5: Determine Optimal Feed Location:** The optimal stage for a feed is where the stage composition is closest to the feed composition. Graphically, this is the stage where we switch operating lines. In this case, the switch from the MOL to the TOL occurs at **Stage 2**. Therefore, the main feed should be introduced on Stage 2.

**Final Answer:** Following the procedure yields a **partial reboiler and 5 ideal stages**, for a total of 6 equilibrium contacts. The optimal location for the main feed is **Stage 2**.

```

## Single-stage Batch Distillation

Single-stage batch distillation, also known as simple or differential distillation, is the most basic method of separating a finite batch of a liquid mixture. In this process, a liquid charge is placed in a heated vessel (the "still"), and the vapor generated is immediately removed and condensed.

```{note}
**The Principle of Simple Distillation**
Simple distillation works because the vapor generated from a boiling liquid mixture is typically richer in the more volatile component (MVC) than the liquid from which it came. As this enriched vapor is continuously removed, the liquid remaining in the still becomes progressively leaner in the MVC. This means the composition of the liquid in the still, the composition of the vapor being produced, and the boiling temperature all change continuously throughout the process.
```

### Important Equations

The process is inherently unsteady-state, so its analysis relies on differential mass balances that are integrated over the course of the distillation.

```{important}
**Key Equations for Simple Distillation**

**Differential Mass Balances (on the still):**
- Overall Balance: $\frac{dW}{dt} = -\dot{D}$
- Component Balance (MVC): $\frac{d(W x_W)}{dt} = -\dot{D} y_D$

**The Rayleigh Equation (Primary Design Equation):**
This equation relates the change in liquid composition to the change in the total amount of liquid in the still. Note that the relationship between $y_D$ and $x_W$ comes from vapor-liquid equilibrium (VLE) data.

$$

\int_{x_{W0}}^{x_W} \frac{dx_W}{y_D - x_W} = \ln\left(\frac{W}{W_0}\right)

$$

**Overall Material Balances (for the entire process):**
These are used to relate the initial state to the final state and the total distillate collected.
- Total Moles: $W_0 = W + D$
- Component Moles: $W_0 x_{W0} = W x_W + D x_{D,avg}$

```

### Derivation of the Rayleigh Equation

The Rayleigh equation is derived by combining the differential balances to eliminate time, providing a direct relationship between the amount of liquid remaining and its composition.

```{dropdown} Derivation of the Rayleigh Equation
**Derivation of the Rayleigh Equation**

**Step 1: Start with Differential Balances:** We begin with the fundamental unsteady-state balances on the contents of the still.

$$
\frac{dW}{dt} = -\dot{D} \quad \text{(Overall)}
$$

$$
\frac{d(W x_W)}{dt} = -\dot{D} y_D \quad \text{(Component)}
$$

**Step 2: Expand the Component Balance:** Apply the product rule for differentiation to the left side of the component balance.

$$
W\frac{dx_W}{dt} + x_W\frac{dW}{dt} = -\dot{D} y_D
$$

**Step 3: Combine the Balances:** To eliminate the distillate rate $\dot{D}$, substitute the overall balance ($\frac{dW}{dt} = -\dot{D}$) into the expanded component balance.

$$
W\frac{dx_W}{dt} + x_W\frac{dW}{dt} = \left(\frac{dW}{dt}\right) y_D
$$

**Step 4: Separate the Variables:** Rearrange the equation to group all terms involving composition ($x_W, y_D$) on one side and all terms involving the total amount ($W$) on the other.

$$
W\frac{dx_W}{dt} = y_D\frac{dW}{dt} - x_W\frac{dW}{dt} = (y_D - x_W)\frac{dW}{dt}
$$

Dividing both sides by $W$ and $(y_D - x_W)$, and cancelling the $dt$ term, yields:

$$
\frac{dx_W}{y_D - x_W} = \frac{dW}{W}
$$

**Step 5: Integrate the Result:** Integrate both sides from the initial state ($W_0, x_{W0}$) to a final state ($W, x_W$).

$$
\int_{x_{W0}}^{x_W} \frac{dx_W}{y_D - x_W} = \int_{W_0}^{W} \frac{dW}{W}
$$

Solving the right-side integral gives the final form of the Rayleigh Equation:

$$
\int_{x_{W0}}^{x_W} \frac{dx_W}{y_D - x_W} = \ln\left(\frac{W}{W_0}\right)
$$


```

### Conceptual Example: Distillation of a System with an Azeotrope

```{note}
**Azeotropes in Distillation**
An **azeotrope** is a liquid mixture which, at its boiling point, produces a vapor of the exact same composition as the liquid ($y=x$). Such mixtures represent a limit to separation by conventional distillation. A **minimum-boiling azeotrope** occurs when the boiling point of the azeotropic mixture is lower than that of either pure component. This azeotrope acts as an "attractor" for the vapor composition during distillation of mixtures on one side of it, and a "repeller" on the other.
```

```{prf:example} Distillation of a System with an Azeotrope
A batch still is charged with a liquid mixture with a mole fraction of 0.2 of component 1. The T-x-y diagram shows that this system has a minimum-boiling azeotrope at a mole fraction of 0.5. With constant heating, describe how the temperature of the still and the composition of the vapor product change over time.
```

```{dropdown} Solution Steps
**Analysis using the T-x-y Diagram**

**Step 1: Initial Vaporization:**
The initial liquid at $x_W = 0.2$ is heated to its boiling point. At this temperature, the vapor in equilibrium with it (found by moving horizontally across the tie-line to the dew-point line) has a composition of approximately $y_D = 0.05$.

**Step 2: The Distillation Path:**
Since the vapor being removed ($y_D \approx 0.05$) is *leaner* in component 1 than the liquid it came from ($x_W = 0.2$), component 2 is being removed preferentially. This causes the liquid remaining in the still to become progressively **enriched in component 1**. As the liquid composition $x_W$ increases from 0.2 towards 0.5, we move up along the bubble-point (liquid) curve. This has two effects:
- The **boiling temperature of the liquid in the still increases**.
- The composition of the vapor being produced, $y_D$, also becomes richer in component 1.

**Step 3: Approaching the Azeotrope:**
This enrichment process continues, with the liquid in the still becoming more and more concentrated in component 1. As $x_W$ approaches the azeotropic composition of 0.5, the boiling temperature of the mixture continues to rise, approaching the minimum boiling point of the azeotrope. The vapor composition $y_D$ also approaches 0.5.

**Step 4: Azeotropic Boiling:**
Eventually, the liquid in the still will reach the azeotropic composition, $x_W = 0.5$. At this point, the liquid and vapor compositions are identical ($x_W = y_D = 0.5$). Any further vaporization produces vapor of that same azeotropic composition. Since the vapor being removed has the same composition as the liquid, the composition of the liquid in the still **no longer changes**. Consequently, the boiling temperature also becomes **constant** and remains at the azeotropic boiling point until all the remaining liquid is boiled away. This is the limit of separation for this starting mixture.

```

### Example Problem: Distillation using T-x-y Data

```{prf:example} Distillation using T-x-y Data
A simple pot still is charged with 50 moles of an ethanol-water mixture. The distillation is started, and the initial vapor temperature (head temperature) is 84$^\circ$C. The process is stopped when the head temperature rises to 89$^\circ$C. Using the provided T-x-y diagram for the ethanol-water system, determine:
1. The total amount of distillate collected (D).
2. The final composition of the liquid remaining in the still (the waste).
3. The average composition of the total collected distillate.
```

```{dropdown} Solution Steps
**Step 1: Strategy: The Rayleigh Equation with Numerical Integration**
The governing equation for this process is the Rayleigh equation. Since this is a single-stage still, the vapor leaving ($y_D$) is in direct equilibrium with the liquid in the still ($x_W$).

$$
\int_{x_{W0}}^{x_{Wf}} \frac{dx_W}{y - x_W} = \ln\left(\frac{W_f}{W_0}\right)
$$

Our plan is to:
(a) Use the given temperatures and the T-x-y diagram to find the initial ($x_{W0}$) and final ($x_{Wf}$) liquid compositions.
(b) Use the x-y data from the diagram to numerically evaluate the integral on the left-hand side.
(c) Solve for the final moles in the still, $W_f$.
(d) Use overall material balances to find the amount and average composition of the distillate.

**Step 2: Determine Compositions from T-x-y Data**
The head temperature is the boiling point of the liquid currently in the still. We use this to find the liquid composition from the bubble-point line on the diagram.
- Initial State ($T=84^\circ$C): Following the 84°C line to the liquid curve gives the initial still composition: $\mathbf{x_{W0} \approx 0.17}$.
- Final State ($T=89^\circ$C): Following the 89°C line to the liquid curve gives the final still composition: $\mathbf{x_{Wf} \approx 0.07}$.
The distillation proceeds from a liquid concentration of 17\% ethanol down to 7\% ethanol.

**Step 3: Perform Numerical Integration**
We must evaluate the integral $\int_{0.17}^{0.07} \frac{dx_W}{y - x_W}$. This is done by taking several points from the VLE diagram between $x_W = 0.07$ and $x_W = 0.17$, calculating the value of $1/(y-x_W)$ at each point, and finding the area under the curve. Using a numerical method like the trapezoidal rule, the value is found to be:

$$
\int_{0.17}^{0.07} \frac{dx_W}{y - x_W} \approx -0.27
$$

The value is negative because we are integrating from a higher concentration to a lower one ($x_{Wf} < x_{W0}$).

**Step 4: Solve for Final Moles in Still ($W_f$)**
Substitute the result of the integral into the Rayleigh equation. We are given $W_0 = 50$ moles.

$$
\ln\left(\frac{W_f}{W_0}\right) = -0.27
$$

$$
\frac{W_f}{50} = e^{-0.27} \approx 0.763 \implies W_f = 50 \times 0.763 = 38.15 \, \text{moles}
$$

**Step 5: Calculate Final Answers**
With $W_f$ known, we can find the remaining quantities using simple material balances.
Total Distillate Collected (D): $D = W_0 - W_f = 50 - 38.15 = 11.85$ moles.
Average Distillate Composition ($x_{D,avg}$):

$$
W_0 x_{W0} = W_f x_{Wf} + D x_{D,avg}
$$

$$
(50)(0.17) = (38.15)(0.07) + (11.85) x_{D,avg}
$$

$$
8.5 = 2.67 + 11.85 x_{D,avg} \implies 11.85 x_{D,avg} = 5.83
$$

$$
x_{D,avg} = \frac{5.83}{11.85} \approx 0.492
$$

**Final Answer Summary for Example 1**
- Total Distillate Collected (D): $\approx 12$ moles.
- Final Still Composition ($x_{Wf}$): 7\% ethanol.
- Average Distillate Composition ($x_{D,avg}$): $\approx 49\%$ ethanol.
A sanity check confirms this is reasonable: the instantaneous vapor was richer than 49\% at the start and leaner at the end.

```

### Example Problem: Distillation using Raoult's Law

```{prf:example} Distillation using Raoult's Law
A single-stage batch still is charged with 75 mol of an 82 mol\% methanol / 18 mol\% water mixture. The distillation is run until the **average** distillate concentration collected is 90.0 mol\% methanol. Assuming the mixture is an ideal solution (follows Raoult's Law) and operates at 760 mmHg:
1. How much total distillate will be collected?
2. How many moles will remain in the still, and what is its final methanol concentration?

The Antoine equations ($P^{\text{sat}}$ in mmHg, T in $^\circ$C) are:
- Methanol: $\log_{10}(P_1^{\text{sat}}) = 8.081 - \frac{1582}{T + 239.7}$
- Water: $\log_{10}(P_2^{\text{sat}}) = 8.071 - \frac{1731}{T + 233.4}$
```

```{dropdown} Solution Steps
**Step 1: Strategy: Iterative Numerical Solution**

This problem is more complex for two reasons: 1) The VLE data is not given directly and must be calculated using Raoult's Law. 2) The stopping condition is based on the *average* distillate composition, which depends on the entire path of the distillation. This means we cannot solve directly and must use an iterative, "marching" solution.

**Step 2: Set up the VLE Calculation Block**

At any given temperature $T$, we can find the equilibrium liquid ($x_W$) and vapor ($y_D$) compositions at $P_{total} = 760$ mmHg.

**VLE Calculation using Raoult's Law**

For any temperature T:
(a) Calculate the vapor pressures of methanol ($P_1^{\text{sat}}$) and water ($P_2^{\text{sat}}$) using their Antoine equations.
(b) Find the liquid mole fraction ($x_W$) that boils at this temperature and total pressure:

$$
x_W = \frac{P_{total} - P_2^{\text{sat}}}{P_1^{\text{sat}} - P_2^{\text{sat}}}
$$

(c) Find the corresponding equilibrium vapor composition ($y_D$):

$$
y_D = \frac{x_W P_1^{\text{sat}}}{P_{total}}
$$

This block of calculations forms the core of our iterative solution.

**Step 3: Describe the Iterative "Marching" Procedure**

The spreadsheet calculation proceeds by taking small steps (e.g., small increments of T or $x_W$) and updating all system properties until the target condition ($x_{D,avg}=0.90$) is met.

(a) **Initialize:** Start with the initial conditions: $W_0=75$ mol, $x_{W0}=0.82$.

(b) **Take a Step:** Choose a new, slightly lower liquid composition, $x_{W, new}$.

(c) **Calculate VLE:** At both the old and new $x_W$, calculate the corresponding temperatures and vapor compositions ($y_D$) using the VLE block from Step 2.

(d) **Update the Rayleigh Integral:** Approximate the integral over this small step using the trapezoidal rule:

$$
\Delta(\text{Integral}) = \frac{1}{2} \left( \left[\frac{1}{y_D-x_W}\right]_{\text{old}} + \left[\frac{1}{y_D-x_W}\right]_{\text{new}} \right) \cdot (x_{W,\text{new}} - x_{W,\text{old}})
$$

The total value of the integral is the running sum of these small step changes.

(e) **Update Moles in Still (W):** Use the new total value of the integral in the Rayleigh equation: $W = W_0 \exp(\text{Integral})$.

(f) **Update Total Distillate (D):** Use the overall balance: $D = W_0 - W$.

(g) **Update Average Composition ($x_{D,avg}$):** Use the overall component balance, solved for $x_{D,avg}$: $x_{D,avg} = (W_0 x_{W0} - W x_W) / D$.

(h) **Check and Repeat:** Compare the calculated $x_{D,avg}$ to the target of 0.90. If they don't match, repeat from step (b) with another small step in $x_W$. The process is complete when $x_{D,avg} = 0.90$.

**Final Answer Summary for Example 2**

The iterative calculation is continued until the target is met. The results obtained from this procedure are:
- **Total Distillate Collected (D):** $\approx 62.5$ moles.
- **Moles Remaining in Still (W):** $\approx 12.5$ moles.
- **Final Still Composition ($x_{Wf}$):** $\approx 42\%$ methanol.

```

## Gas Absorption Columns

__Gas Absorption__ is a mass transfer operation used to selectively remove one or more components (called __solutes__) from a gas stream by contacting it with a liquid __solvent__. The process works because the solute is more soluble in the liquid solvent than the other gases in the stream. A common industrial application is "sour gas sweetening," where acidic gases like H$_2$S are removed from natural gas using an amine solvent.

```{note}
**The Principle of Gas Absorption**
The operation is typically carried out in a tower containing trays or packing where the gas stream flows upwards and the liquid solvent flows downwards. This **counter-current** flow maximizes the concentration difference (the driving force) between the gas and liquid at every point in the column, leading to the most efficient mass transfer of the solute from the gas phase to the liquid phase.
```

### Fundamental Principles and Equations

The design of an absorption column involves combining thermodynamic equilibrium relationships with overall material balances.

```{note}
**Equilibrium Relationship:** On each theoretical stage of the column, the exiting gas and liquid streams are assumed to reach thermodynamic equilibrium. For dilute solutions, this relationship is described by **Henry's Law**, which states that the partial pressure of a solute in the gas phase is proportional to its concentration in the liquid phase.
```

```{important}
**Henry's Law and Equilibrium Constant**
The equilibrium relationship can be expressed in terms of mole fractions:

$$
y_n = \left(\frac{H}{P}\right) x_n \quad \text{or simply} \quad y_n = m \cdot x_n
$$

The temperature dependence of Henry's constant is often described by:

$$
H(T) = H^0 \exp\left[-\frac{E}{R}\left(\frac{1}{T} - \frac{1}{T_0}\right)\right]
$$


```

```{admonition} Term Definitions
:class: tip
- $y_n, x_n$: Mole fractions of the solute in the gas and liquid phases leaving stage $n$.
- $H$: Henry's Law constant [Pressure units, e.g., atm].
- $P$: Total pressure of the system [Pressure units].
- $m$: The equilibrium constant ($m = H/P$) [dimensionless].
- $L, V$: Molar flow rates of the liquid and gas (often on a solute-free basis) [mol/time].
```

```{note}
**The Operating Line:** The relationship between a gas stream rising and a liquid stream descending *between* stages is not governed by equilibrium, but by a **material balance**. The operating line equation relates the composition of the gas entering a stage from below to the liquid entering it from above.
```

```{important}
**The Operating Line Equation**
A material balance for the solute from the top of the column down to an arbitrary stage $n$ gives:

$$
L x_0 + V y_{n+1} = L x_n + V y_1
$$

Rearranging this into the form of a line ($y=mx+b$) gives the operating line equation:

$$
y_{n+1} = \left(\frac{L}{V}\right)x_n + \left(y_1 - \frac{L}{V}x_0\right)
$$


```

### Graphical Method for Stage Calculation

Similar to the McCabe-Thiele method, we can use a graphical method on an x-y diagram to determine the number of theoretical stages required.

```{admonition} Key Lines on the Absorption Diagram
:class: tip
- **Equilibrium Line:** This is a plot of the thermodynamic equilibrium relationship. For dilute systems following Henry's Law, this is a straight line through the origin with a slope of $m$, i.e., $y=mx$.
- **Operating Line:** This is a plot of the material balance equation. It is a straight line with a slope of $L/V$ that connects the compositions at the top of the column (point $(x_0, y_1)$) with the compositions at the bottom (point $(x_N, y_{N+1})$).
```

```{dropdown} Graphical Procedure for Stage Calculation
The number of stages is found by constructing a staircase between the operating line and the equilibrium line, typically starting from the bottom of the column.
1. **Start at the Bottom:** Begin at the point $(x_N, y_{N+1})$ on the operating line. This represents the rich entering gas ($y_{N+1}$) and the rich exiting liquid ($x_N$).
2. **Move to Equilibrium:** The vapor that leaves stage N ($y_N$) is in equilibrium with the liquid on stage N ($x_N$). To find its composition, move **vertically down** from the operating line to the **equilibrium line**.
3. **Move to Operating Line:** The vapor leaving stage N ($y_N$) passes the liquid entering from the stage above ($x_{N-1}$). To find this liquid's composition, move **horizontally to the left** from the equilibrium line to the **operating line**.
4. **Repeat:** This completes one "step" (one theoretical stage). Repeat this process—vertically to equilibrium, horizontally to the operating line—counting each step until the gas composition ($y$) is less than or equal to the desired exit gas composition, $y_1$.
```

### Effect of Operating Parameters

The graphical method provides an excellent way to visualize how changing operating conditions will impact the required number of stages for a given separation.

```{note}
**Effect of Temperature (T)**
- **What it Affects:** The **Equilibrium Line**.
- **How:** Gas solubility in a liquid *decreases* as temperature increases. This increases the Henry's constant, $H$, and thus increases the slope of the equilibrium line ($m=H/P$).
- **Result:** A higher temperature moves the equilibrium line **closer** to the operating line. This reduces the size of the "steps" in the graphical construction, meaning **more stages are required**.
- **Conclusion:** Gas absorption is favored at **lower temperatures**.
```

```{note}
**Effect of Pressure (P)**
- **What it Affects:** The **Equilibrium Line**.
- **How:** Increasing the total system pressure $P$ increases the partial pressure of the solute, driving more of it into the liquid phase. This *decreases* the slope of the equilibrium line ($m=H/P$).
- **Result:** A higher pressure moves the equilibrium line **further away** from the operating line. This increases the size of the steps, meaning **fewer stages are required**.
- **Conclusion:** Gas absorption is favored at **higher pressures**.
```

```{note}
**Effect of Solvent Flow Rate (L/V Ratio)**
- **What it Affects:** The **Operating Line**.
- **How:** The slope of the operating line is equal to the ratio of the liquid to gas molar flow rates, $L/V$.
- **Result:** Increasing the liquid solvent flow rate $L$ increases the slope of the operating line. This moves the operating line **further away** from the equilibrium line, meaning **fewer stages are required**.
- **Conclusion and Trade-off:** A higher solvent flow rate requires a smaller, cheaper column (lower capital cost) but costs more to operate (pumping and regenerating more solvent, higher operating cost). Engineers must choose an optimal $L/V$ ratio that balances these costs. The theoretical **minimum L/V ratio** would require an infinite number of stages.
```

```{note}
**Effect of Inlet and Outlet Compositions**
- **What they Affect:** The **anchor points** of the Operating Line.
- **How:** The operating line must connect the point representing the top of the column $(x_0, y_1)$ to the point representing the bottom $(x_N, y_{N+1})$.
- **Result:** If a recycled solvent with some initial solute is used ($x_0 > 0$), the top of the operating line shifts to the right. If a stricter outlet gas specification is required (a lower $y_1$), the top of the operating line shifts down. Both changes move the operating line closer to the equilibrium line and **require more stages**.
```

### Example Problem: Dilute System - Chloroform Scrubbing

```{prf:example} Chloroform Scrubbing
A laboratory process releases an air stream of 1000 kmol/hr containing 200 ppm of chloroform. To meet environmental standards, this concentration must be reduced to 10 ppm before release. An absorption column using pure water as the solvent is proposed. The system operates at 25$^\circ$C and 1.5 atm. How many theoretical equilibrium stages are required for this separation?
```

```{dropdown} Solution Steps
**Step 1: Strategy and Assumptions**
The first step is to recognize that with solute concentrations in the parts-per-million (ppm) range, this is a **dilute system**.

**Simplifications for Dilute Systems:** For dilute systems (typically when solute concentrations are below 1-2% in both phases), we can make several key simplifications that make the analysis much easier:
- The total liquid ($L$) and gas ($V$) molar flow rates can be assumed to be constant throughout the column because the amount of solute transferred is negligible compared to the total flow.
- We can work with mole fractions ($x, y$) directly. The operating and equilibrium lines are straight, allowing for an analytical solution.

Our plan is to determine the minimum liquid flow rate ($L_{min}$), select a practical operating flow rate, and then solve for the number of stages using both the graphical method and the analytical Kremser equation.

**Step 2: Define Knowns and Find Equilibrium Data**
- **Gas Flow Rate ($V$):** $1000$ kmol/hr.
- **Inlet Gas ($y_{N+1}$):** $200 \, \text{ppm} = 200 \times 10^{-6}$.
- **Outlet Gas ($y_1$):** $10 \, \text{ppm} = 10 \times 10^{-6}$.
- **Inlet Liquid ($x_0$):** $0$ (pure water solvent).
- **Henry's Constant ($H$):** $H = 211$ atm/mole fraction.
- **Equilibrium Line Slope ($m$):** $m = H/P = 211 \, \text{atm} / 1.5 \, \text{atm} = 140.7$.
The equilibrium line is therefore $\mathbf{y = 140.7 x}$.

**Step 3: Determine the Minimum Liquid Flow Rate ($L_{min}$)**
The minimum liquid flow rate corresponds to an infinite number of stages, which occurs when the operating line touches the equilibrium line at the bottom (high-concentration) end of the column. At this "pinch point," the exiting liquid ($x_{N,max}$) is in equilibrium with the entering gas ($y_{N+1}$).

$$
x_{N,max} = \frac{y_{N+1}}{m} = \frac{200 \times 10^{-6}}{140.7} = 1.42 \times 10^{-6}
$$

The slope of this minimum operating line is $(L/V)_{min}$, found from a balance over the whole column:

$$
\left(\frac{L}{V}\right)_{min} = \frac{y_{N+1} - y_1}{x_{N,max} - x_0} = \frac{(200 - 10) \times 10^{-6}}{(1.42 - 0) \times 10^{-6}} = 133.8
$$

$$
L_{min} = V \cdot (L/V)_{min} = 1000 \frac{\text{kmol}}{\text{hr}} \cdot 133.8 = 133,800 \frac{\text{kmol}}{\text{hr}}
$$

**Step 4: Determine the Actual Operating Line**
A common heuristic is to use an actual liquid flow rate $1.1$ to $2.0$ times the minimum. We will use $L_{actual} = 1.4 \cdot L_{min}$.

$$
(L/V)_{actual} = 1.4 \cdot (L/V)_{min} = 1.4 \cdot 133.8 = 187.3
$$

**Step 5: Method A: Graphical Solution**
We plot the equilibrium line ($y=140.7x$) and the operating line. The operating line has a slope of 187.3 and connects the top point $(x_0, y_1) = (0, 10\text{ppm})$ and the bottom point $(x_N, y_{N+1}) = (x_N, 200\text{ppm})$. By stepping off the stages graphically, we find that approximately **7.25 theoretical stages** are required. We would design for **8 stages**.

**Step 6: Method B: Analytical Solution (Kremser Equation)**
For dilute systems with linear equilibrium and operating lines, the Kremser equation provides a direct analytical solution.

$$
N = \frac{\ln\left[ \frac{y_{N+1} - mx_0}{y_1 - mx_0} \left(1 - \frac{1}{A}\right) + \frac{1}{A} \right]}{\ln(A)}
$$

where $A$ is the dimensionless **absorption factor**, $A = \frac{L}{mV}$.

First, calculate the absorption factor:

$$
A = \frac{L/V}{m} = \frac{187.3}{140.7} = 1.33
$$

Since we are using pure solvent ($x_0 = 0$), the equation simplifies:

$$
N = \frac{\ln\left[ \frac{y_{N+1}}{y_1} \left(1 - \frac{1}{A}\right) + \frac{1}{A} \right]}{\ln(A)} = \frac{\ln\left[ \frac{200}{10} \left(1 - \frac{1}{1.33}\right) + \frac{1}{1.33} \right]}{\ln(1.33)}
$$

$$
N = \frac{\ln[20(0.248) + 0.752]}{\ln(1.33)} = \frac{\ln(5.712)}{0.285} \approx 6.1
$$

**Final Answer Summary for Example 1**
The Kremser equation predicts that **6.1 theoretical stages** are required. We would round up and design the column for **7 stages**. The small difference between the graphical and analytical methods is expected and acceptable.

```

### Example Problem: Concentrated System - CO$_2$ Removal

```{prf:example} CO2 Removal
We wish to remove 65\% of the CO$_2$ from a 100 mol/hr gas stream that is initially 8 mol\% CO$_2$ in nitrogen. The scrubbing is done with pure water at room temperature and atmospheric pressure, where the VLE relationship is approximately $y=1640x$. How many equilibrium stages are required if the solvent flow rate is 1.5 times the minimum?
```

```{dropdown} Solution Steps
**Step 1: Strategy: Analysis for a Concentrated System**
First, we must determine if the system is dilute. A significant change in the total molar flow rate means we cannot use the simplifying assumptions of the dilute case.
- Moles CO$_2$ entering: $100 \, \text{mol/hr} \times 0.08 = 8.0$ mol/hr.
- Moles CO$_2$ removed: $8.0 \, \text{mol/hr} \times 0.65 = 5.2$ mol/hr.
- Percent change in total gas flow rate: $\frac{5.2 \, \text{mol/hr removed}}{100 \, \text{mol/hr total in}} = 5.2\%$.

**Rule of Thumb: Concentrated Systems:** When the amount of solute transferred causes the total molar flow rate of either the gas or liquid phase to change by more than 5-10\%, the system should be treated as **concentrated**. This requires using constant **solute-free flow rates** (G for carrier gas, S for solvent) and compositions expressed as **mole ratios** (Y, X).

**Step 2: Define Solute-Free Flow Rates and Mole Ratios**
- **Carrier Gas Flow ($G$):** The inert N$_2$ flow is constant: $G = 100 \cdot (1-0.08) = 92$ mol/hr.
- **Solvent Flow ($S$):** The flow of pure water, to be determined.
- **Mole Ratios:** $Y = \frac{\text{moles CO}_2}{\text{moles N}_2}$, $X = \frac{\text{moles CO}_2}{\text{moles H}_2\text{O}}$.
- **Known Compositions in Mole Ratios:**
    - Inlet gas ($Y_{N+1}$): $Y_{N+1} = \frac{y_{in}}{1-y_{in}} = \frac{0.08}{1-0.08} = 0.0870$.
    - Outlet gas ($Y_1$): Moles CO$_2$ out = $8.0 - 5.2 = 2.8$ mol/hr. $Y_1 = \frac{2.8}{92} = 0.0304$.
    - Inlet liquid ($X_0$): Pure water, so $X_0 = 0$.

**Step 3: Convert Equilibrium Data to Mole Ratios**
The VLE data ($y = 1640x$) must be converted to mole ratios using the relations $Y = y/(1-y)$ and $X = x/(1-x)$. This results in a *curved* equilibrium line on a Y-X plot.

**Step 4: Determine the Operating Line**
The operating line on a Y-X plot is a straight line with slope $S/G$. We first find the minimum slope by finding the pinch point at the bottom of the column.
- At the pinch, the exiting liquid $X_{N,max}$ is in equilibrium with the entering gas $Y_{N+1}=0.0870$.
- Convert to mole fractions to use VLE data: $y = Y/(1+Y) = 0.0870/(1.0870) = 0.0800$.
- Find equilibrium liquid mole fraction: $x = y/1640 = 0.0800/1640 = 4.88 \times 10^{-5}$.
- Convert back to mole ratio: $X_{N,max} = x/(1-x) \approx 4.88 \times 10^{-5}$.
- $(S/G)_{min} = \frac{Y_{N+1} - Y_1}{X_{N,max} - X_0} = \frac{0.0870 - 0.0304}{4.88 \times 10^{-5} - 0} = 1160$.
- $(S/G)_{actual} = 1.5 \cdot (S/G)_{min} = 1.5 \cdot 1160 = 1740$.

**Step 5: Graphical Solution**
We plot the curved equilibrium line and the straight operating line (slope=1740, passing through $(X_0, Y_1) = (0, 0.0304)$). We then step off the stages starting from the bottom point $(X_N, Y_{N+1})$. By constructing the staircase on the Y-X diagram, we find that we cross the target outlet gas composition of $Y_1 = 0.0304$ after approximately **1.9 equilibrium stages**.

**Final Answer Summary for Example 2**
The graphical analysis shows that 1.9 equilibrium stages are needed. Therefore, we would design the column with **2 theoretical stages**.

```

## Stripping Columns

**Stripping**, also known as desorption, is a mass transfer operation that is the reverse of absorption. Its purpose is to selectively remove a dissolved solute from a liquid stream by contacting it with a gas, known as the **stripping agent**.

```{note}
**The Principle of Stripping**
Like absorption, stripping is typically carried out in a counter-current column. The solute-rich liquid enters at the top, and the clean stripping gas enters at the bottom. The counter-current flow maximizes the concentration difference at every point, providing the driving force for the solute to transfer **from the liquid phase to the gas phase**.
```

### Fundamental Principles and Equations

The design equations for stripping are identical in form to those for absorption; however, the relative positions of the operating and equilibrium lines are different, and the direction of mass transfer is from liquid to gas.

```{important}
**Key Stripping Equations**

**Equilibrium Relationship (Henry's Law):**
For dilute solutions, the equilibrium between the liquid and gas on a given stage is described by Henry's Law.

$$
y_n = m \cdot x_n \quad \text{where } m = H/P
$$

**The Operating Line (Material Balance):**
A material balance on the solute relates the compositions of the passing streams between stages.

$$
y_{n+1} = \left(\frac{L}{V}\right)x_n + \left(y_1 - \frac{L}{V}x_0\right)
$$


```

```{admonition} Term Definitions
:class: tip
- $x_0$: Mole fraction of solute in the **entering liquid feed** (at the top, stage 1).
- $x_N$: Mole fraction of solute in the **exiting stripped liquid** (at the bottom, stage N).
- $y_{N+1}$: Mole fraction of solute in the **entering stripping gas** (at the bottom). Often this is 0.
- $y_1$: Mole fraction of solute in the **exiting solute-rich gas** (at the top).
- $L, V$: Molar flow rates of the liquid and gas [mol/time].
```

### Graphical Method for Stripping Columns

```{note}
**Key Feature of the Stripping Diagram**
The number of theoretical stages for a stripping column can be found graphically on an x-y diagram. The key difference from absorption is that the **operating line must lie below the equilibrium line**. This ensures that at every point in the column, the actual vapor-phase concentration ($y$) is lower than the equilibrium concentration, providing a driving force for the solute to move from the liquid to the gas phase.
```

```{dropdown} Graphical Procedure for Stage Calculation
The number of stages is found by constructing a staircase between the equilibrium line and the operating line. It is often intuitive to start from the top of the column (stage 1).
1. **Plot the Lines:** Draw the equilibrium line ($y=mx$) and the operating line, which is the straight line connecting the known top-of-column point $(x_0, y_1)$ and bottom-of-column point $(x_N, y_{N+1})$.
2. **Begin at Stage 1:** The liquid entering the column is $x_0$. This liquid enters Stage 1. Find the point $(x_0, y_1)$ on the diagram. This point is on the operating line. The liquid leaving stage 1 ($x_1$) is in equilibrium with the vapor leaving stage 1 ($y_1$). To find $x_1$, start at $y_1$ and move **horizontally to the right** to the **equilibrium line**. The x-coordinate of this point is $x_1$.
3. **Move to Stage 2:** The liquid $x_1$ flows from stage 1 to stage 2. The vapor that it passes, which is rising from stage 2, is $y_2$. Their compositions are related by the operating line. To find $y_2$, start at $x_1$ and move **vertically up** to the **operating line**. The y-coordinate is $y_2$.
4. **Repeat:** Now find the liquid on stage 2 ($x_2$) that is in equilibrium with $y_2$ by moving **horizontally to the right** to the **equilibrium line**. This completes the step for Stage 2. Continue this process—vertically to the operating line, horizontally to the equilibrium line—counting each "triangle" as one stage, until the liquid composition $x$ is less than or equal to the desired exit liquid composition, $x_N$.
```

### Effect of Operating Parameters

The performance of a stripping column is highly sensitive to the operating conditions. Understanding these effects is key to efficient design.

```{note}
**Effect of Temperature (T)**
- **What it Affects:** The **Equilibrium Line**.
- **How:** Increasing temperature generally *decreases* the solubility of a gas in a liquid, making it easier to strip out. This increases the Henry's constant, $H$, and thus the slope of the equilibrium line ($m=H/P$).
- **Result:** A higher temperature moves the equilibrium line **further away** from the operating line. This increases the size of the graphical steps, meaning **fewer stages are required**.
- **Conclusion:** Stripping is favored at **higher temperatures**.
```

```{note}
**Effect of Pressure (P)**
- **What it Affects:** The **Equilibrium Line**.
- **How:** The slope of the equilibrium line, $m=H/P$, is inversely proportional to the total pressure $P$.
- **Result:** Decreasing the system pressure increases the slope of the equilibrium line, moving it further away from the operating line. This means **fewer stages are required**.
- **Conclusion:** Stripping is favored at **lower pressures**.
```

```{note}
**Effect of Stripping Gas Flow Rate (V)**
- **What it Affects:** The **Operating Line**.
- **How:** The slope of the operating line is $L/V$. Increasing the stripping gas flow rate $V$ (for a fixed liquid rate $L$) *decreases* the slope of the operating line.
- **Result:** A lower slope moves the operating line **further away** from the equilibrium line. This increases the size of the steps, meaning **fewer stages are required**.
- **Conclusion and Trade-off:** A higher stripping gas flow rate requires a smaller, cheaper column (lower capital cost) but has a higher operating cost (compressing and supplying more gas). The theoretical **minimum stripping gas rate** corresponds to an operating line that touches the equilibrium line (a "pinch point"), which would require an infinite number of stages. Engineers must choose an optimal V that balances these costs.
```

### Example Problem: Stripping an Organic from Water

```{prf:example} Stripping an Organic from Water
A single-stage stripping process is used to remove a dissolved organic compound from a water stream. The contaminated water enters the stage at 20$^\circ$C with an organic concentration of 0.05 mol\%. A stream of pure, dry air at 5 bar is contacted with the water to act as the stripping agent. The Henry's Law constant for the organic in water at this temperature is 2.5 bar. What flow rate of air (in moles of air per mole of water) is needed to reduce the amount of organic in the water by 95\%?
```

```{dropdown} Solution Steps
**Step 1: Strategy and Process Basis**
The core of this problem is a material balance on the organic solute around the single equilibrium stage. We will relate the compositions of the exiting liquid and vapor streams using Henry's Law. Since the air flow rate is the unknown, we will solve the material balance for this quantity. Let's first establish a basis for our calculation.

**Calculation Basis and Streams:**
- **Basis:** 1 mole of contaminated water entering the process ($L_{in} = 1$ mol).
- **Liquid In ($L_{in}$):** Contains water and the organic solute.
- **Gas In ($V_{in}$):** Contains $n_{air}$ moles of pure, dry air.
- **Liquid Out ($L_{out}$):** Contains the remaining water and organic. Assumed to be in equilibrium with $V_{out}$.
- **Gas Out ($V_{out}$):** Contains the inlet air plus the stripped organic. Assumed to be in equilibrium with $L_{out}$.

Our goal is to find the ratio $n_{air} / L_{in}$. Since our basis is $L_{in}=1$ mol, we just need to find the value of $n_{air}$.

**Step 2: Material Balance on the Organic Solute**
First, let's quantify the moles of the organic contaminant (C) entering and leaving based on our 1-mole basis.
- **Moles of C IN:** The inlet water has a concentration of 0.05 mol\%, which is a mole fraction of $x_{C,in} = 0.0005$.

  $$
  n_{C,in} = x_{C,in} \cdot L_{in} = (0.0005) \cdot (1 \, \text{mol}) = 5 \times 10^{-4} \, \text{mol}
  $$

- **Moles of C OUT (in Liquid):** The process removes 95\% of the organic, meaning 5\% remains in the liquid.

  $$
  n_{C,L,out} = 0.05 \cdot n_{C,in} = 0.05 \cdot (5 \times 10^{-4}) = 2.5 \times 10^{-5} \, \text{mol}
  $$

- **Moles of C OUT (in Gas):** By difference, 95\% of the inlet organic must have been transferred to the air stream.

  $$
  n_{C,V,out} = 0.95 \cdot n_{C,in} = 0.95 \cdot (5 \times 10^{-4}) = 4.75 \times 10^{-4} \, \text{mol}
  $$

**Step 3: State Simplifying Assumptions**
**Key Simplifying Assumptions:**
To simplify the calculation, we will make two initial assumptions, which are common for processes with very low solute concentrations. We will check their validity later.
1. The total molar flow rate of the liquid stream is approximately constant ($L_{out} \approx L_{in} = 1$ mol).
2. The total molar flow rate of the gas stream is approximately constant ($V_{out} \approx V_{in} = n_{air}$). This implies that both the amount of solute transferred and the amount of water evaporated are negligible compared to the air flow.

**Step 4: Use Equilibrium Relationship (Henry's Law)**
Because this is an equilibrium stage, the exiting liquid and gas streams are in thermodynamic equilibrium. We can relate their compositions using Henry's Law.

$$
y_C \cdot P_{total} = x_C \cdot H_C
$$

First, let's find the mole fraction in the exiting liquid, $x_{C,out}$, using our simplifying assumptions:

$$
x_{C,out} = \frac{\text{moles of C in liquid out}}{\text{total moles of liquid out}} \approx \frac{n_{C,L,out}}{L_{in}} = \frac{2.5 \times 10^{-5} \, \text{mol}}{1 \, \text{mol}} = 2.5 \times 10^{-5}
$$

Now, use Henry's Law to find the corresponding equilibrium mole fraction in the exiting gas, $y_{C,out}$:

$$
y_{C,out} = \frac{x_{C,out} \cdot H_C}{P_{total}} = \frac{(2.5 \times 10^{-5}) \cdot (2.5 \, \text{bar})}{5 \, \text{bar}} = 1.25 \times 10^{-5}
$$

**Step 5: Calculate the Required Air Flow Rate**
We know the total moles of contaminant leaving in the gas stream ($n_{C,V,out}$) and its mole fraction in that stream ($y_{C,out}$). We can use these to find the total moles of the exiting gas stream, $V_{out}$.

$$
n_{C,V,out} = y_{C,out} \cdot V_{out}
$$

$$
4.75 \times 10^{-4} \, \text{mol} = (1.25 \times 10^{-5}) \cdot V_{out}
$$

$$
V_{out} = \frac{4.75 \times 10^{-4}}{1.25 \times 10^{-5}} = 38 \, \text{moles}
$$

Based on our simplifying assumption that $V_{out} \approx V_{in} = n_{air}$, the required air flow rate is 38 moles.

**Step 6: Evaluate the Assumptions**
Is it valid to assume the total flow rates are constant? Let's check the two effects we ignored.
- **Solute Transfer:** The amount of organic transferred ($4.75 \times 10^{-4}$ mol) is tiny compared to the water (1 mol) and air (38 mol) flows. This part of the assumption is excellent.
- **Water Evaporation:** Dry air enters and will become saturated with water vapor. The exiting liquid is almost pure water, so $x_W \approx 1$. The saturation pressure of water at 20$^\circ$C is $P_{W,sat} \approx 0.0234$ bar. The mole fraction of water in the exit gas will be:

  $$
  y_W = \frac{x_W P_{W,sat}}{P_{total}} \approx \frac{1 \cdot (0.0234 \, \text{bar})}{5 \, \text{bar}} = 0.00468
  $$

  The moles of water that evaporate into the exiting gas stream is:

  $$
  n_{W,evap} = \frac{y_W}{1-y_W-y_C} \cdot (n_{air}+n_{C,V,out}) \approx y_W \cdot V_{out} \approx (0.00468) \cdot (38) = 0.178 \, \text{mol}
  $$
  
  The total exiting gas flow is actually $V_{out} = n_{air} + n_{C,V,out} + n_{W,evap} \approx 38 + 0.000475 + 0.178 \approx 38.18$ moles. This is very close to our assumed 38 moles, so the assumption that $V_{out} \approx V_{in}$ is reasonable for this calculation. However, the water loss ($0.178$ mol) is nearly 18\% of the inlet liquid, which might be significant depending on the process objectives.

**Final Answer Summary**
To achieve 95\% removal of the organic compound, approximately **38 moles of air are needed per mole of water**. The high ratio of air to water is required because the organic is not highly volatile out of water.

```

---

## PE Exam Practice Problems

```{prf:example} Practice Problem 1 — McCabe-Thiele Minimum Reflux

A distillation column separates a binary mixture of benzene (more volatile) and toluene. The feed is 40 mol% benzene, saturated liquid ($q = 1$). The distillate specification is $x_D = 0.95$ mol fraction benzene and the bottoms specification is $x_B = 0.05$.

The equilibrium data at the feed composition gives $y^* = 0.62$ when $x = 0.40$.

**(a)** What is the minimum reflux ratio $R_{min}$?

**(b)** At an operating reflux ratio $R = 1.5\,R_{min}$, what is the slope of the rectifying operating line?
```

```{dropdown} Solution

**Part (a): Minimum reflux**

At minimum reflux, the rectifying operating line passes through the pinch point $(x_q, y_q^*)$. For a saturated liquid feed ($q=1$), the $q$-line is vertical at $x = x_F = 0.40$, so the pinch point is $(0.40,\, 0.62)$.

The rectifying operating line at minimum reflux passes through $(x_D, x_D) = (0.95, 0.95)$ and $(0.40, 0.62)$:

$$\text{slope} = \frac{L}{V} = \frac{y_D - y_q}{x_D - x_q} = \frac{0.95 - 0.62}{0.95 - 0.40} = \frac{0.33}{0.55} = 0.600$$

Since $L/V = R/(R+1)$:

$$R_{min} = \frac{L/V}{1 - L/V} = \frac{0.600}{0.400} = \mathbf{1.50}$$

**Part (b): Operating reflux slope**

$$R = 1.5 \times 1.50 = 2.25$$

$$\frac{L}{V} = \frac{R}{R+1} = \frac{2.25}{3.25} = \mathbf{0.692}$$

The rectifying operating line: $y = 0.692\,x + (1-0.692) \times x_D = 0.692\,x + 0.308 \times 0.95 = 0.692\,x + 0.293$
```

---

```{prf:example} Practice Problem 2 — Unsteady Diffusion (Fick's Law)

A large slab of rubber initially contains no solvent ($C_{A0} = 0$). One surface is suddenly exposed to a solvent vapor maintaining $C_{As} = 0.8$ kg/m³ at the surface. The diffusivity of solvent in rubber is $D_{AB} = 8 \times 10^{-12}$ m²/s.

How long (in hours) does it take for the solvent concentration at a depth of 2 mm to reach 0.20 kg/m³?
```

```{dropdown} Solution

**Step 1: Calculate the concentration ratio**

$$\frac{C_A - C_{A0}}{C_{As} - C_{A0}} = \frac{0.20 - 0}{0.80 - 0} = 0.25$$

**Step 2: Relate to error function**

$$0.25 = 1 - \text{erf}\!\left(\frac{x}{2\sqrt{D_{AB}t}}\right) \implies \text{erf}\!\left(\frac{x}{2\sqrt{D_{AB}t}}\right) = 0.75$$

**Step 3: Find the error function argument**

From erf tables: $\text{erf}(0.814) \approx 0.75$, so:

$$\frac{x}{2\sqrt{D_{AB}t}} = 0.814$$

**Step 4: Solve for $t$**

$$\sqrt{D_{AB}t} = \frac{x}{2 \times 0.814} = \frac{0.002}{1.628} = 1.229 \times 10^{-3} \text{ m}$$

$$D_{AB}t = (1.229\times10^{-3})^2 = 1.510\times10^{-6} \text{ m}^2$$

$$t = \frac{1.510\times10^{-6}}{8\times10^{-12}} = 188{,}750 \text{ s} = \mathbf{52.4 \text{ hours}}$$
```

```{caution}
**PE Exam Traps — Mass Transfer**

- **Mole fraction vs. mole ratio in absorption:** Operating and equilibrium lines on an absorption diagram are often plotted in mole ratio ($Y = y/(1-y)$) coordinates for concentrated systems. Using mole fractions when mole ratios are required makes the operating line curved instead of straight — the stage count will be wrong.
- **Absorption vs. stripping — which phase is which:** In absorption, the solute transfers from gas to liquid (gas is stripped, liquid is loaded). In stripping, it goes liquid → gas. The operating line is above the equilibrium curve for absorption, below for stripping. Drawing these backwards is a common diagram error.
- **Minimum reflux pinch point location:** For a saturated liquid feed ($q=1$), the pinch is at the intersection of the $q$-line (vertical at $x_F$) with the equilibrium curve. For a partially vaporized feed ($0 < q < 1$), the $q$-line has a negative slope — the pinch point shifts. Don't assume the pinch is always at the feed tray composition.
- **Error function argument:** The argument of erf is $x/(2\sqrt{Dt})$, not $x/\sqrt{Dt}$ (missing the factor of 2 is extremely common). If you get an erf argument greater than ~2.5, recheck — erf saturates at 1.0 for large arguments.
- **Fick's First vs. Second Law:** First Law ($J = -D\,dC/dz$) is for steady-state. Second Law ($\partial C/\partial t = D\,\partial^2C/\partial x^2$) is for unsteady. Using a steady-state flux equation to analyze a time-varying concentration profile gives nonsense.
```