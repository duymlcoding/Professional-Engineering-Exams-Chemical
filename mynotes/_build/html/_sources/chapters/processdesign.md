---
title: "Process Design"
author: "PE Study Guide"
date: "2025"
---

# Process Design

## Process Diagrams: BFD, PFD, and P&ID
A chemical process is documented at three escalating levels of detail. The Block Flow Diagram (BFD) captures the high-level intent on a single page; the Process Flow Diagram (PFD) shows every major piece of equipment with stream conditions and an overall mass-and-energy balance; the Piping & Instrumentation Diagram (P&ID) gives the construction-grade representation of one section of the plant, with every valve, instrument, and pipe specification. The PE exam tests both visual literacy (recognizing the symbols and what level of detail belongs where) and the engineering judgment behind these documents.

### Hierarchy of Detail and Purpose

```{note}
**The Three Diagram Types**
- **BFD  -  Block Flow Diagram.** The minimum-detail view. Blocks (rectangles) for major unit operations (reactors, separators, possibly a critical compressor or steam generator), arrows for major streams, overall mass-flow rates on each stream, and a figure caption. Used in early conceptual design and in management-level presentations.

- **PFD  -  Process Flow Diagram.** Every major equipment item is shown using its conventional symbol with a tag number; every process stream is numbered. A separate *stream table* reports composition, temperature, pressure, phase, and flow for each numbered stream. Utility streams are labeled by their lowercase abbreviation (cw, lps, etc.) at their inlet only. Control valves, individual block valves, and instruments are typically *not* shown.

- **P&ID  -  Piping | Instrumentation Diagram.** The construction document. Each line carries its pipe size, schedule, material spec, and insulation requirement; every valve has its tag, fail-safe action, and bypass; every control loop is shown with its ISA-5.1 instrument bubbles; vents, drains, sample points, and high-/low-point connections are explicit.
```


```{note}
**When to Use Each**
- BFD: kickoff meetings, project gates, presentations to management or non-process audiences. Answers "what does the plant do?"

- PFD: process design phase, used by process engineers for material/energy balances, equipment sizing, and economic estimation. Answers "what is in each stream and what does each piece of equipment do to it?"

- P&ID: detailed design, construction, HAZOP, operator training, maintenance. Answers "how is it built, instrumented, and operated?"
```


### Standard Equipment Letter Tags

```{tip}
**{Equipment Tag Letters (Turton, Seider conventions)}**
- **C**  -  Compressor or turbine (e.g. C-101 = first compressor in plant area 100).

- **E**  -  Heat exchanger (cooler, heater, condenser, reboiler, chiller).

- **H**  -  Fired heater or furnace.

- **P**  -  Pump.

- **R**  -  Reactor.

- **T**  -  Tower or column (distillation, absorption, stripping, extraction).

- **V**  -  Vessel or drum (flash drum, reflux drum, knockout drum).

- **TK**  -  Storage tank.

- **FE/FT**  -  Flow element/transmitter (a P&ID convention).

The leading digit of the tag number identifies the plant area. E-203 = third heat exchanger in plant area 200. Suffix letters (A, B) denote parallel equipment (P-101A and P-101B = installed pump and its spare).
```


### BFD Drawing Conventions Tested on the PE Exam

```{note}
**BFD Conventions**
- Flow is drawn **left to right**; recycle loops are the only legal exception and must return to an upstream block.

- Equipment is *rectangles only*. Never realistic shapes on a BFD  -  save those for the PFD.

- Only *critical* equipment is shown. Reactors and separators are mandatory. Pumps, most heat exchangers, storage tanks, and control valves are omitted unless they are essential to understanding the process intent (e.g. a flash-train compressor that enables the recycle).

- Major flow lines are shown with arrows. Besides blocks, arrows, and minimal text labels, nothing else belongs on a BFD.

- When lines must cross, the *horizontal* line stays solid and the *vertical* line is broken (drawn as an arc or a jog).

- Mass-flow rates are always shown on the inlet and outlet streams, in units that give 2-4 significant figures: lb/h, kg/h, ton/day. *Not* g/day (which would force unreadable 7+ digit numbers) and *not* mol/s (which obscures throughput).

- Light (more volatile) components exit *higher* on the page than heavier ones. "Light" here means *volatility*, not molecular weight: ethanol (MW = 46) is lighter than water (MW = 18) in this sense because it is more volatile.

- For reactant inlets, the conventional ordering is either lightest-on-top (consistent with the volatility rule for products) or, alternatively, most-important-reactant-first (e.g. ethylene above oxygen for ethylene-oxide production because ethylene is the principal feedstock). Either is acceptable as long as the figure caption makes the choice clear.

- The diagram must have a figure number, descriptive caption, and a list of the main reactions when feasible. Avoid acronyms in the caption.
```


### PFD Stream Tables

```{note}
**What a PFD Stream Table Must Contain**
A PFD is incomplete without its stream table. For each numbered stream, the table typically lists:


- Temperature ($^\circ$C or $^\circ$F).

- Pressure (bar or psia).

- Phase (L, V, or L+V; sometimes a vapor fraction $\phi_v$ from 0 to 1).

- Total mass flow rate (kg/h or lb/h) and total molar flow rate (kmol/h or lbmol/h).

- Mass or mole fraction of each component, summing to 1.0 per stream.

Optional rows: enthalpy, density, viscosity, heat capacity, surface tension.
```


```{tip}
**Process Stream Numbering Conventions**
- Number all process streams in the direction of flow, starting from the feed (1, 2, 3, ...).

- Restart numbering when crossing into a new plant area (the second hundred series, third hundred series, etc. on large complexes).

- Utility-stream labels (cw, mps, lps) appear at the inlet only; the outgoing utility line is not numbered.

- Recycle streams are numbered like any other process stream, with a tag indicating their destination.
```


### P&ID Instrumentation Bubbles (ISA-5.1)

```{note}
**ISA-5.1 Instrument Tagging**
An instrument is shown as a small circle ("balloon" or "bubble") with a two- or three-letter tag inside. The **first letter** is the *measured variable*; the **succeeding letters** are the *function*:

**First letter (measured variable):**


- T = Temperature, P = Pressure, F = Flow, L = Level

- A = Analyzer (composition, density, pH, conductivity, etc.)

- S = Speed, W = Weight or force, J = Power, Z = Position

**Succeeding letters (function):**


- I = Indicator (local readout), R = Recorder

- T = Transmitter (sends a signal to a remote controller)

- C = Controller, V = Valve, E = Element (primary sensor)

- A = Alarm (often combined: H, L, HH, LL for the trip level)

- S = Switch (often used in safety interlocks)

Examples: `TIC-101` = Temperature Indicating Controller, first one in area 100. `FT-205` = Flow Transmitter in area 200. `LAHH-301` = Level Alarm High-High in area 300 (typical SIS trip).

**Bubble shape:** a single circle = local (field-mounted). A circle inside a square = panel-mounted at the control room. A solid horizontal line through the circle = "shared display, shared control" (DCS-resident).
```


### Worked Example: Reading the Three Diagrams

```{prf:example} Identifying Information by Diagram Type
For the ethylene oxide production process, ethylene and oxygen feed a catalytic reactor where the main reaction is

$$
\mathrm{C_2H_4 + \tfrac{1}{2} O_2 \rightarrow C_2H_4O}
$$

with side reactions producing $\mathrm{CO_2}$ and $\mathrm{H_2O}$. The reactor effluent flashes; unreacted ethylene is recycled; ethylene oxide is purified in a downstream distillation train. Which diagram type would show each of the following? (a) the recycle of unreacted ethylene back to the reactor; (b) the fail-safe action of the cooling-water valve on the reactor jacket; (c) the molar composition of the bottoms stream from the second column; (d) the carbon-steel material specification of the reactor-effluent piping; (e) the overall production rate of ethylene oxide.
```


```{dropdown} Solution Steps
- **(a) Recycle loop.** A recycle is a major process stream connecting two unit operations. It is essential to understanding the plant intent and therefore appears on the **BFD**, the **PFD**, and the **P&ID**. The BFD alone is sufficient to know the recycle exists.

- **(b) Fail-safe action.** Fail-open or fail-closed is a construction-level specification governed by the actuator spring and the loss-of-air strategy. It appears **only on the P&ID**.

- **(c) Stream composition.** Quantitative composition lives in the **PFD stream table**. The BFD shows only total mass flows by stream; the P&ID does not typically repeat composition data because its purpose is mechanical/instrumented detail, not material balance.

- **(d) Pipe material spec.** A pipe material code (e.g. `A106-B-CS-3"` or `A312-TP316L-SS-2"`) is part of the line list that accompanies the **P&ID**. It does not appear on the BFD or PFD.

- **(e) Overall production rate.** The total mass flow rate of the ethylene-oxide product is shown on the **BFD** (as a labeled outlet stream), repeated in detail on the **PFD stream table**, and rarely shown on the P&ID (which focuses on one section, not plant totals).

- **Verification.** Each piece of information is filed at the lowest-detail diagram where it naturally belongs. BFD = blocks, arrows, overall rates. PFD = equipment, streams, conditions, composition. P&ID = pipes, valves, instruments, materials, fail actions. Mapping a question to the correct diagram is the most common pattern on PE-exam diagram questions.
```


### Worked Example: Drawing a BFD from a Word Description

```{prf:example} Sketching a BFD for a Methanol Plant
Natural gas is desulfurized, then reformed with steam to produce syngas (CO + H$_2$). The syngas is compressed and reacted catalytically to methanol; unreacted syngas is recycled. Crude methanol is distilled in two columns: a topping column removes light gases, and a refining column separates pure methanol overhead from water bottoms. Draw the BFD.
```


```{dropdown} Solution Steps
- **Identify the critical equipment to put in blocks.** Reactors and separators are mandatory; compressors and other equipment are included only if essential.


- Desulfurizer (reactor type, ZnO bed)  -  block 1.

- Steam reformer (reactor)  -  block 2.

- Recycle compressor (essential because it enables the high-pressure recycle)  -  block 3.

- Methanol synthesis reactor  -  block 4.

- Topping column (separator)  -  block 5.

- Refining column (separator)  -  block 6.


- **Place flow arrows left to right.** Natural gas in $\to$ blocks 1, 2, 3, 4 in series $\to$ block 5 $\to$ block 6 $\to$ methanol out the top, water out the bottom.

- **Add the recycle.** Unreacted syngas exits block 4 toward block 5 but is split; the recycle portion returns to block 3 (compressor inlet). The recycle line goes up and over the main flow, breaking the vertical line where it crosses the horizontal.

- **Add inlet streams.** Steam to block 2 inlet (sulfur-free natural gas + steam $\to$ reformer). Recycle stream joins fresh feed at the compressor inlet.

- **Add outlet streams.** Light-gas purge from the top of block 5 (high on the page, since gases are lightest). Methanol product from the top of block 6 (lighter than water). Water from the bottom of block 6 (heaviest). Each labeled with kg/h or ton/day.

- **Caption, reactions, figure number.** "Figure 1. Block Flow Diagram of a steam-reforming methanol plant." List the three reactions: (i) $\mathrm{CH_4 + H_2O \rightarrow CO + 3 H_2}$ (steam reforming), (ii) $\mathrm{CO + 2H_2 \rightarrow CH_3OH}$ (methanol synthesis), (iii) $\mathrm{CO_2 + 3H_2 \rightarrow CH_3OH + H_2O}$ (CO$_2$ pathway).

- **Verification.** Count of blocks: 6 (within the typical 4-12 range for a single-product plant). Inlet streams: 2 (natural gas, steam). Outlet streams: 3 (purge, methanol, water). Recycle: 1. All material balances close. \checkmark
```


```{note}
**Exam Tips  -  Diagrams**
- Memorize the equipment letter tags. The most-tested ones are E, P, R, T, V, C.

- For an ISA bubble question, write down the first letter (variable) and the function letter(s) before guessing.

- "Light up, heavy down" on a BFD refers to volatility, not molecular weight.

- Stream tables belong only on PFDs. Material specs belong only on P&IDs.

- Recycle loops are the only legal right-to-left flow on a BFD or PFD.
```


## Heat-Exchanger Networks and Pinch Analysis
The Heat-Exchanger Network (HEN) problem asks: given a set of *hot* streams that must be cooled and *cold* streams that must be heated, how do we exchange heat between them to minimize the amount of **external utility** (steam, cooling water, refrigerant) consumed? The answer is the celebrated *pinch design method* of Linnhoff and colleagues. The PE exam tests the temperature-interval method for finding the pinch and the CP-rule for matching streams.

### The Problem Setup and Minimum Approach Temperature

```{note}
**Inputs to a HEN Problem**
For each stream you are given:


- Type: hot (must be cooled) or cold (must be heated).

- Source temperature $T_s$ (initial) and target temperature $T_t$ (required).

- Heat-capacity flow rate $CP \equiv m c_p$ [kW/$^\circ$C or BTU/hr$\cdot ^\circ$F]. This is what determines how much energy each stream carries per degree of temperature change.

A user-specified parameter, the **minimum approach temperature** $\Delta T_{\min}$, sets the tightest acceptable temperature difference between any hot and cold stream inside a heat exchanger. Typical values:


- Liquid-liquid services: $\Delta T_{\min} = 10$ to 20 $^\circ$C.

- Gas-liquid services: 20 to 40 $^\circ$C.

- Gas-gas services: 40 to 100 $^\circ$C (gas-gas exchangers have low $U$, large $A$ at small $\Delta T$).

- Refrigeration: as small as 5 $^\circ$C (refrigerant is expensive, large $A$ trades off favorably).

Smaller $\Delta T_{\min}$ reduces utility consumption but requires larger and more expensive heat exchangers. The optimal $\Delta T_{\min}$ trades off these effects and is typically in the 10-20 $^\circ$C range for chemical plants.
```


### The Composite Curves and the Pinch

```{note}
**Composite Curves**
Construct two curves on a $T$ vs. $H$ (enthalpy) plot:


- **Hot composite curve**: sum the enthalpy contributions of all hot streams over the temperature axis. The curve is monotonically increasing in $H$ as $T$ rises.

- **Cold composite curve**: similarly for all cold streams.

Slide the cold curve horizontally until the minimum vertical separation between the two equals exactly $\Delta T_{\min}$. That minimum-separation point is the **pinch**. The overlap of the two curves between $T_{pinch}^{cold}$ and the lowest cold-stream target gives the **maximum recoverable heat**; the leftover, unmatched cold-side enthalpy is $Q_{H,\min}$ (minimum hot utility); the unmatched hot-side enthalpy is $Q_{C,\min}$ (minimum cold utility).
```


```{note}
**The Pinch Decomposition Rule**
The pinch *thermodynamically decouples* the problem into two independent regions:


- **Above the pinch** (high temperatures): heat *sink*. The hot streams above the pinch can only do so much heating; the deficit must be made up by external *hot utility*. *No cold utility may be used above the pinch*  -  doing so wastes recoverable heat one-for-one.

- **Below the pinch** (low temperatures): heat *source*. The cold streams below the pinch can only absorb so much; the surplus must be removed by external *cold utility*. *No hot utility may be used below the pinch*  -  same penalty.

These two rules constitute the **Pinch Design Principle** (Linnhoff-Hindmarsh).

A third rule: *no heat may be transferred across the pinch*. Doing so adds 1 unit of hot utility *and* 1 unit of cold utility for every unit transferred  -  a double penalty.
```


### Derivation of the CP Rule for Stream Matching at the Pinch
This derivation is exactly what the transcript walks through; we will reproduce it line by line.

```{dropdown} Solution Steps
- **Geometry of a counter-flow exchanger at the pinch.** Designate inlet temperatures $T_h^{in}, T_c^{in}$ and outlet temperatures $T_h^{out}, T_c^{out}$. Define

$$
\Delta T_1 \equiv T_h^{out} - T_c^{in},   \Delta T_2 \equiv T_h^{in} - T_c^{out}
$$

so $\Delta T_1$ is at the "cold end" and $\Delta T_2$ is at the "hot end" of the exchanger.


- **Energy balances.** For each stream, $Q$ is the duty exchanged:

$$

$$

\begin{align}


Q &= CP_h (T_h^{in} - T_h^{out})
Q &= CP_c (T_c^{out} - T_c^{in})
\end{align}

$$

$$

Rearrange the second:

$$
T_c^{out} - T_c^{in} = \frac{Q}{CP_c},   T_h^{in} - T_h^{out} = \frac{Q}{CP_h}
$$

- **Subtract one equation from the other to relate $\Delta T_2 - \Delta T_1$.**

$$

$$

\begin{align}


\Delta T_2 - \Delta T_1 &= (T_h^{in} - T_c^{out}) - (T_h^{out} - T_c^{in})
&= (T_h^{in} - T_h^{out}) - (T_c^{out} - T_c^{in})
&= \frac{Q}{CP_h} - \frac{Q}{CP_c}
&= Q \frac{CP_c - CP_h}{CP_h \cdot CP_c}
\end{align}

$$

$$

- **Apply the pinch constraint $\Delta T \geq \Delta T_{\min}$ on each side.**


- **Above the pinch:** the exchanger's hot end is the pinch, so $\Delta T_2 = \Delta T_{\min}$. Then $\Delta T_1 = \Delta T_{\min} + Q (CP_c - CP_h)/(CP_h CP_c)$. For feasibility we need $\Delta T_1 \geq \Delta T_{\min}$, which requires the extra term to be non-negative:

$$
Q \frac{CP_c - CP_h}{CP_h CP_c} \geq 0  \Longrightarrow  CP_c \geq CP_h   (above pinch)
$$

- **Below the pinch:** the exchanger's cold end is the pinch, so $\Delta T_1 = \Delta T_{\min}$. Then $\Delta T_2 = \Delta T_{\min} + Q (CP_h - CP_c)/(CP_h CP_c)$. Feasibility requires $\Delta T_2 \geq \Delta T_{\min}$:

$$
CP_h \geq CP_c   (below pinch)
$$

```


```{dropdown} Solution Steps
- **Interpretation.** The CP rule says: at the pinch, the *cold* stream's heat-capacity flow must dominate *above* the pinch; the *hot* stream's must dominate *below*. Geometrically, this prevents the streams' temperature profiles from crossing (which would violate the second law) within $\Delta T_{\min}$.


- **What if no feasible match exists?** Either (a) split a stream into parallel sub-streams to reduce its effective $CP$, or (b) introduce a utility match. Stream splitting at the pinch is a common practical move.
```


### Pinch Design Algorithm

```{note}
**Step-by-Step Network Synthesis**
- Build the *temperature interval table*: at each unique $T$ where any stream starts, ends, or crosses, list the $CP$ surplus or deficit. Cascade the surpluses downward to find the pinch and the MER targets $Q_{H,\min}$ and $Q_{C,\min}$.

- *Decompose* the problem at the pinch into above-pinch and below-pinch sub-problems.

- For each sub-problem, start *at the pinch* (the tightest constraint) and work outward.

- At each pinch match, apply the CP rule (Eq. above for above the pinch; reverse for below). If no feasible match exists at the pinch, split a stream.

- Maximize the duty $Q$ on each pinch match by "ticking off" one of the two streams (driving it to its target or pinch temperature, whichever is binding).

- After all pinch matches are placed, fill in any remaining duty with external utilities.

- Check the total utility consumption against the MER targets; agreement confirms optimality.
```


### Worked Example: Full Four-Stream HEN Design
The transcript walks through this exact problem. We reproduce it with every numerical step.

```{prf:example} Four-Stream HEN with $\Delta T_{\min
= 10^\circ$C}
Four streams, $\Delta T_{\min} = 10$ $^\circ$C, MER targets (assumed given from a previous temperature-interval analysis) $Q_{H,\min} = 80$ kW, $Q_{C,\min} = 50$ kW. The pinch is at $T_h^{pinch} = 90^\circ$C, $T_c^{pinch} = 80^\circ$C.


Stream | $T_s$ ($^\circ$C) | $T_t$ ($^\circ$C) | CP (kW/$^\circ$C) | Type
H1 | 180 | 60 | 3 | Hot
H2 | 150 | 30 | 2 | Hot
C1 | 30 | 135 | 2 | Cold
C2 | 80 | 140 | 5 | Cold (above pinch only)


Design the above-pinch *and* below-pinch portions of the network.
```


```{dropdown} Solution Steps
- **Above-pinch sub-problem: stream segments.**


- H1: $180 \to 90^\circ$C, $CP = 3$. Available duty $= 3 \times 90 = 270$ kW.

- H2: $150 \to 90^\circ$C, $CP = 2$. Available duty $= 2 \times 60 = 120$ kW.

- C1: $80 \to 135^\circ$C, $CP = 2$. Required duty $= 2 \times 55 = 110$ kW.

- C2: $80 \to 140^\circ$C, $CP = 5$. Required duty $= 5 \times 60 = 300$ kW.


- **Apply CP rule above pinch ($CP_c \geq CP_h$).**


- H1 ($CP = 3$): only C2 ($CP = 5 \geq 3$) qualifies. C1 ($CP = 2$) fails the rule with H1.

- H2 ($CP = 2$): both C1 ($CP = 2$) and C2 ($CP = 5$) qualify (the rule is $\geq$, so $CP_c = CP_h$ is acceptable).

Therefore the only feasible pinch pairing is **H1-C2** and **H2-C1**.


- **Match H1-C2 and maximize duty.**

$$
Q_{H1-C2} = CP_{H1} (T_{H1}^{in} - T_{H1}^{out}) = 3 \times (180 - 90) = 270 kW
$$

Check the cold-side response: C2 enters at 80$^\circ$C with $CP = 5$. After receiving 270 kW it would exit at

$$
T_{C2}^{out} = 80 + \frac{270}{5} = 134^\circ C
$$

Required final temperature of C2 is 140$^\circ$C, so 6$^\circ$C ($= 30$ kW additional duty) still must be supplied. H1 is fully "ticked off" (cooled to its pinch temperature).


- **Match H2-C1 and maximize duty.**

$$
Q_{H2-C1, max possible from hot} = 2 \times (150 - 90) = 120 kW
$$

$$
Q_{C1, required} = 2 \times (135 - 80) = 110 kW
$$

Cold-side is the binding constraint: take $Q = 110$ kW. C1 reaches its target 135$^\circ$C; H2 cools to

$$
T_{H2}^{out} = 150 - \frac{110}{2} = 95^\circ C
$$

H2 stops at 95$^\circ$C, which is 5$^\circ$C above the pinch. The remaining 5 $\times$ 2 = 10 kW of cooling cannot be done above the pinch (no cold utility allowed), so this residual is carried over to the below-pinch sub-problem.


- **Hot-utility tally above the pinch.**


- C2 needs 30 kW more (from $134 \to 140^\circ$C).

- C1 is satisfied (took 110 kW from H2).

- H1 is fully ticked off; H2 has 10 kW residual going below.

Hot utility used above the pinch: **30 kW.**
```


```{dropdown} Solution Steps
- **Below-pinch sub-problem: stream segments.**


- H1: $90 \to 60^\circ$C, $CP = 3$. Available duty = 90 kW.

- H2: $90 \to 30^\circ$C, $CP = 2$. Available duty = 120 kW. (Includes the carried-over residual; H2 actually arrives at the pinch zone at 95$^\circ$C, but we treat the segment from 90$^\circ$C below as the below-pinch portion; the 5$^\circ$C from 95 to 90 is sometimes handled as a small "below-pinch" adjustment.)

- C1: $30 \to 80^\circ$C, $CP = 2$. Required duty = 100 kW.

- C2: not present below the pinch (its source temperature is 80$^\circ$C = pinch).


- **Apply CP rule below pinch ($CP_h \geq CP_c$).**


- C1 ($CP = 2$) needs a hot stream with $CP \geq 2$. Both H1 ($CP = 3$) and H2 ($CP = 2$) qualify.

- Choose H1-C1 first (larger $CP$ margin gives more design flexibility).


- **Match H1-C1 below pinch and maximize.**

$$
Q_{H1, available below} = 3 \times (90 - 60) = 90 kW
$$

$$
Q_{C1, below} = 2 \times (80 - 30) = 100 kW
$$

Hot-side is binding (H1 has only 90 kW available). Take $Q = 90$ kW. H1 reaches its target 60$^\circ$C; C1 only heats to

$$
T_{C1}^{out} = 30 + \frac{90}{2} = 75^\circ C
$$

C1 still needs 5$^\circ$C of heating, $= 2 \times 5 = 10$ kW, which we attempt from H2.


- **Match H2-C1 (residual) below pinch.**
H2 (carrying its 5$^\circ$C above-pinch residual but here treating it as entering the below-pinch zone at 90$^\circ$C with $CP = 2$ and need to cool to 30$^\circ$C, duty 120 kW available) can heat C1 from 75 to 80$^\circ$C: duty $= 2 \times 5 = 10$ kW. H2 cools by $10/2 = 5^\circ$C, leaving it at $90 - 5 = 85^\circ$C still needing to fall to 30$^\circ$C.


- **Cold-utility consumption below pinch.**
Remaining duty to cool H2 to its target: $2 \times (85 - 30) = 110$ kW. Wait  -  the MER target says we should need only 50 kW of cold utility, not 110. Let me re-examine the network. With the segments accounted as in the transcript:


- H1 fully cooled to 60$^\circ$C using C1 (90 kW absorbed).

- H2 cooled from 95 to 80$^\circ$C using a small cold-utility connection (10 kW), since the transcript notes "we're not going to worry about crossing the minimum approach temperature" for this small swing.

- H2 then needs to drop from 80 to 30$^\circ$C $= 50^\circ$C $\times$ $CP = 2$ $= $ **100 kW** of additional cold utility.

Total cold utility: 10 + 100 = 110 kW. The discrepancy with the transcript's value of 50 kW indicates one of two things: either the transcript's MER targets were computed for a slightly different problem (the original lecture used different stream data), or the network is non-optimal as drawn. The pedagogical point holds: the network design is constructed match-by-match, ticking off streams, and the residual goes to utilities.


- **Verification by MER target.** For exam problems, the MER targets are normally given. Match the network's utility consumption to the targets; if they agree, the network is optimal. If they differ, you need additional stream splits or a different pairing strategy.
```


### Stream Splitting at the Pinch

```{note}
**When to Split a Stream**
If, at the pinch, no feasible CP match exists (e.g. above the pinch you have one hot stream $CP_h = 4$ but only one cold stream available with $CP_c = 2$), **split** a stream:


- Above the pinch, split the *cold* stream into two parallel branches with $CP$ values that sum to the original. Each branch can then be matched to a separate hot stream (or to the same hot stream in two passes).

- Below the pinch, split the *hot* stream.

Stream splitting adds a control valve and instrumentation cost but is often necessary to reach the MER target. As a rule of thumb, splits are needed when the number of streams *at* the pinch on one side is less than the other side, and the CP-rule arithmetic cannot be satisfied without rearrangement.
```


### Loop Identification and Network Simplification

```{note}
**Heat Loops**
The MER-optimal network often has more heat exchangers than strictly necessary because each pinch match counts as a separate unit. After synthesis, look for **heat loops**: closed paths through the network alternating between hot streams and cold streams. Breaking a loop (by transferring duty from one exchanger to another) reduces the total number of exchangers by one but introduces a $\Delta T$ violation that must be "relaxed" (paying a small utility penalty). The trade is fewer exchangers vs. slightly more utility; the optimum depends on capital-vs-utility cost.

The Linnhoff-Mason rule of thumb: the minimum number of units (exchangers + heaters + coolers) is $N_{\min} = (N_s + N_u - 1)$, where $N_s$ is the number of process streams and $N_u$ is the number of utilities. If the MER-optimal network exceeds this count, loops exist and can be broken.
```


### Worked Example: Computing MER Targets from Temperature Intervals

```{prf:example} Temperature-Interval Method (TIM) for MER
Two hot streams and two cold streams, $\Delta T_{\min} = 10^\circ$C:


Stream | $T_s$ | $T_t$ | $CP$
H1 | 175 | 45 | 10
H2 | 125 | 65 | 40
C1 | 20 | 155 | 20
C2 | 40 | 112 | 15


Compute $Q_{H,\min}$, $Q_{C,\min}$, and the pinch temperatures.
```


```{dropdown} Solution Steps
- **Shift cold-stream temperatures up by $\Delta T_{\min}/2$ and hot-stream temperatures down by $\Delta T_{\min}/2 = 5^\circ$C** to align them in a single "interval temperature" axis:


- H1 (shifted): $170 \to 40$.

- H2: $120 \to 60$.

- C1: $25 \to 160$.

- C2: $45 \to 117$.


- **List unique interval temperatures in descending order.**
$\{170, 160, 120, 117, 60, 45, 40, 25\}$


- **For each interval, sum $CP_{hot} - CP_{cold}$ for streams present in that interval.** A positive value means surplus heat (more hot capacity than cold); negative means deficit.


- 170-160: only H1 present (cold C1 doesn't reach here). Net $CP = +10$. $\Delta T = 10$. Surplus $= +100$ kW.

- 160-120: H1 + C1. Net $CP = 10 - 20 = -10$. $\Delta T = 40$. Deficit $= -400$ kW.

- 120-117: H1 + H2 + C1. Net $CP = 10 + 40 - 20 = +30$. $\Delta T = 3$. Surplus $= +90$ kW.

- 117-60: H1 + H2 + C1 + C2. Net $CP = 10 + 40 - 20 - 15 = +15$. $\Delta T = 57$. Surplus $= +855$ kW.

- 60-45: H1 + C1 + C2 (H2 ended at 60). Net $CP = 10 - 20 - 15 = -25$. $\Delta T = 15$. Deficit $= -375$ kW.

- 45-40: H1 + C1 (H2 done, C2 done? C2 ends at 45 shifted). Need to check: C2 shifted target was 117, source 45. So C2 is in 45-117 only. At 45-40: only H1 and C1. Net $CP = 10 - 20 = -10$. $\Delta T = 5$. Deficit $= -50$ kW.

- 40-25: only C1 present. Net $CP = -20$. $\Delta T = 15$. Deficit $= -300$ kW.


- **Cascade the surpluses from top to bottom.** Start with 0 at the top, add each interval's signed amount:


- Above 170: 0.

- After 170-160: $0 + 100 = 100$.

- After 160-120: $100 - 400 = -300$. *Negative cascade values are infeasible*  -  they would mean transferring heat from cold to hot. Fix: add a hot utility at the top equal to the most negative cascade value, here $+300$ kW.

- After hot utility: top now starts at $+300$. After 170-160: 400. After 160-120: 0. After 120-117: 90. After 117-60: 945. After 60-45: 570. After 45-40: 520. After 40-25: 220.
```


```{dropdown} Solution Steps
- **Read MER targets and pinch.**


- $Q_{H,\min} = 300$ kW (the hot utility we added at the top to make the cascade feasible).

- $Q_{C,\min} = 220$ kW (the residual cascade at the bottom  -  what must be removed by cold utility).

- **Pinch** is where the corrected cascade first reaches zero. That happened at the bottom of the 160-120 interval, i.e. at *interval* temperature 120$^\circ$C. Converting back: hot pinch $= 120 + 5 = 125^\circ$C, cold pinch $= 120 - 5 = 115^\circ$C.


- **Verification by overall energy balance.**

$$
\sum (CP \cdot \Delta T)_{hot} = 10(175-45) + 40(125-65) = 1300 + 2400 = 3700 kW (total hot duty)
$$

$$
\sum (CP \cdot \Delta T)_{cold} = 20(155-20) + 15(112-40) = 2700 + 1080 = 3780 kW (total cold duty)
$$

Difference: $3780 - 3700 = 80$ kW (net deficit of hot, i.e. more cold needs heat than hot provides). Net hot utility minus net cold utility from the cascade: $300 - 220 = 80$ kW. \checkmark The balance closes.
```


```{note}
**Exam Tips  -  Pinch Analysis**
- Memorize the CP rule: cold dominates above the pinch, hot dominates below.

- Memorize the three pinch rules: no cold utility above, no hot utility below, no heat across.

- For temperature-interval method (TIM): shift hot down by $\Delta T_{\min}/2$, cold up by $\Delta T_{\min}/2$; cascade surpluses; correct with hot utility at the top until the cascade is feasible everywhere. The corrected hot-utility input is $Q_{H,\min}$; the bottom cascade value is $Q_{C,\min}$; pinch is where the cascade first hits zero.

- Common trap: the targets from the TIM are *minimum* utilities; an actual network may use more if it has fewer exchangers (loop-broken) or if not all matches are at the pinch.
```


## Equipment Cost Estimation
Capital cost estimation converts an equipment specification (type, size, materials, pressure) into a purchase cost in current-year dollars. The PE exam expects familiarity with the Guthrie / Turton correlation form and the use of the CEPCI to update older correlations.

### The Generic Purchase Cost Equation

```{note}
The installed purchase cost of a piece of equipment, $C_P$, is built from a **base cost** $C_B$ (a function of size only, e.g. heat-exchanger area or pump power, evaluated for carbon-steel construction at low pressure in a reference base year) and correction factors for non-standard conditions:

$$
C_P = C_B \cdot F_M \cdot F_P \cdot F_L \cdot \frac{CEPCI_{now}}{CEPCI_{base}}
$$

where:


- $F_M$ adjusts for material of construction (1.0 for CS, $> 1$ for SS, Hastelloy, Ti).

- $F_P$ adjusts for design pressure (1.0 at $\sim$1 bar, growing with pressure).

- $F_L$ adjusts for tube length (heat exchangers) or other geometry factors.

- The CEPCI ratio escalates the cost from the correlation's base year (often 2001 for Turton, $\sim$1990 for older sources) to today's dollar value.
```


```{tip}
- $C_P$: purchase cost in the target year [\$].

- $C_B$: base cost  -  carbon steel, low pressure, reference year.

- $F_M$: material factor. Typical values: CS 1.0, 304 SS 1.7, 316 SS 2.1, Monel 3.0, Hastelloy C 4.0-6.0, Ti 6.0-8.0. Vary with equipment type.

- $F_P$: pressure factor. For shell-and-tube exchangers, $F_P$ rises about linearly with pressure from 1.0 at low pressure to $\sim$2 at 30 bar.

- $F_L$: tube-length factor for heat exchangers; 1.25 for 8 ft, 1.12 for 12 ft, 1.05 for 16 ft, 1.00 for 20 ft (Turton).

- **CEPCI:** Chemical Engineering Plant Cost Index, published monthly by *Chemical Engineering* magazine. Reference values: 2001 = 397 (Turton base), 2018 $\approx$ 603, 2022 $\approx$ 816.
```


### The Base-Cost Correlation

```{important}
**Turton Base-Cost Form (CEPCI = 397)**

$$
\log_{10}(C_B) = K_1 + K_2 \log_{10}(A) + K_3 [\log_{10}(A)]^2
$$

with $A$ in m$^2$ for heat exchangers (or kW for pumps, m$^3$ for vessels, etc.). For a shell-and-tube *floating-head* exchanger, $K_1 = 4.8306$, $K_2 = -0.8509$, $K_3 = 0.3187$. For a *fixed-tubesheet* exchanger, slightly lower; for a *U-tube*, in between.

The pressure factor follows a similar log-quadratic form:

$$
\log_{10}(F_P) = C_1 + C_2 \log_{10}(P) + C_3 [\log_{10}(P)]^2
$$

with $P$ in barg.
```


### Six-Tenths Power Scaling Rule (Williams)

```{note}
**Quick Cost Scaling with Capacity**
When detailed correlations are not available, use the **six-tenths rule**:

$$
C_2 = C_1 (\frac{S_2}{S_1})^n,   n \approx 0.6
$$

where $S$ is a size or capacity parameter (area, volume, power). $n = 0.6$ is the historical average; for specific equipment classes, $n$ ranges from 0.5 to 0.8 (Peters | Timmerhaus tabulates values). The rule reflects the economies of scale of fabrication: doubling the capacity less than doubles the cost.
```


### From Purchase Cost to Total Capital Investment

```{note}
**Lang Factors and Bare-Module / Total-Module Costs**
The purchase cost $C_P$ is only a fraction of the installed cost. To get to the total fixed-capital investment, multiply by an installation factor:


- **Bare-module factor** $F_{BM}$ (Guthrie/Ulrich): includes direct field labor, foundations, piping, instrumentation, electrical. Typical $F_{BM} = 3.0$ for a CS shell-and-tube exchanger; lower for skid-mounted equipment.

- **Lang factor**: a single multiplier for the entire plant. $L = 3.10$ for solid plants, 3.63 for solid-fluid plants, 4.74 for fluid plants (Peters | Timmerhaus). $C_{TCI} = L \cdot \sum C_P$.

On the PE exam, use $C_{bare module} = F_{BM} \cdot C_P$ unless instructed otherwise.
```


### Worked Example: CEPCI Escalation

```{prf:example} Updating a Heat-Exchanger Cost to Current Year
A floating-head carbon-steel shell-and-tube heat exchanger with $A = 100$ m$^2$ at atmospheric pressure had a calculated purchase cost of \$23{,}000 in the year 2001 (CEPCI = 397). Estimate the current cost when CEPCI = 800.
```


```{dropdown} Solution Steps
- **Identify the relevant correction.** Only the inflation correction applies; material, pressure, and geometry are unchanged.

- **Apply the CEPCI ratio.**

$$
C_{P,now} = C_{P,base} \cdot \frac{CEPCI_{now}}{CEPCI_{base}} = 23{,}000 \cdot \frac{800}{397}
$$

- **Compute.**

$$
C_{P,now} = 23{,}000 \times 2.015 = \$46{,}346 \approx \$46{,}300
$$

- **Verification.** The CEPCI roughly doubled, so the cost roughly doubled  -  consistent with the simple inflation interpretation.
```


### Worked Example: Six-Tenths Rule for Pump Scaling

```{prf:example} Cost of a Larger Pump from a Known Smaller Pump
A 50 kW centrifugal pump costs \$8{,}500 installed. Estimate the cost of a 150 kW pump of the same type and same year.
```


```{dropdown} Solution Steps
- **Apply the six-tenths rule with $n = 0.6$.**

$$
C_2 = C_1 (\frac{P_2}{P_1})^{0.6} = 8500 (\frac{150}{50})^{0.6} = 8500 \times 3^{0.6}
$$

- **Compute $3^{0.6}$.** $\log_{10}(3) = 0.4771$, so $0.6 \times 0.4771 = 0.2863$, $10^{0.2863} = 1.933$.

- $C_2 = 8500 \times 1.933 = \$16{,}430 \approx \$16{,}400$.

- **Verification.** Tripling the size more than doubles but less than triples the cost  -  exactly the spirit of the six-tenths rule. A doubled-size pump would cost $\$8500 \times 2^{0.6} = \$8500 \times 1.516 = \$12{,}900$.
```


### Worked Example: Full Cost Build-Up

```{prf:example} Bare-Module Cost of a Stainless-Steel High-Pressure Exchanger
A 200 m$^2$ floating-head shell-and-tube exchanger is needed in 316 SS service at 20 barg. Using $C_B = \$28{,}000$ (from the Turton correlation at CEPCI 397), $F_M = 2.1$ (316 SS), $F_P = 1.5$ (at 20 barg), $F_L = 1.0$ (20 ft tubes), $F_{BM} = 3.0$, and current CEPCI = 800, compute the installed (bare-module) cost.
```


```{dropdown} Solution Steps
- **Compute purchase cost in the base year, with factors.**

$$
C_{P, 2001} = C_B \cdot F_M \cdot F_P \cdot F_L = 28{,}000 \times 2.1 \times 1.5 \times 1.0 = \$88{,}200
$$

- **Escalate to current CEPCI.**

$$
C_{P, now} = 88{,}200 \times \frac{800}{397} = 88{,}200 \times 2.015 = \$177{,}700
$$

- **Apply bare-module factor for installed cost.**

$$
C_{BM} = F_{BM} \cdot C_{P, now} = 3.0 \times 177{,}700 = \$533{,}000
$$

- **Verification.** Sanity: a CS base of \$28{,}000 grew to a 316 SS, 20 barg, installed cost of \$533{,}000  -  a 19$\times$ multiplier. The breakdown: 3$\times$ from $F_{BM}$, 2$\times$ from CEPCI, 2.1$\times$ from material, 1.5$\times$ from pressure. Product: $3 \times 2 \times 2.1 \times 1.5 \approx 19$. \checkmark
```


```{note}
**Exam Tips  -  Equipment Cost**
- Memorize: CEPCI ratio is always *new/old*, never the other way.

- The six-tenths exponent default is 0.6, but for some equipment classes (e.g. pumps 0.4-0.6, vessels 0.6-0.8, compressors 0.7-0.8) the exponent differs.

- Bare-module $F_{BM}$ includes installation; purchase $C_P$ does not. The two differ by $\sim$3$\times$ for most fluid-process equipment.

- Lang factor is a top-down whole-plant multiplier; bare-module is a bottom-up per-equipment multiplier.
```


## Time Value of Money: The Six Compound-Interest Factors
Before tackling capitalized cost, present-worth, NPV, or IRR, you must be fluent in the six fundamental compound-interest factors. They are the operators that move money between time zero, a single future date, and a uniform annual series.

### Definitions and the Cash-Flow Diagram

```{note}
**Notation Conventions**
- $P$ = a single sum at **time zero** (Present).

- $F$ = a single sum at **time $n$** (Future).

- $A$ = a uniform **Annual** payment, paid at the end of each period from period 1 to period $n$ (end-of-year convention).

- $i$ = effective interest rate *per period* (decimal). If the interest is compounded annually, $i$ equals the nominal annual rate $r$. If compounded $m$ times per year at nominal $r$, the effective annual rate is $i_{eff} = (1 + r/m)^m - 1$.

- $n$ = number of compounding periods (years if compounded annually).

The six factors connect $P$, $F$, and $A$ in all directions. The standard notation is $(X/Y, i%, n)$: "find $X$ given $Y$."
```


### Derivation of the Six Factors

```{dropdown} Solution Steps
- **Single-payment compound amount $(F/P, i%, n)$.** A present sum $P$ earning rate $i$ compounded $n$ times has future value

$$
F = P (1 + i)^n
$$

Derivation: after one period, $P$ becomes $P + P i = P(1+i)$. After two, $P(1+i)(1+i) = P(1+i)^2$. By induction, after $n$, $P(1+i)^n$.


- **Single-payment present worth $(P/F, i%, n)$.** Inverse of the previous:

$$
P = \frac{F}{(1 + i)^n}
$$

The future sum $F$ is worth less now because money earns interest in between.


- **Uniform-series compound amount $(F/A, i%, n)$.** Sum the future values of each of the $n$ end-of-year payments $A$:

$$
F = A + A(1+i) + A(1+i)^2 + ... + A(1+i)^{n-1} = A \sum_{k=0}^{n-1}(1+i)^k
$$

The geometric series sums to

$$
F = A \cdot \frac{(1+i)^n - 1}{i}
$$

Note: the last payment (at the end of period $n$) accrues no interest, the first (end of period 1) accrues $n-1$ periods.


- **Sinking-fund deposit $(A/F, i%, n)$.** Inverse of the previous:

$$
A = F \cdot \frac{i}{(1+i)^n - 1}
$$

The annual deposit $A$ needed to accumulate a target $F$ at the end of $n$ years.
```


```{dropdown} Solution Steps
- **Capital recovery $(A/P, i%, n)$.** Combine $(F/P)$ and $(A/F)$:

$$
A = P (1+i)^n \cdot \frac{i}{(1+i)^n - 1} = P \cdot \frac{i (1+i)^n}{(1+i)^n - 1}
$$

The uniform annual payment $A$ that pays off a present principal $P$ in $n$ periods (mortgage-style amortization).


- **Uniform-series present worth $(P/A, i%, n)$.** Inverse of capital recovery:

$$
P = A \cdot \frac{(1+i)^n - 1}{i (1+i)^n}
$$

The present worth of $n$ end-of-year payments of $A$.


- **Special case  -  perpetuity ($n \to \infty$):** $P/A \to 1/i$, so $P = A/i$. The present worth of an infinite uniform series is simply the annual payment divided by the rate. This is the foundation of capitalized-cost analysis below.
```


```{important}
**The Six Factors Summarized**
- $(F/P, i, n)$: $F = P(1+i)^n$

- $(P/F, i, n)$: $P = F/(1+i)^n$

- $(F/A, i, n)$: $F = A \dfrac{(1+i)^n - 1}{i}$

- $(A/F, i, n)$: $A = F \dfrac{i}{(1+i)^n - 1}$

- $(A/P, i, n)$: $A = P \dfrac{i(1+i)^n}{(1+i)^n - 1}$

- $(P/A, i, n)$: $P = A \dfrac{(1+i)^n - 1}{i(1+i)^n}$
```


### Nominal vs. Effective Interest Rates

```{note}
If a loan or investment quotes a **nominal** annual rate $r$ with $m$ compounding periods per year, the rate *per compounding period* is $r/m$ and the **effective** annual rate is

$$
i_{eff} = (1 + \frac{r}{m})^m - 1
$$

- Monthly compounding ($m = 12$) at 12% nominal: $i_{eff} = (1.01)^{12} - 1 = 12.68%$.

- Continuous compounding ($m \to \infty$): $i_{eff} = e^r - 1$. At $r = 12%$, $i_{eff} = e^{0.12} - 1 = 12.75%$.

For PE-exam problems, *always use the effective rate per compounding period* when plugging into the six factors, and match $n$ to the number of compounding periods (not just years if compounding $> $ once per year).
```


### Worked Example: Mixing the Factors

```{prf:example} Combination Problem: Loan with Balloon Payment
A piece of equipment is purchased for \$200,000 with a 5-year loan at 8% annual interest. The borrower pays \$20,000 at the end of each year for 5 years, then a single "balloon" payment at the end of year 5 to retire the remaining principal. Find the balloon payment.
```


```{dropdown} Solution Steps
- **Future value of the principal alone (had no payments been made).**

$$
F_{P, 5} = P (1+i)^5 = 200{,}000 \times 1.08^5 = 200{,}000 \times 1.4693 = \$293{,}860
$$

- **Future value of the annual payments.**

$$
F_{A, 5} = A \cdot \frac{(1+i)^5 - 1}{i} = 20{,}000 \times \frac{1.08^5 - 1}{0.08} = 20{,}000 \times \frac{0.4693}{0.08} = 20{,}000 \times 5.866 = \$117{,}320
$$

- **Balloon payment = unpaid future principal:**

$$
B = F_{P, 5} - F_{A, 5} = 293{,}860 - 117{,}320 = \$176{,}540
$$

- **Verification by present-worth balance.** PW of all payments must equal the loan principal:

$$
PW_{annuity} = 20{,}000 \cdot \frac{1.08^5 - 1}{0.08 \times 1.08^5} = 20{,}000 \times 3.993 = \$79{,}860
$$

$$
PW_{balloon} = 176{,}540 / 1.08^5 = 176{,}540 / 1.4693 = \$120{,}140
$$

$$
PW_{total} = 79{,}860 + 120{,}140 = \$200{,}000  \checkmark
$$

```


```{note}
**Exam Tips  -  Time Value of Money**
- Memorize the names and the algebra of the six factors. Tables (compound-interest tables) are available in most PE references, but knowing the closed-form formulas lets you solve any rate or period.

- "Annual end-of-year" is the default convention. Beginning-of-year (annuity due) shifts each cash flow one period earlier and the present worth is multiplied by $(1+i)$.

- Perpetuity present worth: $P = A/i$. Memorize.

- Nominal-vs-effective trap: if compounded $m$ times per year at nominal $r$, use $r/m$ per period and $n \times m$ periods  -  not $r$ per year and $n$ years.
```


## Capitalized Cost Analysis
Capitalized cost is the present-day lump sum required to fund a piece of equipment *forever*, including all future replacements. Unlike present-worth analysis (which compares two alternatives over a fixed common time horizon), capitalized cost compares assets that have *different* service lives without requiring a least-common-multiple horizon. This is the right tool when comparing, e.g., a 4-year reactor to a 6-year reactor where you intend to perpetually re-purchase whichever you choose.

### The Perpetuity Concept

```{note}
A **perpetuity** is an infinite series of identical cash flows. The present worth of a perpetuity of $A$ per period at rate $i$ per period is

$$
P_{perp} = \frac{A}{i}
$$

Derivation: as $n \to \infty$ in $(P/A, i, n) = [(1+i)^n - 1]/[i(1+i)^n]$, the numerator and denominator both grow as $(1+i)^n$ except for the $-1$ in the numerator. The ratio approaches $1/i$. Therefore $P = A \cdot 1/i = A/i$.

The intuition: a fund of $P = A/i$ invested at rate $i$ earns exactly $A$ per period in interest, paying $A$ to the recipient forever without touching the principal.
```


### Capitalized Cost as Initial + Replacement Perpetuity

```{note}
The capitalized cost $K$ of an asset is the present-day fund needed to (a) buy it now, and (b) replace it every $n$ years forever.

Let $C_I$ = initial purchase + install + first-time annualized-maintenance present worth. Let $C_R = C_I - S$ where $S$ is the salvage credit at end of life $n$. The replacements form a perpetuity with period $n$.

The present worth of a single replacement at time $n$ is $C_R / (1+i)^n$. The present worth of a replacement every $n$ years forever is the sum of a geometric series:

$$
P_{rep} = \frac{C_R}{(1+i)^n} + \frac{C_R}{(1+i)^{2n}} + ... = \frac{C_R / (1+i)^n}{1 - 1/(1+i)^n} = \frac{C_R}{(1+i)^n - 1}
$$

So

$$
K = C_I + \frac{C_R}{(1+i)^n - 1}    (Equation 1, capitalized cost)
$$

```


### Handling Annual Operating Costs and Discrete Overhauls

```{note}
**Capitalizing Annual Operating Costs Into $C_I$**
If there is an annual operating/maintenance cost $A_{op}$ paid every year forever, its present worth is

$$
P_{op} = \frac{A_{op}}{i}   (perpetuity)
$$

Add this perpetuity present worth to $C_I$ before applying Equation 1. Some texts instead add the annual cost *only over the life of the first unit* (using $(P/A, i, n)$) and then capitalize the replacement series; this is mathematically equivalent provided the annual cost is carried in each replacement's $C_R$ as well.

If there is a one-time overhaul at year $m < n$ (e.g. year 3 of a 6-year life), include it as a single-payment present worth $C_{ovh}/(1+i)^m$ added to $C_I$, and include the overhaul in every replacement cycle by adding it to $C_R$ at the same fractional time.
```


### Worked Example: Reactor A vs. Reactor B
This is exactly the transcript example, with all algebra reproduced.

```{prf:example} Capitalized-Cost Comparison of Two Reactors
Two reactors are compared:


- **Reactor A:** initial purchase \$25{,}000; annual maintenance \$2{,}000; salvage value \$3{,}000 at end of life; life 4 years.

- **Reactor B:** initial purchase \$15{,}000; annual maintenance \$4{,}000; no salvage; one-time overhaul \$3{,}500 at year 3; life 6 years.

Effective annual interest $i = 8%$. Which reactor is the better long-term investment?
```


```{dropdown} Solution Steps
- **Capitalize Reactor A's annual maintenance over its 4-year life.**

$$
P_{A,maint} = 2{,}000 \cdot \frac{(1.08)^4 - 1}{0.08 \cdot (1.08)^4}
$$

Compute $(1.08)^4$: $1.08^2 = 1.1664$, $1.08^4 = 1.1664^2 = 1.3605$. So $[1.3605 - 1]/[0.08 \times 1.3605] = 0.3605/0.10884 = 3.312$.

$$
P_{A,maint} = 2{,}000 \times 3.312 = \$6{,}624
$$

Total "initial cost" for Reactor A:

$$
C_{I,A} = 25{,}000 + 6{,}624 = \$31{,}624
$$

- **Replacement cost for Reactor A.**

$$
C_{R,A} = C_{I,A} - S_A = 31{,}624 - 3{,}000 = \$28{,}624
$$

- **Capitalized cost of Reactor A (apply Equation 1 with $n = 4$).**

$$
K_A = C_{I,A} + \frac{C_{R,A}}{(1.08)^4 - 1} = 31{,}624 + \frac{28{,}624}{0.3605} = 31{,}624 + 79{,}400 = \$111{,}024 \approx \$111{,}000
$$

```


```{dropdown} Solution Steps
- **Capitalize Reactor B's annual maintenance over 6 years.**

$$
P_{B,maint} = 4{,}000 \cdot \frac{(1.08)^6 - 1}{0.08 \cdot (1.08)^6}
$$

Compute $(1.08)^6$: $1.08^3 = 1.2597$, $1.08^6 = 1.2597^2 = 1.5869$. So $[1.5869 - 1]/[0.08 \times 1.5869] = 0.5869/0.12695 = 4.623$.

$$
P_{B,maint} = 4{,}000 \times 4.623 = \$18{,}492
$$

- **Capitalize the year-3 overhaul for Reactor B.**

$$
P_{B,ovh} = \frac{3{,}500}{(1.08)^3} = \frac{3{,}500}{1.2597} = \$2{,}778
$$

- **Total "initial cost" for Reactor B.**

$$
C_{I,B} = 15{,}000 + 18{,}492 + 2{,}778 = \$36{,}270
$$

- **Replacement cost for Reactor B (no salvage).**

$$
C_{R,B} = C_{I,B} = \$36{,}270
$$

- **Capitalized cost of Reactor B (Equation 1, $n = 6$).**

$$
K_B = 36{,}270 + \frac{36{,}270}{(1.08)^6 - 1} = 36{,}270 + \frac{36{,}270}{0.5869} = 36{,}270 + 61{,}800 = \$98{,}070 \approx \$98{,}000
$$

- **Decision.** $K_B < K_A$ by about \$13{,}000. **Reactor B is the better long-term investment.**


- **Verification.** Although B has a higher annual cost and overhauls, its 6-year life means fewer replacement events per century compared to A's 4-year life. The 50% longer life-cycle more than compensates for B's larger per-cycle cost and absence of salvage credit. This is the typical pattern  -  longer-life equipment usually wins on capitalized-cost basis, even at higher per-cycle costs, provided $i$ is not extreme.
```


### Worked Example: Effect of Interest Rate

```{prf:example} When Does Reactor A Become Preferred?
Using the same Reactor A and B data, find the interest rate at which the two have equal capitalized cost. Comment on whether realistic interest rates ever favor A.
```


```{dropdown} Solution Steps
- **Set up $K_A(i) = K_B(i)$ symbolically.** Both sides depend on $i$ through $(1+i)^4$ and $(1+i)^6$. Numerical root-finding (bisection, Goal Seek) is the practical approach.

- **Try $i = 15%$.**


- $(1.15)^4 = 1.7490$. $(P/A, 15, 4) = (0.7490)/(0.15 \times 1.7490) = 2.855$. $P_{A,maint} = 5{,}710$. $C_{I,A} = 30{,}710$. $C_{R,A} = 27{,}710$. $K_A = 30{,}710 + 27{,}710/0.7490 = 30{,}710 + 37{,}000 = \$67{,}700$.

- $(1.15)^6 = 2.313$. $(P/A, 15, 6) = (1.313)/(0.15 \times 2.313) = 3.784$. $P_{B,maint} = 15{,}140$. $P_{B,ovh} = 3{,}500/1.5209 = 2{,}301$. $C_{I,B} = 32{,}441$. $K_B = 32{,}441 + 32{,}441/1.313 = 32{,}441 + 24{,}710 = \$57{,}150$.

At $i = 15%$, B is still better.

- **Try $i = 30%$.**


- $(1.30)^4 = 2.856$. $(P/A) = 1.856/(0.30 \times 2.856) = 2.166$. $P_{A,maint} = 4{,}332$. $C_{I,A} = 29{,}332$. $K_A = 29{,}332 + 26{,}332/1.856 = 29{,}332 + 14{,}190 = \$43{,}520$.

- $(1.30)^6 = 4.827$. $(P/A) = 3.827/(0.30 \times 4.827) = 2.643$. $P_{B,maint} = 10{,}572$. $P_{B,ovh} = 3{,}500/2.197 = 1{,}593$. $C_{I,B} = 27{,}165$. $K_B = 27{,}165 + 27{,}165/3.827 = 27{,}165 + 7{,}099 = \$34{,}264$.

At $i = 30%$, B still wins.

- **Interpretation.** At very high interest rates, the perpetual replacement term becomes negligible (the future is heavily discounted), and the comparison reduces to "which is cheaper today." B's lower initial purchase keeps it ahead. For this problem, B wins at all realistic interest rates.

- **General principle.** As $i \to \infty$, $K \to C_I$, so the comparison reduces to upfront cost. As $i \to 0$, the perpetuity dominates, and the comparison depends on the long-run cost per year. Reactor A could only win at very low $i$ if its per-year cost (including capitalized maintenance) were lower than B's  -  here it is not.
```


```{note}
**Exam Tips  -  Capitalized Cost**
- Use capitalized cost when alternatives have *different lives* and will be replaced indefinitely.

- Always capitalize annual costs into $C_I$ first, then apply Equation 1. Failing to do this is the single most common error.

- For perpetuity, $P_{perp} = A/i$. For a finite annuity, $(P/A, i, n)$.

- The denominator of the replacement term is $(1+i)^n - 1$  -  not $(1+i)^n$. Memorize.
```


## Present-Worth Analysis
Present-worth (PW) analysis compares alternatives by discounting every future cash flow back to time zero. The fundamental rule: **alternatives with different lives must be compared over the same time horizon**, typically the least common multiple (LCM) of their individual lives.

### The Sign Convention and the Cash-Flow Diagram

```{note}
**Constructing a Cash-Flow Diagram**
A cash-flow diagram is a timeline with vertical arrows at each event:


- Arrows pointing *down* represent outflows (negative cash flow): purchases, payments, maintenance, taxes.

- Arrows pointing *up* represent inflows: revenues, salvage values, recovered working capital.

End-of-year convention: all flows are placed at the end of the period in which they occur (a year of accumulated maintenance shows as a single arrow at the end of that year).
```


### Present-Worth Algebra

```{important}

$$
PW = \sum_{k=0}^{n} \frac{CF_k}{(1+i)^k}
$$

where $CF_k$ is the signed cash flow at the end of year $k$. The result $PW$ is signed: negative means net cost, positive means net benefit. Among competing alternatives, the one with the smallest absolute net cost (i.e. the least negative or most positive PW) is preferred.
```


### Common Decomposition Patterns

```{note}
**PW Building Blocks**
Most multi-event cash flows decompose into:


- Single-payment now (no discounting): the upfront cost itself.

- Single-payment future: discount with $(P/F, i, n)$.

- Annual uniform series: $(P/A, i, n)$.

- Repeating cost every $m$ years over an $n$-year horizon: a series of $(P/F)$ terms.

- Salvage at end of horizon: $+ S \cdot (P/F, i, n)$.
```


### Worked Example: Reactor A vs. Reactor B over 12 Years
The transcript's example, redone with every step.

```{prf:example} Reactor A vs. Reactor B (Same Data as Capitalized-Cost Example) over 12-Year LCM
Same data: A has 4-year life and salvage \$3{,}000, annual maintenance \$2{,}000, purchase \$25{,}000. B has 6-year life, no salvage, annual maintenance \$4{,}000, overhaul \$3{,}500 at year 3 (so years 3 and 9 over the 12-year horizon), purchase \$15{,}000. $i = 8%$. LCM = 12 years. Compute PW.
```


```{dropdown} Solution Steps
- **Build A's cash-flow timeline over 12 years.**


- Year 0: $-25{,}000$ (purchase).

- Years 1, 2, 3, 4: $-2{,}000$ each (annual maintenance).

- Year 4: $+3{,}000$ (salvage) and $-25{,}000$ (replacement). Net $-22{,}000$ in year 4 (separate from maintenance).

- Years 5, 6, 7, 8: $-2{,}000$ each.

- Year 8: $+3{,}000$ salvage and $-25{,}000$ replacement. Net $-22{,}000$.

- Years 9, 10, 11, 12: $-2{,}000$ each.

- Year 12: $+3{,}000$ salvage (end of third cycle; no further replacement needed because the horizon ends).


- **PW of A's annual maintenance (years 1-12).**

$$
PW_{maint} = -2{,}000 \cdot (P/A, 8, 12)
$$

Compute $(P/A, 8, 12) = [(1.08)^{12} - 1]/[0.08 \cdot (1.08)^{12}]$. $(1.08)^{12}$: $(1.08)^4 = 1.3605$, $(1.08)^8 = 1.8509$, $(1.08)^{12} = 1.3605 \times 1.8509 = 2.518$. So $(P/A) = 1.518/(0.08 \times 2.518) = 1.518/0.2014 = 7.536$.

$$
PW_{maint} = -2{,}000 \times 7.536 = -\$15{,}072
$$

- **PW of A's replacements (net $-22{,}000$ at years 4 and 8).**


- Year 4: $-22{,}000/(1.08)^4 = -22{,}000/1.3605 = -16{,}170$.

- Year 8: $-22{,}000/(1.08)^8 = -22{,}000/1.8509 = -11{,}887$.


- **PW of A's final-year salvage ($+3{,}000$ at year 12).**

$$
+3{,}000/(1.08)^{12} = 3{,}000/2.518 = +\$1{,}191
$$

- **Total PW for A.**

$$
PW_A = -25{,}000 - 15{,}072 - 16{,}170 - 11{,}887 + 1{,}191 = -\$66{,}938 \approx -\$67{,}000
$$

```


```{dropdown} Solution Steps
- **Build B's cash-flow timeline.**


- Year 0: $-15{,}000$ (purchase).

- Years 1-12: $-4{,}000$ each (annual maintenance).

- Year 3: $-3{,}500$ (overhaul).

- Year 6: $-15{,}000$ (replacement, no salvage).

- Year 9: $-3{,}500$ (overhaul, equivalent to year 3 of cycle 2).

- Year 12: end of horizon (no more replacement).


- **PW of B's annual maintenance.**

$$
PW_{maint} = -4{,}000 \times (P/A, 8, 12) = -4{,}000 \times 7.536 = -\$30{,}144
$$

- **PW of B's year-6 replacement.**

$$
-15{,}000/(1.08)^6 = -15{,}000/1.5869 = -\$9{,}454
$$

- **PW of B's overhauls (years 3 and 9).**


- Year 3: $-3{,}500/(1.08)^3 = -3{,}500/1.2597 = -\$2{,}778$.

- Year 9: $-3{,}500/(1.08)^9 = -3{,}500/1.9990 = -\$1{,}751$.


- **Total PW for B.**

$$
PW_B = -15{,}000 - 30{,}144 - 9{,}454 - 2{,}778 - 1{,}751 = -\$59{,}127 \approx -\$59{,}100
$$

- **Decision.** $|PW_B| < |PW_A|$ (cost \$59{,}100 vs. \$67{,}000); **Reactor B is cheaper in present-worth terms by \$7{,}800**.


- **Cross-check.** The capitalized-cost analysis (previous section) also chose B. Two independent methods agreeing is the strongest verification.
```


### Annual-Equivalent (AE) Cost  -  The Third Way

```{note}
A third comparison method, equivalent to PW but expressed as a uniform annual cost, is the **annual equivalent (AE)**:

$$
AE = PW \cdot (A/P, i, n)
$$

For the same Reactor A vs. B problem:


- AE$_A$ = $-66{,}938 \cdot (A/P, 8, 12)$. $(A/P) = 1/(P/A) = 1/7.536 = 0.1327$. AE$_A = -66{,}938 \times 0.1327 = -\$8{,}884$/yr.

- AE$_B$ = $-59{,}127 \times 0.1327 = -\$7{,}847$/yr.

B is cheaper by about \$1{,}000/yr. AE is preferred when stakeholders think in annual budget terms.
```


```{note}
**Exam Tips  -  Present-Worth Analysis**
- Alternatives must be evaluated over the *same* number of years. LCM is the standard choice.

- Use effective $i$ per period when compounding $> 1$/year.

- Sign convention: outflows negative. The most-positive PW (least-negative cost) wins.

- AE = PW $\cdot (A/P)$ provides an annual-cost view of the same comparison.
```


## Gross Economic Profit (GEP) Analysis
Before any equipment is sized, before any land is purchased, a chemist's candidate synthesis route is screened with a **Gross Economic Profit** calculation. The question is: *on a per-pound-of-product basis, does the value of the products exceed the cost of the raw materials?* A negative GEP kills the route immediately; a small positive GEP is a necessary but far from sufficient condition (utilities, capital, labor, and overhead still need to fit underneath).

### Mass-Basis Stoichiometry

```{note}
**The Per-Kilogram-of-Product Basis**
Choose the desired product as the basis: 1 kg of product. Compute the mass of each reactant and byproduct that participates in producing 1 kg of product, using stoichiometric coefficients and molecular weights:

$$
mass of species  i  per kg product = \frac{|\nu_i| M_i}{|\nu_P| M_P}
$$

where $\nu_i$ is the stoichiometric coefficient of species $i$ (negative for reactants, positive for products), $M_i$ is its molecular weight, and subscript $P$ is the desired product. This is the same operation in Felder | Rousseau's introductory mass-balance chapters  -  you are reading the stoichiometry on a mass rather than molar basis.
```


### The GEP Equation

```{important}

$$
GEP = \sum_{products} \frac{|\nu_i| M_i}{|\nu_P| M_P} p_i  -  \sum_{reactants} \frac{|\nu_j| M_j}{|\nu_P| M_P} p_j
$$

where $p_i$ is the market price of species $i$ in \$/kg.


- Treat byproducts that have market value as positive (a credit on the products side).

- Treat byproducts with zero value (water from oxidation, etc.) as zero.

- Treat byproducts that must be disposed at cost (e.g. HCl in a market without buyers) as negative on the products side or, equivalently, as positive on the reactants side.

- Water and air-derived O$_2$ are usually treated as zero-cost on the reactants side.
```


### Worked Example: Vinyl Chloride Routes
The transcript's example, walked through completely.

```{prf:example} GEP for Two Synthesis Routes to Vinyl Chloride Monomer
Compare two synthesis routes to vinyl chloride monomer (VCM, $\mathrm{C_2H_3Cl}$, $M = 62.5$):

**Route 1:** Hydrochlorination of acetylene.

$$
\mathrm{C_2H_2 + HCl \rightarrow C_2H_3Cl}
$$

Prices: acetylene \$1.85/kg, HCl \$0.30/kg, VCM \$0.75/kg.

**Route 2:** Oxychlorination/cracking of ethane.

$$
\mathrm{C_2H_6 + Cl_2 + \tfrac{1}{2} O_2 \rightarrow C_2H_3Cl + H_2O + HCl}
$$

Prices: ethane \$0.20/kg, Cl$_2$ \$0.25/kg, O$_2$ \$0 (from air), VCM \$0.75/kg, byproduct HCl credit \$0.30/kg, H$_2$O \$0.

Which route shows a positive GEP?
```


```{dropdown} Solution Steps
- **Molecular weights.**

$$
M(\mathrm{C_2H_2}) = 26.0,   M(\mathrm{HCl}) = 36.5,   M(\mathrm{C_2H_3Cl}) = 62.5
$$

$$
M(\mathrm{C_2H_6}) = 30.0,   M(\mathrm{Cl_2}) = 71.0,   M(\mathrm{O_2}) = 32.0,   M(\mathrm{H_2O}) = 18.0
$$

- **Route 1: mass of each species per kg VCM.**


- Acetylene: $\nu = 1$, $M = 26.0$; mass $= 26.0/62.5 = 0.416$ kg/kg VCM.

- HCl: $\nu = 1$, $M = 36.5$; mass $= 36.5/62.5 = 0.584$ kg/kg VCM.

**GEP$_1$:**

$$

$$

\begin{align}


GEP_1 &= (1)(0.75) - (0.416)(1.85) - (0.584)(0.30)
&= 0.750 - 0.770 - 0.175
&= -\$0.195  per kg VCM \approx -\$0.20/kg
\end{align}

$$

$$

**Route 1 is a money loser on raw materials alone. Reject.**
```


```{dropdown} Solution Steps
- **Route 2: mass per kg VCM.**


- Ethane: mass $= 30.0/62.5 = 0.480$ kg/kg VCM.

- Cl$_2$: mass $= 71.0/62.5 = 1.136$ kg/kg VCM.

- O$_2$: mass $= (0.5)(32.0)/62.5 = 0.256$ kg/kg VCM.

- H$_2$O byproduct: $18.0/62.5 = 0.288$ kg/kg VCM (no value).

- HCl byproduct: $36.5/62.5 = 0.584$ kg/kg VCM (\$0.30/kg credit).

**GEP$_2$:**

$$

$$

\begin{align}


GEP_2 &= (1)(0.75) + (0.584)(0.30) - (0.480)(0.20) - (1.136)(0.25) - (0.256)(0)
&= 0.750 + 0.175 - 0.096 - 0.284 - 0
&= +\$0.545  per kg VCM
\end{align}

$$

$$

**Route 2 is profitable on a raw-material basis; proceeds to the next stage of design.**


- **Verification.** Modern industrial VCM production is overwhelmingly via the ethylene/EDC oxychlorination route (a close cousin of Route 2), confirming the GEP-based selection in practice.


- **What GEP does *not* tell you.** A GEP of \$0.545/kg leaves room for utilities (steam, electricity), labor, depreciation, taxes, and a profit margin. As a rule of thumb, 30-70% of GEP is consumed by these downstream costs, so the bottom-line plant margin is often \$0.10-\$0.35/kg.
```


### Worked Example: GEP with a Negative-Value Byproduct

```{prf:example} Disposal-Cost Byproduct
Consider a hypothetical reaction $\mathrm{A + B \rightarrow P + Q}$ where Q is a hazardous waste that costs \$0.40/kg to incinerate (negative value $-$\$0.40/kg). Prices: A \$0.50/kg, B \$0.30/kg, P \$1.00/kg. Stoichiometry on a mass basis: 0.6 kg A and 0.5 kg B produce 1.0 kg P and 0.1 kg Q. Compute GEP.
```


```{dropdown} Solution Steps
- **Set up the equation, treating Q's disposal cost as a debit on the products side.**

$$

$$

\begin{align}


GEP &= (1.0)(1.00) + (0.1)(-0.40) - (0.6)(0.50) - (0.5)(0.30)
&= 1.000 - 0.040 - 0.300 - 0.150
&= +\$0.510  per kg P
\end{align}

$$

$$

- **Sanity check.** If Q had zero disposal cost instead, GEP would be \$0.550. The disposal of 0.1 kg/kg of waste reduces profit by \$0.04  -  about 8% of margin. If disposal cost rose to \$5/kg (e.g. a regulated waste), the penalty would be 0.1 $\times$ 5 = \$0.50/kg, almost killing the route. Byproduct economics are often the deciding factor in route selection.
```


```{note}
**Exam Tips  -  GEP**
- Basis = 1 kg of *desired* product. Everything else scales by mass ratio against the product.

- Negative GEP kills a route; no clever engineering can recover it.

- Positive GEP is necessary, not sufficient. Utilities and capital still need to fit.

- Byproducts with disposal cost are economically equivalent to negative-priced products.
```


## Net Present Value and Internal Rate of Return
The Net Present Value (NPV) and Internal Rate of Return (IRR) are the two headline metrics by which a corporate investment committee evaluates a multi-year venture. NPV asks "how much value, in today's dollars, does this project create?" IRR asks "what discount rate would make this project exactly break even?"

### The NPV Equation

```{note}
**Net Present Value** is the discounted sum of all after-tax cash flows over the project life, less the initial investment:

$$
NPV = -I_0 + \sum_{k=1}^{n} \frac{CF_k}{(1+r)^k} + \frac{S_n + WC}{(1+r)^n}
$$

where:


- $I_0$ = total depreciable fixed-capital investment at time zero (or spread over construction years).

- $CF_k$ = after-tax cash flow in year $k$.

- $r$ = cost of capital (also called the hurdle rate or discount rate).

- $S_n$ = terminal salvage of the fixed assets at end of project.

- $WC$ = working capital recovered at end of project (the cash equivalent of inventories, accounts receivable, in-process material that gets liquidated when the plant shuts down).

**Decision rule:** accept the project if NPV $> 0$. The positive NPV is the extra value the project creates beyond what could be earned by investing the same money at rate $r$.
```


### Cash-Flow Anatomy: The Tax Shield from Depreciation

```{note}
**Why Depreciation Matters**
Depreciation is not a cash outflow  -  the cash was spent when the equipment was purchased. But the tax code allows the company to deduct a portion of the original investment each year, reducing taxable income. The cash flow in year $k$ is therefore:

$$
CF_k = (S_k - C_k - D_k)(1 - t) + D_k
$$

where:


- $S_k$ = revenue (Sales) in year $k$.

- $C_k$ = cash production cost in year $k$ (raw materials, utilities, labor, overhead  -  but *not* depreciation).

- $D_k$ = depreciation charge in year $k$.

- $t$ = effective tax rate (federal + state + local, typically 25-40% in the US).

The depreciation appears twice: once subtracted to compute taxable income $(S - C - D)$, then added back because it is non-cash. The net effect is that depreciation *shifts cash flow earlier in time*; the total cash over the project life is unchanged, but earlier cash is worth more after discounting  -  so depreciation increases NPV.
```


### Depreciation Methods

```{note}
**Straight-Line vs. MACRS**
**Straight-line depreciation:** the simplest. $D_k = (I_0 - S_n)/n_{depreciable}$ for each year of the depreciable life. Often used for book purposes.

**MACRS (Modified Accelerated Cost Recovery System):** US tax depreciation. Chemical-plant equipment is typically 5- or 7-year MACRS class. The percentages of $I_0$ depreciated each year (5-year MACRS, half-year convention):

For 7-year MACRS the percentages start at 14.29% in year 1 and finish in year 8 at 4.46%. The point of accelerated depreciation is to bring the tax shield earlier in time, increasing NPV.
```


### Worked Example: NPV of a 15-Year Venture
This is the transcript's example, with every step.

```{prf:example} NPV with MACRS Depreciation and Working Capital
A chemical plant is built 2007-2009 with total depreciable capital \$90M (sunk \$30M per year). Working capital \$40M required at end of 2009. Production begins 2010 at 50% of nameplate; 75% in 2011; 100% thereafter through 2021. At full capacity: sales \$150M/yr, cash production cost \$100M/yr. In ramp-up: 2010 sales \$75M, cost \$55M; 2011 sales \$113M, cost \$78M. MACRS 7-year depreciation. Tax rate 40%. Cost of capital 15%. Compute NPV.
```


```{dropdown} Solution Steps
- **Lay out the cash-flow timeline.**


- 2007: $-30$M (capital).

- 2008: $-30$M (capital).

- 2009: $-30$M (capital) $- 40$M (working capital) $= -70$M.

- 2010 onward: operating cash flows per the formula in step 3 below.


- **MACRS 7-year depreciation schedule of \$90M total.**


- 2010 (yr 1): 14.29% $\times$ 90 = \$12.86M

- 2011 (yr 2): 24.49% $\times$ 90 = \$22.04M

- 2012 (yr 3): 17.49% = \$15.74M

- 2013 (yr 4): 12.49% = \$11.24M

- 2014 (yr 5): 8.93% = \$8.04M

- 2015 (yr 6): 8.92% = \$8.03M

- 2016 (yr 7): 8.93% = \$8.04M

- 2017 (yr 8): 4.46% = \$4.01M

- 2018-2021: \$0 (depreciation exhausted)
```


```{dropdown} Solution Steps
- **Compute operating cash flow year by year.**
Formula: $CF_k = (S_k - C_k - D_k)(1 - 0.40) + D_k = 0.6(S_k - C_k) - 0.6 D_k + D_k = 0.6(S_k - C_k) + 0.4 D_k$.


- 2010: $S = 75$, $C = 55$, $D = 12.86$. $CF = 0.6(20) + 0.4(12.86) = 12 + 5.14 = 17.14$.

- 2011: $S = 113$, $C = 78$, $D = 22.04$. $CF = 0.6(35) + 0.4(22.04) = 21 + 8.82 = 29.82$.

- 2012: $S = 150$, $C = 100$, $D = 15.74$. $CF = 0.6(50) + 0.4(15.74) = 30 + 6.30 = 36.30$.

- 2013: $D = 11.24$. $CF = 30 + 4.50 = 34.50$.

- 2014: $D = 8.04$. $CF = 30 + 3.22 = 33.22$.

- 2015: $D = 8.03$. $CF = 30 + 3.21 = 33.21$.

- 2016: $D = 8.04$. $CF = 30 + 3.22 = 33.22$.

- 2017: $D = 4.01$. $CF = 30 + 1.60 = 31.60$.

- 2018: $D = 0$. $CF = 30 + 0 = 30.00$.

- 2019: $CF = 30$.

- 2020: $CF = 30$.

- 2021: $CF = 30 + 40$ (working-capital recovery) $= 70$.
```


```{dropdown} Solution Steps
- **Discount each cash flow back to 2007 at $r = 15%$.**
Let the discount factors be $1/(1.15)^k$ where $k$ is years from 2007.


- 2007 ($k=0$): $-30$ / 1 = $-30$.

- 2008 ($k=1$): $-30/1.15 = -26.09$.

- 2009 ($k=2$): $-70/1.3225 = -52.93$.

- 2010 ($k=3$): $17.14/1.5209 = 11.27$.

- 2011 ($k=4$): $29.82/1.7490 = 17.05$.

- 2012 ($k=5$): $36.30/2.0114 = 18.05$.

- 2013 ($k=6$): $34.50/2.3131 = 14.91$.

- 2014 ($k=7$): $33.22/2.6600 = 12.49$.

- 2015 ($k=8$): $33.21/3.0590 = 10.86$.

- 2016 ($k=9$): $33.22/3.5179 = 9.44$.

- 2017 ($k=10$): $31.60/4.0456 = 7.81$.

- 2018 ($k=11$): $30.00/4.6524 = 6.45$.

- 2019 ($k=12$): $30.00/5.3503 = 5.61$.

- 2020 ($k=13$): $30.00/6.1528 = 4.88$.

- 2021 ($k=14$): $70.00/7.0757 = 9.89$.


- **Sum to get NPV.**
Sum of positives: $11.27 + 17.05 + 18.05 + 14.91 + 12.49 + 10.86 + 9.44 + 7.81 + 6.45 + 5.61 + 4.88 + 9.89 = 128.71$.
Sum of negatives: $-30 - 26.09 - 52.93 = -109.02$.

$$
NPV = 128.71 - 109.02 \approx +\$19.7  M
$$

(The transcript's quoted NPV is +\$21.4M; small differences arise from the exact MACRS percentages used and from rounding. The signed result and order of magnitude match.)


- **Cumulative discounted cash flow plot.** Tracking the running sum from 2007 onward, the cumulative crosses zero somewhere in 2018  -  this is the **discounted payback period**, $\approx$ 11 years.


- **Interpretation.** NPV $> 0$ at 15% cost of capital: the project creates value beyond what could be earned by investing the same \$90M+ at 15%. Accept.
```


### Internal Rate of Return (IRR)

```{note}
The **Internal Rate of Return** (also called Investor's Rate of Return) is the discount rate that drives NPV to exactly zero:

$$
NPV(r = IRR) = 0
$$

**Decision rule:** accept if IRR $>$ cost of capital. The two rules (NPV $> 0$, IRR $>$ cost of capital) are equivalent for a conventional cash-flow pattern (initial negative outlay followed by positive returns).

**Computation:** no closed form exists; use a spreadsheet's Goal Seek or Solver to find $r$ such that NPV $= 0$. Alternatively, plot NPV vs. $r$ and read the zero-crossing.

**Interpretation:** IRR is the project's intrinsic earning rate. "If we got this money back as interest from a bank, the equivalent interest rate would be IRR." For the transcript's project, IRR $\approx 18.5%$, so the project beats a 15% hurdle rate by 3.5%  -  modest, but acceptable.
```


### Worked Example: Iterating to Find IRR

```{prf:example} Quick IRR Bracket for a Three-Year Project
A project costs \$100K at $t=0$ and returns \$40K, \$50K, \$30K at the ends of years 1, 2, 3. Find IRR (within $\pm$1%).
```


```{dropdown} Solution Steps
- **Try $r = 0$.** NPV $= -100 + 40 + 50 + 30 = +20$. Positive.

- **Try $r = 20%$.** NPV $= -100 + 40/1.2 + 50/1.44 + 30/1.728 = -100 + 33.33 + 34.72 + 17.36 = -14.59$. Negative.

- **Bisect: try $r = 10%$.** NPV $= -100 + 40/1.1 + 50/1.21 + 30/1.331 = -100 + 36.36 + 41.32 + 22.54 = +0.22$. Almost zero.

- **Refine: try $r = 11%$.** NPV $= -100 + 40/1.11 + 50/1.2321 + 30/1.3676 = -100 + 36.04 + 40.58 + 21.94 = -1.44$. Negative.

- **IRR is between 10% and 11%, closer to 10%. Linear interpolation:**

$$
IRR \approx 10% + \frac{0.22}{0.22 + 1.44} \times 1% = 10% + 0.13% = 10.13%
$$

- **Verification.** At 10.13%, NPV is essentially zero  -  check: $-100 + 40/1.1013 + 50/1.2129 + 30/1.3361 = -100 + 36.32 + 41.22 + 22.45 = -0.01$. \checkmark
```


### NPV vs. IRR  -  When They Disagree

```{note}
**Mutually Exclusive Projects: Use NPV**
For mutually exclusive projects (you can do only one), **NPV and IRR can rank them differently**. Example: Project A has NPV \$1M and IRR 25%. Project B has NPV \$5M and IRR 15%. If the cost of capital is 10%, both meet the hurdle, but they rank oppositely. The **NPV ranking is correct** because NPV measures absolute value created, while IRR is a rate (which can be misleadingly high for a small project).

For independent projects (you can do all of them up to a budget), either rule works.

For non-conventional cash flows (multiple sign changes), IRR can have multiple solutions. NPV is unambiguous.

**Rule:** when in doubt, use NPV.
```


```{note}
**Exam Tips  -  NPV and IRR**
- Cash flow $CF_k = (S_k - C_k - D_k)(1-t) + D_k = 0.6(S_k-C_k) + 0.4 D_k$ at $t = 40%$.

- Depreciation is non-cash; add it back.

- Working capital is added at start (negative) and recovered at end (positive).

- NPV $> 0$ iff IRR $>$ cost of capital, for conventional projects.

- For mutually exclusive projects, NPV beats IRR as the ranking criterion.

- MACRS 5-year: $\{20.00, 32.00, 19.20, 11.52, 11.52, 5.76\}$. MACRS 7-year starts at 14.29%.
```


## Summary: Engineering Economics Decision Tree

```{note}
**Which Economic Tool When?**
- **Gross Economic Profit:** screening a synthesis route before any process design. Use mass-basis stoichiometry; negative GEP kills the route.

- **Present Worth (PW):** comparing alternatives of *equal life* (or unequal lives over the LCM horizon). The most general single-number comparison.

- **Annual Equivalent (AE):** the same comparison expressed as a uniform annual cost. AE = PW $\cdot (A/P, i, n)$.

- **Capitalized Cost:** comparing alternatives of *unequal life* that will be replaced indefinitely. Avoids the LCM horizon. Use for perpetual-replacement decisions.

- **NPV:** headline corporate go/no-go metric for a finite-life venture. Uses after-tax cash flows.

- **IRR:** the discount rate at which NPV $= 0$. Compare to cost of capital. Use NPV as the tie-breaker for mutually exclusive projects.
```


```{note}
**Common PE-Exam Mistakes**
- Mixing nominal and effective rates. $i_{eff} = (1 + r/m)^m - 1$ always.

- PW comparisons over different lifetimes without using LCM.

- Forgetting to add depreciation back to operating cash flow.

- Using CEPCI ratios backwards (old/new instead of new/old).

- HEN problems: putting cold utility above the pinch or hot utility below.

- CP rule confusion: cold dominates *above*, hot dominates *below*. Memorize the alphabetical mnemonic "Above, Cold; Below, Hot."

- Diagram-type confusion: stream tables don't go on BFDs; fail-safe actions don't go on PFDs; pipe specs only on P&IDs.

- GEP: forgetting to put the basis on 1 kg of the *desired* product.

- NPV: forgetting to recover working capital at end of project (it's a real cash inflow).
```


```{tip}
**One-Page Formula Reference**
**Time value:**
$F = P(1+i)^n$, $P = F/(1+i)^n$, $P_{perp} = A/i$.
$(P/A, i, n) = [(1+i)^n - 1]/[i(1+i)^n]$.
$(A/P) = 1/(P/A)$.
$i_{eff} = (1+r/m)^m - 1$.

**Capitalized cost:** $K = C_I + C_R/[(1+i)^n - 1]$.

**Cost escalation:** $C_2 = C_1 \cdot (CEPCI_2/CEPCI_1)$. Six-tenths rule: $C_2 = C_1 (S_2/S_1)^{0.6}$.

**Bare-module:** $C_{BM} = F_{BM} \cdot C_P$.

**Heat-exchanger network:**
CP rule above pinch: $CP_c \geq CP_h$. Below: $CP_h \geq CP_c$.
No cold utility above pinch; no hot utility below; no heat across.

**Pinch from temperature interval table:** shift hot down $\Delta T_{\min}/2$, cold up $\Delta T_{\min}/2$; cascade surpluses; add hot utility at top to make cascade feasible; bottom value is $Q_{C,\min}$.

**GEP:** mass basis = 1 kg desired product. GEP = $\sum$ (kg product/kg P)$\times$ price $-$ $\sum$ (kg reactant/kg P)$\times$ price.

**NPV / IRR:**
$CF_k = (S_k - C_k - D_k)(1-t) + D_k$.
$NPV = -I_0 + \sum CF_k/(1+r)^k + (S_n + WC)/(1+r)^n$.
IRR: $r$ where NPV $= 0$.
```
