---
author: PE Study Guide
date: "2025"
title: Fluid Mechanics Study Guide
---

# Fluid Mechanics

## Quick Reference: Key Equations

| Topic | Formula | Notes |
|-------|---------|-------|
| Mech. energy balance | $\frac{\Delta P}{\rho} + \frac{\Delta u^2}{2} + g\Delta z + \hat{F} = \frac{\dot{W}_s}{\dot{m}}$ | Real fluid |
| Bernoulli (ideal) | $\frac{P}{\rho} + \frac{u^2}{2} + gz = \text{const}$ | No friction, no shaft work |
| Reynolds number | $Re = \frac{\rho u D}{\mu} = \frac{u D}{\nu}$ | Laminar $<2100$, Turbulent $>4000$ |
| Darcy-Weisbach | $\hat{F} = f \frac{L}{D} \frac{u^2}{2}$ | $f$ = Darcy friction factor |
| Hagen-Poiseuille | $\Delta P = \frac{128 \mu L Q}{\pi D^4}$ | Laminar flow only |
| Continuity | $\dot{m} = \rho_1 A_1 u_1 = \rho_2 A_2 u_2$ | Steady state |
| Hydrostatic pressure | $\Delta P = \rho g \Delta z$ | Incompressible fluid |
| Pump power | $\dot{W}_p = \dot{m}\,g\,\Delta z + \dot{m}\,\hat{F} + \dot{m}\,\Delta P/\rho$ | From MEB |
| Pump efficiency | $\eta = \dot{W}_{fluid}/\dot{W}_{shaft}$ | Always $<1$ |
| Venturi / orifice | $u_2 = \sqrt{\frac{2(P_1-P_2)/\rho}{1-(A_2/A_1)^2}}$ | From Bernoulli + continuity |
| Manometer | $P_1 - P_2 = (\rho_{fluid} - \rho_{ref})g\Delta h$ | U-tube |
| Newtonian shear | $\tau = \mu\,\frac{du}{dy}$ | $\mu$ = dynamic viscosity |
| Kinematic viscosity | $\nu = \mu/\rho$ | [m²/s] |

---

## Mechanical Energy Balance

The Mechanical Energy Balance is a fundamental tool in fluid dynamics, derived from the first law of thermodynamics. It is used to analyze systems where mechanical forms of energy are of primary interest, such as in pipe flow, pumps, and turbines.

### Fundamental Equations

```{admonition} Term Definitions
:class: tip

- $\Delta P$: Change in pressure ($P_{out} - P_{in}$) [Pa].
- $\rho$: Fluid density [kg/m$^3$].
- $\Delta u^2$: Change in the square of the average fluid velocity ($u_{out}^2 - u_{in}^2$) [m$^2$/s$^2$].
- $g$: Gravitational constant (9.81 m/s$^2$).
- $\Delta z$: Change in elevation ($z_{out} - z_{in}$) [m].
- $\dot{W}_s$: Rate of shaft work added to the fluid (by a pump) or removed from the fluid (by a turbine) [J/s or W].
- $\dot{m}$: Mass flow rate of the fluid [kg/s].
- $\hat{F}$: Frictional energy loss per unit mass [J/kg]. This term is always positive.

```

```{important}
**Mechanical Energy Balance (with Friction):**
This is the most common form used for real fluids. The term $\hat{F}$ accounts for the conversion of mechanical energy into thermal energy due to viscous dissipation (friction).

$$

\frac{\Delta P}{\rho} + \frac{\Delta u^2}{2} + g\Delta z + \hat{F} = \frac{\dot{W}_s}{\dot{m}}

$$


```

```{important}
**The Bernoulli Equation (Ideal Fluid):**
This is a simplified form for a system with no shaft work ($\dot{W}_s=0$) and no frictional losses ($\hat{F}=0$). It applies to ideal, inviscid fluid flow.

$$

\frac{\Delta P}{\rho} + \frac{\Delta u^2}{2} + g\Delta z = 0

$$


```

### Derivation from the First Law of Thermodynamics

The Mechanical Energy Balance is a practical rearrangement of the First Law of Thermodynamics for a steady-state, open system.

```{dropdown} Derivation of the Mechanical Energy Balance
1. **Start with the General Energy Balance:** The first law for a steady-state, open system is:

   $$\dot{m} \left( \Delta h + \frac{\Delta u^2}{2} + g\Delta z \right) = \dot{Q} + \dot{W}_s$$

   where $\Delta h$ is the change in specific enthalpy ($h_{out} - h_{in}$).

2. **Introduce the Definition of Enthalpy:** Substitute the definition of specific enthalpy, $h = \bar{U} + Pv$, where $\bar{U}$ is specific internal energy and $v$ is specific volume ($v=1/\rho$):

   $$\dot{m} \left( \Delta \bar{U} + \Delta(Pv) + \frac{\Delta u^2}{2} + g\Delta z \right) = \dot{Q} + \dot{W}_s$$

3. **Apply the Incompressible Fluid Assumption:** For liquids, we can assume the fluid is incompressible, meaning its density $\rho$ (and specific volume $v$) is constant. This simplifies the pressure-volume term:

   $$\Delta(Pv) = P_{out}v - P_{in}v = v(P_{out} - P_{in}) = v\Delta P = \frac{\Delta P}{\rho}$$

4. **Rearrange and Define Frictional Loss:** Substitute the simplified pressure term and divide the entire equation by the mass flow rate $\dot{m}$:

   $$\Delta \bar{U} + \frac{\Delta P}{\rho} + \frac{\Delta u^2}{2} + g\Delta z = \frac{\dot{Q}}{\dot{m}} + \frac{\dot{W}_s}{\dot{m}}$$

   Moving the internal energy and heat transfer terms to the left side isolates the mechanical terms:

   $$\frac{\Delta P}{\rho} + \frac{\Delta u^2}{2} + g\Delta z + \left( \Delta \bar{U} - \frac{\dot{Q}}{\dot{m}} \right) = \frac{\dot{W}_s}{\dot{m}}$$
   
   The term $(\Delta \bar{U} - \dot{Q}/\dot{m})$ represents the irreversible loss of mechanical energy to friction. We define this group as the frictional loss term, $\hat{F}$, which gives the final form of the balance.

```

### Example: Flow from a Coffee Urn

```{prf:example} Flow from Coffee Urn
**Question:** A 60-cm tall coffee urn is filled to the top. It dispenses coffee through a 0.7-cm diameter nozzle that is 12 cm above the table surface. How long does it take to pour a 200-mL cup of coffee?

```

```{dropdown} Solution Steps
**Step 1: Strategy and Assumptions:**
We can model this using the Bernoulli equation, which is appropriate for low-viscosity fluids with negligible friction over short distances. We apply the equation between the top surface of the coffee (point 1) at height $z_1 = 0.60$ m and the nozzle exit (point 2) at height $z_2 = 0.12$ m. We assume no friction and no shaft work.

**Step 2: Analyze the Bernoulli Equation Terms:**

$$

\frac{P_2 - P_1}{\rho} + \frac{u_2^2 - u_1^2}{2} + g(z_2 - z_1) = 0

$$

Pressure: Both the top surface and nozzle exit are open to atmosphere, so $P_1 = P_2$ and $\Delta P = 0$.
Velocity: The urn diameter is much larger than the nozzle, so the liquid level drops slowly and $u_1 \approx 0$. We solve for the exit velocity $u_2$.
Potential Energy: The height change is $z_2 - z_1 = 0.12 - 0.60 = -0.48$ m.

**Step 3: Solve for Exit Velocity ($u_2$):**
The Bernoulli equation simplifies to Torricelli's Law:

$$

\frac{u_2^2}{2} + g(-0.48 \, \text{m}) = 0 \implies u_2 = \sqrt{2 \cdot g \cdot (0.48 \, \text{m})}

$$

$$

u_2 = \sqrt{2 \cdot (9.81 \, \text{m/s}^2) \cdot (0.48 \, \text{m})} = \sqrt{9.4176 \, \text{m}^2/\text{s}^2} = 3.069 \, \text{m/s}

$$

**Step 4: Calculate Time to Fill Cup:**
Find the volumetric flow rate through the nozzle. The nozzle area is $A_2 = \frac{\pi d^2}{4} = \frac{\pi (0.007)^2}{4} = 3.848 \times 10^{-5} \, \text{m}^2$.
The volumetric flow rate is $v = A_2 \cdot u_2 = (3.848 \times 10^{-5}) \cdot (3.069) = 1.181 \times 10^{-4} \, \text{m}^3/\text{s}$.
For a 200 mL cup ($2 \times 10^{-4} \, \text{m}^3$):

$$

\text{Time} = \frac{2 \times 10^{-4}}{1.181 \times 10^{-4}} = 1.69 \, \text{s}

$$

The time required is approximately **1.7 seconds**.

```

### Example: Vertical Water Jet

```{prf:example} Vertical Water Jet

**Question:** Water flows through a 2.5-cm ID pipe at 115 L/min and 0.15-bar gauge pressure. It vents vertically 1.0 m above the pipe. How high will the water shoot from the vent? Assume no frictional losses.
```

```{dropdown} Solution Steps

**Step 1: Strategy and Coordinate System:**
We will apply the Bernoulli equation between a point inside the pipe just before the vent (point 1) and the highest point of the water jet (point 2). We assume no friction and steady state. Let the centerline of the pipe be the reference height, so $z_1 = 0$. Point 2 is the peak of the jet's trajectory at height $z_2 = 1.0 \, \text{m} + H$, where $H$ is the height above the vent.

**Step 2: Analyze the Bernoulli Equation Terms:**
The Bernoulli equation states that the total mechanical energy is conserved between points 1 and 2.

$$

\frac{P_1}{\rho} + \frac{u_1^2}{2} + gz_1 = \frac{P_2}{\rho} + \frac{u_2^2}{2} + gz_2

$$

Given: $P_1 = 0.15$ bar (gauge), $P_2 = 0$ bar (gauge) at atmospheric pressure, $u_2 = 0$ m/s at maximum height, $z_1 = 0$ m and $z_2 = 1.0 + H$.

**Step 3: Calculate Inlet Velocity ($u_1$):**
Convert the volumetric flow rate to SI units:

$$

v = 115 \frac{\text{L}}{\text{min}} \times \frac{1 \, \text{m}^3}{1000 \, \text{L}} \times \frac{1 \, \text{min}}{60 \, \text{s}} = 0.001917 \, \text{m}^3/\text{s}

$$

The pipe area is $A_1 = \frac{\pi d^2}{4} = \frac{\pi (0.025 \, \text{m})^2}{4} = 0.0004909 \, \text{m}^2$.

$$

u_1 = \frac{v}{A_1} = \frac{0.001917 \, \text{m}^3/\text{s}}{0.0004909 \, \text{m}^2} = 3.905 \, \text{m/s}

$$

**Step 4: Solve for Height ($H$):**
Substitute the known values into the Bernoulli equation using SI units. Convert $P_1 = 0.15 \, \text{bar} = 15,000 \, \text{Pa}$ and use $\rho_{water} = 1000$ kg/m$^3$ and $g = 9.81$ m/s$^2$.

$$

\frac{15000}{1000} + \frac{(3.905)^2}{2} + 0 = 0 + 0 + 9.81 \cdot (1.0 + H)

$$

$$

15.0 + 7.625 = 9.81 \cdot (1.0 + H)

$$

$$

H = \frac{22.625}{9.81} - 1.0 = 2.306 - 1.0 = 1.306 \, \text{m}

$$

The water will shoot approximately **1.3 meters** above the vent.

```

## The Bernoulli Equation: A Force Balance Approach

While the Mechanical Energy Balance is derived from thermodynamics (an energy balance), the famous Bernoulli equation can also be understood from first principles using Newton's second law ($\vec{F}=m\vec{a}$), which is a force balance. This approach provides a deeper physical intuition for how pressure, velocity, and elevation are related in a moving fluid.

### Fundamental Equations

The derivation begins with a force balance on a tiny fluid element and, after several key simplifying assumptions, results in the well-known algebraic form of the Bernoulli equation.

```{admonition} Term Definitions
:class: tip

- $\nu$: Fluid velocity along a streamline [m/s]. (Note: We use $\nu$ here to distinguish it from reactor volume $V$).
- $P$: Static pressure, the pressure you would feel if you were moving with the fluid [Pa or N/m$^2$].
- $\rho$: Fluid density [kg/m$^3$].
- $g$: Acceleration due to gravity (9.81 m/s$^2$).
- $\gamma$: Specific weight of the fluid, defined as $\gamma = \rho g$ [N/m$^3$].
- $z$: Elevation height, measured vertically from a reference point [m].
- $A$: Cross-sectional area of flow [m$^2$].
- $s$: A coordinate that follows the path of the fluid streamline.

```

```{important}
**Euler's Equation: The Equation of Motion**
This is the differential equation resulting directly from the force balance on a fluid element, before integration. It relates the change in velocity, elevation, and pressure along a streamline.

$$

\rho\nu \frac{d\nu}{ds} + \rho g \frac{dz}{ds} + \frac{dP}{ds} = 0

$$


```

```{important}
**The Bernoulli Equation: The Integrated Form**
After integrating Euler's Equation and assuming the fluid is incompressible, we get the classic Bernoulli equation. It states that the sum of the pressure head, velocity head, and elevation head is constant along a single streamline for an ideal fluid.

$$

P + \frac{1}{2}\rho\nu^2 + \rho gz = \text{constant}

$$


```

### Derivation of the Bernoulli Equation

This derivation shows how applying a simple force balance to a small fluid element leads directly to the Bernoulli equation.

```{dropdown} Derivation from Newton's Second Law
1. **Define a Fluid Element and its Acceleration:**
   Imagine a tiny, cylindrical "packet" of fluid moving along a path called a streamline. According to Newton's second law, the sum of the forces on this element ($\sum \delta F_s$) must equal its mass ($\delta m$) times its acceleration ($a_s$) in the direction of the streamline.
   
   $$\sum \delta F_s = (\delta m) a_s$$
   
   The acceleration $a_s = \frac{d\nu}{dt}$ can be rewritten using the chain rule as $a_s = \frac{d\nu}{ds} \frac{ds}{dt}$. Since velocity is the rate of change of position ($\nu = \frac{ds}{dt}$), the acceleration becomes $a_s = \nu \frac{d\nu}{ds}$.

2. **Analyze the Forces (with a Key Assumption):**

   **Crucial Assumption: Inviscid Flow**

   To simplify the force analysis, we make our first major assumption: the fluid is **inviscid**, meaning it has zero viscosity. This implies that there are no frictional (shear) forces between fluid layers or between the fluid and the pipe walls. The only forces we consider are pressure and gravity.

   - **Gravity Force:** The weight of the element is its specific weight times its volume, $\delta W = \gamma \cdot \delta V$. The component of this force acting along the streamline (opposing the motion) is $-\delta W \sin\theta = -(\gamma \sin\theta) \delta V$.
   - **Pressure Force:** If the pressure changes along the streamline, there will be a net force. The net pressure force is caused by the pressure gradient and is given by $\delta F_{ps} = -\frac{dP}{ds} \delta V$.

3. **Form the Equation of Motion:**
   Now we plug the forces and the acceleration term back into Newton's law:
   
   $$\left(-\gamma \sin\theta - \frac{dP}{ds}\right)\delta V = (\rho \delta V) \left(\nu \frac{d\nu}{ds}\right)$$
   
   The differential volume element $\delta V$ cancels from all terms, giving Euler's equation of motion. We can also substitute $\gamma = \rho g$ and, from trigonometry, recognize that $\sin\theta = \frac{dz}{ds}$ (the change in height over the change in path length).
   
   $$-\rho g \frac{dz}{ds} - \frac{dP}{ds} = \rho\nu \frac{d\nu}{ds}$$

4. **Integrate Along the Streamline:**
   
   To get from this differential equation to an algebraic one, we make another key assumption: the flow is **steady** (it doesn't change with time). We can then multiply the entire equation by $ds$ and integrate each term along the streamline:

   $$\int dP + \int \rho\nu d\nu + \int \rho g dz = \text{constant}$$

5. **Apply the Incompressible Assumption:**

   To solve the integrals, we make our final key assumption: the fluid is **incompressible**, meaning its density $\rho$ is constant. The terms can now be integrated easily:

   $$P + \frac{1}{2}\rho\nu^2 + \rho g z = \text{constant}$$
   
   This is the Bernoulli equation, which holds for any two points along the same streamline in a steady, inviscid, incompressible flow.

```

### Applications of the Bernoulli Equation

```{prf:example} Air Flow Through Pipe and Nozzle
**Question:** Air flows steadily through a horizontal pipe of 10 cm diameter. It exits into the atmosphere through an 8 cm diameter nozzle. The gauge pressure in the pipe is 800 Pa. Assuming air is incompressible with a density of 1.23 kg/m$^3$, what is the velocity of the air at the exit?

```

```{dropdown} Solution Steps
**Step 1: Strategy: Using Two Equations for Two Unknowns**
This problem involves two unknown velocities: the velocity inside the pipe ($\nu_1$) and the velocity at the nozzle exit ($\nu_2$). To solve for two unknowns, we need two independent equations. We will use:
1. The **Bernoulli Equation**, which relates pressure and velocity changes (an energy relationship).
2. The **Continuity Equation**, which relates velocities and areas (a mass balance).
We apply these equations between point 1 (inside the pipe) and point 2 (at the nozzle exit).

**Step 2: Apply the Bernoulli Equation:**

$$

\frac{P_1}{\rho} + \frac{\nu_1^2}{2} + gz_1 = \frac{P_2}{\rho} + \frac{\nu_2^2}{2} + gz_2

$$

We simplify this equation based on the problem statement:
- **Potential Energy:** The pipe is horizontal, so the elevation is constant ($z_1 = z_2$). The $gz$ terms cancel out.
- **Pressure:** We are given gauge pressures (pressure above atmospheric). $P_1 = 800$ Pa. The nozzle exits to the atmosphere, so its gauge pressure is $P_2 = 0$ Pa.

The simplified equation becomes: $\frac{P_1}{\rho} + \frac{\nu_1^2}{2} = \frac{\nu_2^2}{2}$. Rearranging gives our first main equation:

$$

P_1 = \frac{1}{2}\rho (\nu_2^2 - \nu_1^2)

$$

**Step 3: Apply the Continuity Equation:**
The continuity equation is a statement of mass conservation. For an incompressible fluid ($\rho = \text{constant}$), it simplifies to the volumetric flow rate being constant: $A_1 \nu_1 = A_2 \nu_2$. We can express $\nu_1$ in terms of $\nu_2$:

$$

\nu_1 = \nu_2 \left( \frac{A_2}{A_1} \right) = \nu_2 \left( \frac{\pi d_2^2 / 4}{\pi d_1^2 / 4} \right) = \nu_2 \left( \frac{d_2}{d_1} \right)^2

$$

$$

\nu_1 = \nu_2 \left( \frac{8 \, \text{cm}}{10 \, \text{cm}} \right)^2 = \nu_2 (0.8)^2 = 0.64 \nu_2

$$

This is our second main equation.

**Step 4: Solve the System of Equations:**
Now we substitute the expression for $\nu_1$ from Step 3 into the equation from Step 2:

$$

P_1 = \frac{1}{2}\rho (\nu_2^2 - (0.64\nu_2)^2) = \frac{1}{2}\rho (\nu_2^2 - 0.4096\nu_2^2) = \frac{1}{2}\rho (0.5904 \nu_2^2)

$$

Finally, we plug in the known values for $P_1$ and $\rho$ and solve for our target variable, $\nu_2$:

$$

800 \, \text{Pa} = \frac{1}{2} (1.23 \, \text{kg/m}^3) (0.5904 \nu_2^2)

$$

$$

800 = (0.615 \, \text{kg/m}^3) (0.5904 \nu_2^2) = 0.363 \cdot \nu_2^2

$$

$$

\nu_2^2 = \frac{800}{0.363} = 2203.8 \implies \nu_2 = \sqrt{2203.8} = 46.94 \, \text{m/s}

$$

The velocity at the exit is approximately **47 m/s**.

**Step 5: Check the Incompressible Assumption:**
Is it valid to treat air as incompressible? The rule of thumb is that this assumption is reasonable if the fluid's velocity is less than 30% of the speed of sound (Mach number $< 0.3$). The speed of sound in air is about 343 m/s. Here, $M \approx 47/343 \approx 0.14$, which is well below 0.3. The assumption is justified.

```

```{prf:example} Flow from Coffee Urn (Torricelli's Law)
**Question:** A 60-cm tall coffee urn is filled to the top. It dispenses coffee through a 0.7-cm diameter nozzle that is 12 cm above the table surface. How long does it take to pour a 200-mL cup of coffee?

```

```{dropdown} Solution Steps
**Step 1: Strategy and Assumptions:**
We apply the Bernoulli equation between the top surface of the coffee (point 1) at height $z_1 = 0.60$ m and the nozzle exit (point 2) at height $z_2 = 0.12$ m. We assume ideal flow: inviscid, steady, and incompressible.

**Step 2: Apply the Bernoulli Equation:**

$$

\frac{P_1}{\rho} + \frac{\nu_1^2}{2} + gz_1 = \frac{P_2}{\rho} + \frac{\nu_2^2}{2} + gz_2

$$

We simplify each term based on the physical situation. For pressure, both the top surface and nozzle exit are open to atmosphere, so $P_1 = P_2 = 0$ gauge and the pressure term cancels. For velocity, the urn's diameter is much larger than the nozzle's, so the surface level drops slowly and $\nu_1 \approx 0$. The height change is $\Delta z = z_2 - z_1 = 0.12 - 0.60 = -0.48$ m.

**Step 3: Solve for Exit Velocity ($\nu_2$):**
The Bernoulli equation simplifies significantly:

$$

0 + 0 + gz_1 = 0 + \frac{\nu_2^2}{2} + gz_2 \implies \frac{\nu_2^2}{2} = g(z_1 - z_2)

$$

This result is known as **Torricelli's Law**. It shows that the exit velocity depends only on the height difference between the surface and the outlet.

$$

\nu_2 = \sqrt{2g(z_1 - z_2)} = \sqrt{2 \cdot (9.81 \, \text{m/s}^2) \cdot (0.48 \, \text{m})} = 3.069 \, \text{m/s}

$$

**Step 4: Calculate Time to Fill Cup:**
Find the volumetric flow rate through the nozzle. Converting the exit velocity to cm/s gives $306.9 \, \text{cm/s}$.

$$

v_{flow} = A_2 \cdot \nu_2 = \left(\frac{\pi (0.7 \, \text{cm})^2}{4}\right) \cdot (306.9 \, \text{cm/s}) = (0.3848 \, \text{cm}^2) \cdot (306.9 \, \text{cm/s}) = 118.1 \, \text{cm}^3/\text{s}

$$

For a 200 mL cup:

$$

\text{Time} = \frac{200 \, \text{cm}^3}{118.1 \, \text{cm}^3/\text{s}} = 1.69 \, \text{s}

$$

The time required is approximately **1.7 seconds**.

```

```{prf:example} Pitot Tube on Plane
**Question:** A pitot-static tube is placed on the nose of a plane traveling 100 m/s at an elevation of 4000 m. What is the pressure difference measured by the device? Assume the density of air is 0.8194 kg/m$^3$ at this elevation.

```

```{dropdown} Solution Steps
**Step 1: Principle of the Pitot Tube:**
A Pitot tube is a pressure-measurement instrument used to measure fluid flow velocity. It works by creating a **stagnation point**, a point in a fluid flow where the local velocity has been brought to zero. By converting the fluid's kinetic energy entirely into pressure energy at this single point, we can deduce the original velocity.

**Step 2: Strategy and Assumptions:**
We apply the Bernoulli equation between a point in the undisturbed free stream far from the plane (point 1) and the stagnation point at the very tip of the Pitot tube (point 2). We assume steady, inviscid, incompressible flow relative to the moving plane.

**Step 3: Apply the Bernoulli Equation:**

$$

\frac{P_1}{\rho} + \frac{\nu_1^2}{2} + gz_1 = \frac{P_2}{\rho} + \frac{\nu_2^2}{2} + gz_2

$$

We simplify the terms for this application. For potential energy, the measurement is made over negligible elevation change, so $z_1 \approx z_2$ and the $gz$ terms cancel. For velocity, the free stream velocity is $\nu_1 = 100$ m/s and the stagnation point has $\nu_2 = 0$ m/s. For pressure, $P_1$ is the static pressure and $P_2$ is the stagnation pressure, with $\Delta P = P_2 - P_1$.

**Step 4: Solve for the Pressure Difference:**
The Bernoulli equation simplifies to:

$$

\frac{P_1}{\rho} + \frac{\nu_1^2}{2} = \frac{P_2}{\rho}

$$

Rearranging gives the dynamic pressure formula:

**Dynamic Pressure**

$$

\Delta P = P_2 - P_1 = \frac{1}{2}\rho \nu_1^2

$$

Substituting the given values:

$$

\Delta P = \frac{1}{2} (0.8194 \, \text{kg/m}^3) (100 \, \text{m/s})^2 = \frac{1}{2} (0.8194) (10000) = 4097 \, \text{Pa}

$$

The pressure difference measured by the device is approximately **4.1 kPa**.

```

## Dimensionless Groups

In the study of fluid mechanics, heat transfer, and mass transfer, we often encounter complex phenomena that are difficult to describe with simple equations. Dimensionless groups are powerful tools that help engineers simplify these complex problems, allowing us to scale experiments and generalize results across a wide range of conditions.

```{note}
**The Power of Dimensionless Groups**

A **dimensionless group** (or dimensionless number) is a quantity that has no physical units. It is formed by creating a ratio of two competing physical quantities, such as different types of forces, rates of energy transport, or time scales. Because the units in the numerator and denominator are designed to cancel out, the result is a pure number.

- **Simplifying Complexity:** They reduce the number of variables in a problem. Instead of studying how a fluid's behavior changes with density, velocity, diameter, and viscosity separately, we can combine them into a single variable: the Reynolds number. This makes analysis much more manageable.
- **Dynamic Similitude and Scaling:** They are the key to making small-scale experiments relevant to large-scale reality. If you can match the key dimensionless numbers for a model airplane in a wind tunnel to those of a real airplane in flight, the flow patterns will be similar. This principle of "dynamic similitude" allows for cost-effective design and testing.
- **Generalizing Results:** Dimensionless groups allow for the creation of universal correlations and charts. For example, the Moody chart, which describes friction in pipes, plots the friction factor against the Reynolds number. This single chart works for water, oil, air, or any other common fluid, regardless of the pipe size.
```

### The Reynolds Number (Re)

The most famous and fundamental dimensionless group in fluid mechanics is the Reynolds number. Its value tells us about the fundamental nature or "regime" of a fluid's flow.

```{important}
**Reynolds Number for Flow in a Pipe**

$$

Re = \frac{\rho \nu D}{\mu}

$$


```

```{note}
**Physical Meaning: A Ratio of Competing Forces**
The Reynolds number represents the ratio of **inertial forces** to **viscous forces** acting on a fluid. You can think of it as a battle between forces promoting chaos and forces promoting order.

$$

Re = \frac{\text{Inertial Forces (tend to cause turbulence)}}{\text{Viscous Forces (tend to resist motion and keep it smooth)}}

$$

- **Inertial Forces** (represented by the numerator, $\rho \nu D$): These forces are related to the fluid's momentum, its tendency to keep moving in a straight line. High density, high velocity, and large pipe diameters contribute to high inertia. At high levels, inertia causes any small disturbance in the flow to grow, leading to chaotic, unpredictable motion.
- **Viscous Forces** (represented by the denominator, $\mu$): These are the forces of internal friction within fluid. Viscosity acts to resist motion and dampen out disturbances, keeping the flow smooth and orderly. Honey has high viscous forces; air has low viscous forces.

```

```{admonition} Interpreting the Reynolds Number for Pipe Flow
:class: tip


The value of the Reynolds number tells us which force is winning the "battle" and thus determines the character of the flow.
- **$Re < 2100$ (Laminar Flow):** At low Reynolds numbers, viscous forces dominate. They are strong enough to suppress any disturbances, and the fluid flows in smooth, parallel layers (or "laminae") with no mixing between them. The flow is orderly, silent, and predictable.
- **$Re > 4000$ (Turbulent Flow):** At high Reynolds numbers, inertial forces dominate. They overwhelm the viscous forces, and any small disturbance grows into large, chaotic eddies and swirls. The flow path of any individual particle is unpredictable. Turbulent flow is associated with high energy dissipation and efficient mixing.
- **$2100 < Re < 4000$ (Transitional Flow):** This is an unstable region where the flow can fluctuate between laminar and turbulent behavior. It is generally avoided in engineering design.

```

### Example: Calculating the Reynolds Number

```{prf:example} Calculating Reynolds Number for Water Flow
**Question:** Water flows through a large pipe with a diameter of 1.0 meter at a velocity of 100 cm/s. The density of water is 1.0 g/cm$^3$ and its viscosity is 1.0 centipoise (cP). Calculate the Reynolds number and determine the flow regime.

```

```{dropdown} Solution Steps
**Step 1: Strategy: The Importance of Consistent Units**
**The Golden Rule of Dimensionless Numbers:** The single most important step in calculating any dimensionless number is to ensure all physical parameters are expressed in a **consistent set of base units** before they are plugged into the formula. Mixing units (e.g., meters and centimeters, or different units of viscosity) is the most common source of error. You can use SI (Meter-Kilogram-Second) or CGS (Centimeter-Gram-Second) or any other consistent system, but you cannot mix them.

**Step 2: Convert All Parameters to the CGS System:**
Let's check each parameter and convert it if necessary.
Density ($\rho$): Given as $1.0 \, \text{g/cm}^3$, already in CGS units.
Velocity ($\nu$): Given as $100 \, \text{cm/s}$, already in CGS units.
Diameter ($D$): Given as $1.0 \, \text{m}$, convert to cm: $D = 1.0 \, \text{m} \times \frac{100 \, \text{cm}}{1 \, \text{m}} = 100 \, \text{cm}$.
Viscosity ($\mu$): Given as $1.0 \, \text{centipoise (cP)}$. The base unit in CGS is the poise, where 1 poise = 1 g/(cm·s), so $\mu = 1.0 \, \text{cP} = 0.01 \, \text{poise} = 0.01 \, \frac{\text{g}}{\text{cm}\cdot\text{s}}$.

**Step 3: Calculate the Reynolds Number:**
Substitute the consistent CGS values into the formula. First, verify that units cancel correctly:

$$

Re = \frac{\rho \nu D}{\mu} \implies \text{Units} = \frac{(\frac{\text{g}}{\text{cm}^3}) \cdot (\frac{\text{cm}}{\text{s}}) \cdot (\text{cm})}{\frac{\text{g}}{\text{cm}\cdot\text{s}}} = \text{Unitless}

$$

Now perform the numerical calculation:

**Reynolds Number Calculation**

$$

Re = \frac{(1.0 \, \text{g/cm}^3) \cdot (100 \, \text{cm/s}) \cdot (100 \, \text{cm})}{0.01 \, \text{g/(cm}\cdot\text{s)}} = \frac{10000}{0.01} = 1,000,000

$$

**Step 4: Conclusion: Determine the Flow Regime**
The calculated Reynolds number is $Re = 1 \times 10^6$. Since $1,000,000 > 4000$ (the critical value for pipe flow), the flow is definitively **turbulent**.

```

### Other Important Dimensionless Groups in Chemical Engineering

```{admonition} Key Dimensionless Groups in Transport Phenomena
:class: tip



| **Name (Symbol)** | **Formula & Physical Meaning** | **Application & Significance** |
| :--- | :--- | :--- |
| **Prandtl Number ($Pr$)** | $Pr = \frac{\text{Momentum Diffusivity}}{\text{Thermal Diffusivity}} = \frac{\nu}{\alpha} = \frac{C_p \mu}{k}$ <br> $\nu$: kinematic viscosity, $\alpha$: thermal diffusivity, $C_p$: specific heat, $\mu$: dynamic viscosity, $k$: thermal conductivity. | Relates the thickness of the velocity boundary layer to the thermal boundary layer. It is a fluid property that connects how momentum and heat move through the fluid. |
| **Nusselt Number ($Nu$)** | $Nu = \frac{\text{Convective Heat Transfer}}{\text{Conductive Heat Transfer}} = \frac{hL}{k}$ <br> $h$: heat transfer coefficient, $L$: characteristic length, $k$: thermal conductivity. | Measures how much heat transfer is enhanced by fluid motion (convection). $Nu=1$ signifies heat transfer by pure conduction only. It is the target variable in most heat transfer correlations. |
| **Schmidt Number ($Sc$)** | $Sc = \frac{\text{Momentum Diffusivity}}{\text{Mass Diffusivity}} = \frac{\nu}{D_{AB}} = \frac{\mu}{\rho D_{AB}}$ <br> $D_{AB}$: mass diffusivity. | The direct mass transfer analog of the Prandtl number. It relates the thickness of the velocity boundary layer to the mass (concentration) boundary layer. |
| **Sherwood Number ($Sh$)** | $Sh = \frac{\text{Convective Mass Transfer}}{\text{Diffusive Mass Transfer}} = \frac{k_c L}{D_{AB}}$ <br> $k_c$: mass transfer coefficient. | The direct mass transfer analog of the Nusselt number. It measures how much mass transfer is enhanced by fluid motion. It is the target variable in most mass transfer correlations. |
| **Peclet Number ($Pe$)** | $Pe = \frac{\text{Advective (Bulk) Transport}}{\text{Diffusive Transport}} = \frac{Lv}{D}$ <br> $L$: length, $v$: velocity, $D$: diffusion coefficient. | Can be written as $Pe_{heat} = Re \cdot Pr$ or $Pe_{mass} = Re \cdot Sc$. In reactor design, it determines if a reactor behaves like an ideal PFR (high Pe, bulk flow dominates) or an ideal CSTR (low Pe, diffusion/mixing dominates). |
| **Froude Number ($Fr$)** | $Fr^2 = \frac{\text{Inertial Forces}}{\text{Gravitational Forces}} = \frac{v^2}{gL}$ <br> $v$: velocity, $g$: gravity, $L$: length. | Crucial in systems with a free surface, like flow in open channels (rivers), flow over dams, and agitated tanks. It helps predict wave formation and surface behavior. |

```

## Fluid Pressure vs. Elevation (Incompressible vs. Compressible Cases)

One of the most fundamental concepts in fluid statics (the study of fluids at rest) is understanding how pressure changes with depth or altitude. The method for calculating this change depends entirely on a crucial property of the fluid: its compressibility. This section will derive the governing equations for both incompressible and compressible fluids and compare the results to a real-world example.

### The Fundamental Equation of Fluid Statics

```{note}
**Why Pressure Changes with Depth**
Imagine a column of fluid at rest, like the water in a swimming pool. A small "packet" or element of fluid within this column is not moving, which means the net force on it must be zero (Newton's First Law). There are three vertical forces acting on this element:
1. A downward force from the pressure of the fluid *above* it.
2. An upward force from the pressure of the fluid *below* it.
3. A downward force due to its own **weight**.

For the element to be stationary, the upward pressure force must perfectly balance the downward pressure force plus the element's weight. This means the pressure below must be slightly greater than the pressure above. This small difference, when summed up over the entire depth, leads to the large pressure changes we experience.

```

```{important}
**The Differential Equation of Fluid Statics**
A formal force balance on a differential fluid element yields the fundamental equation that governs all of fluid statics:

$$

\frac{dP}{dz} = -\gamma = -\rho g

$$


```

```{admonition} Variable Definitions
:class: tip


- $P$: The absolute pressure at a given point in the fluid.
- $z$: The vertical coordinate, or elevation. By convention, $z$ is defined as positive in the **upward** direction.
- $\gamma$: The **specific weight** of the fluid, which is its weight per unit volume. For a fluid with density $\rho$ in a gravitational field $g$, $\gamma = \rho g$.
- The negative sign in the equation is crucial: it means that as elevation ($z$) **increases**, pressure ($P$) **decreases**.

```

### Case 1: The Incompressible Fluid

```{note}
**The Incompressible Fluid Model**
An incompressible fluid is one whose density, $\rho$, is assumed to be constant, regardless of changes in pressure. This is an excellent assumption for most **liquids** (like water or oil) and is a reasonable assumption for gases over very small changes in elevation where the pressure change is minimal.

```

The derivation is straightforward because if $\rho$ is constant, then the specific weight $\gamma = \rho g$ is also constant. We can solve the fundamental equation by direct integration:

$$

dP = -\gamma dz \implies \int_{P_1}^{P_2} dP = \int_{z_1}^{z_2} -\gamma dz \implies P_2 - P_1 = -\gamma (z_2 - z_1)

$$

It is often more intuitive to talk about depth. If we let point 2 be at a depth $h$ below point 1, then $h = z_1 - z_2$. The equation becomes:

```{important}
**Pressure in an Incompressible Fluid**

$$

\Delta P = P_2 - P_1 = \gamma h = \rho g h

$$

**Conclusion:** For an incompressible fluid at rest, pressure increases **linearly** with depth.

```

### Case 2: The Compressible Fluid (Isothermal Ideal Gas)

```{note}
**The Compressible Fluid Model**
A compressible fluid is one whose density changes significantly with pressure. All **gases** are compressible. To solve the static equation, we can no longer treat $\rho$ as a constant. We need an "equation of state" that relates density and pressure. The simplest is the Ideal Gas Law. In this first case, we will also assume the temperature is constant (**isothermal**).

```

The derivation requires separating variables before integrating:

1. Start with the fundamental equation: $\frac{dP}{dz} = -\rho g$.
2. Use the Ideal Gas Law to substitute for density: $\rho = \frac{P}{RT}$, where $R$ is the specific gas constant for the fluid.
3. The equation becomes a separable differential equation: $\frac{dP}{dz} = -\frac{Pg}{RT} \implies \frac{dP}{P} = -\frac{g}{RT} dz$.
4. Integrate both sides from state 1 to state 2. Since we assume T is constant, all terms on the right are constant and can be taken out of the integral:
   $$ \int_{P_1}^{P_2} \frac{dP}{P} = -\frac{g}{RT} \int_{z_1}^{z_2} dz \implies \ln\left(\frac{P_2}{P_1}\right) = -\frac{g(z_2 - z_1)}{RT} $$

```{important}
**Pressure in an Isothermal Compressible Fluid**
To solve for pressure directly, we exponentiate both sides:

$$

P_2 = P_1 \exp\left[-\frac{g(z_2-z_1)}{RT}\right]

$$

**Conclusion:** For an isothermal, compressible ideal gas, pressure decreases **exponentially** with altitude.

```

### Example: Pressure Calculation at High Altitude

```{prf:example} Air Pressure at 40,000 Feet
**Question:** Calculate the air pressure at an altitude of 40,000 feet above sea level using three different physical models: (1) incompressible, (2) compressible isothermal, and (3) compressible non-isothermal. Compare the results to the standard atmospheric value of 18.7 kPa.

```

```{admonition} Given Information and Constants
:class: tip


- **Altitude:** $z_2 = 40,000 \, \text{ft} \times \frac{0.3048 \, \text{m}}{1 \, \text{ft}} = 12,192$ m.
- **Sea Level (Point 1):** $z_1 = 0$ m, $P_1 = 101.33$ kPa = 101,330 Pa, $T_1 = T_0 = 15^\circ\text{C} = 288.15$ K.
- **Constants:** $g = 9.807$ m/s$^2$. Gas constant for air, $R = 286.9$ J/(kg·K).
- **Model 1 Data:** Specific weight of air at sea level, $\gamma = 12.014$ N/m$^3$.
- **Model 3 Data:** Standard atmospheric temperature lapse rate, $\beta = 0.00650$ K/m.

```

```{dropdown} Solution: Model 1 Incompressible Fluid
This model assumes the density (and specific weight) of air remains constant at its sea-level value all the way up to 40,000 feet.

**Incompressible Formula**

$$

P_2 = P_1 - \gamma (z_2 - z_1)

$$

$$

P_2 = 101,330 \, \text{Pa} - (12.014 \, \text{N/m}^3)(12,192 \, \text{m} - 0 \, \text{m})

$$

$$

P_2 = 101,330 \, \text{Pa} - 146,465 \, \text{Pa} = -45,135 \, \text{Pa} = \textbf{-45.1 kPa}

$$

**Analysis of Model 1**
The result of a negative absolute pressure is **physically impossible**. This demonstrates that the incompressible fluid model is completely inappropriate for gases over large changes in altitude. The density of air decreases significantly with altitude, so assuming it is constant vastly overestimates the weight of the air column, leading to this nonsensical result.

```

```{dropdown} Solution: Model 2 Compressible Isothermal Fluid
This model accounts for the fact that density changes with pressure, but assumes the temperature remains constant at its sea-level value of 15°C.

**Isothermal Compressible Formula**

$$

P_2 = P_1 \exp\left[-\frac{g(z_2-z_1)}{RT_0}\right]

$$

First, let's calculate the value of the dimensionless group in the exponent:

$$

\frac{g(z_2-z_1)}{RT_0} = \frac{(9.807 \, \text{m/s}^2)(12,192 \, \text{m})}{(286.9 \, \text{J/(kg}\cdot\text{K)})(288.15 \, \text{K})} = \frac{119,560}{82,665} = 1.446

$$

Now, calculate the pressure:

$$

P_2 = (101.33 \, \text{kPa}) \cdot \exp(-1.446) = (101.33) \cdot (0.2355) = \textbf{23.9 kPa}

$$

**Analysis of Model 2**
This result is physically realistic: a positive pressure that is much lower than sea-level pressure. However, it is still significantly different from the true value. This is because the atmosphere is not isothermal; it gets much colder at high altitudes. Assuming a constant warm temperature underestimates the density of the air aloft, which in turn underestimates the weight of the air column and results in a predicted pressure that is too high.

```

```{dropdown} Solution: Model 3 Compressible NonIsothermal Fluid
This is the most realistic model. It accounts for density changing with pressure and also models the fact that temperature decreases linearly with altitude in the troposphere. The pressure formula for a linear temperature lapse rate is:

**Non-Isothermal Compressible Formula**

$$

P_2 = P_1 \left[ \frac{T_0 - \beta z_2}{T_0 - \beta z_1} \right]^{\frac{g}{R\beta}}

$$

First, let's calculate the value of the exponent:

$$

\frac{g}{R\beta} = \frac{9.807 \, \text{m/s}^2}{(286.9 \, \text{J/(kg}\cdot\text{K)})(0.00650 \, \text{K/m})} = 5.259

$$

Now, calculate the pressure. Note that at sea level, $z_1=0$.

$$

P_2 = (101.33 \, \text{kPa}) \left[ \frac{288.15 - (0.00650)(12192)}{288.15 - 0} \right]^{5.259}

$$

$$

P_2 = (101.33) \left[ \frac{288.15 - 79.25}{288.15} \right]^{5.259} = (101.33) \left[ \frac{208.9}{288.15} \right]^{5.259} = (101.33) \left[ 0.725 \right]^{5.259}

$$

$$

P_2 = (101.33) \cdot (0.1842) = \textbf{18.67 kPa}

$$

**Analysis of Model 3**
This result is extremely close to the standard tabulated value of 18.7 kPa. This demonstrates that using a more realistic physical model, one that accounts for both compressibility and the actual temperature profile of the atmosphere.

```

```{admonition} Final Comparison and Key Takeaway
:class: tip


Let's summarize the results and see how they compare to the actual value.
- **Incompressible Model:** -45.1 kPa (Physically Impossible, $>$300% error)
- **Isothermal Model:** 23.9 kPa (Plausible, but has a 28% error)
- **Non-Isothermal Model:** 18.7 kPa (Highly Accurate, $<$1% error)
- **Actual Value:** 18.7 kPa

**Conclusion:** This example clearly shows the importance of selecting the appropriate physical assumptions for a fluid statics problem. While the incompressible assumption ($\Delta P = \rho g h$) is excellent for liquids, it fails completely for gases over large elevation changes. For gases, accounting for compressibility is essential, and for the highest accuracy, one must also account for temperature variations.

```

## Pipe Flow: Determining Pumping Power

A common and practical problem in fluid mechanics is determining the power required to pump a fluid through a piping system. This analysis requires a comprehensive application of the energy balance, accounting for changes in pressure, velocity, and elevation.

### Example: Pumping Water for a Ski Resort

```{prf:example} Pumping Water for Snow Making
**Question:** A ski resort needs to pump water at 10°C from a reservoir at an elevation of 6500 ft to a snow-making machine at 7300 ft. The water flows through 1000 ft of 2-inch diameter commercial steel pipe at a rate of 0.25 ft$^3$/s. The pressure required at the inlet of the snow machine is 20 psi (gauge). The piping system includes a sharp-edged entrance, a fully open gate valve, and two standard 90$^\circ$ elbows. Determine the horsepower that must be delivered to the water by the pump.

```

```{dropdown} Solution Steps
**Step 1: Strategy: The Extended Bernoulli Equation**

**Why the Simple Bernoulli Equation Is Not Enough:** The simple Bernoulli equation ($P + \frac{1}{2}\rho\nu^2 + \rho gz = \text{constant}$) is a statement of energy conservation for an *ideal* fluid, where there is no friction and no external work being done. Our system is real, not ideal, because we are adding energy with a **pump** and losing energy to **friction** in the pipe and fittings. Therefore, we must use the **Extended Bernoulli Equation**, also known as the steady-state Mechanical Energy Balance.

**The Extended Bernoulli Equation (in Head Form)**

We write the energy balance between point 1 (the reservoir surface) and point 2 (the snow machine inlet):

$$

\frac{P_1}{\gamma} + \frac{\nu_1^2}{2g} + z_1 + h_p = \frac{P_2}{\gamma} + \frac{\nu_2^2}{2g} + z_2 + h_L

$$

The equation contains several key terms: $\frac{P}{\gamma}$ represents the pressure head (energy stored due to pressure), $\frac{\nu^2}{2g}$ represents the velocity head (kinetic energy), $z$ represents the elevation head (potential energy due to height), $h_p$ represents the pump head (energy added by the pump), and $h_L$ represents the total head loss.

**Step 2: Simplify the Energy Balance:**

Let's analyze the conditions at points 1 and 2 to eliminate terms and create a workable equation.

At point 1 (reservoir surface): The reservoir surface is open to atmosphere, so its gauge pressure is $P_1 = 0$ psi. The reservoir is large compared to the pipe, so the velocity of the surface dropping is negligible: $\nu_1 \approx 0$ ft/s. We set the reservoir elevation as our reference datum, so $z_1 = 0$ ft.

At point 2 (snow machine inlet): The elevation of the snow machine is $z_2 = 7300 \, \text{ft} - 6500 \, \text{ft} = 800$ ft above the reservoir. The pressure at point 2 is given as $P_2 = 20$ psi (gauge). The velocity at point 2, $\nu_2$, is the velocity inside the pipe, which we must calculate.
Substituting these simplifications into the main equation:

$$

\frac{0}{\gamma} + \frac{0^2}{2g} + 0 + h_p = \frac{P_2}{\gamma} + \frac{\nu_2^2}{2g} + z_2 + h_L

$$

$$

h_p = \frac{P_2}{\gamma} + \frac{\nu_2^2}{2g} + z_2 + h_L

$$

This is our working equation. To solve for $h_p$, we need to calculate each term on the right side.

**Step 3: Calculate Fluid Velocity and Flow Characteristics:**

Before we can calculate head losses, we need to determine the fluid velocity and flow regime.

First, convert the pipe diameter to consistent units: $D = 2 \, \text{in} \times \frac{1 \, \text{ft}}{12 \, \text{in}} = 0.1667$ ft.

Calculate the pipe cross-sectional area: $A = \frac{\pi D^2}{4} = \frac{\pi (0.1667 \, \text{ft})^2}{4} = 0.02182$ ft$^2$.

Determine the fluid velocity: $\nu_2 = \frac{\text{Flow Rate (Q)}}{A} = \frac{0.25 \, \text{ft}^3/\text{s}}{0.02182 \, \text{ft}^2} = 11.46$ ft/s.

This velocity will be used in multiple calculations throughout our solution.

Next, we need to determine if the flow is laminar or turbulent by calculating the Reynolds number. For water at 10°C (50°F), the kinematic viscosity is $\nu \approx 1.41 \times 10^{-5}$ ft$^2$/s.

**Reynolds Number Calculation**

$$

Re = \frac{\nu_2 D}{\nu} = \frac{(11.46 \, \text{ft/s})(0.1667 \, \text{ft})}{1.41 \times 10^{-5} \, \text{ft}^2/\text{s}} = 1.35 \times 10^5

$$

Since $Re = 135,000 > 4000$, the flow is definitively **turbulent**. This is crucial information for determining the friction factor in the next step.

**Step 4: Calculate Major Head Loss (Pipe Friction):**

**The Darcy-Weisbach Equation and the Moody Chart:**

Major head loss represents the energy lost due to friction as fluid flows along the length of a pipe. For turbulent flow in rough pipes, this loss depends on both the Reynolds number and the relative roughness of the pipe surface. We calculate it using the Darcy-Weisbach equation, where the key parameter is the **friction factor, $f$**, which we determine from the **Moody Chart**.

**Darcy-Weisbach Equation**

$$

h_{L,major} = f \frac{L}{D} \frac{\nu_2^2}{2g}

$$

To find the friction factor $f$, we need the relative roughness of the pipe. For commercial steel pipe, the average roughness height is $\epsilon \approx 0.00015$ ft. The relative roughness is:

$$

\frac{\epsilon}{D} = \frac{0.00015 \, \text{ft}}{0.1667 \, \text{ft}} \approx 0.0009

$$

Using the Moody Chart: Locate $Re = 1.35 \times 10^5$ on the horizontal axis, move vertically up until you intersect the curve corresponding to $\epsilon/D = 0.0009$, then move horizontally left to read the friction factor from the vertical axis. This gives $f \approx 0.021$.

Now calculate the major head loss:

$$

h_{L,major} = (0.021) \frac{1000 \, \text{ft}}{0.1667 \, \text{ft}} \frac{(11.46 \, \text{ft/s})^2}{2 \cdot (32.2 \, \text{ft/s}^2)}

$$

$$

h_{L,major} = (0.021) \cdot (6000) \cdot (2.035 \, \text{ft}) = 126 \cdot 2.035 = \textbf{256.4 ft}

$$

**Step 5: Calculate Minor Head Loss (Fittings and Components):**

Minor losses occur due to flow disruption through fittings, valves, entrances, exits, and direction changes. Each component has a specific loss coefficient.

**Minor Loss Equation**

$$

h_{L,minor} = \sum K_L \frac{\nu_2^2}{2g}

$$

The term $K_L$ is a dimensionless **loss coefficient** specific to each fitting, obtained from standard engineering tables:
Sharp-edged entrance from reservoir to pipe: $K_L = 0.5$. This represents the energy lost as the fluid accelerates from essentially zero velocity in the large reservoir to the pipe velocity.
Fully open gate valve: $K_L = 0.15$. Gate valves, when fully open, create minimal flow disruption.
Two standard 90° elbows: $K_L = 0.9$ each. Elbows cause flow separation and secondary flows, leading to energy loss.
Total for two elbows: $2 \times 0.9 = 1.8$.

Total loss coefficient: $\sum K_L = 0.5 + 0.15 + 1.8 = 2.45$.
Calculate the minor head loss:

$$

h_{L,minor} = (2.45) \frac{(11.46 \, \text{ft/s})^2}{2 \cdot (32.2 \, \text{ft/s}^2)} = (2.45) \cdot (2.035 \, \text{ft}) = \textbf{5.0 ft}

$$

**Step 6: Calculate Total Head Loss:**

The total head loss is the sum of major and minor losses:

$$

h_L = h_{L,major} + h_{L,minor} = 256.4 + 5.0 = \textbf{261.4 ft}

$$

Notice that the major head loss (pipe friction) dominates in this long pipeline system, representing over 98% of the total head loss.

**Step 7: Calculate the Total Pump Head Required:**

Now we have all components needed to solve our simplified energy balance equation from Step 2:

$$

h_p = \frac{P_2}{\gamma} + \frac{\nu_2^2}{2g} + z_2 + h_L

$$

Let's calculate each term systematically:

**Pressure Head at Point 2:** We need to convert the gauge pressure at the snow machine inlet to head units. The specific weight of water is $\gamma = 62.4$ lb$_f$/ft$^3$.

First, convert pressure to consistent units: $P_2 = 20 \, \frac{\text{lb}_f}{\text{in}^2} \times \frac{144 \, \text{in}^2}{1 \, \text{ft}^2} = 2880$ lb$_f$/ft$^2$.

Then calculate pressure head: $\frac{P_2}{\gamma} = \frac{2880 \, \text{lb}_f/\text{ft}^2}{62.4 \, \text{lb}_f/\text{ft}^3} = 46.2$ ft.

**Velocity Head at Point 2:** This represents the kinetic energy of the fluid at the delivery point.

$$

\frac{\nu_2^2}{2g} = \frac{(11.46 \, \text{ft/s})^2}{2 \cdot (32.2 \, \text{ft/s}^2)} = \frac{131.3}{64.4} = 2.0 \text{ ft}

$$

**Elevation Head:** This is the gravitational potential energy difference between the reservoir and snow machine: $z_2 = 800$ ft.

**Total Head Loss:** From our previous calculation: $h_L = 261.4$ ft.

Substituting all values:

$$

h_p = 46.2 + 2.0 + 800 + 261.4 = \textbf{1109.6 ft}

$$

The pump must provide approximately **1110 ft** of head to the water.

**Physical Interpretation:** This means the pump must add enough energy to the water to: (1) overcome the 800 ft elevation gain, (2) provide the required 20 psi pressure at the snow machine, (3) overcome 261.4 ft of frictional losses, and (4) provide the kinetic energy for 11.46 ft/s flow velocity.

**Step 8: Calculate the Required Pump Power:**

The hydraulic power that must be delivered to the fluid (often called "water horsepower") is calculated using the fundamental relationship between flow rate, head, and power.

**Fluid Power Calculation**

$$

\text{Power}_{\text{fluid}} = \gamma Q h_p

$$

Where $\gamma$ is the specific weight of the fluid, $Q$ is the volumetric flow rate, and $h_p$ is the pump head.
Substituting our values:

$$

\text{Power}_{\text{fluid}} = (62.4 \, \text{lb}_f/\text{ft}^3) \cdot (0.25 \, \text{ft}^3/\text{s}) \cdot (1110 \, \text{ft})

$$

$$

\text{Power}_{\text{fluid}} = 17,316 \, \frac{\text{ft}\cdot\text{lb}_f}{\text{s}}

$$

Convert to horsepower using the standard conversion factor (1 hp = 550 ft·lb$_f$/s):

$$

\text{Horsepower} = 17,316 \, \frac{\text{ft}\cdot\text{lb}_f}{\text{s}} \times \frac{1 \, \text{hp}}{550 \, \text{ft}\cdot\text{lb}_f/\text{s}} = \textbf{31.5 hp}

$$


```

```{admonition} Important Note on Pump Efficiency and Motor Power
:class: tip


This 31.5 hp represents the **hydraulic power** that must be delivered to the water. However, real pumps are not 100% efficient due to mechanical friction, fluid leakage, and other losses. If the pump operates at 80% efficiency (typical for centrifugal pumps), the required shaft power would be: $31.5 / 0.80 = 39.4$ hp. Additionally, the electric motor driving the pump also has efficiency losses (typically 85-95%). If the motor efficiency is 90%, the required electrical power would be: $39.4 / 0.90 = 43.8$ hp. Therefore, while the theoretical minimum power to move the water is 31.5 hp, the actual electrical power consumption would likely be 40-45 hp in a real system.

```

## Air Flow Through a Constriction

```{note}
**The Venturi Effect: High Velocity Means Low Pressure**
A classic application of the Bernoulli equation is analyzing flow through a constriction, such as a Venturi meter. This setup demonstrates a fundamental and often counter-intuitive principle:
1. **Continuity:** For a fluid of constant density, the mass flow rate ($\dot{m} = \rho A \nu$) must be constant. Where the pipe area $A$ gets smaller (in the "throat"), the velocity $\nu$ *must increase* to maintain the same flow rate.
2. **Energy Conservation (Bernoulli):** The Bernoulli equation ($P + \frac{1}{2}\rho\nu^2 = \text{const}$ for a horizontal pipe) is a statement of energy conservation. As the kinetic energy ($\frac{1}{2}\rho\nu^2$) increases in the high-velocity throat, the pressure energy ($P$) *must decrease* to keep the total energy constant.

This phenomenon, where the pressure in the constricted section is lower than in the wider sections, is known as the **Venturi effect**.

```

### Example: Velocity in a Constriction (Venturi Effect)

```{prf:example} Velocity in a Constriction (Venturi Effect)
**Question:** Air with a density of 1.0 kg/m$^3$ flows steadily and incompressibly through a horizontal constriction. The pressure at the wide entrance (point 1) is 10 kPa greater than the pressure at the narrow throat (point 2). The cross-sectional area at the entrance is five times the area at the throat ($A_1 = 5A_2$). What is the air speed at the throat ($\nu_2$)?

```

```{dropdown} Solution Steps
**Step 1: Strategy: Two Equations, Two Unknowns**
We have two unknown velocities, $\nu_1$ and $\nu_2$. We can solve for them by setting up a system of two equations: the Bernoulli equation and the continuity equation.
1. The **Bernoulli Equation**, which relates pressure and velocity changes (an energy relationship).
2. The **Continuity Equation**, which relates velocities and areas (a mass balance).
We apply these equations between point 1 (inside the pipe) and point 2 (at the nozzle exit).

**Step 2: Apply the Bernoulli Equation:**
For a horizontal pipe ($z_1 = z_2$) with no friction or shaft work:

$$

P_1 + \frac{1}{2}\rho\nu_1^2 = P_2 + \frac{1}{2}\rho\nu_2^2

$$

Rearranging for the known pressure difference:

$$

P_1 - P_2 = \frac{1}{2}\rho(\nu_2^2 - \nu_1^2)

$$

**Step 3: Apply the Continuity Equation:**
For an incompressible fluid, the volumetric flow rate is constant: $A_1\nu_1 = A_2\nu_2$. We can express the upstream velocity $\nu_1$ in terms of the throat velocity $\nu_2$:

$$

\nu_1 = \nu_2 \left(\frac{A_2}{A_1}\right)

$$

We are given that $A_1 = 5A_2$, so the ratio $\frac{A_2}{A_1} = \frac{1}{5} = 0.2$.

$$

\nu_1 = 0.2 \nu_2

$$

**Step 4: Solve the System of Equations:**
Substitute the expression for $\nu_1$ from continuity into the Bernoulli equation:

$$

P_1 - P_2 = \frac{1}{2}\rho \left(\nu_2^2 - (0.2\nu_2)^2\right) = \frac{1}{2}\rho \left(\nu_2^2 - 0.04\nu_2^2\right)

$$

$$

P_1 - P_2 = \frac{1}{2}\rho (0.96\nu_2^2)

$$

Now, plug in the known values to solve for the unknown velocity, $\nu_2$.
- $P_1 - P_2 = 10 \, \text{kPa} = 10,000$ Pa.
- $\rho = 1.0$ kg/m$^3$.

$$

10,000 \, \text{Pa} = \frac{1}{2} (1.0 \, \text{kg/m}^3) (0.96\nu_2^2)

$$

$$

10,000 = 0.48 \cdot \nu_2^2

$$

$$

\nu_2^2 = \frac{10,000}{0.48} = 20,833 \, \text{m}^2/\text{s}^2

$$

$$

\nu_2 = \sqrt{20,833} = 144.3 \, \text{m/s}

$$

The speed of the air at the throat is approximately **140 m/s**.

```

## Manometry

Manometry is the science of measuring pressure using liquid columns in tubes. A manometer is a simple yet powerful device that measures pressure differences by balancing the weight of a column of fluid against another pressure. Understanding how to analyze a manometer is a foundational skill in fluid mechanics and engineering, as it provides a very direct and intuitive way to think about pressure.

### The Principle of Hydrostatic Head

The operation of every manometer is based on the principle of **hydrostatic pressure**, which is the pressure exerted by a fluid at rest due to the force of gravity.

```{note}
**Origin of Pressure in a Fluid Column**
Imagine a stationary column of water in a glass. The water has mass, and due to gravity, it has weight. This weight exerts a downward force on the bottom of the glass. The pressure at the bottom is simply this total downward force distributed over the bottom area. The deeper you go, the more water is above you, the greater the weight, and therefore the higher the pressure.

```

We can derive a simple formula for this pressure with a few logical steps:

1. Pressure is defined as force per unit area: $P = \frac{F}{A}$.
2. The force exerted by the fluid column is its weight: $F = \text{mass} \cdot g$.
3. We can express mass in terms of density ($\rho$) and volume ($V$): $\text{mass} = \rho \cdot V$.
4. The volume of a uniform column is its cross-sectional area times its height: $V = A \cdot h$.
5. Combining these, we substitute steps 4, 3, and 2 into step 1: $P = \frac{(\rho \cdot A \cdot h) \cdot g}{A}$.

The area ($A$) of the column cancels out, leaving the fundamental hydrostatic pressure equation:

```{important}
**Hydrostatic Pressure Equation**

$$

P_{\text{hydrostatic}} = \rho g h

$$


```

This important result tells us that the pressure exerted by a fluid column depends only on its density ($\rho$), height ($h$), and gravity ($g$) - not on the shape of the container or the total amount of fluid. The term $\rho g$ is also known as the **specific weight**, $\gamma$. So, the equation is often written as $P = \gamma h$.

```{note}
**The Fundamental Rule of Manometry**
The analysis of any manometer, no matter how complex, relies on one simple, crucial rule:
*The pressure at any two points at the same horizontal level in a single, continuous fluid at rest is the same.*

Why is this true? Imagine if the pressure at point A was higher than at point B on the same horizontal level. This pressure difference would create a net force, causing the fluid to flow from A to B. But a manometer contains fluid *at rest* (in static equilibrium). Therefore, there can be no net forces, and the pressures must be equal. We use this rule by drawing a horizontal "datum" line at an interface between fluids and equating the pressures on the left and right sides of that line.

```

### The Simple U-Tube Manometer

The most common type of manometer is a U-shaped tube containing a dense liquid (often mercury or colored water), known as the manometer fluid.

```{note}
**Measuring the Gauge Pressure of a Gas**
Consider a U-tube manometer with one end connected to a tank of pressurized gas and the other end open to the atmosphere. The gas pushes the manometer fluid down on the left side and up on the right side. To find the pressure of the gas, we apply our fundamental rule at the lowest fluid interface (we'll call this our datum line).
$P_{\text{left at datum}} = P_{\text{right at datum}}$

- **Pressure on the Left Side:** The pressure at the datum line is simply the pressure of the gas, $P_{gas}$. We can ignore the weight of the small column of gas above the datum because the density of gas is thousands of times smaller than the density of the liquid, making its contribution negligible.
- **Pressure on the Right Side:** The pressure at the datum line is the sum of two pressures: the atmospheric pressure ($P_{atm}$) pushing down on the open end, plus the hydrostatic pressure from the column of manometer fluid of height $h$ that is above the datum.
So, $P_{\text{right}} = P_{atm} + \rho_{\text{fluid}} g h$.

```

Equating the two sides gives the absolute pressure of the gas: $P_{gas} = P_{atm} + \rho g h$. More often, we are interested in the __gauge pressure__.

```{important}
**U-Tube Manometer Gauge Pressure**

$$

P_{gas, \text{gauge}} = P_{gas} - P_{atm} = \rho g h

$$


```

### Applying Manometry Equations from First Principles

```{note}
**The "Walking" Method: A Universal Approach**
Instead of memorizing a different formula for every type of manometer, it is much more powerful to use a single, universal method. We call this the "walking" method:
1. Start at a point of known (or desired) pressure.
2. "Walk" through the continuous fluid paths to the other end.
3. Whenever you move **down** a vertical distance $h$, you **add** the hydrostatic pressure of that fluid column ($+\rho g h$). Whenever you move **up** a vertical distance $h$, you **subtract** the hydrostatic pressure ($-\rho g h$).

```

```{admonition} Piezometer Tube
:class: tip


This is the simplest manometer: a single vertical tube attached to a container of liquid.
- **Equation:** $P_{A,gauge} = \gamma_1 h_1 = \rho_1 g h_1$.
- **Explanation:** Start at the surface of the liquid in the tube, which is at atmospheric pressure ($P_{atm}$). Walk *down* a height $h_1$ through the fluid to point A. This means we add pressure: $P_A = P_{atm} + \gamma_1 h_1$. The gauge pressure is therefore just $\gamma_1 h_1$. This only works for measuring liquid pressures that are greater than atmospheric.

```

```{admonition} Inclined Manometer
:class: tip


This is a variation of the differential manometer designed for measuring very small pressure differences with high precision.

**The Principle of Amplification:** The analysis is identical to the differential manometer, with one key difference. The vertical height of the manometer fluid column, $h_2$, is not measured directly. Instead, we measure the much larger displacement, $l_2$, along the inclined tube. From trigonometry, the vertical height is simply:

$$h_2 = l_2 \sin(\theta)$$

By making the angle $\theta$ small, a very small vertical change $h_2$ (due to a small pressure difference) results in a large, easily readable displacement $l_2$, effectively amplifying the measurement.

**Formula:**

$$P_A - P_B = \gamma_2 l_2 \sin(\theta) + \gamma_3 h_3 - \gamma_1 h_1$$

```

```{admonition} Differential U-Tube Manometer
:class: tip


This device is extremely useful as it measures the pressure **difference** between two points, A and B, which might both be at high pressure.

**Formula:**
$$P_A - P_B = \gamma_2 h_2 + \gamma_3 h_3 - \gamma_1 h_1$$

**Explanation using the "Walking" Method:**
1. Start at point A, where the pressure is $P_A$.
2. Walk **down** through fluid 1 by a height $h_1$. The pressure increases: $P_A + \gamma_1 h_1$. You are now at the lowest point on the left.
3. Move horizontally across the continuous manometer fluid (fluid 2) to the right side. The pressure does not change.
4. Now walk **up** through the manometer fluid (fluid 2) by a height $h_2$. The pressure decreases: $P_A + \gamma_1 h_1 - \gamma_2 h_2$.
5. Continue walking **up** through fluid 3 by a height $h_3$ to get to point B. The pressure decreases again: $P_A + \gamma_1 h_1 - \gamma_2 h_2 - \gamma_3 h_3$.
6. The expression you are left with is the pressure at point B. So, $P_B = P_A + \gamma_1 h_1 - \gamma_2 h_2 - \gamma_3 h_3$.
7. Rearranging this equation to solve for the pressure difference, $P_A - P_B$, gives the formula above.

```

### Example: Hydrostatic Balance in an Inclined Manometer

```{prf:example} Hydrostatic Balance in an Inclined Manometer
**Question:** An inclined manometer contains water, oil (SG=0.85), and mercury (SG=13.6). The left vertical tube has an inner diameter (ID) of 2 cm, and the inclined right tube has an ID of 1 cm. Initially, the system is at equilibrium. Then, the pressure $P_1$ is increased by 50 mm of mercury. What is the change in the reading along the inclined scale ($y$)? The angle of inclination is 30$^\circ$.

```

```{dropdown} Solution Steps
**Step 1: Strategy: Hydrostatic and Volume Balances**

This is a hydrostatic problem, but because the fluid levels change, we must also consider a volume (or mass) balance. The plan is:
1. Use a **volume balance** on the mercury to find a geometric relationship between the level drop in the left tube ($x$) and the displacement along the incline in the right tube ($y$).
2. Use a **hydrostatic pressure balance** to relate the applied change in pressure ($\Delta P_1$) to the changes in the fluid column heights.
3. Combine these two relationships to solve for the unknown displacement, $y$.

**Step 2: Relate Displacements with a Volume Balance:**

When the pressure $P_1$ increases, it pushes the mercury down in the left tube by a vertical distance $x$. This volume of mercury must move into the right tube, causing the level to rise a distance $y$ along the incline. Since mercury is incompressible, the volume is conserved.

$$(\text{Volume of mercury lost from left tube}) = (\text{Volume of mercury gained in right tube})$$

$$A_{\text{left}} \cdot x = A_{\text{right}} \cdot y$$

Since area $A = \pi d^2 / 4$, the $\pi/4$ terms cancel:

$$d_{\text{left}}^2 x = d_{\text{right}}^2 y \implies (2 \, \text{cm})^2 x = (1 \, \text{cm})^2 y \implies \textbf{y = 4x}$$

This is a crucial geometric constraint: the displacement along the incline is four times the vertical drop in the left tube.

**Step 3: Relate Pressure Change to Displacements via Hydrostatics:**

By writing the full hydrostatic balance equation from $P_1$ to $P_2$ for the initial and final states and then subtracting them, we can arrive at an equation for the *change* in pressure. The change in pressure, $\Delta P_1 = P_1' - P_1$, is balanced by the net change in the weights of the fluid columns due to the displacements $x$ and $y$:

$$\Delta P_1 = -\gamma_{\text{oil}} (y \sin\theta) + \gamma_{\text{Hg}} (y \sin\theta + x) - \gamma_{\text{water}} (x)$$

**Step 4: Solve for the Displacements:**

Substitute the geometric constraint $y=4x$ into the pressure change equation:

$$\Delta P_1 = x \cdot [-\gamma_{\text{oil}} (4 \sin\theta) + \gamma_{\text{Hg}} (4 \sin\theta + 1) - \gamma_{\text{water}}]$$

Using SI units: $\Delta P_1 = 50 \, \text{mmHg} \times 133.32 \, \text{Pa/mmHg} = 6666$ Pa. The specific weights are $\gamma_{\text{water}} = 1000 \times 9.81 = 9810$ N/m$^3$, $\gamma_{\text{oil}} = 0.85 \times 9810 = 8338.5$ N/m$^3$, $\gamma_{\text{Hg}} = 13.6 \times 9810 = 133,416$ N/m$^3$, and $\sin(30^\circ) = 0.5$.

$$6666 = x \cdot [-8338.5(4 \times 0.5) + 133416(4 \times 0.5 + 1) - 9810]$$

$$6666 = x \cdot [-16677 + 133416(3) - 9810] = x \cdot [373,761]$$

$$x = \frac{6666}{373761} = 0.0178 \, \text{m} = 1.78 \, \text{cm}$$

The change in the reading on the inclined scale is:

$$y = 4x = 4 \times 1.78 = 7.12 \, \text{cm}$$

A pressure increase of 50 mmHg causes the reading on the incline to change by **7.1 cm**.

```

## Viscosity and Shear Stress

Viscosity is arguably the most important property of a fluid when it comes to analyzing its motion. It describes the fluid's inherent "thickness" or resistance to flowing. Understanding the relationship between viscosity and the forces that cause flow (shear stress) is fundamental to nearly all problems in fluid dynamics, from pumping oil through a pipe to designing aerodynamic vehicles.

### Fundamental Equations and Definitions

```{important}
**Newton's Law of Viscosity**
For many common fluids, the relationship between the internal "smearing" force (shear stress) and the rate of fluid deformation is linear. This relationship is known as Newton's Law of Viscosity:

$$

\tau = \mu \frac{du}{dy}

$$


```

```{admonition} Variable Definitions
:class: tip


- $\tau$: **Shear Stress** - This is the force per unit area that acts *parallel* (tangential) to a surface. Imagine spreading honey on toast; the force you apply with the knife parallel to the bread creates a shear stress in the honey. Its units are Pascals (Pa) or Newtons per square meter (N/m$^2$).
- $\mu$: **Dynamic Viscosity** - This is a fluid property that measures its intrinsic resistance to flow. Honey has a high viscosity; water has a low viscosity. Its units are Pascal-seconds (Pa·s).
- $\frac{du}{dy}$: **Velocity Gradient** (or Rate of Shearing Strain) - This term describes how quickly the fluid velocity changes as you move away from a surface. A steep gradient means the velocity changes rapidly over a short distance. Its units are inverse seconds (s$^{-1}$).

```

### Conceptual Framework

```{note}
**What is Shear Stress?**
A fluid, by definition, is a substance that deforms continuously when a shear stress is applied, no matter how small. A shear stress is created when a force acts tangentially on a surface. The classic way to visualize this is to consider a fluid contained between two parallel plates. If we pull the top plate sideways, we are applying a shear stress to the fluid.

```

```{note}
**The No-Slip Condition and the Velocity Gradient**
The scenario in Figure 1 illustrates two of the most important concepts in fluid mechanics:
1. **The No-Slip Condition:** This is an empirical observation that a fluid in direct contact with a solid surface will "stick" to it and have the exact same velocity as that surface. In Figure 1, the fluid touching the bottom plate ($y=0$) has zero velocity, and the fluid touching the top plate ($y=H$) moves with the plate's velocity, $U$.
2. **The Velocity Gradient:** Because of the no-slip condition, a velocity profile must develop within the fluid, transitioning from zero at the bottom to $U$ at the top. The rate at which the velocity changes from one fluid layer to the next, $\frac{du}{dy}$, is the velocity gradient. It is this gradient that, when multiplied by the fluid's viscosity, gives the shear stress.

```

### Newtonian and Non-Newtonian Fluids

The relationship between shear stress ($\tau$) and the rate of strain ($\frac{du}{dy}$) defines the type of fluid.

```{note}
**Newtonian Fluids**
A fluid is **Newtonian** if the shear stress is linearly proportional to the rate of shearing strain. For these fluids, viscosity ($\mu$) is a constant property that only depends on temperature and pressure, not on how fast the fluid is being sheared. This simple relationship, $\tau = \mu \frac{du}{dy}$, holds true for many common fluids like water, oil, gasoline, and air.

```

```{note}
**Non-Newtonian Fluids**
Many important fluids do not follow this simple linear relationship. Their "apparent viscosity" changes depending on the applied shear rate.
- **Shear Thinning (Pseudoplastic):** Apparent viscosity *decreases* as the shear rate increases. They get "thinner" the faster you stir them. This is the most common non-Newtonian behavior. Examples: paint, blood, latex.
- **Shear Thickening (Dilatant):** Apparent viscosity *increases* with increasing shear rate. They get "thicker" the faster you stir them. Example: a cornstarch and water mixture (oobleck).
- **Bingham Plastics:** These are materials that require a minimum stress, called a **yield stress** ($\tau_0$), to be applied before they begin to flow at all. Below this stress, they behave like a solid. Example: ketchup, toothpaste, mayonnaise.

```

### Example: Film Flow Down an Inclined Surface

```{prf:example} Film Flow Down an Inclined Surface
**Question:** Crude oil with a specific gravity of 0.85 flows steadily in a thin film down a wide surface inclined 30$^\circ$ below the horizontal. The film has a thickness of 0.125 inches. The velocity profile is given by the equation:

$$

u(y) = \frac{\rho g \sin\theta}{\mu} \left(Hy - \frac{y^2}{2}\right)

$$

where $y$ is the distance perpendicular to the surface. Determine the magnitude of the shear stress that the fluid exerts on the inclined surface.

```

```{dropdown} Solution Steps
**Step 1: Strategy: Apply Newton's Law of Viscosity**
Our goal is to find the shear stress, $\tau$, at the solid surface ($y=0$). The governing equation is $\tau = \mu \frac{du}{dy}$. The plan is to:
1. Differentiate the given velocity profile $u(y)$ to find the velocity gradient, $\frac{du}{dy}$.
2. Substitute this gradient into Newton's law of viscosity to get an expression for shear stress, $\tau(y)$.
3. Evaluate this expression at the surface ($y=0$) to find the specific shear stress we need.

**Step 2: Differentiate the Velocity Profile:**
We are given $u(y)$. The terms $\rho, g, \sin\theta, \mu,$ and $H$ are all constants with respect to the variable $y$.

$$

\frac{du}{dy} = \frac{d}{dy} \left[ \frac{\rho g \sin\theta}{\mu} \left(Hy - \frac{y^2}{2}\right) \right] = \frac{\rho g \sin\theta}{\mu} \cdot \frac{d}{dy}\left(Hy - \frac{y^2}{2}\right)

$$

$$

\frac{du}{dy} = \frac{\rho g \sin\theta}{\mu} (H - y)

$$

**Step 3: Calculate the Shear Stress Expression, $\tau(y)$:**
Now, substitute the expression for $\frac{du}{dy}$ into the shear stress equation, $\tau(y) = \mu \frac{du}{dy}$:

$$

\tau(y) = \mu \left[ \frac{\rho g \sin\theta}{\mu} (H - y) \right]

$$

A very interesting thing happens: the viscosity term $\mu$ cancels out. This means for this specific gravity-driven film flow, the shear stress within the fluid does not depend on the fluid's viscosity, but rather on the weight of the fluid above it.

$$

\tau(y) = \rho g (H - y) \sin\theta

$$

**Step 4: Evaluate Shear Stress at the Surface ($y=0$):**
The question asks for the shear stress acting *on the surface*. This corresponds to the position $y=0$.

$$

\tau_{\text{surface}} = \tau(0) = \rho g (H-0) \sin\theta = \rho g H \sin\theta

$$

**Step 5: Perform the Numerical Calculation:**

We must use a consistent set of units. The source problem uses English Engineering units, so we will use that system.
- **Density ($\rho$):** $\rho = (\text{Specific Gravity}) \times \rho_{\text{water}}$. In this system, $\rho_{\text{water}} = 1.94 \, \text{slugs/ft}^3$.
  $$\rho = 0.85 \cdot (1.94 \, \text{slugs/ft}^3) = 1.649 \, \text{slugs/ft}^3$$
- **Gravity ($g$):** $g = 32.2 \, \text{ft/s}^2$.
- **Film Thickness ($H$):** $H = 0.125 \, \text{in} \times \frac{1 \, \text{ft}}{12 \, \text{in}} = 0.01042 \, \text{ft}$.
- **Angle ($\theta$):** $\sin(30^\circ) = 0.5$.

Now, substitute these values. The unit `slug` is defined such that 1 lb$_\text{f}$ = 1 slug $\cdot$ ft/s$^2$.

$$

\tau_{\text{surface}} = (1.649 \, \frac{\text{slug}}{\text{ft}^3}) \cdot (32.2 \, \frac{\text{ft}}{\text{s}^2}) \cdot (0.01042 \, \text{ft}) \cdot (0.5)

$$

$$

\tau_{\text{surface}} = 0.2766 \, \frac{\text{slug} \cdot \text{ft}}{\text{ft}^2 \cdot \text{s}^2} = 0.2766 \, \frac{\text{lb}_\text{f}}{\text{ft}^2} 

$$


```

### Example: Determining Viscosity Experimentally

```{prf:example} Determining Viscosity Experimentally

**Question:** A toothpick is placed concentrically inside a 5 mm diameter straw full of a mysterious fluid. There is a 1 mm gap between the toothpick and the straw on all sides. A length of 50 mm of the toothpick is submerged in the fluid. When a constant force of 0.1 N is used to pull the toothpick out, it moves at a constant velocity of 0.1 m/s. What is the viscosity of the fluid? Assume the fluid is Newtonian and the velocity profile in the narrow gap is linear.
```

```{dropdown} Solution Steps
**Step 1: Strategy: Rearrange Newton's Law of Viscosity**
Our governing equation is $\tau = \mu \frac{du}{dy}$. We want to find the viscosity, $\mu$. We can rearrange the equation to solve for it:

$$\mu = \frac{\tau}{du/dy}$$

Our plan is to calculate the shear stress ($\tau$) and the velocity gradient ($\frac{du}{dy}$) from the information given in the problem.

**Step 2: Calculate the Shear Stress ($\tau$):**

Shear stress is the tangential force applied divided by the surface area over which it acts.

$$\tau = \frac{F}{A}$$

- **Force ($F$):** The problem states a constant pulling force of $F = 0.1$ N.

- **Area ($A$):** This is the cylindrical surface area of the toothpick that is in contact with the fluid.

- The straw has a 5 mm diameter. The annular gap is 1 mm on each side.

- Toothpick diameter $d_{\text{toothpick}} = d_{\text{straw}} - 2 \cdot (\text{gap}) = 5 \, \text{mm} - 2(1 \, \text{mm}) = 3 \, \text{mm} = 0.003 \, \text{m}$.

- Length in fluid $L = 50$ mm = 0.050 m.

$$A = (\text{circumference}) \times (\text{length}) = \pi d_{\text{toothpick}} L$$

$$= \pi \cdot (0.003 \, \text{m}) \cdot (0.050 \, \text{m}) = 0.0004712 \, \text{m}^2$$

Now we can calculate the shear stress:

$$\tau = \frac{0.1 \, \text{N}}{0.0004712 \, \text{m}^2} = 212.2 \, \text{N/m}^2 = \textbf{212.2 Pa}$$

**Step 3: Calculate the Velocity Gradient ($\frac{du}{dy}$):**

**The Linear Velocity Profile Assumption:** For fluid flow in a very narrow gap (an annulus), it is often a very good approximation to assume the velocity changes linearly across the gap. This means we can approximate the differential term $\frac{du}{dy}$ with the difference term $\frac{\Delta u}{\Delta y}$.

- The change in velocity, $\Delta u$, is the difference between the toothpick's velocity (0.1 m/s) and the stationary straw's velocity (0 m/s). So, $\Delta u = 0.1 \, \text{m/s}$.

- The distance over which this change occurs, $\Delta y$, is the size of the gap: $1 \, \text{mm} = 0.001 \, \text{m}$.

$$

\frac{du}{dy} \approx \frac{\Delta u}{\Delta y} = \frac{0.1 \, \text{m/s}}{0.001 \, \text{m}} = \textbf{100 s ⁻¹}

$$

**Step 4: Solve for Viscosity ($\mu$):**
Now we can substitute our calculated values for $\tau$ and $\frac{du}{dy}$ into our rearranged equation from Step 1.

**Calculating Viscosity**

$$

\mu = \frac{\tau}{du/dy} = \frac{212.2 \, \text{Pa}}{100 \, \text{s}^{-1}} = 2.122 \, \text{Pa}\cdot\text{s}

$$

**Step 5: Interpret the Result:**
The standard SI unit for viscosity is the Pascal-second (Pa·s). A more common unit in practice is the centipoise (cP), where 1 Pa·s = 1000 cP.

$$

\mu = 2.122 \, \text{Pa}\cdot\text{s} \times \frac{1000 \, \text{cP}}{1 \, \text{Pa}\cdot\text{s}} = 2122 \, \text{cP}

$$

For context, the viscosity of water at room temperature is about 1 cP, olive oil is about 80 cP, and honey is around 2,000-10,000 cP. The mysterious fluid has a viscosity similar to that of honey or a thick syrup.

```

---

## PE Exam Practice Problems

```{prf:example} Practice Problem 1: Pump Sizing

Water ($\rho = 1000$ kg/m³, $\mu = 0.001$ Pa·s) is pumped at 0.05 m³/s from a lower reservoir (elevation 0 m) to an upper tank (elevation 25 m) through 200 m of commercial steel pipe with inner diameter $D = 0.10$ m. The Darcy friction factor is $f = 0.018$.

**(a)** What is the fluid velocity in the pipe?

**(b)** What is the frictional head loss (J/kg)?

**(c)** What is the required pump shaft power (kW), assuming 80% pump efficiency?
```

```{dropdown} Solution

**Step 1: Flow velocity**

$$u = \frac{Q}{A} = \frac{0.05}{\pi(0.10)^2/4} = \frac{0.05}{7.854\times10^{-3}} = 6.37 \text{ m/s}$$

**Step 2: Frictional loss (Darcy-Weisbach)**

$$\hat{F} = f\frac{L}{D}\frac{u^2}{2} = 0.018 \times \frac{200}{0.10} \times \frac{(6.37)^2}{2} = 0.018 \times 2000 \times 20.29 = \mathbf{730 \text{ J/kg}}$$

**Step 3: Mechanical energy balance** (both reservoir surfaces: $u \approx 0$, $P = P_{atm}$)

$$\frac{\dot{W}_s}{\dot{m}} = g\Delta z + \hat{F} = 9.81 \times 25 + 730 = 245 + 730 = \mathbf{975 \text{ J/kg}}$$

**Step 4: Shaft power**

$$\dot{m} = \rho Q = 1000 \times 0.05 = 50 \text{ kg/s}$$

$$\dot{W}_{fluid} = 975 \times 50 = 48{,}750 \text{ W}$$

$$\dot{W}_{shaft} = \frac{\dot{W}_{fluid}}{\eta} = \frac{48{,}750}{0.80} = \mathbf{60.9 \text{ kW}}$$
```

---

```{prf:example} Practice Problem 2: Reynolds Number and Flow Regime

Crude oil ($\rho = 870$ kg/m³, $\mu = 0.025$ Pa·s) flows through a 6-inch (0.152 m) pipeline at a volumetric flow rate of 0.08 m³/s.

**(a)** What is the Reynolds number? Is flow laminar or turbulent?

**(b)** If the flow were laminar, what would the pressure drop be over 500 m using Hagen-Poiseuille? Is laminar flow physically consistent here?
```

```{dropdown} Solution

**Part (a): Reynolds number**

$$u = Q/A = 0.08 / (\pi \times 0.152^2/4) = 0.08/0.01815 = 4.41 \text{ m/s}$$

$$Re = \frac{\rho u D}{\mu} = \frac{870 \times 4.41 \times 0.152}{0.025} = \frac{583.7}{0.025} = \mathbf{23{,}350}$$

Flow is **turbulent** ($Re \gg 4000$). Use turbulent friction factor correlations (Moody chart), not Hagen-Poiseuille.

**Part (b): Hagen-Poiseuille check**

$$\Delta P = \frac{128 \mu L Q}{\pi D^4} = \frac{128 \times 0.025 \times 500 \times 0.08}{\pi \times (0.152)^4} = \frac{128}{8.39\times10^{-4}} \approx 38{,}500 \text{ Pa}$$

This result is **not physically valid** here - Hagen-Poiseuille assumes laminar flow ($Re < 2100$), but $Re = 23{,}350$. The actual turbulent pressure drop would be several times higher and must use the Darcy-Weisbach equation with a turbulent friction factor.
```

```{caution}
**PE Exam Traps: Fluid Mechanics**

- **Darcy vs. Fanning friction factor:** The Darcy (Moody) friction factor $f_D = 4f_{Fanning}$. The Darcy-Weisbach equation uses $f_D$; many textbooks and the Churchill correlation give $f_F$. Always confirm which form a given $f$ value is for - using $f_F$ in place of $f_D$ underestimates friction loss by 4×.
- **MEB sign convention:** $\dot{W}_s/\dot{m}$ is positive when a pump adds energy to the fluid; it's negative for a turbine that extracts energy. Getting this backwards gives pump power instead of turbine power or vice versa.
- **Bernoulli applies only to streamlines without friction or shaft work.** If a pump is present, or the problem mentions a pressure drop, use the full MEB. Bernoulli applied across a pump gives zero work, which is wrong.
- **Velocity at open reservoir surface:** At a large open reservoir, the surface velocity is approximately zero ($u \approx 0$). Using the pipe velocity at this point is a common mistake that adds a phantom kinetic energy term.
- **Hagen-Poiseuille is laminar only ($Re < 2100$).** Never apply it to turbulent flow - it will dramatically underpredict pressure drop. Always check Reynolds number first.
```