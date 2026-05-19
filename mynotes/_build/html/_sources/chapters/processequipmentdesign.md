---
title: "Process Equipment Design"
author: "PE Study Guide"
date: "2025"
---

# Process Equipment Design

## Heat-Exchanger Symbols and Utility Streams on a PFD
A PFD assigns each heat exchanger the tag `E-NXX` (E for exchanger, leading digit = plant area). Each exchanger has two sides: a **utility stream** (steam, cooling water, refrigerant, etc.) drawn with one line convention, and a **process stream** (the material being reacted, separated, or sold) drawn with another. The utility's job is to drive the process stream to its target temperature with minimum capital and operating cost.

### Reading the Two Lines on a Heat-Exchanger Symbol

```{note}
**Stream Convention on the Symbol**
Most textbooks draw two lines through the heat-exchanger circle:


- The *black, zig-zagging* line represents the **utility stream** (passes back and forth through the tubes or shell).

- The *grey, straight-through* line represents the **process stream**.

An *upward-pointing* utility arrow at the inlet indicates a stream whose temperature increases through the exchanger (e.g. cooling water leaving warmer than it entered — it absorbed process-side heat). A *downward-pointing* arrow indicates a utility that cools as it gives up heat (e.g. condensing steam).

Important: “utility” does not automatically mean “tube side.” The tube/shell assignment is a separate engineering decision based on chemical compatibility, pressure rating, and fouling potential (covered in a later section).
```


### Standard Utility Stream Codes

```{tip}
**Lowercase Utility Codes Used on PFDs**
On a PFD, only the utility *inlet* stream is labeled with its lowercase code; the outlet is implicit (the same utility, warmer or cooler).


- **cw** — cooling water from a cooling tower; inlet $\sim$30$^\circ$C, outlet $\sim$40–45$^\circ$C typical.

- **rw** — refrigerated water; inlet $\sim$5–10$^\circ$C.

- **rb** — refrigerated brine (CaCl$_2$ or MEG solution); inlet $\sim$-45$^\circ$C.

- **lps** — low-pressure saturated steam, $\sim$4 barg, $T_sat \approx 140$–160$^\circ$C.

- **mps** — medium-pressure steam, $\sim$10 barg, $T_sat \approx 180$–200$^\circ$C.

- **hps** — high-pressure steam, $\sim$40 barg, $T_sat \approx 250$–270$^\circ$C.

- **el** — electric resistance heating (220/440/660 V).

- **htm** — heat-transfer medium (Dowtherm A, Therminol 66); can reach 350–400$^\circ$C without high pressure.

Cooling tower water is limited at the cold end by the local wet-bulb temperature: a tower can cool water to roughly $T_{wet bulb} + 3^\circ$C in practice. In hot, humid climates this places a floor on what process-stream temperatures cooling water can achieve.
```


### Utility-Sizing Rule of Thumb (5–20$^\circ$C Rule)

```{note}
**Why Utility $\Delta T$ Should Be Modest**
Design the utility flow rate so the utility temperature change $\Delta T_{util}$ falls between roughly 5 and 20$^\circ$C. Both ends of the range are bounded for economic reasons:


- $\Delta T_{util} < 5^\circ$C requires a very large utility mass flow to carry the duty. The cooling-tower or steam-boiler equipment must be oversized to handle this flow, and pumping/blower costs rise.

- $\Delta T_{util} > 20^\circ$C means the utility supply equipment is being asked to deliver a large enthalpy swing per unit mass. For cooling water this is rarely a problem (the cooling tower can handle a 20$^\circ$C swing), but for steam, the upstream pressure-let-down station becomes constrained, and for refrigerants, more refrigeration compression power is needed.

For *condensing* steam or *evaporating* refrigerant, the temperature is fixed by saturation; only the flow rate varies. In those cases the rule of thumb is replaced by a target outlet vapor-fraction (condensate is typically returned as subcooled liquid; refrigerant is vaporized to dry saturation or slightly superheated).
```


### Worked Example: Sizing the Cooling-Water Flow

```{prf:example} Cooling-Water Flow for a Process Cooler
A process stream delivers 250 kW of cooling duty to a heat exchanger. Cooling water enters at 30$^\circ$C. (a) What is the required cooling-water mass flow if the design $\Delta T_{util} = 10^\circ$C? (b) What is the flow if $\Delta T_{util}$ is reduced to 3$^\circ$C? (c) Comment on the comparison.
```


```{dropdown} Solution Steps
- **Heat-capacity flow equation.** For a sensible-heat (no phase change) utility,

$$
Q = m_{cw}c_{p,water}\Delta T_{util}
$$

    Using $c_{p,water} = 4.18$ kJ/(kg$\cdot$K).

- **(a) At $\Delta T_{util** = 10^\circ$C:}

$$
m_{cw} = \frac{250}{4.18 \times 10} = \frac{250}{41.8} = 5.98  kg/s = 21{,}500  kg/h
$$

- **(b) At $\Delta T_{util** = 3^\circ$C:}

$$
m_{cw} = \frac{250}{4.18 \times 3} = \frac{250}{12.54} = 19.9  kg/s = 71{,}700  kg/h
$$

- **(c) Comparison.** Reducing $\Delta T_{util}$ from 10 to 3$^\circ$C tripled the required cooling-water flow. The cooling tower, the supply pump, and all piping must be sized 3.3$\times$ larger. The capital and operating cost penalty is significant for what is essentially the same heat duty. This is exactly why the 5–20$^\circ$C rule of thumb exists: it sits in the cost-minimum band where neither the heat-exchanger area (which favors low $\Delta T_util$) nor the utility equipment (which favors moderate-to-large $\Delta T_util$) dominates.

- **Verification.** The two flows differ by a factor of 3.33, which matches the inverse $\Delta T$ ratio 10/3 = 3.33. \checkmark
```


### Generic vs. Rigorous Heat-Exchanger Blocks in Simulators

```{note}
**Why CHEMCAD/Aspen “Generic” Heat Exchangers Are Dangerous**
Process simulators offer two heat-exchanger block types:


- **Generic / one-sided block:** you specify only the process inlet and the desired outlet temperature; the simulator computes the duty $Q$ and reports it. No utility stream is connected. The block is a *placeholder*.

- **Rigorous / two-sided block:** both streams are connected; the block solves the energy balance and the $Q = UA\Delta T_{LM}$ equation simultaneously. The simulator can return “infeasible” if the chosen utility is too cold/hot to drive the required temperature change.

The danger of generic blocks: the simulator will happily heat your stream to 10{,}000$^\circ$C or cool it to near absolute zero if you ask. It assumes a utility of sufficient capacity exists. **Always replace generic blocks with rigorous ones before finalizing a design.** Design reactors and separators first (the process backbone); then size heat exchangers as the last step.
```


```{note}
**Exam Tips — PFD Heat-Exchanger Conventions**
- Utility codes are lowercase, two- or three-letter (cw, rw, lps, mps, hps).

- Only the utility *inlet* stream gets labeled; outlet is implicit.

- Target utility $\Delta T$: 5–20$^\circ$C for sensible-heat utilities. Smaller $\to$ utility equipment oversized; larger $\to$ supply constraints.

- “E-tag” equipment is a heat exchanger (E-101 = first exchanger in plant area 100).
```


## The Thirteen Common Heat-Exchanger Types
Choosing the right heat-exchanger type is one of the most consequential decisions in equipment design. Each of the thirteen common families occupies a niche defined by area range, allowable $\Delta T$, viscosity, phase-change service, pressure rating, fouling tendency, and cost. We will catalogue each, then state the selection algorithm.

### Shell-and-Tube Family (The Default for Large Duty)

```{note}
**Shell-and-Tube: Three Sub-Types**
Shell-and-tube exchangers are the workhorse of the chemical industry. They handle large area (up to $\sim$1000 m$^2$ in a single shell), wide temperature and pressure range, and are cheap on a \$/m$^2$ basis at scale. The three sub-types differ in how they manage *thermal expansion* between the tubes and the shell.


- **Fixed-tubesheet:** the tubes are welded to two stationary tubesheets, one at each end of the shell. Cheapest of the three. *Cannot accommodate large differential expansion* — if tube and shell expand by very different amounts, the tubes buckle or the tubesheet weld fails. Suitable when $\Delta T_{LM} < 100^\circ$C (rule of thumb). Tube bundle is *not removable*, so shell-side mechanical cleaning is impossible — use only for clean shell-side service.

- **Floating-head:** one tubesheet is fixed; the other “floats” inside an internal cover, free to slide axially as the tubes expand. Tolerates any $\Delta T_{LM}$ within the materials' limits. Bundle is removable for shell-side cleaning. Workhorse for hot service ($\Delta T_{LM} \geq 100^\circ$C).

- **U-tube:** tubes are bent into hairpins so both ends terminate at the same tubesheet. The bend absorbs thermal expansion. Cheapest after fixed; thermal-expansion-tolerant. Drawback: the U-bend cannot be mechanically cleaned, so use only with clean tube-side fluids. Common for steam reboilers (clean steam side, fouling process side outside the tubes).
```


### Small-Area Exchangers ($< 200$ m$^2$)

```{note}
**{Double-Pipe, Multi-Pipe, Scraped-Wall, Spiral-Plate}**
For small duties (typically $< 50$–200 m$^2$), the shell-and-tube overhead is unjustified. Four alternative families:


- **Double-pipe (hairpin):** a tube inside a tube. Conceptually the simplest exchanger. Each leg is a single shell-tube unit; multiple legs are joined in series. Handles very high pressure (small-diameter shell tolerates it well) and is easy to clean. Limited to small areas ($< 50$ m$^2$).

- **Multi-pipe:** several tubes inside one larger tube (an extension of double-pipe). Compact alternative for slightly larger duties.

- **Scraped-wall:** a tube with motor-driven rotating scraper blades inside. Used for very viscous fluids (heavy oils, polymers) or for slurries that would foul a smooth-wall exchanger. The scraping prevents stagnant boundary layers and keeps $U$ high.

- **Spiral-plate:** a hollow plate rolled into a coil with the channels separated. One fluid flows through the rolled plate from center to periphery; the other flows through the void space between coils in counter-flow. Compact, self-cleaning (induced turbulence), tolerant of viscous fluids and small solids.
```


### Phase-Change Specialists

```{note}
**{Bayonet, Kettle Reboiler, Spiral Tube}**
For processes that demand boiling or condensing, three families excel:


- **Bayonet:** like a shell-and-tube without the shell — the tube bundle is dropped into the process vessel itself, fixed at one end only (the other end is free). Each tube has an inner concentric tube; fluid enters through the inner pipe and returns via the annulus. Used for submerged heating of a vessel's contents (e.g. a stripping column's reboiler integrated into the column sump). Accommodates expansion via the single-fixed-end design.

- **Kettle reboiler:** a shell-and-tube with an expanded shell on one end providing a large *vapor disengagement space*. The tube bundle sits in a pool of liquid; heat-transfer fluid (steam) flows through the tubes, vaporizing the shell-side liquid. The expanded space above lets the vapor disentrain liquid droplets before exiting. Standard reboiler for distillation columns when the boilup ratio is high.

- **Spiral tube:** a coiled tube inside a shell. Compact, suitable for small condensers or vaporizers ($< 50$ m$^2$). Good for viscous, fouling, or corrosive fluids because the coil promotes turbulence.
```


### Plate-Style Exchangers (Compact, High Efficiency)

```{note}
**{Plate-and-Frame, Plate-and-Fin}**
Plate exchangers achieve very large area in small volume by stacking many thin plates with corrugated channels between them. Two main subtypes:


- **Plate-and-frame (PHE):** a stack of corrugated metal plates separated by elastomeric gaskets and pressed together by a frame. Hot and cold fluids alternate channels. Very high $U$ (5–7 kW/m$^2$$\cdot$K for water-water), area up to $\sim$2500 m$^2$. Easy to expand (add plates). Limits: gasket-bounded temperature ($\sim$180$^\circ$C) and pressure ($\sim$25 barg). Not for fouling or large-particle fluids (narrow channels clog). The standard choice in food, dairy, and pharmaceutical service.

- **Plate-and-fin (brazed aluminum):** aluminum plates with corrugated fin spacers, brazed into a permanent block. Areas to 30{,}000 m$^2$ in one unit. Excellent for cryogenic service (LNG, air separation) where the aluminum thermal conductivity matters. Multi-stream: a single block can handle 3–6 streams simultaneously, enabling high heat integration in a small footprint.

Both plate styles tend to be expensive on a \$/m$^2$ basis at small areas but extremely cost-effective at large area where they dominate over shell-and-tube. Both have high pressure drop and are poor choices for viscous, fouling, or corrosive fluids.
```


### Air-Cooled (Fin-Fan) Exchangers

```{note}
**When Cooling Water Is Not Available**
**Air-cooled (fin-fan):** a tube bundle with extended-surface (finned) tubes, cooled by motor-driven fans blowing ambient air. No shell — the air is in open contact with the fins. Hot fluid always travels tube-side (air is always the cooling medium). Areas to 20{,}000 m$^2$.

**Used when** cooling water is scarce (desert plants, offshore platforms), or when the process side is above $\sim$60$^\circ$C and air-cooling is the most economical disposal of low-grade heat. **Limitation:** the cold-side temperature is bounded by the local dry-bulb temperature; air-coolers cannot achieve the lower temperatures that cooling water can in temperate climates.
```


### The Heat-Exchanger Selection Algorithm

```{note}
**Step-By-Step Selection**
- **Estimate the required area** from $Q = UA\Delta T_{LM}$ using an appropriate first-pass $U$ (see the next section).

- **Filter by area range.** Tiny areas $\to$ double-pipe; small $\to$ multi-pipe, spiral-plate; moderate to large $\to$ shell-and-tube or plate-and-frame; very large $\to$ plate-and-fin or air-cooler.

- **Filter by phase change.** Boiling shell-side $\to$ kettle reboiler. Submerged heating $\to$ bayonet. Cryogenic multistream $\to$ plate-and-fin.

- **Filter by viscosity, fouling, corrosivity.** Viscous or slurry $\to$ scraped-wall or spiral-plate. Highly fouling $\to$ shell-and-tube (mechanically cleanable). Cleanable plate $\to$ gasketed plate-and-frame.

- **Filter by temperature/pressure limits.** Plate-and-frame caps at $\sim$180$^\circ$C, 25 barg. Plate-and-fin caps at moderate pressures, very low T good. Shell-and-tube can handle 600+ barg and -200 to +600$^\circ$C with appropriate metallurgy.

- **Filter by $\Delta T_{LM**$.} Above $\sim$100$^\circ$C in shell-and-tube, switch from fixed-tubesheet to floating-head or U-tube to accommodate differential thermal expansion.

- **Compare lifetime cost** (capital + utility + maintenance + cleaning) of the survivors and pick the cheapest.
```


```{note}
**Exam Tips — Heat-Exchanger Selection**
- Pairings to memorize: kettle reboiler $\leftrightarrow$ distillation bottoms; floating-head $\leftrightarrow$ high-$\Delta T$ service ($\geq 100^\circ$C); air-cooler $\leftrightarrow$ desert plants or condensers above 60$^\circ$C process side; plate-and-fin $\leftrightarrow$ LNG / air separation; scraped-wall $\leftrightarrow$ crystallizing or polymer service.

- Fixed-tubesheet for clean, low-$\Delta T$ service. The cheapest shell-and-tube — but only when it works.

- U-tube: only when the tube-side fluid is clean (cannot mechanically clean the U-bend).

- Plate-and-frame: highest $U$ per dollar of capital — but watch pressure, temperature, and fouling limits.
```


## Heat-Exchanger Sizing: $Q = U A F \Delta T_{LM$}
Every shell-and-tube sizing problem reduces to five numbers: heat duty $Q$, overall coefficient $U$, log-mean temperature difference $\Delta T_{LM}$, correction factor $F$, and required area $A$. The PE exam tests all five.

### Derivation of the Log-Mean Temperature Difference
The starting point is the differential energy balance on a counter-flow heat exchanger.

```{dropdown} Solution Steps
- **Differential energy balance on a strip $dA$ of exchanger area.** The local hot-side and cold-side temperatures vary along the length. For a counter-flow exchanger with both streams flowing in opposite directions:

$$
dQ = UdA(T_h - T_c) = UdA\Delta T(x)
$$

    Simultaneously, the hot fluid loses energy at the rate $dQ = -m_h c_{p,h}dT_h$ (its temperature drops) and the cold fluid gains energy at the rate $dQ = -m_c c_{p,c}dT_c$ (its temperature rises, but $dT_c < 0$ in the direction of hot flow because cold flows the opposite way).


- **Express $d(\Delta T)$ in terms of $dQ$.** Subtract the two stream balances:

$$
d(\Delta T) = dT_h - dT_c = -(\frac{1}{m_h c_{p,h}} - \frac{1}{m_c c_{p,c}}) dQ
$$

    Note that for counter-flow with $m_h c_{p,h} = m_c c_{p,c}$, $d(\Delta T) = 0$ and the temperature difference is constant along the exchanger — the classic “balanced counter-flow” result.


- **Eliminate $dQ$ using the rate equation.** Substitute $dQ = UdA\Delta T$:

$$
\frac{d(\Delta T)}{\Delta T} = -U(\frac{1}{m_h c_{p,h}} - \frac{1}{m_c c_{p,c}}) dA
$$

    The right side is a constant in $A$. Integrate from end 1 (one end of the exchanger, where $\Delta T = \Delta T_1$) to end 2 (the other end, $\Delta T_2$):

$$
\ln(\frac{\Delta T_2}{\Delta T_1}) = -UA(\frac{1}{m_h c_{p,h}} - \frac{1}{m_c c_{p,c}})
$$

- **Eliminate the heat-capacity-rate term.** From the overall stream balances $Q = m_h c_{p,h}(T_{h,in} - T_{h,out})$ and $Q = m_c c_{p,c}(T_{c,out} - T_{c,in})$,

$$
\frac{1}{m_h c_{p,h}} = \frac{T_{h,in} - T_{h,out}}{Q},   \frac{1}{m_c c_{p,c}} = \frac{T_{c,out} - T_{c,in}}{Q}
$$

    Substituting:

$$
\ln(\frac{\Delta T_2}{\Delta T_1}) = -\frac{UA}{Q}[(T_{h,in} - T_{h,out}) - (T_{c,out} - T_{c,in})] = -\frac{UA}{Q}(\Delta T_2 - \Delta T_1)
$$

```


```{dropdown} Solution Steps
- **Rearrange to the canonical LMTD form.** Solving for $Q$:

$$
Q = UA\frac{\Delta T_2 - \Delta T_1}{\ln(\Delta T_2/\Delta T_1)}
$$

    Define the **log-mean temperature difference**:

$$
\Delta T_{LM = \frac{\Delta T_2 - \Delta T_1}{\ln(\Delta T_2/\Delta T_1)} = \frac{\Delta T_1 - \Delta T_2}{\ln(\Delta T_1/\Delta T_2)}}
$$

    Both forms are equivalent (the second is sometimes more intuitive). The final design equation is

$$
Q = UA\Delta T_{LM}   (Equation 1, pure counter-flow)
$$

- **Why the log-mean and not the arithmetic mean?** The $\Delta T$ varies exponentially along the exchanger length, not linearly. The arithmetic mean $\Delta T = (\Delta T_1 + \Delta T_2)/2$ overestimates the driving force when $\Delta T_1 \neq \Delta T_2$. The two means coincide as $\Delta T_1 \to \Delta T_2$.


- **Special cases.** If $\Delta T_1 = \Delta T_2$ (balanced counter-flow with $m_h c_{p,h} = m_c c_{p,c}$, or a condenser with constant-T condensation against constant-T evaporation), the formula is indeterminate (0/0). The limit gives $\Delta T_{LM} = \Delta T_1 = \Delta T_2$ (the constant value).


- **Verification.** The LMTD reduces to $\Delta T_1$ when $\Delta T_2 = 0$ (after applying L'H\^opital — though such a design has zero approach at one end and infinite area). The formula is symmetric in the two ends. \checkmark
```


### The Correction Factor $F$ for Non-Counter-Flow

```{note}
Pure counter-flow gives the maximum $\Delta T_{LM}$. Real shell-and-tube exchangers have multi-pass tube arrangements (1-2, 2-4, etc., shell-tube passes) that mix counter-flow with cross-flow regions, reducing the effective driving force. The correction factor $F$ adjusts for this:

$$
Q = UAF\Delta T_{LM}
$$

$F$ is a dimensionless function of two ratios:

$$
P = \frac{T_{c,out} - T_{c,in}}{T_{h,in} - T_{c,in}},   R = \frac{T_{h,in} - T_{h,out}}{T_{c,out} - T_{c,in}} = \frac{(mc_p)_c}{(mc_p)_h}
$$

Look up $F$ from a chart specific to the exchanger configuration (TEMA charts in Perry's). Typical values are 0.75 to 0.95. **Rule:** $F \geq 0.8$ is acceptable; below 0.8 the design is too compromised — add a shell pass in series, or use a different configuration.

For pure counter-flow, $F = 1$.
```


### Heat Duty $Q$ from Stream Properties

```{important}
**Two Cases for Computing $Q$**
**Sensible heat (no phase change):**

$$
Q = mc_p\Delta T
$$

where $\Delta T$ is the temperature change of the stream of interest. Use the stream that does not change phase; if both streams are sensible, either gives the same $Q$ by overall energy balance.

**Latent heat (phase change at constant $T$):**

$$
Q = m\lambda
$$

where $\lambda$ is the latent heat of vaporization (or condensation) at the saturation temperature.

**Combined (partial phase change):** integrate over the phase fractions, typically as

$$
Q = m_Lc_{p,L}\Delta T_L + m_v\lambda + m_vc_{p,v}\Delta T_v
$$

for cooling that takes a stream from superheated vapor to subcooled liquid.
```


### Typical Overall Heat-Transfer Coefficients $U$

```{tip}
**Typical $U$ Ranges (W/m$^2$$\cdot$K) — Perry's Handbook**
First-pass estimates by service:


- Gas-to-gas (atmospheric, no fouling): 10–50 (low; needs huge area).

- Gas-to-liquid (e.g. air-cooler, process condenser with air): 50–400.

- Light hydrocarbon liquid–liquid: 300–1000.

- Water–water (both clean): 800–1500.

- Steam condensing $\to$ water heating: 1500–4000.

- Steam condensing $\to$ boiling water (reboiler): 1500–3500.

- Refrigerant evaporating $\to$ process condensing: 800–1500.

- Liquid-liquid in plate-and-frame: 3000–7000 (the small channel and high turbulence give very high $U$).

A computed $U$ falling outside its plausible band signals a calculation error or an inappropriate exchanger type. Always sanity-check.
```


### Computing $U$ from Individual Resistances

```{important}
**The Resistance-in-Series Method**
The overall coefficient referenced to the outside area of the tubes is

$$
\frac{1}{U_o} = \frac{1}{h_o} + R_{f,o} + \frac{xA_o/A_{mean}}{k_{wall}} + \frac{A_o}{A_i} R_{f,i} + \frac{A_o}{A_ih_i}
$$

- $h_o, h_i$: outside and inside film heat-transfer coefficients (from Nusselt correlations: Dittus-Boelter for turbulent in-tube, Bell-Delaware for shell-side).

- $R_{f,o}, R_{f,i}$: fouling factors (TEMA tables: $\sim$1.7$\times 10^{-4}$ m$^2$K/W for clean water; up to 10$\times 10^{-4}$ for fouling hydrocarbons).

- $x$: tube wall thickness; $k_{wall}$: thermal conductivity of wall.

- $A_o/A_i$: area-ratio (outside/inside) to reference all resistances to the outside surface.

The dominant resistance(s) reveal where to invest design effort. For gas-side controlling, add fins (extended surface) on the gas side to increase effective $A$; for fouling-controlling, schedule frequent cleaning or specify wider fouling allowances; for wall-controlling (rare), use thinner or higher-conductivity tubes.
```


### Worked Example: Sizing a Cooling-Water Exchanger

```{prf:example} Sizing a Counter-Flow Cooler
A process stream of $m = 15{,}000$ kg/h, $c_p = 2.5$ kJ/(kg$\cdot$K), must be cooled from 110$^\circ$C to 60$^\circ$C using cooling water entering at 30$^\circ$C and leaving at 45$^\circ$C. Counter-flow, $F = 1$, estimated $U = 600$ W/(m$^2 \cdot$K). Find $Q$, the cooling-water flow, $\Delta T_{LM}$, and the heat-transfer area $A$.
```


```{dropdown} Solution Steps
- **Heat duty from the process side.**

$$
Q = mc_p\Delta T = (\frac{15{,}000}{3600})(2.5)(110 - 60) = (4.167)(2.5)(50) = 520.9  kW
$$

- **Cooling-water flow rate from energy balance.** The same $Q$ is absorbed by the cooling water.

$$
m_{cw} = \frac{Q}{c_{p,water}\Delta T_{cw}} = \frac{520.9}{(4.18)(15)} = \frac{520.9}{62.7} = 8.31  kg/s = 29{,}900  kg/h
$$

- **$\Delta T_{LM**$ for counter-flow.} End 1 (cold end): process exits at 60$^\circ$C, cooling water enters at 30$^\circ$C, so $\Delta T_1 = 60 - 30 = 30^\circ$C. End 2 (hot end): process enters at 110$^\circ$C, cooling water exits at 45$^\circ$C, so $\Delta T_2 = 110 - 45 = 65^\circ$C.

$$
\Delta T_{LM} = \frac{\Delta T_2 - \Delta T_1}{\ln(\Delta T_2/\Delta T_1)} = \frac{65 - 30}{\ln(65/30)} = \frac{35}{\ln(2.167)} = \frac{35}{0.7732} = 45.3^\circC
$$

- **Required heat-transfer area.**

$$
A = \frac{Q}{UF\Delta T_{LM}} = \frac{520{,}900W}{(600)(1)(45.3)} = \frac{520{,}900}{27{,}180} = 19.2  m^2
$$

- **Verification — four cross-checks.**


- Approach: both $\Delta T$ ends ($65^\circ$C and $30^\circ$C) exceed $\Delta T_{\min} = 10^\circ$C. \checkmark

- Utility $\Delta T = 15^\circ$C is in the 5–20 band. \checkmark

- $U = 600$ W/m$^2$K is plausible for a light-hydrocarbon-to-water service. \checkmark

- 19.2 m$^2$ is small — a double-pipe or compact plate-and-frame would work; a 6-inch shell-and-tube with $\sim$50 tubes of 4-foot length is the closest standard shell-and-tube size.
```


### Worked Example: Co-current vs. Counter-Current LMTD

```{prf:example} The $\Delta T_{LM
$ Penalty of Co-Current Flow}
For the same service (process 110$\to$60$^\circ$C, cooling water 30$\to$45$^\circ$C), compute $\Delta T_{LM}$ in (a) counter-flow and (b) co-current flow. By how much does the required area change?
```


```{dropdown} Solution Steps
- **Counter-flow (from previous example):** $\Delta T_{LM} = 45.3^\circ$C.


- **Co-current flow.** Both streams enter at the same end and exit at the same end. End 1 (entrance): $\Delta T_1 = 110 - 30 = 80^\circ$C. End 2 (exit): $\Delta T_2 = 60 - 45 = 15^\circ$C.

$$
\Delta T_{LM} = \frac{80 - 15}{\ln(80/15)} = \frac{65}{\ln(5.333)} = \frac{65}{1.6740} = 38.8^\circC
$$

- **Area comparison at constant $Q$ and $U$.**

$$
\frac{A_{co}}{A_{counter}} = \frac{\Delta T_{LM,counter}}{\Delta T_{LM,co}} = \frac{45.3}{38.8} = 1.17
$$

    The co-current arrangement needs 17% more area for the same service.


- **The deeper limit.** Co-current flow cannot in principle cool the process below the cooling-water outlet temperature — if the process target were 35$^\circ$C and the cooling-water outlet were 45$^\circ$C, the design would be infeasible in co-current and only feasible in counter-flow. **Counter-flow is therefore the default** for any service where the temperature ranges overlap.


- **Verification.** Co-current and counter-current give the same $\Delta T_{LM}$ if and only if the temperature ranges of the two streams do not overlap (one stream is entirely above the other in temperature). The overlap here is significant (process 60–110$^\circ$C, water 30–45$^\circ$C), so counter-flow's advantage is correspondingly large. \checkmark
```


### Worked Example: Sizing a Steam Reboiler (Latent Heat)

```{prf:example} Kettle Reboiler for a Distillation Column
A distillation column requires 3{,}500 kW of reboil duty. The process side boils at 95$^\circ$C; low-pressure steam at 6 barg condenses at 158$^\circ$C and is returned as saturated condensate. Latent heat of steam at 158$^\circ$C: $\lambda = 2{,}080$ kJ/kg. Estimated $U = 2{,}000$ W/m$^2$K (steam condensing $\to$ boiling, with $\sim$10% fouling allowance). Size the reboiler.
```


```{dropdown} Solution Steps
- **Steam flow required.**

$$
m_{steam} = \frac{Q}{\lambda} = \frac{3{,}500kW}{2{,}080kJ/kg} = 1.683kg/s = 6{,}060kg/h
$$

- **$\Delta T_{LM**$ for two isothermal streams.} Both sides are at constant temperature (condensing steam at 158$^\circ$C, boiling process at 95$^\circ$C), so $\Delta T_1 = \Delta T_2 = 158 - 95 = 63^\circ$C. The LMTD degenerates to this constant:

$$
\Delta T_{LM} = 63^\circC,   F = 1(no multi-pass correction needed)
$$

- **Required area.**

$$
A = \frac{Q}{U \cdot \Delta T_{LM}} = \frac{3{,}500{,}000W}{(2{,}000)(63)} = \frac{3{,}500{,}000}{126{,}000} = 27.8m^2
$$

- **Verification.** A 28 m$^2$ kettle reboiler is moderate-size, well within shell-and-tube range. The 63$^\circ$C driving force is comfortable. Steam flow 6{,}060 kg/h corresponds to roughly 1 ton/h — a small-to-medium distillation column.


- **Design notes.**


- Use a *kettle* (expanded-shell) geometry to allow vapor disengagement above the tube bundle, preventing entrainment back to the column.

- Steam tube-side (high pressure tolerance, clean fluid); process boil shell-side.

- Tube MOC: carbon steel is adequate for both sides at 158$^\circ$C and benign process composition; upgrade for chloride or acid service.
```


```{note}
**Exam Tips — Heat-Exchanger Sizing**
- Memorize the LMTD formula and apply it correctly to both ends (cold-end and hot-end $\Delta T$, then ln-mean).

- Counter-flow is the default; co-current rarely justified (often necessary when feed-flow direction is fixed by other constraints).

- Multi-pass shell-and-tube requires the correction factor $F$ from charts. $F \geq 0.8$ acceptable; otherwise re-configure.

- Sanity-check $U$ against the standard ranges — a calculated value far outside indicates an error.

- For phase-change duties, $Q = m\lambda$. Both sides isothermal $\to$ $\Delta T_{LM}$ is just the constant difference.
```


## Shell-Side vs. Tube-Side Fluid Assignment
For a shell-and-tube exchanger, the engineer must decide which fluid flows tube-side and which shell-side. This is not automatic in process simulators — the user makes the decision based on chemical compatibility, pressure ratings, fouling tendency, and cleaning access. Getting the assignment right reduces capital cost and improves reliability.

### Reasons to Put a Fluid on the Tube Side

```{note}
**Tube-Side Indicators**
A fluid prefers the *tube* side if it is:


- **Corrosive.** Tubes can be specified in exotic alloys (titanium, Hastelloy, Inconel) at low cost; the surrounding shell can be cheap carbon steel. Putting the corrosive fluid shell-side would force the whole shell to be expensive.

- **Fouling.** Tubes are mechanically cleanable by rotating brushes or hydroblasting (provided the tube bundle is removable or a straight-tube design). Shell-side fouling is much harder to remove — often requires chemical cleaning or full removal of the bundle and a fire-hose washdown.

- **High pressure (or vacuum).** Small-diameter tubes resist pressure better than large-diameter shells (hoop stress scales with diameter). Putting high-pressure steam tube-side is much cheaper than building a high-pressure shell.

- **Toxic, lethal, or hydrogen-bearing.** Tube-side reduces the leak surface area and provides better mechanical containment. The shell-to-atmosphere is the only sealed interface.

- **Treated or specially conditioned** (e.g. boiler feedwater) so that the tube-side metallurgy can be matched specifically to it.
```


### Reasons to Put a Fluid on the Shell Side

```{note}
**Shell-Side Indicators**
A fluid prefers the *shell* side if it is:


- **Condensing.** Large vapor space available on the shell side; vapor enters at the top and condensate drains naturally to the bottom. Tube-side condensing forces a more complex separator and reduces effective heat-transfer area.

- **Boiling.** Same logic: shell-side vapor disengagement is easy (especially in kettle reboilers). Tube-side boiling is possible (thermosiphon reboilers) but requires careful flow-instability analysis.

- **Viscous.** Shell-side baffles induce cross-flow turbulence that breaks up the boundary layer of a viscous fluid much more effectively than tube-side flow (which would otherwise be laminar at viscous-fluid velocities). Higher $h$ achieved.

- **Low pressure-drop tolerant.** Shell-side $\Delta P$ is generally smaller than tube-side $\Delta P$ for the same flow.
```


### Worked Example: Selecting Sides for an Oxygen-Heating Exchanger

```{prf:example} Tube/Shell Assignment for High-Pressure Steam Heating Oxygen
An exchanger heats 99%+ pure oxygen gas from 30 to 220$^\circ$C using high-pressure saturated steam at 45 barg ($T_sat \approx 257^\circ$C, condensing). Oxygen is an active oxidizer at elevated temperature. Steam is benign. Assign tube and shell sides.
```


```{dropdown} Solution Steps
- **Apply the pressure criterion.** The two streams' pressures differ by a factor of 45 (steam at 45 barg vs. oxygen at $\sim$1–5 barg). The high-pressure stream goes *tube side* where small-diameter tubes tolerate the pressure cheaply.

$$
Steam: tube side. Oxygen: shell side.
$$

- **Cross-check with the condensing criterion.** Condensing fluids prefer shell-side. Here the steam is condensing — so the condensing criterion would put steam shell-side. **Conflict.** The pressure criterion takes precedence (capital savings from CS-tube + CS-shell design with steam in tubes outweigh the small condensing-side $\Delta P$ penalty).

- **Cross-check with the corrosive criterion.** Hot oxygen at 220$^\circ$C is a fire/explosion hazard with hydrocarbon-contaminated carbon steel. The oxygen-wetted surface must be cleaned and made of an oxidation-resistant alloy (typically 316 SS). Putting oxygen shell-side means only the shell needs to be 316 SS; the tubes (steam-only) can be cheaper carbon steel. **Confirms the assignment.**

- **Verification.** The chosen configuration minimizes the expensive-alloy footprint: only the shell wall sees oxygen. Tubes are CS, tubesheets and channel might be CS with a 316 SS oxygen-side cladding, and the cost penalty over an all-CS exchanger is modest. The alternative (oxygen tube-side, steam shell-side, full 316 SS tubing) would double or triple the cost without operational benefit.
```


### Worked Example: Fouling Process Fluid + Cooling Water

```{prf:example} Tube/Shell Assignment for a Fouling Process Cooler
A heavy gasoil at 200$^\circ$C must be cooled to 80$^\circ$C using cooling water (clean, treated). The gasoil has a known fouling tendency (asphaltene deposition). Cooling water is at low pressure ($\sim$3 barg); gasoil at moderate pressure ($\sim$10 barg). Assign sides.
```


```{dropdown} Solution Steps
- **Apply the fouling criterion.** Fouling fluid goes tube-side for mechanical-cleaning access.

$$
Gasoil: tube side. Cooling water: shell side.
$$

- **Cross-check with pressure:** gasoil is higher pressure (10 vs. 3 barg) — also points to tube side. **Confirms.**

- **Cross-check with corrosivity:** gasoil at 200$^\circ$C is not strongly corrosive (no $H_2S$ specified), so MOC is not a deciding factor.

- **Cleaning plan.** Specify a removable bundle (floating-head shell-and-tube) and schedule periodic hydroblast cleaning of the tube ID. If the bundle were U-tube (cheaper), the tube-side U-bends could not be cleaned — a wrong choice given known fouling.

- **Verification.** The combination “floating-head + fouling fluid tube-side + clean shell-side fluid” is the textbook fouling-service configuration. \checkmark
```


### When Criteria Conflict

```{note}
**Tie-Breaking**
When two criteria point in opposite directions:


- Pressure usually wins over condensing (because the capital cost of a high-pressure shell can easily double the exchanger price).

- Fouling usually wins over viscosity (mechanical cleaning access is more valuable than the marginal $h$ improvement of shell-side baffling).

- Corrosion usually wins over everything if the alternative is an all-exotic-alloy build.

- When in doubt, put cooling water shell-side and the process fluid tube-side. This is the dominant industrial convention because process fluids tend to dominate the fouling, corrosion, and pressure-rating concerns.
```


```{note}
**Exam Tips — Side Assignment**
- Memorize the four tube-side indicators (corrosive, fouling, high-pressure, toxic) and the four shell-side indicators (condensing, boiling, viscous, low $\Delta P$ required).

- For the PE exam, expect a scenario with multiple competing factors and a question of the form “which goes tube-side?” Identify the dominant criterion and justify.

- The hot/cold temperature of the streams is *not* a deciding factor by itself.
```


## Materials of Construction for Heat Exchangers
The materials selection for a heat exchanger is one of the most consequential cost decisions. The tubes and the shell can (and often should) be made of different materials — the tubes match the tube-side fluid's chemistry; the shell matches the shell-side fluid's chemistry. “Mismatched” MOC is normal industrial practice and often cuts the exchanger cost in half compared to all-one-alloy construction.

### Materials Selection Order of Operations

```{note}
**Three-Step MOC Selection**
- **Temperature limits.** Carbon steel (CS) A516 is good to about 425$^\circ$C continuously and down to roughly $-29^\circ$C (below this, impact testing per ASME is required; switch to low-temp variants A350 LF2 or A203, or to austenitic SS for cryogenic). Above 425$^\circ$C, low-Cr steels (1.25Cr, 2.25Cr) or austenitic SS take over. Below $-100^\circ$C: austenitic 304/304L SS. Below $-195^\circ$C (LNG, air separation): 9% Ni steel or aluminum.

- **Chemical compatibility.** Screen the candidate materials against the actual process chemistry: oxidizers, chlorides, sulfides, acids, bases, hydrogen. Eliminate alloys that fail in this service. This is where corrosion-engineering tables (Hamner's, NACE) become essential.

- **Cost.** Among the survivors, pick the cheapest. Consider *cladded* construction (cheap CS base + thin expensive liner) for large vessels where the wall thickness is dominated by mechanical strength, not corrosion.
```


### Common MOC Choices for Tubes and Shell

```{tip}
**Industrial MOC Catalogue**
- **Carbon steel** (A516-70, A106-B): cheap workhorse for non-corrosive service, steam, hydrocarbons, water below dew point. Service envelope $-29$ to $+425^\circ$C.

- **A201 low-alloy steel**: a CS variant good down to $-45^\circ$C; useful for refrigerant-side tubing.

- **304/304L SS**: mildly oxidizing fluids, food, pharma. Avoid above 60$^\circ$C with chlorides ($>$ 50 ppm) due to chloride SCC.

- **316/316L SS**: Mo addition improves pitting resistance. Dilute sulfuric (below $\sim$10%), seawater (cold), most organic acids.

- **Copper alloys**: Admiralty brass and 90/10 Cu-Ni for surface condensers in seawater; resists biofouling.

- **Monel (Ni-Cu 400)**: HF service, hot caustic, seawater handling.

- **Inconel 625, Hastelloy C-276**: aggressive oxidizing acids, hot chlorides, mixed acids.

- **Titanium Gr 2**: wet chlorine, hypochlorite, oxidizing chlorides, seawater. Catastrophic in dry chlorine or HF.

- **Tantalum**: hot strong acids; the “universal” acid material, very expensive.

- **Glass-lined steel, PTFE-lined steel**: hot HCl, dilute sulfuric below 70$^\circ$C, concentrated organics.
```


### Cladded Construction

```{note}
**Why Cladded Plate Saves Money**
A pressure vessel's wall thickness is typically set by hoop stress (ASME Sec. VIII), not by corrosion. Once the wall is $\sim$1/2$”$ thick to resist pressure, the additional thickness for corrosion is small. **Cladded plate** exploits this:


- A thick (e.g. 25 mm) layer of cheap carbon steel provides the structural strength.

- A thin (e.g. 3 mm) layer of expensive corrosion-resistant alloy (316L SS, Inconel) is metallurgically bonded to the process-wetted side.

- The bond is achieved by hot-rolling, explosion welding, or weld overlay.

Cost: typically 60–80% of solid corrosion-resistant construction. Inspection: required more often than solid construction to verify the clad layer is intact and not breached by pitting that has reached the CS substrate.
```


### Worked Example: MOC for the Oxygen-Heating Exchanger

```{prf:example} MOC Selection: Steam Heats Pure Oxygen
For the previous example (steam at 45 barg, 257$^\circ$C condensing in the tubes; oxygen at 30 to 220$^\circ$C in the shell), select MOC for tubes and shell. Justify with cost and safety considerations.
```


```{dropdown} Solution Steps
- **Shell MOC (oxygen-wetted).** Pure oxygen at $> 200^\circ$C is a fire and detonation hazard when in contact with hydrocarbon-contaminated carbon steel. The CS surface, if exposed to even trace amounts of oil, can ignite catastrophically in oxygen. The accepted MOC for hot pure-oxygen service is austenitic stainless — **316 SS** is the standard choice. This matches the upstream compressor (C-101, also 316 SS for oxygen service) per industry practice.

- **Tube MOC (steam-wetted).** Saturated steam at 257$^\circ$C and 45 barg is benign in carbon steel up to roughly 400–425$^\circ$C continuous service. **Carbon steel (A179 or A210)** is standard. Specifying 316 SS tubes for steam service would add cost without benefit.

- **Cost saving from mixed MOC.** If we forced all-316 SS construction, the exchanger cost would approximately double over CS tubes + 316 SS shell. The mixed configuration uses 316 SS only where chemically required (the oxygen-wetted shell) and CS where it suffices (the steam-wetted tubes).

- **Verification: NACE/ASME compliance.** For oxygen service, both ASME B31.3 Chapter X and ASTM G88/G94 govern — requires degreased, particulate-free construction with non-flammable lubricants. The 316 SS shell satisfies the material requirement; the cleaning protocol is process-specification, not MOC-specification.

- **Tubesheet MOC.** The tubesheet sees both fluids; conventionally, the tubesheet matches the more demanding side. Here: 316 SS tubesheet, with the carbon-steel tubes seal-welded to it (autogenous TIG welds for compatibility).
```


### Worked Example: MOC for a Refrigerant Tube-Side, Process Shell-Side

```{prf:example} MOC for a Refrigerated Process Cooler
A heat exchanger uses Freon-22 refrigerant at $-40^\circ$C (vaporizing tube-side) to cool a non-corrosive hydrocarbon process stream shell-side. Specify MOC.
```


```{dropdown} Solution Steps
- **Tube MOC (refrigerant-wetted at $-40^\circ$C).** Standard CS is brittle below $-29^\circ$C. Use **A201 low-alloy steel** or a low-temp CS variant qualified by ASME impact testing. Service envelope to $-45^\circ$C. For colder service (e.g. $-60^\circ$C), step up to 304 SS or 9% Ni steel.

- **Shell MOC (hydrocarbon process side).** The process is non-corrosive at moderate temperature. **Carbon steel** (A516-70) is adequate.

- **Verification.** Both materials are within their service envelopes. Mixed CS shell + low-temp-CS tubes is a small cost premium over all-CS but is required for the cold-tube-side service.
```


```{note}
**Exam Tips — Heat-Exchanger MOC**
- Tube and shell MOC can differ; doing so often saves 30–50% of capital. Match each to its wetted fluid.

- Pure-oxygen and chlorine service require non-CS construction even at modest temperatures.

- Below $-29^\circ$C, standard CS becomes brittle; switch to A201, 304 SS, or 9% Ni steel depending on minimum temperature.

- Sour service ($H_2S$): NACE MR0175 governs; typically lower-strength steels and post-weld heat treatment to avoid sulfide stress cracking.
```


## Pressure-Vessel Design (ASME Section VIII Div. 1)
Most process vessels in chemical plants — reactors, separators, knockout drums, columns above their internals, heat-exchanger shells — are governed by ASME Boiler and Pressure Vessel Code Section VIII Division 1. The PE exam tests the thin-wall design equations and the basic concept of corrosion allowance.

### Thin-Wall Approximation and the Two Stress Equations

```{note}
**Hoop vs. Longitudinal Stress**
For a thin-walled cylindrical shell under internal pressure $P$, with inside radius $R$ and wall thickness $t$, the stresses are


- Hoop (circumferential) stress: $\sigma_h = P R / t$.

- Longitudinal (axial) stress: $\sigma_\ell = P R / (2t)$ — exactly half the hoop stress.

Hoop stress is always larger, so the hoop equation governs the design.

The “thin-wall” assumption requires $t/R < 0.1$ (or equivalently $P/SE < 0.385$). Above this, use the thick-wall (Lam\'e) equations; below, the thin-wall ones are accurate.
```


### The ASME Section VIII Div. 1 Design Equations

```{important}
**{ASME Sec. VIII Div. 1, Paragraph UG-27}**
For a cylindrical shell under internal pressure, the minimum required wall thickness is the larger of the hoop and longitudinal results:

**Hoop (governs when $P/SE < 0.385$):**

$$
t = \frac{P R}{S E - 0.6 P}
$$

**Longitudinal:**

$$
t = \frac{P R}{2 S E + 0.4 P}
$$

The $-0.6P$ and $+0.4P$ correction terms account for the finite-thickness curvature effect that the simple thin-shell equation ignores; they keep the ASME formula accurate at moderate $P/S$.

Add the **corrosion allowance** $CA$ to $t$ to get the final design thickness. Round up to the next standard plate gauge.
```


```{tip}
- $P$: design pressure [psig, kPa, or bar]. Set as MAWP + 10% margin, or design pressure + safety-valve setting.

- $R$: inside radius of the shell [in or mm].

- $S$: allowable stress at design temperature [psi or MPa], from ASME Sec. II Part D for the specified material. Decreases with rising temperature.

- $E$: longitudinal weld-joint efficiency. 1.00 fully radiographed butt welds; 0.85 spot-radiographed; 0.70 no radiography. Choose to optimize cost (radiography is moderately expensive but lets you use a thinner wall).

- $CA$: corrosion allowance. Typical values: 1/16$”$ (1.6 mm) for clean noncorrosive service; 1/8$”$ (3.2 mm) general; 1/4$”$ (6.4 mm) corrosive.
```


### External Pressure (Vacuum Service)

```{note}
**Buckling Governs for External Pressure**
A vessel under external pressure (vacuum service) fails by *buckling*, not by yielding — the wall snaps inward elastically before the material yields. The design uses ASME Sec. VIII Div. 1 Paragraph UG-28 with empirical B-charts that account for shell geometry (length-to-diameter ratio, $D_o/t$).

External-pressure designs are substantially more conservative than equivalent internal-pressure designs — a vacuum vessel may need a wall thickness 2–3$\times$ the internal-pressure value for the same diameter. **Stiffening rings** (welded circumferentially every few feet) reduce the effective unsupported length and let you use a thinner wall.
```


### Worked Example: Wall Thickness of a Process Reactor

```{prf:example} Reactor Wall Thickness
A vertical cylindrical reactor: ID = 60 in (1.524 m), design pressure 250 psig, design temperature 600$^\circ$F. MOC: SA-516 Gr. 70 carbon steel. $S = 17{,}500$ psi at 600$^\circ$F (from ASME Sec. II Part D). Fully radiographed butt welds, $E = 1.0$. Corrosion allowance 1/8 in. Find the required wall thickness and the nearest commercial plate gauge.
```


```{dropdown} Solution Steps
- **Check the thin-wall assumption.**

$$
\frac{P}{SE} = \frac{250}{17{,}500 \times 1.0} = 0.0143 \ll 0.385  \checkmark
$$

    The hoop equation governs. (If $P/SE > 0.385$, use the thick-wall Lam\'e equations from Sec. VIII Div. 1 Appendix 1-1.)

- **Compute pressure-design thickness from the hoop equation.** $R = 30$ in.

$$
t_{pressure} = \frac{P R}{S E - 0.6 P} = \frac{(250)(30)}{(17{,}500)(1.0) - 0.6(250)} = \frac{7{,}500}{17{,}500 - 150} = \frac{7{,}500}{17{,}350} = 0.432in
$$

- **Add corrosion allowance.**

$$
t_{total} = t_{pressure} + CA = 0.432 + 0.125 = 0.557in
$$

- **Round up to a standard plate gauge.** Standard plate increments: 3/8, 7/16, 1/2, 9/16, 5/8, 11/16, 3/4 in. The next size above 0.557 is **9/16 in = 0.5625 in**. Specify 9/16-in plate.

- **Verification — check hoop stress at the chosen wall.**

$$
\sigma_h = \frac{P R}{t - CA} = \frac{(250)(30)}{0.5625 - 0.125} = \frac{7{,}500}{0.4375} = 17{,}143psi < S = 17{,}500psi  \checkmark
$$

    The actual stress is just below the allowable — a tight but acceptable design. If a manufacturing tolerance reduces the wall thickness slightly, the stress could approach $S$, which is why the standard practice is to specify the next gauge up rather than the calculated minimum.
```


### Heads and Closures

```{note}
**Sizing Vessel Heads**
The thickness of the dished or hemispherical end-cap (“head”) of a vessel is governed by similar formulas with different shape factors:


- **Hemispherical head:** $t = PR/(2SE - 0.2P)$. The cheapest head per unit area (half the cylinder thickness for the same conditions) but the most expensive to fabricate (requires forging or extensive pressing).

- **2:1 ellipsoidal head:** $t = PD/(2SE - 0.2P)$ where $D$ is the inside diameter. The compromise — moderate cost and moderate thickness.

- **Torispherical (ASME flanged | dished):** $t = 0.885PL/(SE - 0.1P)$ where $L$ is the crown radius. Cheapest to fabricate (deep-drawn from flat plate) but thickest.

For a process vessel of moderate pressure, 2:1 ellipsoidal heads are the most common choice.
```


```{note}
**Exam Tips — Pressure Vessels**
- Hoop stress = 2$\times$ longitudinal stress. Hoop equation governs.

- Memorize the thin-wall cutoff $P/SE < 0.385$.

- Add corrosion allowance *after* solving for pressure-design thickness.

- Round up to standard plate; the most common increment is 1/16 in.

- Joint efficiency $E$: 1.00 (full radiography), 0.85 (spot), 0.70 (none). Cost trade-off with plate weight.

- Vacuum/external-pressure: governed by buckling, much more conservative; add stiffening rings to reduce effective length.
```


## Pump Selection and NPSH
Pumps move liquid; compressors move gas. The PE exam tests pump-type selection by flow-and-head, hydraulic power calculation, and the universally-tested NPSH (Net Positive Suction Head) analysis to prevent cavitation.

### Pump Type Selection by Flow and Head

```{note}
**Five Pump Families**
- **Centrifugal (radial-flow):** the workhorse. High flow, low-to-moderate head ($< 200$ m), clean fluids, smooth performance curve. Used for $\sim$70% of plant pumps.

- **Centrifugal (axial-flow):** very high flow, low head ($< 20$ m). Cooling-tower circulation, flood control.

- **Positive-displacement (PD) reciprocating:** high head ($> 200$ m), low flow, ability to handle viscous fluids or metering duty. Constant volumetric delivery per stroke.

- **PD rotary (gear, lobe, screw):** viscous fluids ($> 100$ cP), moderate flow and head. Self-priming. Cannot tolerate solids.

- **Diaphragm:** hazardous service, slurries, sealed (no leak path). Pulsating delivery.

The selection map plots flow (x-axis, log scale) vs. head (y-axis, log scale) with regions for each family.
```


### Specific Speed and Impeller Geometry

```{important}
**Specific Speed**
For a centrifugal pump, the specific speed is

$$
N_s = \frac{N\sqrt{Q}}{H^{3/4}}
$$

with $N$ in rpm, $Q$ in gpm, $H$ in feet (US units). Specific speed is a similarity-law parameter that classifies impeller types:


- $N_s \sim 500$–2000: radial-flow impeller (high head, low flow).

- $N_s \sim 2000$–5000: mixed-flow (Francis-type) impeller.

- $N_s \sim 5000$–15000: axial-flow (propeller) impeller.

At a given desired flow and head, only certain $N_s$ ranges can be achieved at high efficiency; this dictates the impeller geometry.
```


### Hydraulic Power and Brake Power

```{important}
**Pump Power**
**Hydraulic power** (the useful power delivered to the fluid):

$$
P_{hyd} = mgH = \rhogQH  [SI: W]
$$

or, in US units, $P_{hyd}[hp] = Q[gpm] \cdot H[ft] \cdot SG / 3960$.

**Brake power** (the shaft power the motor must deliver):

$$
P_{brake} = \frac{P_{hyd}}{\eta_{pump}}
$$

Typical pump efficiency: 50–65% for small (< 5 hp) pumps, 70–85% for moderate-size centrifugals.

**Motor input power** adds motor losses:

$$
P_{electric} = \frac{P_{brake}}{\eta_{motor}}
$$

with $\eta_{motor} \approx 90$–95% for modern TEFC induction motors.
```


### NPSH: Available vs. Required

```{note}
**The Cavitation Criterion**
Cavitation occurs in a centrifugal pump when the local fluid pressure at the impeller eye falls below the fluid vapor pressure. Vapor bubbles form, then collapse violently as the fluid moves to a higher-pressure region of the impeller. The collapse erodes the impeller and creates noise, vibration, and (in extreme cases) loss of head.

To prevent cavitation, the **available NPSH** (NPSH$_A$) at the pump suction must exceed the **required NPSH** (NPSH$_R$, a pump characteristic from the manufacturer curve), with a safety margin of at least 0.6 m (2 ft):

$$
NPSH_A \geq NPSH_R + 0.6m
$$

```


```{important}
**Computing NPSH$_A$**

$$
NPSH_A = \frac{P_{abs} - P_{vap}}{\rho g} + z_s - h_{f,s}
$$

- $P_{abs}$: absolute pressure at the liquid surface of the source vessel (atmospheric + any gas pressure).

- $P_{vap}$: vapor pressure of the fluid at operating temperature.

- $\rho$: fluid density at operating temperature.

- $z_s$: static suction head. Positive if the source is above the pump centerline (flooded suction); negative if below (suction lift).

- $h_{f,s}$: friction head loss in the suction piping (positive value subtracted; never use a negative friction loss).

Note that $P_{vap}$ rises strongly with temperature. Hot fluids (water above 70$^\circ$C, hydrocarbons near their bubble point) are at maximum cavitation risk.
```


### Worked Example: NPSH$_A$ for a Hot-Water Pump

```{prf:example} Hot-Water Pump Cavitation Check
Water at 90$^\circ$C ($P_{vap} = 70$ kPa, $\rho = 965$ kg/m$^3$) is pumped from an atmospheric tank ($P_{abs} = 101.3$ kPa). The water surface is 2.0 m above the pump centerline (flooded suction). Suction-line friction loss is 1.5 m of water. The pump's NPSH$_R$ at the design flow is 3.0 m. Determine NPSH$_A$ and assess whether the pump will cavitate.
```


```{dropdown} Solution Steps
- **Pressure head term (convert kPa to m of water).**

$$
\frac{P_{abs} - P_{vap}}{\rho g} = \frac{(101.3 - 70.0) \times 10^3Pa}{965 \times 9.81Pa/m} = \frac{31{,}300}{9{,}467} = 3.31m
$$

- **Add static head, subtract friction.**

$$
NPSH_A = 3.31 + 2.0 - 1.5 = 3.81m
$$

- **Compare to NPSH$_R$ with safety margin.**

$$
Margin = NPSH_A - NPSH_R = 3.81 - 3.0 = 0.81m > 0.6m  \checkmark
$$

    The pump will operate safely without cavitation at the design point.


- **Sensitivity check: what if water is heated to 100$^\circ$C?** $P_{vap}$ rises to 101.3 kPa (boiling at atmospheric), so the pressure head term collapses:

$$
\frac{P_{abs} - P_{vap}}{\rho g} = \frac{101.3 - 101.3}{…} = 0
$$

$$
NPSH_A = 0 + 2.0 - 1.5 = 0.5m \ll 3.0m
$$

    The pump would cavitate immediately. The design has very little thermal headroom — a process upset that heats the water by another 10$^\circ$C destroys NPSH$_A$. The fix is to raise the source tank (more $z_s$) or lower the operating temperature.


- **Verification.** Hot-water service is the classic cavitation risk: $P_{vap}$ rises rapidly with $T$ in the boiling region. The 90$^\circ$C operating point is at the edge of acceptability; a safer design would either use a flooded-suction configuration with more elevation or a deaerated, cooler feed.
```


### The Affinity Laws

```{important}
**Centrifugal Pump Scaling**
For a single pump operating at different speeds (or for geometrically-similar pumps of different sizes):


- Flow: $Q \propto N \cdot D^3$

- Head: $H \propto N^2 \cdot D^2$

- Power: $P \propto N^3 \cdot D^5$

where $N$ is rotational speed and $D$ is impeller diameter. The affinity laws are exact for inviscid scaling and approximately correct at modest Reynolds-number variations.

**Use case:** changing pump speed via VFD (variable-frequency drive). Halving the speed gives half the flow, one-quarter the head, and one-eighth the power. This is why VFD throttling is dramatically more energy-efficient than valve throttling for a centrifugal pump.
```


### Compressor Selection (Brief)

```{note}
**Compressor Type by Pressure Ratio and Flow**
- **Reciprocating:** high pressure ratio per stage ($\sim$3–4), low flow, high efficiency. Used for hydrogen, syngas, high-pressure compression.

- **Centrifugal (multistage):** high flow, moderate per-stage pressure ratio ($\sim$1.5–2). The standard for refinery and gas-plant duty. Multistage stack achieves high overall ratio.

- **Axial:** extremely high flow, low per-stage ratio. Used in large air-separation trains, gas-turbine compression sections.

- **Rotary screw / lobe:** oil-flooded; moderate flow, modest pressure ($< 10$ bar). Refrigeration and instrument air.

For compressors, the polytropic or isentropic head equation governs (analog of pump $H$):

$$
H_{poly} = \frac{Z R T_1}{M}\frac{k}{k-1}[(\frac{P_2}{P_1})^{(k-1)/k} - 1] / \eta_p
$$

```


```{note}
**Exam Tips — Pumps and NPSH**
- Centrifugal pump for the majority of plant duty; PD for high head or metering or viscous.

- NPSH$_A$ = $(P_{abs} - P_{vap})/(\rho g) + z_s - h_{f,s}$. Must exceed NPSH$_R$ by 0.6 m.

- Cavitation traps: (1) using gauge pressure instead of absolute; (2) sign error on friction head; (3) forgetting that $P_{vap}$ depends on temperature.

- Affinity laws: $Q \propto N$, $H \propto N^2$, $P \propto N^3$. VFD throttling saves much more energy than valve throttling.
```


## Distillation Column Sizing (Brief)
Distillation columns are sized in two stages: number of theoretical stages (Fenske-Underwood-Gilliland shortcut or rigorous McCabe-Thiele), then column diameter and height for the chosen internals.

### Number of Theoretical Stages: FUG Shortcut

```{important}
**Fenske-Underwood-Gilliland (FUG) Shortcut**
The FUG method estimates $N_{stages}$ in three stages:

**Fenske (minimum stages at total reflux):**

$$
N_{\min} = \frac{\log[\dfrac{x_D/(1 - x_D)}{x_B/(1 - x_B)}]}{\log \alpha_{avg}}
$$

where $x_D, x_B$ are distillate and bottoms compositions of the light key and $\alpha_{avg}$ is the average relative volatility (geometric mean of $\alpha$ at top and bottom).

**Underwood (minimum reflux):** solve

$$
\sum_i \frac{\alpha_i z_i}{\alpha_i - \theta} = 1 - q
$$

for $\theta$ (a root between the light- and heavy-key $\alpha$'s), then

$$
R_{\min} + 1 = \sum_i \frac{\alpha_i x_{D,i}}{\alpha_i - \theta}
$$

**Gilliland correlation** (actual stages from $N_{\min}$ and the chosen $R$, typically $R = 1.2$–1.5$R_{\min}$):

$$
\frac{N - N_{\min}}{N + 1} = 1 - \exp[\frac{1 + 54.4 X}{11 + 117.2 X}\frac{X - 1}{X^{0.5}}],   X = \frac{R - R_{\min}}{R + 1}
$$

or read from a Gilliland chart.
```


### Column Diameter from Flooding

```{important}
**Souders-Brown Diameter**
The maximum vapor superficial velocity that avoids flooding (entrainment of liquid by upward-moving vapor) is

$$
U_{\max} = C_{SB}\sqrt{\frac{\rho_L - \rho_V}{\rho_V}}
$$

where $C_{SB}$ (Souders-Brown capacity factor, read from Fair's chart) ranges $0.05$–$0.15$ m/s for trayed columns. Design at 70–85% of flood velocity. The column diameter is

$$
D = \sqrt{\frac{4V}{\piU_{design}}}
$$

where $V$ is the vapor volumetric flow at column operating conditions.
```


### Tray vs. Packed

```{note}
- **Trays** (sieve, valve, bubble cap): preferred for $D > 0.6$ m, fouling fluids, wide turndown (5:1 valve trays, 3:1 sieve), easy maintenance and cleaning. Tray spacing typically 0.6 m, so column height $\approx 0.6 \cdot N_{actual trays}$.

- **Random packing** (Pall rings, IMTP): lower pressure drop than trays, smaller diameter columns, vacuum service.

- **Structured packing** (Mellapak, Flexipac): highest efficiency (lowest HETP), very low $\Delta P$/stage, but limited turndown. Standard in cryogenic air separation, high-purity service.

HETP (Height Equivalent to a Theoretical Plate): structured 0.3–0.5 m; random 0.5–1.0 m. So column height $\approx HETP \cdot N_{theoretical}$ for packing.
```


```{note}
**Exam Tips — Distillation Sizing**
- For shortcut sizing, identify whether $\alpha$ or VLE data is given. $\alpha$ given $\to$ FUG. VLE only $\to$ McCabe-Thiele graphical.

- Operating $R = 1.2$–1.5 $R_{\min}$ is the usual cost-optimum (capital decreases with more stages; energy increases with more reflux; the optimum is near 1.3 $R_{\min}$).

- Tray vs. packing: $D < 0.6$ m or vacuum $\to$ packing; otherwise $\to$ trays unless extreme efficiency is needed.
```


## Equipment Summary Tables
After a PFD is drawn, each major equipment item receives an **equipment summary table** (also called an equipment list, spec sheet, or data sheet) that gives the vendor everything needed to quote and fabricate the unit.

```{tip}
**Heat-Exchanger Equipment Summary Table Contents**
For each exchanger E-NXX, the table reports:


- Type (e.g. shell-and-tube floating head, kettle reboiler, double-pipe, plate-and-frame).

- Area $A$ in m$^2$ (from sizing calculation).

- Heat duty $Q$ in kW.

- Overall heat-transfer coefficient $U$ in W/m$^2$$\cdot$K (computed or estimated).

- Log-mean temperature difference $\Delta T_{LM}$ in $^\circ$C (with $F$ correction if multi-pass).

- Shell-side fluid: identity, flow rate, inlet/outlet temperatures, inlet/outlet pressures, phase (L, V, L+V, or numeric vapor fraction).

- Tube-side fluid: same items.

- MOC for shell, tubes, tubesheet, baffles. May differ; cite ASME/ASTM spec (e.g. A516-70 for shell, A179 for tubes).

- Design pressure and design temperature (used for ASME Sec. VIII calculations).

- Tube length, diameter, number, pitch (for shell-and-tube).

- Insulation specification.

The table is part of the inquiry package sent to vendors; the vendor returns a firm price and delivery quotation.
```


```{note}
**Phase Designation Convention**
Read the inlet and outlet vapor fractions from the simulator and translate:


- $\phi_v = 1$ in and out: gas/vapor (label “V” or “gas”).

- $\phi_v = 0$ in and out: liquid (label “L”).

- $\phi_v = 1$ in, $\phi_v = 0$ out: condensing (label “condensed” or “cond.”).

- $\phi_v = 0$ in, $\phi_v = 1$ out: vaporizing (“vaporized” or “vap.”).

- Partial: e.g. $\phi_v = 1 \to 0.8$ partial condensation; $\phi_v = 0.2 \to 0.1$ partial condensation of a two-phase feed. Report both endpoints.

Density and viscosity entries are often omitted for condensing/vaporizing streams because they change dramatically; phase label is more useful.
```


## Summary: Equipment Design Decision Tree

```{note}
**Which Equipment When?**
- Heat exchanger needed? Start with $Q = UAF\Delta T_{LM}$ to estimate $A$. Then run the selection algorithm (area $\to$ shell-and-tube vs. alternatives; phase change $\to$ kettle/bayonet; viscous $\to$ scraped/spiral; cold-utility scarcity $\to$ air-cooler).

- Tube/shell assignment: corrosive, fouling, high-pressure, toxic $\to$ tube. Condensing, boiling, viscous, low-$\Delta P$ $\to$ shell. When in doubt, cooling water shell-side and process fluid tube-side.

- MOC: start CS, upgrade only as chemistry/temperature demands. Mix tube and shell MOC freely; consider cladded plate for large vessels.

- Pressure vessel: hoop equation governs for thin wall ($P/SE < 0.385$). Add corrosion allowance and round up to standard gauge.

- Pump selection: centrifugal as default; PD for high head, viscous, or metering. Always check NPSH$_A$ vs. NPSH$_R$ with 0.6-m margin.

- Compressor: centrifugal for moderate ratio + high flow; reciprocating for high ratio + low flow; axial for very high flow + low ratio.

- Distillation column: FUG for stages, Souders-Brown for diameter; tray for $D > 0.6$ m and tolerance fluids, packing for vacuum / high efficiency.
```


```{tip}
**One-Page Formula Reference**
**Heat exchanger:**
$Q = U A F \Delta T_{LM}$.
$\Delta T_{LM} = (\Delta T_1 - \Delta T_2)/\ln(\Delta T_1/\Delta T_2)$.
$Q = mc_p\Delta T$ (sensible); $Q = m\lambda$ (latent).
$F$ from TEMA charts, target $\geq 0.8$.

**Utility duty:** $m_{util} = Q/(c_p\Delta T_{util})$; target $\Delta T_{util} = 5$–$20^\circ$C.

**Pressure vessel (ASME Sec. VIII Div. 1):**
Hoop: $t = PR/(SE - 0.6P)$; longitudinal $t = PR/(2SE + 0.4P)$.
Add corrosion allowance; round to standard gauge.
Thin-wall valid if $P/SE < 0.385$.

**Pump:**
$P_{hyd} = \rho g Q H$; $P_{brake} = P_{hyd}/\eta$.
NPSH$_A = (P_{abs} - P_{vap})/(\rho g) + z_s - h_{f,s}$; require $\geq$ NPSH$_R$ + 0.6 m.
Affinity: $Q \propto N$, $H \propto N^2$, $P \propto N^3$.

**Distillation:**
Fenske: $N_{\min} = \log[(x_D/(1-x_D))/(x_B/(1-x_B))]/\log\alpha$.
Operating $R \approx 1.3R_{\min}$.
Souders-Brown diameter: $U_{\max} = C_{SB}\sqrt{(\rho_L - \rho_V)/\rho_V}$, design at 70–85% flood.

**Typical $U$ (W/m$^2$K):** gas-gas 10–50, gas-liq 50–400, water-water 800–1500, steam-water 1500–4000.
```
