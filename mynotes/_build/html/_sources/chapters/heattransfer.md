---
title: "Complete Heat Transfer Fundamentals: Theory, Applications, and Problem Solving"
author: "PE Study Guide"
date: "2024"
---

# Complete Heat Transfer Fundamentals

## Quick Reference: Key Equations

| Topic | Formula | Notes |
|-------|---------|-------|
| Fourier's Law (1D) | $q = -kA\,dT/dx$ | Conduction |
| Plane wall resistance | $R_{cond} = L/(kA)$ | Thermal resistance |
| Cylindrical wall | $q = 2\pi k L\,(T_1-T_2)/\ln(r_2/r_1)$ | Hollow cylinder |
| Newton's Law of Cooling | $q = h A (T_s - T_\infty)$ | Convection |
| Convective resistance | $R_{conv} = 1/(hA)$ | Series with conduction |
| Overall HTC | $1/UA = \sum R_{total}$ | Series resistances |
| Radiation | $q = \varepsilon\sigma A(T_s^4 - T_{surr}^4)$ | $T$ in K; $\sigma=5.67\times10^{-8}$ W/m²·K⁴ |
| Nusselt number | $Nu = hL/k$ | Dimensionless $h$ |
| Prandtl number | $Pr = \mu C_p/k = \nu/\alpha$ | Fluid property |
| Reynolds number | $Re = \rho u L/\mu$ | Flow regime |
| Dittus-Boelter | $Nu = 0.023\,Re^{0.8}Pr^n$ | $n=0.4$ heating, $0.3$ cooling |
| LMTD | $\Delta T_{lm} = (\Delta T_1 - \Delta T_2)/\ln(\Delta T_1/\Delta T_2)$ | Heat exchangers |
| LMTD design eq. | $q = UA\,F\,\Delta T_{lm}$ | $F$ = correction factor |
| NTU | $NTU = UA/C_{min}$ | Effectiveness method |
| Effectiveness | $\varepsilon = q/q_{max}$ | $q_{max} = C_{min}(T_{h,in}-T_{c,in})$ |
| Clausius-Clapeyron | $\ln(P_2/P_1) = (\Delta H_{vap}/R)(1/T_1 - 1/T_2)$ | Phase change |

---

This comprehensive guide covers the fundamental principles of heat transfer including conduction, convection, and radiation, along with practical applications to heat exchangers and psychrometric processes. The material is designed for engineering students preparing for professional engineering examinations and practitioners needing a thorough reference.

## Introduction to Heat Transfer

Heat transfer is the science of thermal energy transport driven by temperature differences. Understanding heat transfer is essential for designing and analyzing thermal systems ranging from simple insulated pipes to complex heat exchangers and industrial processes.

### The Three Modes of Heat Transfer

Heat energy can be transferred by three fundamental mechanisms:

1. **Conduction**: Heat transfer through a stationary medium (solid, liquid, or gas) by molecular interaction. Energy is transferred from high-temperature regions to low-temperature regions through direct contact.

2. **Convection**: Heat transfer between a solid surface and a moving fluid. This mode combines conduction within the fluid near the surface with the bulk motion of the fluid.

3. **Radiation**: Heat transfer by electromagnetic waves. Unlike conduction and convection, radiation does not require a medium and can occur through a vacuum.

```{note}
In many practical engineering applications, multiple modes of heat transfer occur simultaneously. For example, heat loss from a hot pipe involves conduction through the pipe wall, convection to the surrounding air, and radiation to the environment.
```

### Sign Conventions and Units

Throughout this guide, we adopt the following conventions:

- Heat transfer rate $q$ is measured in Watts [W] or Btu/hr
- Heat flux $q''$ (heat transfer per unit area) is measured in W/m² or Btu/hr·ft²
- Temperature can be in Celsius [°C], Kelvin [K], or Fahrenheit [°F]
- Temperature differences are equivalent in °C and K (ΔT in °C = ΔT in K)
- Positive $q$ indicates heat transfer in the assumed positive direction

```{important}
When using the Stefan-Boltzmann law for radiation or gas laws, temperature **must** be in absolute units (Kelvin or Rankine). Always convert Celsius to Kelvin by adding 273.15.
```

---

## Heat Transfer by Conduction

Conduction is the most basic mode of heat transfer, occurring through direct molecular interaction within a material or between materials in direct contact. This section develops the fundamental equations governing steady-state conduction and applies them to practical geometries.

### Fourier's Law of Heat Conduction

```{prf:definition} Fourier's Law
:label: def-fourier-law

Conduction is the transfer of thermal energy through a medium by the direct interaction of its constituent particles. The rate of this transfer is governed by Fourier's Law, which states that the heat transfer rate is proportional to the area normal to the heat flow and the temperature gradient in that direction.
```

The mathematical expression of Fourier's Law in one dimension is:

$$

q = -k A \frac{dT}{dx}

$$

```{important}
**Key Variables for Conduction:**

- $q$ = rate of heat transfer [W]
- $q''$ = heat flux, or heat transfer rate per unit area ($q/A$) [W/m²]
- $k$ = thermal conductivity of the material [W/m·K]
- $A$ = cross-sectional area perpendicular to heat flow [m²]
- $\frac{dT}{dx}$ = temperature gradient in direction of heat flow [K/m]

The **negative sign** in Fourier's Law signifies that heat flows down the temperature gradient (from hot to cold). If temperature decreases with increasing $x$ (negative gradient), heat flows in the positive $x$ direction (positive $q$).
```

#### Physical Interpretation of Thermal Conductivity

Thermal conductivity $k$ is a material property that quantifies how readily a material conducts heat:

- **High $k$** (metals like copper: $k \approx 400$ W/m·K): Excellent heat conductors
- **Medium $k$** (water: $k \approx 0.6$ W/m·K): Moderate heat conductors  
- **Low $k$** (air: $k \approx 0.025$ W/m·K, insulation): Poor heat conductors (good insulators)

The thermal conductivity generally:
- **Increases** with temperature for gases
- **Decreases** with temperature for metals
- **Varies** for liquids and depends on molecular structure

```{seealso}
Thermal conductivity data for engineering materials can be found in standard references such as:
- Perry's Chemical Engineers' Handbook
- Incropera & DeWitt's Fundamentals of Heat and Mass Transfer
- ASHRAE Handbook of Fundamentals
```

### The Heat Diffusion Equation

For more complex situations involving time-varying temperatures, internal heat generation, or multiple dimensions, we start with the general heat diffusion equation (also called the heat equation).

#### General Form in Cartesian Coordinates

The complete heat diffusion equation in three dimensions is:

$$

\frac{\partial}{\partial x}\left(k \frac{\partial T}{\partial x}\right) + \frac{\partial}{\partial y}\left(k \frac{\partial T}{\partial y}\right) + \frac{\partial}{\partial z}\left(k \frac{\partial T}{\partial z}\right) + \dot{q} = \rho c_p \frac{\partial T}{\partial t}

$$

where:
- $\dot{q}$ = volumetric heat generation rate [W/m³]
- $\rho$ = density [kg/m³]
- $c_p$ = specific heat capacity [J/kg·K]
- $t$ = time [s]

The left side represents heat transfer by conduction in three dimensions plus internal heat generation. The right side represents the rate of thermal energy storage in the material.

#### Common Simplifying Assumptions

Most practical problems involve simplifications:

```{admonition} Standard Assumptions for Simplified Analysis
:class: tip

1. **Steady-State**: Temperature does not change with time, $\frac{\partial T}{\partial t} = 0$

2. **One-Dimensional**: Temperature varies in only one direction, e.g., $\frac{\partial T}{\partial y} = \frac{\partial T}{\partial z} = 0$

3. **No Heat Generation**: $\dot{q} = 0$ (no chemical reactions, electrical heating, or nuclear processes)

4. **Constant Thermal Conductivity**: $k$ is independent of temperature (valid for small temperature ranges)
```

### Conduction Through a Plane Wall

We now derive the temperature profile and heat transfer rate for the simplest geometry: a flat wall with uniform properties under steady-state, one-dimensional conditions.

#### Step 1: Simplify the Heat Diffusion Equation

Applying the standard assumptions, the general equation reduces to:

$$

\frac{d}{dx}\left(k \frac{dT}{dx}\right) = 0

$$

For constant thermal conductivity:

$$

k \frac{d^2T}{dx^2} = 0 \quad \implies \quad \frac{d^2T}{dx^2} = 0

$$

This ordinary differential equation states that the second derivative of temperature with respect to position is zero, meaning the temperature gradient is constant.

#### Step 2: Integrate to Find Temperature Distribution

Integrating once with respect to $x$:

$$

\frac{dT}{dx} = C_1

$$

This shows the temperature gradient is constant (as expected for steady, one-dimensional conduction with no heat generation).

Integrating a second time:

$$

T(x) = C_1 x + C_2

$$

This is the general solution showing that temperature varies **linearly** with position. The constants $C_1$ and $C_2$ are determined from boundary conditions.

#### Step 3: Apply Boundary Conditions

For a plane wall of thickness $L$ with known surface temperatures:

- **Boundary Condition 1**: At $x = 0$, $T(0) = T_{s1}$
  
  $$

  C_1(0) + C_2 = T_{s1} \implies C_2 = T_{s1}

  $$

- **Boundary Condition 2**: At $x = L$, $T(L) = T_{s2}$
  
  $$

  C_1 L + T_{s1} = T_{s2} \implies C_1 = \frac{T_{s2} - T_{s1}}{L}

  $$

#### Step 4: Final Equations

Substituting the constants back into our expressions:

```{important}
**Temperature Profile for a Plane Wall:**

$$

T(x) = \frac{T_{s2} - T_{s1}}{L}x + T_{s1}

$$

This can also be written in dimensionless form:

$$

\frac{T(x) - T_{s1}}{T_{s2} - T_{s1}} = \frac{x}{L}

$$

**Heat Transfer Rate:**

From Fourier's Law with $\frac{dT}{dx} = C_1 = \frac{T_{s2} - T_{s1}}{L}$:

$$

q = -k A \frac{T_{s2} - T_{s1}}{L} = k A \frac{T_{s1} - T_{s2}}{L}

$$

**Heat Flux:**

$$

q'' = \frac{q}{A} = k \frac{T_{s1} - T_{s2}}{L}

$$

```

Notice the heat transfer rate is positive when $T_{s1} > T_{s2}$, confirming that heat flows from the hot surface to the cold surface.

### Thermal Resistance Concept

By analogy with Ohm's Law for electrical circuits ($V = IR$), we can express heat transfer through a plane wall as:

$$

q = \frac{\Delta T}{R_{thermal}}

$$

where the **thermal resistance** is:

$$

R_{thermal} = \frac{L}{kA}

$$

For a thermal resistance per unit area (often more convenient):

$$

R'' = \frac{L}{k} \quad [m^2 \cdot K/W]

$$

Then:

$$

q = \frac{\Delta T}{R''} \cdot A

$$

```{admonition} Electrical-Thermal Analogy
:class: note

The analogy between thermal and electrical systems is powerful:

| Thermal | Electrical |
|---------|-----------|
| Heat flow rate, $q$ [W] | Current, $I$ [A] |
| Temperature difference, $\Delta T$ [K] | Voltage difference, $\Delta V$ [V] |
| Thermal resistance, $R$ [K/W] | Electrical resistance, $R$ [Ω] |

This analogy allows us to use circuit analysis techniques (series/parallel resistances, Kirchhoff's laws) to solve complex heat transfer problems.
```

### Composite Walls

For walls composed of multiple layers of different materials in series, the total thermal resistance is the sum of individual resistances:

$$

R_{total} = R_1 + R_2 + R_3 + \cdots = \frac{L_1}{k_1 A} + \frac{L_2}{k_2 A} + \frac{L_3}{k_3 A} + \cdots

$$

The heat transfer rate through the composite wall is:

$$

q = \frac{T_{s1} - T_{sn}}{R_{total}} = \frac{T_{s1} - T_{sn}}{\sum_{i} \frac{L_i}{k_i A}}

$$

```{prf:example} Three-Layer Composite Wall
:label: ex-composite-wall

A furnace wall consists of three layers:
- Layer 1 (inside): Fire brick, $L_1 = 0.10$ m, $k_1 = 1.0$ W/m·K
- Layer 2 (middle): Insulating brick, $L_2 = 0.15$ m, $k_2 = 0.2$ W/m·K  
- Layer 3 (outside): Red brick, $L_3 = 0.05$ m, $k_3 = 0.7$ W/m·K

The inside surface temperature is $T_{s1} = 600°C$ and the outside surface temperature is $T_{s4} = 50°C$. The wall area is $A = 10$ m². Find the heat transfer rate.

**Solution:**

Calculate individual thermal resistances:

$$

R_1 = \frac{0.10}{1.0 \times 10} = 0.01 \text{ K/W}

$$

$$

R_2 = \frac{0.15}{0.2 \times 10} = 0.075 \text{ K/W}

$$

$$

R_3 = \frac{0.05}{0.7 \times 10} = 0.00714 \text{ K/W}

$$

Total resistance:

$$

R_{total} = 0.01 + 0.075 + 0.00714 = 0.09214 \text{ K/W}

$$

Heat transfer rate:

$$

q = \frac{600 - 50}{0.09214} = \frac{550}{0.09214} = 5970 \text{ W} \approx 6.0 \text{ kW}

$$

The heat loss through the furnace wall is approximately 6.0 kW.
```

### Heat Generation in Solids

When internal heat generation occurs (e.g., electrical resistance heating, nuclear decay, exothermic chemical reactions), the heat diffusion equation includes the source term $\dot{q}$.

For steady-state, one-dimensional conduction with uniform heat generation in a plane wall:

$$

\frac{d^2T}{dx^2} + \frac{\dot{q}}{k} = 0

$$

The solution (with symmetric boundary conditions) yields a parabolic temperature profile rather than linear.

```{prf:example} Volumetric Heat Generation in a Pipe Wall
:label: ex-pipe-heat-generation

Water is heated as it flows through a thick-walled pipe. Determine the uniform volumetric heat generation rate ($\dot{q}$) within the pipe wall required to achieve a specific temperature rise in the water.

**Given:**
- Pipe Length: $L = 10$ m
- Inside Diameter: $D_i = 0.015$ m
- Outside Diameter: $D_o = 0.030$ m
- Water Mass Flow Rate: $\dot{m} = 0.3$ kg/s
- Water Inlet Temperature: $T_{in} = 25°C$
- Water Outlet Temperature: $T_{out} = 45°C$
- Water Specific Heat: $c_p = 4178$ J/kg·K
- Outer surface is perfectly insulated

**Solution:**

**Step 1: Calculate Total Heat Transfer Rate to Water**

The heat transferred to the water equals its enthalpy change:

$$

q = \dot{m} c_p (T_{out} - T_{in})

$$

$$

q = (0.3 \text{ kg/s}) \times (4178 \text{ J/kg·K}) \times (45°C - 25°C)

$$

$$

q = 0.3 \times 4178 \times 20 = 25068 \text{ W}

$$

**Step 2: Calculate Pipe Wall Volume**

The volume of the hollow cylindrical pipe wall:

$$

V_{wall} = \frac{\pi}{4}(D_o^2 - D_i^2) \times L

$$

$$

V_{wall} = \frac{\pi}{4}((0.030)^2 - (0.015)^2) \times 10

$$

$$

V_{wall} = \frac{\pi}{4}(0.0009 - 0.000225) \times 10 = \frac{\pi}{4}(0.000675) \times 10 \approx 0.0053 \text{ m}^3

$$

**Step 3: Calculate Required Heat Generation Rate**

Since the outer surface is insulated, all generated heat goes to the water:

$$

\dot{q} = \frac{q}{V_{wall}} = \frac{25068}{0.0053} \approx 4.73 \times 10^6 \text{ W/m}^3

$$

**Final Answer:** The required uniform volumetric heat generation rate is approximately **4.73 MW/m³**.
```

---

## Heat Transfer by Convection

Convection is heat transfer between a solid surface and a moving fluid. This mode combines conduction within the fluid near the surface (where the fluid velocity is low) with the bulk motion (advection) of the fluid. Convection is classified into two types:

- **Forced Convection**: Fluid motion is induced by external means (pumps, fans, wind)
- **Natural (Free) Convection**: Fluid motion is caused by buoyancy forces due to density differences resulting from temperature variations

### Newton's Law of Cooling

The rate of convective heat transfer is given by Newton's Law of Cooling:

$$

q_{conv} = h A_s (T_s - T_{\infty})

$$

```{important}
**Key Variables for Convection:**

- $q_{conv}$ = rate of convective heat transfer [W]
- $h$ = convective heat transfer coefficient [W/m²·K]
- $A_s$ = surface area for heat transfer [m²]
- $T_s$ = temperature of the solid surface [K or °C]
- $T_{\infty}$ = free-stream (bulk) temperature of the fluid [K or °C]
```

**Important Note:** Unlike thermal conductivity $k$ (which is a fluid property), the heat transfer coefficient $h$ is **not** a fluid property. Instead, $h$ depends on:
- Fluid properties (viscosity, density, specific heat, thermal conductivity)
- Flow conditions (velocity, laminar vs. turbulent)
- Surface geometry (flat plate, cylinder, sphere, etc.)
- Surface roughness and orientation

The primary challenge in convection analysis is determining the appropriate value of $h$ for a given situation.

### Boundary Layer Concepts

When a fluid flows over a surface, two distinct boundary layers develop:

```{prf:definition} Momentum Boundary Layer
:label: def-momentum-bl

The **momentum boundary layer** ($\delta$) is the region near the surface where the fluid velocity is affected by viscous forces. The fluid velocity is zero at the surface (no-slip condition) and increases to the free-stream velocity $u_{\infty}$.

Formally, $\delta$ is defined as the distance from the surface where:

$$

u(y=\delta) = 0.99 u_{\infty}

$$

```

```{prf:definition} Thermal Boundary Layer
:label: def-thermal-bl

The **thermal boundary layer** ($\delta_t$) is the region near the surface where the fluid temperature is affected by heat transfer with the surface. The fluid temperature varies from $T_s$ at the surface to $T_{\infty}$ in the free stream.

Formally, $\delta_t$ is defined as the distance from the surface where:

$$

\frac{T(y=\delta_t) - T_s}{T_{\infty} - T_s} = 0.99

$$

```

The relative thickness of these boundary layers is governed by the Prandtl number (discussed below). Both boundary layers grow in thickness as fluid moves along the surface.

### Dimensionless Numbers in Convection

Convection analysis relies heavily on dimensionless groups that characterize different physical phenomena:

#### Reynolds Number

```{prf:definition} Reynolds Number
:label: def-reynolds

The **Reynolds number** ($Re$) is the ratio of inertial forces to viscous forces:

$$

Re = \frac{\rho u L_c}{\mu} = \frac{u L_c}{\nu}

$$

where:
- $\rho$ = fluid density [kg/m³]
- $u$ = characteristic velocity [m/s]
- $L_c$ = characteristic length [m]
- $\mu$ = dynamic viscosity [kg/m·s or Pa·s]
- $\nu = \mu/\rho$ = kinematic viscosity [m²/s]
```

**Physical Meaning:** The Reynolds number determines whether flow is laminar (smooth, ordered) or turbulent (chaotic, mixing):

- **Laminar flow**: $Re < Re_{critical}$ (typically $Re < 2300$ for pipes, $Re_x < 5 \times 10^5$ for flat plates)
- **Turbulent flow**: $Re > Re_{critical}$
- **Transition region**: Near $Re_{critical}$

For flow over a flat plate, the **local Reynolds number** at position $x$ is:

$$

Re_x = \frac{u_{\infty} x}{\nu}

$$

This increases with distance from the leading edge, causing flow to transition from laminar to turbulent at the critical Reynolds number.

#### Prandtl Number

```{prf:definition} Prandtl Number
:label: def-prandtl

The **Prandtl number** ($Pr$) is the ratio of momentum diffusivity to thermal diffusivity:

$$

Pr = \frac{\nu}{\alpha} = \frac{\mu c_p}{k}

$$

where:
- $\alpha = k/(\rho c_p)$ = thermal diffusivity [m²/s]
- $c_p$ = specific heat at constant pressure [J/kg·K]
```

**Physical Meaning:** The Prandtl number compares the rate at which momentum diffuses to the rate at which heat diffuses:

- **$Pr < 1$** (liquid metals, $Pr \approx 0.01$): Heat diffuses faster than momentum; $\delta_t > \delta$
- **$Pr \approx 1$** (gases, $Pr \approx 0.7$): Momentum and heat diffuse at similar rates; $\delta_t \approx \delta$
- **$Pr > 1$** (water $Pr \approx 7$, oils $Pr \approx 100-10000$): Momentum diffuses faster than heat; $\delta > \delta_t$

The Prandtl number is essentially a fluid property (depends only on fluid properties, not flow conditions).

#### Nusselt Number

```{prf:definition} Nusselt Number
:label: def-nusselt

The **Nusselt number** ($Nu$) is the dimensionless heat transfer coefficient:

$$

Nu = \frac{h L_c}{k_f}

$$

where $k_f$ is the thermal conductivity of the fluid.
```

**Physical Meaning:** The Nusselt number represents the ratio of convective to conductive heat transfer:

- $Nu = 1$: Pure conduction (no convection enhancement)
- $Nu > 1$: Convection enhances heat transfer beyond pure conduction

The Nusselt number is the primary dependent variable in convection correlations. Most correlations have the form:

$$

Nu = f(Re, Pr, \text{geometry})

$$

To find the heat transfer coefficient, we:
1. Calculate $Re$ and $Pr$ from fluid properties and flow conditions
2. Use the appropriate correlation to find $Nu$
3. Solve for $h$ from the definition: $h = \frac{Nu \cdot k_f}{L_c}$

### Systematic Approach to Convection Problems

```{admonition} Step-by-Step Procedure for Convection Calculations
:class: tip

**Step 1: Identify the Geometry**

Determine the physical configuration:
- External flow: flat plate, cylinder, sphere
- Internal flow: circular pipe, rectangular duct, annulus
- Natural or forced convection

**Step 2: Determine Fluid Properties**

Evaluate fluid properties at the appropriate reference temperature. Common choices:
- **Film temperature**: $T_f = (T_s + T_{\infty})/2$ (most common)
- **Free-stream temperature**: $T_{\infty}$ (for some correlations)
- **Bulk mean temperature**: $T_m$ (for internal flows)

Required properties: $k_f$, $\mu$ (or $\nu$), $\rho$, $c_p$

**Step 3: Calculate Reynolds Number**

$$

Re_{L_c} = \frac{\rho u L_c}{\mu} = \frac{u L_c}{\nu}

$$

Choose appropriate characteristic length $L_c$:
- Flat plate: length from leading edge
- Cylinder/sphere: diameter
- Pipe: diameter

**Step 4: Calculate Prandtl Number**

$$

Pr = \frac{\mu c_p}{k_f} = \frac{\nu}{\alpha}

$$

**Step 5: Select and Apply Correlation**

Based on geometry and Reynolds number, choose the appropriate Nusselt number correlation:

$$

Nu = f(Re, Pr, \text{other parameters})

$$

Common form: $Nu = C Re^m Pr^n$

**Step 6: Calculate Heat Transfer Coefficient**

$$

h = \frac{Nu \cdot k_f}{L_c}

$$

**Step 7: Calculate Heat Transfer Rate**

$$

q_{conv} = h A_s (T_s - T_{\infty})

$$

```

### Common Convection Correlations

While a complete catalog of correlations is beyond this guide's scope, here are some frequently used correlations:

#### Forced Convection Over a Flat Plate

**Laminar flow** ($Re_x < 5 \times 10^5$):

Local Nusselt number:

$$

Nu_x = 0.332 Re_x^{1/2} Pr^{1/3} \quad (Pr \geq 0.6)

$$

Average Nusselt number over length $L$:

$$

\overline{Nu}_L = 0.664 Re_L^{1/2} Pr^{1/3}

$$

**Turbulent flow** ($Re_x > 5 \times 10^5$):

Average Nusselt number (mixed laminar-turbulent):

$$

\overline{Nu}_L = (0.037 Re_L^{4/5} - 871) Pr^{1/3}

$$

valid for $0.6 \leq Pr \leq 60$ and $5 \times 10^5 < Re_L < 10^8$.

#### Forced Convection in Circular Pipes

For **fully developed turbulent flow** in smooth pipes ($Re_D > 10000$):

**Dittus-Boelter equation**:

$$

Nu_D = 0.023 Re_D^{4/5} Pr^n

$$

where:
- $n = 0.4$ for heating (fluid heated, $T_s > T_m$)
- $n = 0.3$ for cooling (fluid cooled, $T_s < T_m$)
- Valid for: $0.7 \leq Pr \leq 160$, $Re_D \geq 10000$, $L/D \geq 10$

For **laminar flow** in circular pipes ($Re_D < 2300$), fully developed:
- Constant surface temperature: $Nu_D = 3.66$
- Constant surface heat flux: $Nu_D = 4.36$

#### Natural Convection

For natural convection from a vertical plate, the Nusselt number depends on the Rayleigh number:

$$

Ra_L = Gr_L \cdot Pr = \frac{g \beta (T_s - T_{\infty}) L^3}{\nu^2} \cdot Pr

$$

where:
- $g$ = gravitational acceleration [m/s²]
- $\beta$ = volumetric thermal expansion coefficient [1/K] ($\beta \approx 1/T_f$ for ideal gases)
- $Gr_L$ = Grashof number (buoyancy/viscous forces)

**Vertical plate** (laminar, $10^4 < Ra_L < 10^9$):

$$

\overline{Nu}_L = 0.59 Ra_L^{1/4}

$$

**Vertical plate** (turbulent, $10^9 < Ra_L < 10^{13}$):

$$

\overline{Nu}_L = 0.10 Ra_L^{1/3}

$$

```{seealso}
For comprehensive collections of heat transfer correlations, consult:
- Incropera, DeWitt, Bergman & Lavine: *Fundamentals of Heat and Mass Transfer*
- Churchill & Chu: "Correlating Equations for Laminar and Turbulent Free Convection from a Vertical Plate"
- Gnielinski: "New Equations for Heat and Mass Transfer in Turbulent Pipe and Channel Flow"
```

### Local vs. Average Heat Transfer Coefficients

The heat transfer coefficient $h$ generally varies along a surface due to boundary layer development. We distinguish between:

**Local heat transfer coefficient** ($h_x$): The value at a specific location $x$ on the surface.

**Average heat transfer coefficient** ($\bar{h}_L$): The integrated average over the entire surface of length $L$:

$$

\bar{h}_L = \frac{1}{L} \int_0^L h_x \, dx

$$

The total heat transfer from a surface uses the average coefficient:

$$

q_{total} = \bar{h}_L A (T_s - T_{\infty})

$$

```{prf:example} Calculating Average Coefficient from Local Coefficient
:label: ex-average-h

The local heat transfer coefficient for flow over a 1-meter long flat plate is given by:

$$

h_x = 5x^{-1/3} \text{ W/m}^2\cdot\text{K}

$$

where $x$ is the distance from the leading edge in meters. Find the average heat transfer coefficient $\bar{h}_L$ for the entire plate.

**Solution:**

Apply the definition of average heat transfer coefficient:

$$

\bar{h}_L = \frac{1}{L} \int_0^L h_x \, dx = \frac{1}{1} \int_0^1 5x^{-1/3} \, dx

$$

Evaluate the integral:

$$

\int 5x^{-1/3} \, dx = 5 \cdot \frac{x^{2/3}}{2/3} = 7.5 x^{2/3}

$$

$$

\bar{h}_L = \left[ 7.5 x^{2/3} \right]_0^1 = 7.5(1)^{2/3} - 7.5(0)^{2/3} = 7.5 \text{ W/m}^2\cdot\text{K}

$$

**Final Answer:** The average heat transfer coefficient is **7.5 W/m²·K**.

**Note:** At the trailing edge ($x = 1$ m), the local coefficient is $h_x(1) = 5(1)^{-1/3} = 5$ W/m²·K. The average value is higher because the coefficient is much larger near the leading edge where the boundary layer is thin.
```

### Overall Heat Transfer Coefficient

When heat is transferred through a composite system involving multiple modes in series (e.g., convection → conduction → convection), it's convenient to define an **overall heat transfer coefficient** $U$ that accounts for all resistances:

$$

q = U A \Delta T_{overall}

$$

For resistances in series, the overall coefficient is related to the total thermal resistance:

$$

U = \frac{1}{R''_{total} \cdot A} = \frac{1}{R''_{total}}

$$

where $R''_{total}$ is the total thermal resistance per unit area.

#### Composite Plane Wall with Convection

For a composite wall with convection on both sides:

$$

R''_{total} = R''_{conv,1} + R''_{cond,1} + R''_{cond,2} + \cdots + R''_{cond,n} + R''_{conv,2}

$$

$$

R''_{total} = \frac{1}{h_1} + \frac{L_1}{k_1} + \frac{L_2}{k_2} + \cdots + \frac{L_n}{k_n} + \frac{1}{h_2}

$$

The overall heat transfer coefficient is:

$$

U = \left( \frac{1}{h_1} + \sum_{i=1}^n \frac{L_i}{k_i} + \frac{1}{h_2} \right)^{-1}

$$

```{prf:example} Overall U for a Composite Wall
:label: ex-overall-u

A wall consists of three material layers:
- Layer 1: $L_1 = 0.1$ m, $k_1 = 1.0$ W/m·K
- Layer 2: $L_2 = 0.05$ m, $k_2 = 0.04$ W/m·K (insulation)
- Layer 3: $L_3 = 0.15$ m, $k_3 = 0.8$ W/m·K

Inside convection coefficient: $h_1 = 20$ W/m²·K

Outside convection coefficient: $h_2 = 10$ W/m²·K

Find the overall heat transfer coefficient $U$.

**Solution:**

Calculate individual resistances per unit area:

$$

R''_{conv,1} = \frac{1}{20} = 0.050 \text{ m}^2\cdot\text{K/W}

$$

$$

R''_{cond,1} = \frac{0.1}{1.0} = 0.100 \text{ m}^2\cdot\text{K/W}

$$

$$

R''_{cond,2} = \frac{0.05}{0.04} = 1.250 \text{ m}^2\cdot\text{K/W}

$$

$$

R''_{cond,3} = \frac{0.15}{0.8} = 0.188 \text{ m}^2\cdot\text{K/W}

$$

$$

R''_{conv,2} = \frac{1}{10} = 0.100 \text{ m}^2\cdot\text{K/W}

$$

Total resistance:

$$

R''_{total} = 0.050 + 0.100 + 1.250 + 0.188 + 0.100 = 1.688 \text{ m}^2\cdot\text{K/W}

$$

Overall heat transfer coefficient:

$$

U = \frac{1}{1.688} = 0.593 \text{ W/m}^2\cdot\text{K}

$$

**Final Answer:** $U = 0.59$ W/m²·K

**Analysis:** The insulation layer (Layer 2) dominates the thermal resistance ($R''_{cond,2} = 1.250$ out of $R''_{total} = 1.688$, or 74% of total resistance). This is typical: in well-designed insulated systems, the insulation provides most of the thermal resistance.
```

---

## Heat Transfer by Radiation

Radiation is the transfer of energy by electromagnetic waves. Unlike conduction and convection, radiation does not require a medium and can occur through a vacuum. All surfaces at temperatures above absolute zero emit thermal radiation.

### Fundamental Radiative Properties

To analyze radiative heat transfer, we must understand four key radiative fluxes at a surface:

```{important}
**The Four Radiative Heat Fluxes:**

1. **Emissive Power** ($E$): Rate at which radiation is **emitted** from a surface per unit area [W/m²]

2. **Irradiation** ($G$): Rate at which radiation is **incident upon** (strikes) a surface from all surroundings per unit area [W/m²]

3. **Radiosity** ($J$): Total rate at which radiation **leaves** a surface per unit area [W/m²] (sum of emitted and reflected radiation)

4. **Net Radiative Heat Flux** ($q''_{rad}$): Net rate of energy transfer away from the surface by radiation [W/m²]
```

The relationship between these quantities is:

$$

q''_{rad} = J - G

$$

If $J > G$, the surface has a net heat loss by radiation. If $G > J$, the surface has a net heat gain.

### Blackbody Radiation

```{prf:definition} Blackbody
:label: def-blackbody

A **blackbody** is an idealized surface that:
1. Absorbs all incident radiation ($\alpha = 1$)
2. Emits the maximum possible thermal radiation at a given temperature
3. Has emissive power that depends only on temperature (not direction or wavelength)
```

The emissive power of a blackbody is given by the Stefan-Boltzmann Law:

$$

E_b = \sigma T^4

$$

where:
- $E_b$ = blackbody emissive power [W/m²]
- $\sigma = 5.67 \times 10^{-8}$ W/m²·K⁴ (Stefan-Boltzmann constant)
- $T$ = absolute temperature [K] (**must be in Kelvin**)

```{warning}
**Critical Reminder:** The Stefan-Boltzmann Law requires temperature in **absolute units** (Kelvin). Always convert Celsius to Kelvin:

$$

T[K] = T[°C] + 273.15

$$

For example, a surface at 25°C has $T = 298.15$ K, and its blackbody emissive power is:

$$

E_b = 5.67 \times 10^{-8} \times (298.15)^4 = 448 \text{ W/m}^2

$$

```

### Real Surface Properties

Real surfaces emit less radiation than a blackbody at the same temperature. This is characterized by the **emissivity** $\epsilon$:

```{prf:definition} Emissivity
:label: def-emissivity

**Emissivity** ($\epsilon$) is the ratio of the radiation emitted by a real surface to that emitted by a blackbody at the same temperature:

$$

\epsilon = \frac{E}{E_b}

$$

where $0 \leq \epsilon \leq 1$.
```

For a real surface:

$$

E = \epsilon E_b = \epsilon \sigma T^4

$$

Typical emissivity values:
- Polished metals: $\epsilon \approx 0.02 - 0.10$ (poor emitters/absorbers)
- Oxidized metals: $\epsilon \approx 0.2 - 0.8$
- Non-metals (wood, brick, paint): $\epsilon \approx 0.8 - 0.95$ (good emitters/absorbers)
- Blackbody (ideal): $\epsilon = 1.0$

### Surface Radiative Properties

When irradiation $G$ strikes a surface, it is:
- **Absorbed** (fraction $\alpha$)
- **Reflected** (fraction $\rho$)
- **Transmitted** (fraction $\tau$)

Energy conservation requires:

$$

\alpha + \rho + \tau = 1

$$

For **opaque** surfaces (most solids), $\tau = 0$, so:

$$

\alpha + \rho = 1

$$

```{important}
**Key Surface Properties:**

- **Absorptivity** ($\alpha$): Fraction of incident radiation absorbed ($0 \leq \alpha \leq 1$)
- **Reflectivity** ($\rho$): Fraction of incident radiation reflected ($0 \leq \rho \leq 1$)
- **Transmissivity** ($\tau$): Fraction of incident radiation transmitted ($0 \leq \tau \leq 1$)
```

#### Gray Surface Assumption

A **gray surface** is one whose radiative properties are independent of wavelength. For a gray surface in thermal equilibrium (Kirchhoff's Law):

$$

\alpha = \epsilon

$$

This simplification is widely used in engineering calculations and is reasonably accurate for many materials.

### Radiosity

The **radiosity** $J$ is the total radiation leaving a surface, combining emitted and reflected components:

$$

J = E + \rho G

$$

For an opaque, gray surface with $\rho = 1 - \alpha = 1 - \epsilon$:

$$

J = \epsilon \sigma T^4 + (1 - \epsilon) G

$$

The net radiative heat flux from a surface can be written as:

$$

q''_{rad} = \frac{E_b - J}{(1-\epsilon)/\epsilon}

$$

This form suggests a resistance analogy, which leads to the radiation network method.

### View Factors

In thermal radiation, the **view factor** (also called configuration factor or shape factor) is a purely geometric quantity describing how well two surfaces "see" each other.

```{prf:definition} View Factor
:label: def-view-factor

The view factor $F_{ij}$ is the **fraction of radiation leaving surface $i$** that directly strikes **surface $j$**.

- The first subscript ($i$) denotes the emitting surface
- The second subscript ($j$) denotes the receiving surface
- $0 \leq F_{ij} \leq 1$
```

View factors are essential for calculating radiation exchange between surfaces. They depend only on geometry (surface sizes, shapes, and relative orientations), not on surface temperatures or properties.

#### View Factor Rules

Most view factor problems can be solved using three fundamental rules:

```{prf:theorem} Summation Rule
:label: thm-summation-rule

For an enclosure of $n$ surfaces, all radiation leaving surface $i$ must be intercepted by surfaces of the enclosure:

$$

\sum_{j=1}^{n} F_{ij} = F_{i1} + F_{i2} + \cdots + F_{in} = 1

$$

This includes the view factor from a surface to itself, $F_{ii}$:
- For **flat** or **convex** surfaces: $F_{ii} = 0$
- For **concave** surfaces: $F_{ii} > 0$
```

```{prf:theorem} Reciprocity Rule
:label: thm-reciprocity-rule

The reciprocity relationship relates a view factor $F_{ij}$ to its inverse $F_{ji}$:

$$

A_i F_{ij} = A_j F_{ji}

$$

where $A_i$ and $A_j$ are the surface areas.
```

```{prf:theorem} Additive Rule (Superposition)
:label: thm-additive-rule

If surface $j$ is subdivided into parts $j_1, j_2, \ldots, j_n$:

$$

F_{i,j} = F_{i,j_1} + F_{i,j_2} + \cdots + F_{i,j_n}

$$

This allows complex geometries to be analyzed by combining simpler ones.
```

```{prf:example} View Factors for Hemispherical Duct
:label: ex-hemisphere-view-factors

Consider a long duct whose cross-section is a hemisphere. Let Surface 1 be the flat floor and Surface 2 be the curved ceiling. The hemisphere has radius $r$ and length $L$. Determine the view factors $F_{12}$, $F_{21}$, and $F_{22}$.

**Solution:**

**Step 1: Calculate Surface Areas**

Surface 1 (flat floor):

$$

A_1 = (2r) \times L

$$

Surface 2 (curved semi-cylinder):

$$

A_2 = \frac{1}{2}(2\pi r) \times L = \pi r L

$$

**Step 2: Find $F_{12}$ using Summation Rule**

For surface 1 (flat):

$$

F_{11} + F_{12} = 1

$$

Since surface 1 is flat, $F_{11} = 0$:

$$

F_{12} = 1

$$

**Physical interpretation:** All radiation leaving the flat floor must strike the curved ceiling (nowhere else to go).

**Step 3: Find $F_{21}$ using Reciprocity**

$$

A_2 F_{21} = A_1 F_{12}

$$

$$

F_{21} = F_{12} \frac{A_1}{A_2} = 1 \times \frac{2rL}{\pi r L} = \frac{2}{\pi} \approx 0.637

$$

**Step 4: Find $F_{22}$ using Summation Rule**

For surface 2:

$$

F_{21} + F_{22} = 1

$$

$$

F_{22} = 1 - F_{21} = 1 - \frac{2}{\pi} \approx 0.363

$$

**Physical interpretation:** About 36.3% of radiation leaving the curved ceiling strikes itself (because it's concave).

**Final Answers:**
- $F_{12} = 1.0$ (all radiation from floor hits ceiling)
- $F_{21} \approx 0.637$ (about 64% of radiation from ceiling hits floor)
- $F_{22} \approx 0.363$ (about 36% of radiation from ceiling hits itself)
```

### Radiation Exchange Between Surfaces

For an enclosure of opaque, diffuse, gray surfaces, radiation exchange can be modeled using a thermal resistance network analogous to electrical circuits.

#### Surface Resistance

The **surface resistance** represents the opposition to radiation leaving a surface due to non-ideal emissivity:

$$

R_{surf,i} = \frac{1 - \epsilon_i}{\epsilon_i A_i}

$$

The net heat transfer rate leaving surface $i$ is:

$$

q_i = \frac{E_{b,i} - J_i}{R_{surf,i}} = \frac{\sigma T_i^4 - J_i}{(1-\epsilon_i)/(\epsilon_i A_i)}

$$

For a blackbody ($\epsilon_i = 1$), the surface resistance is zero, and $E_{b,i} = J_i$.

#### Space Resistance

The **space resistance** (or geometric resistance) represents the geometric opposition to radiation between two surfaces:

$$

R_{space,ij} = \frac{1}{A_i F_{ij}} = \frac{1}{A_j F_{ji}}

$$

(The equality follows from reciprocity.)

The net radiation exchange between surfaces $i$ and $j$ is:

$$

q_{ij} = \frac{J_i - J_j}{R_{space,ij}}

$$

#### Constructing the Radiation Network

```{admonition} Procedure for Drawing Radiation Networks
:class: tip

For an enclosure of $n$ opaque, diffuse, gray surfaces:

**Step 1:** Create **potential nodes** for each surface representing $E_{b,i} = \sigma T_i^4$

**Step 2:** Create **radiosity nodes** for each surface representing $J_i$

**Step 3:** Connect each $E_{b,i}$ node to its $J_i$ node with surface resistance $R_{surf,i} = \frac{1-\epsilon_i}{\epsilon_i A_i}$

**Step 4:** Connect every radiosity node $J_i$ to every other radiosity node $J_j$ with space resistance $R_{space,ij} = \frac{1}{A_i F_{ij}}$

Once the network is drawn, use circuit analysis (Kirchhoff's laws, nodal analysis) to solve for unknown temperatures and heat transfer rates.
```

The total net heat leaving surface $i$ is:

$$

q_i = \frac{E_{b,i} - J_i}{R_{surf,i}} = \sum_{j=1}^{n} \frac{J_i - J_j}{R_{space,ij}}

$$

```{note}
For a **two-surface enclosure** (surfaces $i$ and $j$ completely surround each other), the net radiation exchange simplifies to:

$$

q_{ij} = \frac{\sigma(T_i^4 - T_j^4)}{\frac{1-\epsilon_i}{\epsilon_i A_i} + \frac{1}{A_i F_{ij}} + \frac{1-\epsilon_j}{\epsilon_j A_j}}

$$

If both surfaces are large and parallel ($F_{ij} = 1$, $A_i = A_j = A$):

$$

q_{ij} = \frac{\sigma A (T_i^4 - T_j^4)}{\frac{1}{\epsilon_i} + \frac{1}{\epsilon_j} - 1}

$$

```

---

## Heat Exchangers

Heat exchangers are devices designed to efficiently transfer thermal energy from one fluid to another. They are ubiquitous in engineering applications including power plants, refrigeration systems, chemical processes, and HVAC systems.

### Heat Exchanger Types

**Classification by flow arrangement:**

1. **Parallel Flow (Co-current)**: Both fluids enter at the same end and flow in the same direction
2. **Counter-flow**: Fluids enter at opposite ends and flow in opposite directions
3. **Cross-flow**: Fluids flow perpendicular to each other
4. **Shell-and-tube**: One fluid flows through tubes while the other flows around the tubes in a shell

**Classification by construction:**

1. **Double-pipe (concentric tube)**: Simplest type, one tube inside another
2. **Shell-and-tube**: Multiple tubes enclosed in a shell
3. **Plate**: Fluids flow between corrugated plates
4. **Compact**: High surface area per volume (e.g., car radiators)

### Fundamental Energy Balance

For a heat exchanger with no heat loss to surroundings (adiabatic):

$$

q = \dot{m}_h c_{p,h} (T_{h,in} - T_{h,out}) = \dot{m}_c c_{p,c} (T_{c,out} - T_{c,in})

$$

where subscripts $h$ and $c$ denote hot and cold fluids.

This equation states that the heat lost by the hot fluid equals the heat gained by the cold fluid.

### Log Mean Temperature Difference (LMTD) Method

The LMTD method is the primary approach for heat exchanger design and analysis when inlet and outlet temperatures are known or can be calculated.

#### Concept

In a heat exchanger, the temperature difference between hot and cold fluids **varies along the length** of the exchanger. The LMTD is the appropriate average temperature difference to use in the basic heat transfer equation.

The total heat transfer rate is:

$$

q = U A \Delta T_{lm}

$$

where:
- $U$ = overall heat transfer coefficient [W/m²·K]
- $A$ = total heat transfer surface area [m²]
- $\Delta T_{lm}$ = log mean temperature difference [K or °C]

#### Calculating LMTD

The LMTD is the logarithmic average of the temperature differences at the two ends:

$$

\Delta T_{lm} = \frac{\Delta T_A - \Delta T_B}{\ln(\Delta T_A / \Delta T_B)}

$$

where $\Delta T_A$ and $\Delta T_B$ are the temperature differences between hot and cold streams at the two ends of the exchanger.

**Important:** When $\Delta T_A \approx \Delta T_B$ (differ by less than ~10%), the LMTD formula can give numerical errors. In this case, use the arithmetic mean:

$$

\Delta T_{lm} \approx \frac{\Delta T_A + \Delta T_B}{2} \quad \text{(when } \Delta T_A \approx \Delta T_B \text{)}

$$

#### For Parallel Flow

$$

\Delta T_A = T_{h,in} - T_{c,in} \quad \text{(inlet end)}

$$

$$

\Delta T_B = T_{h,out} - T_{c,out} \quad \text{(outlet end)}

$$

```{note}
In parallel flow, the outlet temperature of the cold fluid can **never exceed** the outlet temperature of the hot fluid: $T_{c,out} < T_{h,out}$ always.
```

#### For Counter-flow

$$

\Delta T_A = T_{h,in} - T_{c,out} \quad \text{(hot inlet / cold outlet end)}

$$

$$

\Delta T_B = T_{h,out} - T_{c,in} \quad \text{(hot outlet / cold inlet end)}

$$

```{note}
Counter-flow is **more efficient** than parallel flow because it maintains a larger average temperature difference. In counter-flow, the cold fluid outlet temperature can approach (or even theoretically exceed) the hot fluid outlet temperature.
```

```{important}
**Design Considerations:**

- Always calculate temperature differences as $\Delta T = T_{hot} - T_{cold}$ to ensure positive values
- **Large LMTD** ($> 100°C$): Can indicate potential thermal stress problems requiring special exchanger designs (floating head, U-tube, expansion joints)
- Verify LMTD calculations from simulation software manually to catch errors
```

```{prf:example} Sizing a Parallel-Flow Heat Exchanger
:label: ex-parallel-flow-hx

Hot oil is cooled in a parallel-flow concentric tube heat exchanger using water.

**Given:**
- Hot fluid (oil): $T_{oil,in} = 100°C$, $T_{oil,out} = 60°C$, $\dot{m}_{oil} = 0.15$ kg/s, $c_{p,oil} = 2131$ J/kg·°C
- Cold fluid (water): $T_{water,in} = 25°C$
- Temperature difference at outlet: $\Delta T_2 = 10°C$ (specified)
- Overall heat transfer coefficient: $U = 38.1$ W/m²·°C
- Inner tube diameter: $D_i = 0.03$ m

Determine the required length $L$ of the heat exchanger.

**Solution:**

**Step 1: Calculate Heat Transfer Rate**

$$

q = \dot{m}_{oil} c_{p,oil} (T_{oil,in} - T_{oil,out})

$$

$$

q = (0.15) \times (2131) \times (100 - 60) = 0.15 \times 2131 \times 40 = 12786 \text{ W}

$$

**Step 2: Determine Water Outlet Temperature**

From the given outlet temperature difference:

$$

\Delta T_2 = T_{oil,out} - T_{water,out} = 10°C

$$

$$

T_{water,out} = T_{oil,out} - 10 = 60 - 10 = 50°C

$$

**Step 3: Calculate LMTD**

Temperature differences at the ends:

$$

\Delta T_1 = T_{oil,in} - T_{water,in} = 100 - 25 = 75°C

$$

$$

\Delta T_2 = T_{oil,out} - T_{water,out} = 60 - 50 = 10°C

$$

Log mean temperature difference:

$$

\Delta T_{lm} = \frac{\Delta T_1 - \Delta T_2}{\ln(\Delta T_1/\Delta T_2)} = \frac{75 - 10}{\ln(75/10)} = \frac{65}{\ln(7.5)} = \frac{65}{2.015} \approx 32.2°C

$$

**Step 4: Calculate Required Length**

The heat transfer area for a tube is $A = \pi D_i L$. From $q = U A \Delta T_{lm}$:

$$

L = \frac{q}{U \pi D_i \Delta T_{lm}}

$$

$$

L = \frac{12786}{38.1 \times \pi \times 0.03 \times 32.2} = \frac{12786}{115.6} \approx 110.6 \text{ m}

$$

**Final Answer:** The required heat exchanger length is approximately **110.6 meters**.

**Practical Note:** This is quite long for a double-pipe exchanger. In practice, a more compact design (shell-and-tube or plate) would likely be preferred.
```

```{prf:example} Heat Exchanger Mass Flow Rate Calculation
:label: ex-hx-mass-flow

Lubricating oil is cooled by water in a counter-current concentric tube heat exchanger.

**Given:**
- Hot fluid (oil): $\dot{m}_{oil} = 0.1$ kg/s, $T_{oil,in} = 100°C$, $T_{oil,out} = 55°C$, $c_{p,oil} = 2131$ J/kg·°C
- Cold fluid (water): $T_{water,in} = 30°C$, $T_{water,out} = 40°C$, $c_{p,water} = 4178$ J/kg·°C

Determine the required mass flow rate of water.

**Solution:**

**Step 1: Set Up Energy Balance**

For an adiabatic heat exchanger:

$$

\dot{m}_{oil} c_{p,oil} (T_{oil,in} - T_{oil,out}) = \dot{m}_{water} c_{p,water} (T_{water,out} - T_{water,in})

$$

**Step 2: Solve for Unknown Mass Flow Rate**

$$

\dot{m}_{water} = \frac{\dot{m}_{oil} c_{p,oil} (T_{oil,in} - T_{oil,out})}{c_{p,water} (T_{water,out} - T_{water,in})}

$$

**Step 3: Substitute Values**

$$

\dot{m}_{water} = \frac{0.1 \times 2131 \times (100 - 55)}{4178 \times (40 - 30)}

$$

$$

\dot{m}_{water} = \frac{0.1 \times 2131 \times 45}{4178 \times 10} = \frac{9589.5}{41780} \approx 0.2295 \text{ kg/s}

$$

**Final Answer:** The required water flow rate is approximately **0.23 kg/s**.

**Step 4: Verification (Optional)**

Check energy balance:
- Heat lost by oil: $q = 0.1 \times 2131 \times 45 = 9589.5$ W
- Heat gained by water: $q = 0.2295 \times 4178 \times 10 = 9585$ W

The values match within rounding error, confirming our calculation.
```

### NTU-Effectiveness Method

The Effectiveness-NTU method is an alternative approach particularly useful when outlet temperatures are **unknown**. It's also valuable for parametric studies and performance analysis.

#### Key Parameters

```{prf:definition} Heat Capacity Rate
:label: def-heat-capacity-rate

The **heat capacity rate** $C$ is the rate at which a fluid stream can transport thermal energy:

$$

C = \dot{m} c_p \quad [W/K]

$$

We identify:
- $C_{min}$ = minimum of $C_h$ and $C_c$
- $C_{max}$ = maximum of $C_h$ and $C_c$
- $C_r = C_{min}/C_{max}$ = heat capacity ratio
```

```{prf:definition} Heat Exchanger Effectiveness
:label: def-effectiveness

The **effectiveness** $\epsilon$ is the ratio of actual heat transfer to the maximum possible heat transfer:

$$

\epsilon = \frac{q_{actual}}{q_{max}}

$$

where:

$$

q_{max} = C_{min}(T_{h,in} - T_{c,in})

$$

This maximum occurs in an infinitely long counter-flow exchanger where the fluid with $C_{min}$ experiences the full temperature difference.
```

```{prf:definition} Number of Transfer Units (NTU)
:label: def-ntu

The **Number of Transfer Units** is a dimensionless parameter characterizing the "thermal size" of a heat exchanger:

$$

NTU = \frac{UA}{C_{min}}

$$

Physical meaning: NTU represents the heat transfer capacity of the exchanger relative to the heat capacity rate of the limiting fluid.
```

#### Effectiveness Relationships

The effectiveness depends on NTU, $C_r$, and flow arrangement. Common relationships:

**Counter-flow heat exchanger:**

$$

\epsilon = \frac{1 - \exp[-NTU(1-C_r)]}{1 - C_r \exp[-NTU(1-C_r)]} \quad (C_r < 1)

$$

$$

\epsilon = \frac{NTU}{1 + NTU} \quad (C_r = 1)

$$

**Parallel-flow heat exchanger:**

$$

\epsilon = \frac{1 - \exp[-NTU(1+C_r)]}{1 + C_r}

$$

**Shell-and-tube** (one shell pass, even number of tube passes):

More complex; typically obtained from charts or specialized equations.

For design purposes, these relationships can be inverted to find NTU given $\epsilon$ and $C_r$:

**Counter-flow:**

$$

NTU = \frac{1}{C_r - 1} \ln\left(\frac{\epsilon - 1}{\epsilon C_r - 1}\right) \quad (C_r \neq 1)

$$

#### When to Use Each Method

**Use LMTD method when:**
- Inlet and outlet temperatures are known or easily calculated
- Designing a new heat exchanger (sizing for required duty)
- Straightforward calculations needed

**Use NTU-effectiveness method when:**
- Outlet temperatures are unknown
- Analyzing performance of existing heat exchanger
- Conducting parametric studies (effect of flow rate changes, etc.)
- Using rating rather than design approach

```{prf:example} NTU Method: Finding Overall Heat Transfer Coefficient
:label: ex-ntu-method

A thin-walled, counter-flow, concentric tube heat exchanger uses hot gases to heat pressurized water.

**Given:**
- Cold fluid (water): $\dot{m}_c = 1.0$ kg/s, $c_{p,c} = 4197$ J/kg·K, $T_{c,in} = 40°C$, $T_{c,out} = 140°C$
- Hot fluid (gas): $\dot{m}_h = 1.9$ kg/s, $c_{p,h} = 1000$ J/kg·K, $T_{h,in} = 350°C$, $T_{h,out} = 100°C$
- Heat transfer area: $A = 20$ m²

Determine the overall heat transfer coefficient $U$.

**Solution:**

**Step 1: Calculate Heat Capacity Rates**

Cold fluid:

$$

C_c = \dot{m}_c c_{p,c} = 1.0 \times 4197 = 4197 \text{ W/K}

$$

Hot fluid:

$$

C_h = \dot{m}_h c_{p,h} = 1.9 \times 1000 = 1900 \text{ W/K}

$$

Therefore:

$$

C_{min} = C_h = 1900 \text{ W/K}

$$

$$

C_{max} = C_c = 4197 \text{ W/K}

$$

$$

C_r = \frac{C_{min}}{C_{max}} = \frac{1900}{4197} = 0.453

$$

**Step 2: Calculate Effectiveness**

Actual heat transfer (using hot fluid):

$$

q = C_h(T_{h,in} - T_{h,out}) = 1900 \times (350 - 100) = 475000 \text{ W}

$$

Maximum possible heat transfer:

$$

q_{max} = C_{min}(T_{h,in} - T_{c,in}) = 1900 \times (350 - 40) = 589000 \text{ W}

$$

Effectiveness:

$$

\epsilon = \frac{q}{q_{max}} = \frac{475000}{589000} = 0.806

$$

**Alternative calculation** (since hot fluid has $C_{min}$):

$$

\epsilon = \frac{T_{h,in} - T_{h,out}}{T_{h,in} - T_{c,in}} = \frac{350 - 100}{350 - 40} = \frac{250}{310} = 0.806

$$

**Step 3: Calculate NTU from Effectiveness**

For counter-flow with $C_r \neq 1$:

$$

NTU = \frac{1}{C_r - 1} \ln\left(\frac{\epsilon - 1}{\epsilon C_r - 1}\right)

$$

$$

NTU = \frac{1}{0.453 - 1} \ln\left(\frac{0.806 - 1}{0.806 \times 0.453 - 1}\right)

$$

$$

NTU = \frac{1}{-0.547} \ln\left(\frac{-0.194}{-0.635}\right) = \frac{1}{-0.547} \ln(0.3055)

$$

$$

NTU = (-1.828) \times (-1.186) = 2.17

$$

**Step 4: Calculate Overall Heat Transfer Coefficient**

From the definition of NTU:

$$

U = \frac{NTU \cdot C_{min}}{A} = \frac{2.17 \times 1900}{20} = \frac{4123}{20} = 206.15 \text{ W/m}^2\cdot\text{K}

$$

**Final Answer:** The overall heat transfer coefficient is approximately **206 W/m²·K**.

**Analysis:** This value of $U$ is reasonable for gas-to-liquid heat transfer. The effectiveness of 0.806 (80.6%) indicates this is a well-designed heat exchanger operating efficiently.
```

---

## Psychrometrics and Phase Change

This section covers applications involving humid air and phase change processes, with emphasis on using the psychrometric chart and estimating thermodynamic properties.

### Psychrometric Chart Fundamentals

A psychrometric chart graphically represents the thermodynamic properties of moist air. It's an essential tool for analyzing air conditioning and humidification processes.

#### Key Properties on the Chart

**Primary variables:**
- **Dry-bulb temperature** ($T_{db}$): Actual air temperature, plotted on horizontal axis [°C or °F]
- **Absolute humidity** ($\omega$): Mass of water vapor per mass of dry air, plotted on vertical axis [kg H₂O/kg dry air]

**Derived properties (read from chart lines):**
- **Relative humidity** (RH): Curved lines showing constant RH [%]
- **Wet-bulb temperature** ($T_{wb}$): Diagonal lines sloping down-left [°C or °F]
- **Specific enthalpy**: Diagonal lines similar to wet-bulb lines [kJ/kg dry air]
- **Specific volume** ($v_h$): Steeper diagonal lines [m³/kg dry air]
- **Dew point temperature**: Follow horizontal (constant $\omega$) left to 100% RH curve

#### Using the Psychrometric Chart

```{admonition} General Procedure
:class: tip

1. **Locate the state point** using two independent properties (typically $T_{db}$ and one other)
2. **Read all other properties** at that point from the appropriate lines
3. **Follow process lines** to find final states:
   - Constant $\omega$: horizontal line (sensible heating/cooling)
   - Constant $T_{wb}$: diagonal line (adiabatic humidification)
   - Constant RH: curved line
```

### Adiabatic Humidification

In adiabatic humidification (evaporative cooling), water evaporates into an air stream with no external heat added. The energy for evaporation comes from the air itself, causing the air temperature to drop while its humidity increases.

**Key principle:** Adiabatic humidification follows a line of **constant wet-bulb temperature** on the psychrometric chart.

```{prf:example} Adiabatic Spray Chamber
:label: ex-psychrometric

Humid air at 40°C and 20% relative humidity enters an adiabatic spray chamber at 100 m³/hr. The air is humidified by evaporating liquid water and leaves at 50% RH. Determine the outlet temperature and the rate of water evaporation.

**Solution:**

**Step 1: Locate Inlet State (Point 1)**

On the psychrometric chart:
- Find intersection of $T_{db,1} = 40°C$ (vertical line) and RH = 20% (curved line)
- Mark this as Point 1

**Step 2: Follow Process Line**

From Point 1:
- Identify the constant wet-bulb temperature line passing through Point 1
- Follow this diagonal line up and to the left

**Step 3: Locate Outlet State (Point 2)**

The process stops where the constant $T_{wb}$ line intersects the RH = 50% curve. Mark as Point 2.

From Point 2, read outlet temperature by moving vertically down to the horizontal axis:

$$

T_{db,2} \approx 30°C

$$

**Step 4: Read Absolute Humidities**

Moving horizontally from each point to the vertical axis:
- At Point 1: $\omega_1 \approx 0.0092$ kg H₂O/kg dry air
- At Point 2: $\omega_2 \approx 0.0132$ kg H₂O/kg dry air

**Step 5: Read Specific Volume**

From the steeper diagonal lines at Point 1:

$$

v_{h,1} \approx 0.9 \text{ m}^3/\text{kg dry air}

$$

**Step 6: Calculate Mass Flow Rate of Dry Air**

$$

\dot{m}_{dry\,air} = \frac{\dot{V}_1}{v_{h,1}} = \frac{100 \text{ m}^3/\text{hr}}{0.9 \text{ m}^3/\text{kg dry air}} = 111.1 \text{ kg dry air/hr}

$$

**Step 7: Calculate Water Evaporation Rate**

$$

\dot{m}_{evap} = \dot{m}_{dry\,air} \times (\omega_2 - \omega_1)

$$

$$

\dot{m}_{evap} = 111.1 \times (0.0132 - 0.0092) = 111.1 \times 0.004 = 0.444 \text{ kg H}_2\text{O/hr}

$$

**Final Answers:**
- **Outlet temperature:** Approximately **30°C**
- **Water evaporation rate:** Approximately **0.44 kg/hr**

**Physical interpretation:** The air cooled from 40°C to 30°C while gaining moisture, demonstrating the evaporative cooling effect.
```

### Estimating Heat of Vaporization

The heat of vaporization (enthalpy of vaporization) is a critical property for phase change calculations. It can be estimated using the Clausius-Clapeyron equation combined with accurate vapor pressure data.

#### Clausius-Clapeyron Equation

The integrated form (assuming constant $\Delta H_v$ over a small temperature range):

$$

\ln(P_{sat}) = -\frac{\Delta H_v}{R} \left(\frac{1}{T}\right) + C

$$

This is a linear equation in the variables $\ln(P_{sat})$ vs. $1/T$, with slope $m = -\Delta H_v/R$.

where:
- $P_{sat}$ = saturation vapor pressure
- $\Delta H_v$ = molar heat of vaporization [J/mol]
- $R = 8.314$ J/mol·K (universal gas constant)
- $T$ = absolute temperature [K]

#### Antoine Equation

The Antoine equation is an accurate empirical correlation for vapor pressure:

$$

\log_{10}(P_{sat}) = A - \frac{B}{T + C}

$$

Constants $A$, $B$, and $C$ are substance-specific and tabulated in references.

#### Strategy for Estimating $\Delta H_v$

1. Use Antoine equation to generate accurate $P_{sat}$ data at two temperatures bracketing the temperature of interest
2. Convert to Clausius-Clapeyron variables: $\ln(P_{sat})$ vs. $1/T$
3. Calculate slope from the two points
4. Determine $\Delta H_v$ from the slope

```{prf:example} Heat of Vaporization of Benzene
:label: ex-heat-vaporization

Estimate the heat of vaporization of benzene at 60°C using:

Antoine equation for benzene:

$$

\log_{10}(P_{sat}) = 6.906 - \frac{1211}{T + 220.8}

$$

where $T$ is in °C and $P_{sat}$ is in Torr.

**Solution:**

**Step 1: Generate Vapor Pressure Data**

Choose $T_1 = 55°C$ and $T_2 = 65°C$ (bracketing 60°C).

At $T_1 = 55°C$:

$$

\log_{10}(P_{sat,1}) = 6.906 - \frac{1211}{55 + 220.8} = 6.906 - 4.391 = 2.515

$$

$$

P_{sat,1} = 10^{2.515} = 327.3 \text{ Torr}

$$

At $T_2 = 65°C$:

$$

\log_{10}(P_{sat,2}) = 6.906 - \frac{1211}{65 + 220.8} = 6.906 - 4.237 = 2.669

$$

$$

P_{sat,2} = 10^{2.669} = 466.7 \text{ Torr}

$$

**Step 2: Convert to Clausius-Clapeyron Variables**

Convert temperatures to Kelvin and take natural logarithm of pressures:

Point 1:
- $T_1 = 55 + 273.15 = 328.15$ K → $1/T_1 = 0.003047$ K⁻¹
- $\ln(P_{sat,1}) = \ln(327.3) = 5.791$

Point 2:
- $T_2 = 65 + 273.15 = 338.15$ K → $1/T_2 = 0.002957$ K⁻¹
- $\ln(P_{sat,2}) = \ln(466.7) = 6.146$

**Step 3: Calculate Slope**

$$

m = \frac{\Delta(\ln P_{sat})}{\Delta(1/T)} = \frac{6.146 - 5.791}{0.002957 - 0.003047}

$$

$$

m = \frac{0.355}{-0.00009} = -3944 \text{ K}

$$

**Step 4: Calculate Heat of Vaporization**

From $m = -\Delta H_v/R$:

$$

\Delta H_v = -m \times R = -(-3944) \times 8.314 = 32785 \text{ J/mol}

$$

**Final Answer:** The heat of vaporization of benzene at 60°C is approximately **32.8 kJ/mol**.

**Note:** Literature values for benzene at 60°C are around 32.5-33.0 kJ/mol, confirming our estimate is accurate.
```

---

## Summary and Key Takeaways

This comprehensive guide has covered the fundamental principles of heat transfer across all three modes: conduction, convection, and radiation, along with applications to heat exchangers and psychrometric processes.

### Core Principles

**Conduction:**
- Governed by Fourier's Law: $q = -kA\frac{dT}{dx}$
- Linear temperature profile for steady-state, one-dimensional, no generation
- Thermal resistance concept enables circuit analogy: $R = L/(kA)$
- Composite walls: resistances add in series

**Convection:**
- Governed by Newton's Law of Cooling: $q = hA(T_s - T_{\infty})$
- Heat transfer coefficient $h$ depends on flow conditions, geometry, and fluid properties
- Dimensionless groups (Re, Pr, Nu) characterize convection
- Boundary layer concepts explain convection mechanisms

**Radiation:**
- Stefan-Boltzmann Law: $E = \epsilon\sigma T^4$ (temperature must be in Kelvin!)
- View factors characterize geometric radiation exchange
- Resistance network method solves complex radiation problems
- Surface properties ($\epsilon$, $\alpha$, $\rho$) determine radiative behavior

**Heat Exchangers:**
- LMTD method: $q = UA\Delta T_{lm}$ (known temperatures)
- NTU-effectiveness method: $\epsilon = q/q_{max}$ (unknown temperatures)
- Counter-flow is more efficient than parallel flow
- Energy balance: heat lost by hot fluid = heat gained by cold fluid

### Problem-Solving Strategy

```{admonition} General Approach to Heat Transfer Problems
:class: tip

1. **Draw a clear diagram** showing system geometry, boundaries, and heat flow direction
2. **Identify the heat transfer mode(s)** involved
3. **List known and unknown quantities** with units
4. **State assumptions** (steady-state, one-dimensional, constant properties, etc.)
5. **Write governing equations** (Fourier, Newton, Stefan-Boltzmann, energy balance)
6. **Select appropriate correlations** (for convection) or formulas
7. **Solve systematically**, checking units at each step
8. **Verify reasonableness** of results (positive temperatures, heat flows in correct direction, etc.)
```

### Common Pitfalls to Avoid

**Unit errors:**
- Temperature in Kelvin for radiation calculations
- Consistent units throughout (SI or English)
- Pay attention to mass flow vs. volumetric flow

**Conceptual errors:**
- Forgetting surface vs. film temperature for property evaluation
- Using local vs. average heat transfer coefficients incorrectly
- Incorrect view factor relationships

**Calculation errors:**
- Sign errors in heat transfer direction
- Forgetting to convert between heat transfer rate and heat flux
- Arithmetic mistakes in LMTD calculation

### Advanced Topics and Extensions

This guide provides a foundation for more advanced heat transfer topics including:
- Transient (unsteady) conduction
- Multi-dimensional heat transfer
- Heat transfer with phase change (boiling, condensation)
- Convection in complex geometries
- Radiation in participating media
- Compact heat exchangers and advanced designs
- Numerical methods for heat transfer

### Further Study

For deeper understanding and additional applications, consult:

**Textbooks:**
- Incropera, DeWitt, Bergman & Lavine: *Fundamentals of Heat and Mass Transfer*
- Çengel & Ghajar: *Heat and Mass Transfer: Fundamentals and Applications*
- Holman: *Heat Transfer*

**Handbooks:**
- Perry's Chemical Engineers' Handbook
- ASHRAE Handbook - Fundamentals
- Heat Exchanger Design Handbook (Hewitt)

**Standards:**
- TEMA (Tubular Exchanger Manufacturers Association) Standards
- ASME Boiler and Pressure Vessel Code

### Practice Problems

Regular practice is essential for mastery. Work through problems involving:
1. Conduction through composite walls with convection boundaries
2. Convection coefficient calculations for various geometries
3. Radiation exchange in enclosures
4. Heat exchanger sizing and rating
5. Combined mode heat transfer problems

Focus on understanding the physics and methodology rather than memorizing formulas. With solid fundamentals and systematic problem-solving approaches, you can tackle any heat transfer challenge.

---

## Nomenclature

**Roman Symbols:**
- $A$ = area [m²]
- $c_p$ = specific heat at constant pressure [J/kg·K]
- $C$ = heat capacity rate [W/K]
- $D$ = diameter [m]
- $E$ = emissive power [W/m²]
- $F_{ij}$ = view factor from surface $i$ to surface $j$ [-]
- $G$ = irradiation [W/m²]
- $h$ = heat transfer coefficient [W/m²·K]
- $J$ = radiosity [W/m²]
- $k$ = thermal conductivity [W/m·K]
- $L$ = length or thickness [m]
- $\dot{m}$ = mass flow rate [kg/s]
- $Nu$ = Nusselt number [-]
- $NTU$ = number of transfer units [-]
- $P$ = pressure [Pa]
- $Pr$ = Prandtl number [-]
- $q$ = heat transfer rate [W]
- $q''$ = heat flux [W/m²]
- $\dot{q}$ = volumetric heat generation rate [W/m³]
- $R$ = thermal resistance [K/W] or gas constant [J/mol·K]
- $R''$ = thermal resistance per unit area [m²·K/W]
- $Re$ = Reynolds number [-]
- $T$ = temperature [K or °C]
- $U$ = overall heat transfer coefficient [W/m²·K]
- $u$ = velocity [m/s]
- $V$ = volume [m³]

**Greek Symbols:**
- $\alpha$ = thermal diffusivity [m²/s] or absorptivity [-]
- $\beta$ = coefficient of volumetric expansion [1/K]
- $\delta$ = boundary layer thickness [m]
- $\Delta T$ = temperature difference [K or °C]
- $\epsilon$ = emissivity [-] or heat exchanger effectiveness [-]
- $\mu$ = dynamic viscosity [kg/m·s or Pa·s]
- $\nu$ = kinematic viscosity [m²/s]
- $\rho$ = density [kg/m³] or reflectivity [-]
- $\sigma$ = Stefan-Boltzmann constant, $5.67 \times 10^{-8}$ W/m²·K⁴
- $\tau$ = transmissivity [-]
- $\omega$ = absolute humidity [kg H₂O/kg dry air]

**Subscripts:**
- $b$ = blackbody
- $c$ = cold fluid or convection
- $f$ = fluid or film
- $h$ = hot fluid
- $i, j$ = surface indices
- $in$ = inlet
- $lm$ = log mean
- $max$ = maximum
- $min$ = minimum
- $out$ = outlet
- $s$ = surface
- $t$ = thermal
- $x$ = local value at position $x$
- $\infty$ = free stream

**Superscripts:**
- $''$ = per unit area

---

## Appendix A: Additional Worked Examples

This appendix provides additional comprehensive examples demonstrating the application of heat transfer principles to practical engineering problems.

### Example A.1: Conduction Through Cylindrical Pipe

```{prf:example} Insulated Steam Pipe
:label: ex-cylindrical-pipe

Steam at 200°C flows through a steel pipe with inner diameter $D_i = 0.10$ m and outer diameter $D_o = 0.12$ m. The pipe is insulated with a 0.05 m thick layer of insulation. The convection coefficient inside the pipe is $h_i = 500$ W/m²·K, and outside the insulation is $h_o = 10$ W/m²·K. The ambient air temperature is 25°C.

Properties:
- Steel: $k_{steel} = 50$ W/m·K
- Insulation: $k_{ins} = 0.04$ W/m·K

Find: (a) Heat loss per unit length of pipe, (b) Temperature at the pipe outer surface

**Solution:**

For cylindrical coordinates, thermal resistances are:

$$

R_{conv,i} = \frac{1}{h_i A_i} = \frac{1}{2\pi r_i L h_i}

$$

$$

R_{cond,cyl} = \frac{\ln(r_o/r_i)}{2\pi k L}

$$

**Per unit length** ($L = 1$ m):

Inner radius: $r_1 = 0.05$ m

Outer radius of steel: $r_2 = 0.06$ m

Outer radius of insulation: $r_3 = 0.06 + 0.05 = 0.11$ m

$$

R'_{conv,i} = \frac{1}{2\pi(0.05)(500)} = 6.37 \times 10^{-3} \text{ K·m/W}

$$

$$

R'_{cond,steel} = \frac{\ln(0.06/0.05)}{2\pi(50)} = 5.82 \times 10^{-4} \text{ K·m/W}

$$

$$

R'_{cond,ins} = \frac{\ln(0.11/0.06)}{2\pi(0.04)} = 2.43 \text{ K·m/W}

$$

$$

R'_{conv,o} = \frac{1}{2\pi(0.11)(10)} = 0.145 \text{ K·m/W}

$$

Total resistance per unit length:

$$

R'_{total} = 6.37 \times 10^{-3} + 5.82 \times 10^{-4} + 2.43 + 0.145 = 2.58 \text{ K·m/W}

$$

**Part (a): Heat loss per unit length**

$$

q' = \frac{T_{steam} - T_{amb}}{R'_{total}} = \frac{200 - 25}{2.58} = 67.8 \text{ W/m}

$$

**Part (b): Pipe outer surface temperature**

The temperature drop across the steel pipe:

$$

\Delta T_{steel} = q' \times R'_{cond,steel} = 67.8 \times 5.82 \times 10^{-4} = 0.039 \text{ K}

$$

The temperature drop from steam to inner surface:

$$

\Delta T_{conv,i} = q' \times R'_{conv,i} = 67.8 \times 6.37 \times 10^{-3} = 0.43 \text{ K}

$$

Pipe outer surface temperature:

$$

T_{pipe,outer} = 200 - 0.43 - 0.039 = 199.5°\text{C}

$$

**Answers:**
- Heat loss: **67.8 W/m**
- Pipe outer surface temperature: **199.5°C**

**Analysis:** The insulation is highly effective. The insulation resistance (2.43 K·m/W) represents 94% of the total thermal resistance, demonstrating why insulation is critical for hot pipe applications.
```

### Example A.2: Natural Convection from Heated Plate

```{prf:example} Vertical Heated Plate
:label: ex-natural-convection

A vertical plate measuring 0.5 m high by 0.3 m wide is maintained at a uniform temperature of 80°C in air at 20°C. Estimate the heat transfer rate by natural convection.

Air properties at film temperature $T_f = (80 + 20)/2 = 50°C = 323$ K:
- $k = 0.028$ W/m·K
- $\nu = 1.8 \times 10^{-5}$ m²/s  
- $Pr = 0.71$
- $\beta = 1/T_f = 1/323 = 0.0031$ K⁻¹

**Solution:**

**Step 1: Calculate Rayleigh Number**

The characteristic length for a vertical plate is its height: $L = 0.5$ m

$$

Ra_L = \frac{g\beta(T_s - T_{\infty})L^3}{\nu^2} Pr

$$

$$

Ra_L = \frac{9.81 \times 0.0031 \times (80-20) \times (0.5)^3}{(1.8 \times 10^{-5})^2} \times 0.71

$$

$$

Ra_L = \frac{9.81 \times 0.0031 \times 60 \times 0.125}{3.24 \times 10^{-10}} \times 0.71 = 5.08 \times 10^8

$$

**Step 2: Select Correlation**

Since $10^4 < Ra_L < 10^9$, use laminar natural convection correlation:

$$

\overline{Nu}_L = 0.59 Ra_L^{1/4}

$$

$$

\overline{Nu}_L = 0.59 \times (5.08 \times 10^8)^{0.25} = 0.59 \times 150.3 = 88.7

$$

**Step 3: Calculate Heat Transfer Coefficient**

$$

\bar{h} = \frac{\overline{Nu}_L \times k}{L} = \frac{88.7 \times 0.028}{0.5} = 4.97 \text{ W/m}^2\cdot\text{K}

$$

**Step 4: Calculate Heat Transfer Rate**

Surface area: $A = 0.5 \times 0.3 = 0.15$ m²

$$

q = \bar{h} A (T_s - T_{\infty}) = 4.97 \times 0.15 \times (80 - 20) = 44.7 \text{ W}

$$

**Final Answer:** The natural convection heat transfer rate is approximately **45 W**.

**Note:** Natural convection coefficients (typically 2-25 W/m²·K for gases) are much lower than forced convection coefficients (typically 25-250 W/m²·K for gases), explaining why fans significantly improve cooling.
```

### Example A.3: Radiation Exchange in an Enclosure

```{prf:example} Two-Surface Radiation Exchange
:label: ex-radiation-enclosure

Two large parallel plates are separated by a small distance. Plate 1 has $T_1 = 600$ K, $\epsilon_1 = 0.7$, and area $A_1 = 2$ m². Plate 2 has $T_2 = 400$ K and $\epsilon_2 = 0.5$. Calculate the net radiation heat transfer from Plate 1 to Plate 2.

**Solution:**

For large parallel plates, $F_{12} = 1$ (all radiation from one plate hits the other).

**Method 1: Direct Formula**

For two large parallel plates with $A_1 = A_2 = A$:

$$

q_{12} = \frac{\sigma A (T_1^4 - T_2^4)}{\frac{1}{\epsilon_1} + \frac{1}{\epsilon_2} - 1}

$$

$$

q_{12} = \frac{5.67 \times 10^{-8} \times 2 \times (600^4 - 400^4)}{\frac{1}{0.7} + \frac{1}{0.5} - 1}

$$

$$

q_{12} = \frac{5.67 \times 10^{-8} \times 2 \times (129.6 \times 10^9 - 25.6 \times 10^9)}{1.429 + 2.0 - 1}

$$

$$

q_{12} = \frac{1.134 \times 10^{-7} \times 104 \times 10^9}{2.429} = \frac{11794}{2.429} = 4856 \text{ W}

$$

**Method 2: Resistance Network**

Surface resistance for Plate 1:

$$

R_{surf,1} = \frac{1-\epsilon_1}{\epsilon_1 A_1} = \frac{1-0.7}{0.7 \times 2} = \frac{0.3}{1.4} = 0.214 \text{ K/W}

$$

Surface resistance for Plate 2:

$$

R_{surf,2} = \frac{1-\epsilon_2}{\epsilon_2 A_2} = \frac{1-0.5}{0.5 \times 2} = \frac{0.5}{1.0} = 0.5 \text{ K/W}

$$

Space resistance:

$$

R_{space} = \frac{1}{A_1 F_{12}} = \frac{1}{2 \times 1} = 0.5 \text{ K/W}

$$

Total resistance:

$$

R_{total} = 0.214 + 0.5 + 0.5 = 1.214 \text{ K/W}

$$

Blackbody emissive powers:

$$

E_{b1} = \sigma T_1^4 = 5.67 \times 10^{-8} \times 600^4 = 7348 \text{ W/m}^2

$$

$$

E_{b2} = \sigma T_2^4 = 5.67 \times 10^{-8} \times 400^4 = 1452 \text{ W/m}^2

$$

Heat transfer:

$$

q = \frac{A(E_{b1} - E_{b2})}{R_{total} \times A} = \frac{E_{b1} - E_{b2}}{R_{total}/A} = \frac{A(E_{b1} - E_{b2})}{R_{total}}

$$

Wait, let me recalculate using the driving potential correctly:

$$

q = \frac{E_{b1} \cdot A_1 - E_{b2} \cdot A_2}{R_{total}}

$$

Actually, with the resistance network, the driving force is:

$$

q = \frac{A_1 E_{b1} - A_2 E_{b2}}{(1-\epsilon_1)/\epsilon_1 + 1/F_{12} + (1-\epsilon_2)/\epsilon_2}

$$

This gives the same result as Method 1: **4856 W**

**Analysis:** The net radiation heat transfer from the hot plate to the cold plate is 4.86 kW. This is significant compared to convection in many applications, especially at elevated temperatures where radiation scales as $T^4$.
```

### Example A.4: Combined Modes Heat Transfer

```{prf:example} Fin with Convection and Radiation
:label: ex-combined-modes

A thin aluminum fin (thickness 2 mm, height 50 mm) extends from a wall at 100°C into air at 20°C. The fin has emissivity $\epsilon = 0.9$. Estimate the heat transfer from the fin considering both convection and radiation.

Assume:
- Convection coefficient: $h = 15$ W/m²·K
- Fin width (into page): 1 m
- Fin tip is adiabatic

**Solution:**

**Step 1: Calculate Surface Area**

For a rectangular fin, considering both sides:

$$

A_s = 2 \times \text{height} \times \text{width} = 2 \times 0.05 \times 1 = 0.1 \text{ m}^2

$$

**Step 2: Convective Heat Transfer**

For a simple estimate (treating fin as isothermal at average temperature):

$$

q_{conv} = h A_s (T_{base} - T_{\infty})

$$

$$

q_{conv} = 15 \times 0.1 \times (100 - 20) = 120 \text{ W}

$$

**Step 3: Radiative Heat Transfer**

Assuming surroundings are at air temperature (293 K):

$$

q_{rad} = \epsilon \sigma A_s (T_{s}^4 - T_{surr}^4)

$$

Using average fin temperature (approximately 80°C = 353 K as estimate):

$$

q_{rad} = 0.9 \times 5.67 \times 10^{-8} \times 0.1 \times (353^4 - 293^4)

$$

$$

q_{rad} = 0.9 \times 5.67 \times 10^{-8} \times 0.1 \times (1.554 \times 10^{10} - 0.737 \times 10^{10})

$$

$$

q_{rad} = 5.1 \times 10^{-9} \times 8.17 \times 10^9 = 41.7 \text{ W}

$$

**Step 4: Total Heat Transfer**

$$

q_{total} = q_{conv} + q_{rad} = 120 + 41.7 = 161.7 \text{ W}

$$

**Final Answer:** Total heat transfer is approximately **162 W**, with convection contributing 74% and radiation 26%.

**Analysis:** At these moderate temperatures, radiation is significant but not dominant. At higher temperatures, radiation becomes increasingly important (scales as $T^4$). This demonstrates why combined mode analysis is important for accurate thermal predictions.
```

---

## Appendix B: Useful Correlations and Data

### Standard Convection Correlations Summary

#### External Flow Over Flat Plate

**Laminar** ($Re_x < 5 \times 10^5$):

Local:

$$

Nu_x = 0.332 Re_x^{1/2} Pr^{1/3}

$$

Average:

$$

\overline{Nu}_L = 0.664 Re_L^{1/2} Pr^{1/3}

$$

**Turbulent** ($5 \times 10^5 < Re_x < 10^8$):

Local:

$$

Nu_x = 0.0296 Re_x^{4/5} Pr^{1/3}

$$

Average (mixed):

$$

\overline{Nu}_L = (0.037 Re_L^{4/5} - 871) Pr^{1/3}

$$

#### Flow Over Cylinder

**Average Nusselt number** (Churchill-Bernstein):

$$

\overline{Nu}_D = 0.3 + \frac{0.62 Re_D^{1/2} Pr^{1/3}}{[1+(0.4/Pr)^{2/3}]^{1/4}} \left[1 + \left(\frac{Re_D}{282000}\right)^{5/8}\right]^{4/5}

$$

Valid for $Re_D Pr > 0.2$.

#### Internal Flow in Pipes

**Fully developed laminar flow**:
- Constant surface temperature: $Nu_D = 3.66$
- Constant heat flux: $Nu_D = 4.36$

**Turbulent flow** (Gnielinski equation, $3000 < Re_D < 5 \times 10^6$, $0.5 < Pr < 2000$):

$$

Nu_D = \frac{(f/8)(Re_D - 1000)Pr}{1 + 12.7(f/8)^{1/2}(Pr^{2/3} - 1)}

$$

where $f = (0.790 \ln Re_D - 1.64)^{-2}$ is the friction factor.

#### Natural Convection

**Vertical plate or cylinder** ($10^4 < Ra_L < 10^9$):

$$

\overline{Nu}_L = 0.59 Ra_L^{1/4}

$$

**Vertical plate or cylinder** ($10^9 < Ra_L < 10^{13}$):

$$

\overline{Nu}_L = 0.10 Ra_L^{1/3}

$$

**Horizontal cylinder**:

$$

\overline{Nu}_D = \left\{0.60 + \frac{0.387 Ra_D^{1/6}}{[1+(0.559/Pr)^{9/16}]^{8/27}}\right\}^2

$$

Valid for $Ra_D < 10^{12}$.

### Typical Property Values at 300 K

#### Gases at Atmospheric Pressure

| Fluid | $k$ [W/m·K] | $c_p$ [J/kg·K] | $\mu \times 10^5$ [Pa·s] | $Pr$ [-] |
|-------|------------|---------------|------------------------|---------|
| Air | 0.026 | 1007 | 1.85 | 0.71 |
| CO₂ | 0.017 | 871 | 1.50 | 0.77 |
| H₂O (vapor) | 0.019 | 2014 | 0.97 | 1.00 |

#### Liquids

| Fluid | $k$ [W/m·K] | $c_p$ [J/kg·K] | $\mu \times 10^3$ [Pa·s] | $Pr$ [-] |
|-------|------------|---------------|------------------------|---------|
| Water | 0.613 | 4179 | 0.855 | 5.83 |
| Engine oil | 0.145 | 1909 | 490 | 6400 |
| Mercury | 8.54 | 140 | 1.53 | 0.025 |
| Ethanol | 0.169 | 2470 | 1.08 | 15.8 |

#### Solids

| Material | $k$ [W/m·K] | $\rho$ [kg/m³] | $c_p$ [J/kg·K] |
|----------|------------|---------------|---------------|
| Copper | 401 | 8933 | 385 |
| Aluminum | 237 | 2702 | 903 |
| Steel (1% C) | 43 | 7854 | 434 |
| Glass | 1.4 | 2500 | 750 |
| Concrete | 1.4 | 2300 | 880 |
| Wood (oak) | 0.17 | 750 | 2390 |
| Insulation (fiberglass) | 0.038 | 12 | 835 |

### Critical Dimensionless Numbers

#### Reynolds Number

$$

Re = \frac{\rho u L}{\mu} = \frac{u L}{\nu}

$$

**Critical values:**
- Pipe flow: $Re_{crit} \approx 2300$
- Flat plate: $Re_{x,crit} \approx 5 \times 10^5$

#### Nusselt Number

$$

Nu = \frac{h L}{k}

$$

Represents ratio of convective to conductive heat transfer.

#### Prandtl Number

$$

Pr = \frac{\mu c_p}{k} = \frac{\nu}{\alpha}

$$

Represents ratio of momentum to thermal diffusivity.

**Typical ranges:**
- Liquid metals: $Pr \sim 0.01$
- Gases: $Pr \sim 0.7$
- Water: $Pr \sim 7$
- Oils: $Pr \sim 100-1000$

#### Grashof Number

$$

Gr = \frac{g \beta (T_s - T_{\infty}) L^3}{\nu^2}

$$

Represents ratio of buoyancy to viscous forces in natural convection.

#### Rayleigh Number

$$

Ra = Gr \cdot Pr = \frac{g \beta (T_s - T_{\infty}) L^3}{\nu \alpha}

$$

Combined parameter for natural convection.


## PE Exam Practice Problems

```{prf:example} Practice Problem 1 — Composite Wall with Convection

A furnace wall consists of three layers in series:
- Refractory brick: $k_1 = 1.2$ W/m·K, $L_1 = 0.20$ m
- Insulating firebrick: $k_2 = 0.15$ W/m·K, $L_2 = 0.10$ m
- Steel shell: $k_3 = 50$ W/m·K, $L_3 = 0.01$ m

The inner surface is exposed to flue gas at $T_{hot} = 900°C$ with convection coefficient $h_i = 30$ W/m²·K. The outer steel surface is cooled by air at $T_{cold} = 25°C$ with $h_o = 10$ W/m²·K.

**(a)** What is the total thermal resistance per unit area (m²·K/W)?

**(b)** What is the steady-state heat flux (W/m²)?
```

```{dropdown} Solution

**Step 1: Individual thermal resistances per unit area** $R'' = L/k$ or $1/h$

$$R''_{conv,i} = 1/h_i = 1/30 = 0.0333 \text{ m}^2\text{·K/W}$$
$$R''_1 = L_1/k_1 = 0.20/1.2 = 0.1667 \text{ m}^2\text{·K/W}$$
$$R''_2 = L_2/k_2 = 0.10/0.15 = 0.6667 \text{ m}^2\text{·K/W}$$
$$R''_3 = L_3/k_3 = 0.01/50 = 0.0002 \text{ m}^2\text{·K/W}$$
$$R''_{conv,o} = 1/h_o = 1/10 = 0.1000 \text{ m}^2\text{·K/W}$$

**Step 2: Total resistance (series)**

$$R''_{total} = 0.0333 + 0.1667 + 0.6667 + 0.0002 + 0.1000 = \mathbf{0.967 \text{ m}^2\text{·K/W}}$$

**Step 3: Heat flux**

$$q'' = \frac{\Delta T}{R''_{total}} = \frac{900 - 25}{0.967} = \mathbf{905 \text{ W/m}^2}$$

**Key observation:** The insulating firebrick ($R'' = 0.667$) dominates — it accounts for 69% of the total resistance. The steel shell is negligible (0.02%). This is typical: metals conduct very well and rarely limit heat transfer in industrial walls.
```

---

```{prf:example} Practice Problem 2 — Shell-and-Tube Heat Exchanger (LMTD)

A counterflow shell-and-tube heat exchanger heats 2.0 kg/s of water from 20°C to 70°C using hot oil ($C_p = 2.0$ kJ/kg·K) entering at 120°C. The overall heat transfer coefficient is $U = 350$ W/m²·K.

**(a)** What is the required heat duty (kW)?

**(b)** If the oil exits at 80°C, what heat exchange area is required?
```

```{dropdown} Solution

**Part (a): Heat duty**

$$\dot{Q} = \dot{m}_{water} C_{p,water} \Delta T_{water} = 2.0 \times 4.184 \times (70-20) = \mathbf{418.4 \text{ kW}}$$

**Part (b): LMTD and area**

Counterflow configuration: hot oil 120°C → 80°C; cold water 70°C ← 20°C

$$\Delta T_1 = T_{h,in} - T_{c,out} = 120 - 70 = 50°\text{C}$$
$$\Delta T_2 = T_{h,out} - T_{c,in} = 80 - 20 = 60°\text{C}$$

$$\Delta T_{lm} = \frac{\Delta T_1 - \Delta T_2}{\ln(\Delta T_1/\Delta T_2)} = \frac{50 - 60}{\ln(50/60)} = \frac{-10}{\ln(0.833)} = \frac{-10}{-0.1823} = \mathbf{54.9°\text{C}}$$

$$A = \frac{\dot{Q}}{U\,\Delta T_{lm}} = \frac{418{,}400}{350 \times 54.9} = \frac{418{,}400}{19{,}215} = \mathbf{21.8 \text{ m}^2}$$
```

```{caution}
**PE Exam Traps — Heat Transfer**

- **LMTD $\Delta T$ assignment in counterflow vs. parallel flow:** In counterflow, $\Delta T_1$ is hot-in minus cold-OUT and $\Delta T_2$ is hot-out minus cold-IN. Swapping these (using the parallel-flow convention) gives a wrong (smaller) LMTD and an overestimated area. Draw the temperature profiles first.
- **Radiation requires absolute temperature (K⁴).** Stefan-Boltzmann is $q = \varepsilon\sigma A(T_s^4 - T_{surr}^4)$, where $T$ is in Kelvin. Using Celsius gives an answer off by orders of magnitude. 273 K vs. 0°C barely matters for $\Delta T$ in conduction/convection — but $T^4$ makes it critical for radiation.
- **Thermal resistance is additive only in series.** Parallel resistances add as $1/R_{total} = 1/R_1 + 1/R_2$. A composite wall with different paths (fin + bare wall) is a parallel network, not series. Treating parallel paths as series dramatically overestimates resistance.
- **Dittus-Boelter exponent:** $n = 0.4$ when the fluid is being **heated** (fluid is cooler than the wall); $n = 0.3$ when the fluid is being **cooled**. This affects Nu by ~10-15% and is frequently tested.
- **NTU method required for unknown exit temperatures:** If both outlet temperatures are unknown (e.g., "find exit temperatures given UA and inlet conditions"), use NTU-effectiveness, not LMTD. LMTD requires knowing all four temperatures.
```

**End of Document**

*This comprehensive guide provides the fundamental knowledge needed for analyzing and designing heat transfer systems. Regular practice with diverse problems will build proficiency in applying these principles to real engineering challenges.*
