---
title: "Instrumentation & Process Control"
author: "PE Study Guide"
date: "2025"
---

# Instrumentation & Process Control

## Preliminaries: Laplace-Transform Toolbox
Process-control analysis lives in the Laplace domain. Almost every theorem in this chapter is derived by transforming a time-domain ODE, manipulating the resulting algebraic equation, and inverting the result. Before diving into first-order systems, we collect the transforms and theorems we will use repeatedly so that every later derivation is fully self-contained.

```{note}
**Definition of the Laplace Transform**
For a time-domain signal $f(t)$ defined for $t \geq 0$, the Laplace transform is


$$
F(s) = L\{f(t)\} = \int_0^{\infty} f(t) e^{-s t} dt
$$


The variable $s$ is complex. The transform converts differentiation into multiplication, integration into division, and convolution into a product  -  which is why every linear ODE becomes a linear algebraic equation in the $s$-domain.
```


```{important}
**Transform Pairs We Will Use**
- Unit impulse: $\delta(t)  \leftrightarrow  1$

- Unit step: $u(t)  \leftrightarrow  \dfrac{1}{s}$

- Step of magnitude $M$: $M u(t)  \leftrightarrow  \dfrac{M}{s}$

- Ramp: $t  \leftrightarrow  \dfrac{1}{s^2}$

- Exponential decay: $e^{-a t}  \leftrightarrow  \dfrac{1}{s + a}$

- Sine: $\sin(\omega t)  \leftrightarrow  \dfrac{\omega}{s^2 + \omega^2}$

- Cosine: $\cos(\omega t)  \leftrightarrow  \dfrac{s}{s^2 + \omega^2}$

- Damped sine: $e^{-a t}\sin(\omega t)  \leftrightarrow  \dfrac{\omega}{(s+a)^2 + \omega^2}$

- Damped cosine: $e^{-a t}\cos(\omega t)  \leftrightarrow  \dfrac{s + a}{(s+a)^2 + \omega^2}$

- Time-shifted: $f(t - \theta) u(t-\theta)  \leftrightarrow  e^{-\theta s} F(s)$   (dead time)
```


```{important}
**Operator Theorems**
- Derivative: $L\{\dfrac{df}{dt}\} = s F(s) - f(0)$

- Second derivative: $L\{\dfrac{d^2f}{dt^2}\} = s^2 F(s) - s f(0) - f'(0)$

- Initial-value theorem: $\displaystyle\lim_{t \to 0^+} f(t) = \lim_{s \to \infty} s F(s)$

- Final-value theorem: $\displaystyle\lim_{t \to \infty} f(t) = \lim_{s \to 0} s F(s)$   (only if all poles of $sF(s)$ lie in the left half-plane).
```


```{note}
**Deviation Variables  -  Why We Always Use Them**
Throughout this chapter, every variable is a **deviation** from a reference steady state:


$$
y(t) \equiv Y(t) - Y,   x(t) \equiv X(t) - X
$$


where lower-case denotes deviation and upper-case denotes absolute value. Two consequences:


- The initial condition at the reference steady state is identically zero ($y(0)=0$, $y'(0)=0$, ...), which kills every initial-condition term in the Laplace derivative theorem.

- Process transfer functions $G(s) = Y(s)/X(s)$ are written without bias terms, exactly as $\dfrac{K}{\tau s + 1}$ or $\dfrac{K e^{-\theta s}}{\tau s + 1}$.

After solving for the deviation $y(t)$, the actual process value at any time is $Y(t) = Y + y(t)$. *Forgetting to add $Y$ back is the single most common error in first-order step-response problems.*
```


```{note}
**Partial Fractions, Heaviside Cover-Up, and Their Use**
Inverting a rational $F(s) = N(s)/D(s)$ requires decomposing it into a sum of simple fractions whose inverse transforms appear in our table. Two methods will appear throughout this chapter:

**(a) Generic partial fractions** (good for any polynomial denominator):


$$
\frac{N(s)}{(s - a)(s - b)} = \frac{A}{s - a} + \frac{B}{s - b}
$$


Multiply through by the LCD, expand, and match coefficients of each power of $s$.

**(b) Heaviside cover-up** (faster for distinct linear factors): the residue at $s = a$ is


$$
A = [ (s - a) F(s) ]_{s = a}
$$


We will use partial fractions in deriving the first-order step response and the cover-up technique in deriving the FOPDT step response.
```


## First-Order Systems: Complete Step-Response Derivation
A first-order linear process is the workhorse model of process control. A liquid-level tank with a linear outlet resistance, a stirred-tank thermocouple, a CSTR concentration response, the lag introduced by a valve actuator  -  all can be approximated as first-order with two parameters: a steady-state gain $K$ and a time constant $\tau$.

### The Transfer Function in Standard Form

```{note}
A **first-order process** is one whose time-domain dynamics are described by the linear, constant-coefficient ODE (in deviation variables)


$$
\tau \frac{dy(t)}{dt} + y(t) = K x(t)
$$


where $x$ is the input deviation, $y$ is the output deviation, $K$ is the steady-state gain, and $\tau$ is the time constant. Taking the Laplace transform (with $y(0) = 0$) gives


$$
\tau s Y(s) + Y(s) = K X(s)
$$


$$
\frac{Y(s)}{X(s)} = G(s) = \frac{K}{\tau s + 1}
$$


This rational function is the *transfer function* of the process in *standard form*  -  denominator polynomial normalized so the constant term is unity.
```


### Step-Input Derivation in Generic Terms
We will follow the transcript exactly: a generic transfer function $G(s) = K/(\tau s + 1)$ subjected to a step input of magnitude $M$. Working in generic letters means the answer is universal  -  the same formula applies whether the process is a level tank, a heat exchanger, or a reactor.

```{dropdown} Solution Steps
- **Transform the input.** The step of magnitude $M$ is $x(t) = M u(t)$, whose Laplace transform is


$$
X(s) = L\{M u(t)\} = \frac{M}{s}
$$


- **Form the output transform.** Substitute into $Y(s) = G(s) X(s)$:


$$
Y(s) = \frac{K}{\tau s + 1} \cdot \frac{M}{s} = \frac{K M}{s(\tau s + 1)}
$$


This is the equation we must invert to obtain $y(t)$.


- **Partial-fraction decomposition.** Write


$$
\frac{K M}{s(\tau s + 1)} = \frac{A}{s} + \frac{B}{\tau s + 1}
$$


Multiply both sides by the common denominator $s(\tau s + 1)$:


$$
K M = A(\tau s + 1) + B s = (\tau A + B) s + A
$$


- **Match coefficients.** The left side is $KM$, a constant, so coefficient of $s^1$ must vanish and coefficient of $s^0$ must equal $KM$:


- $s^0$ (constants): $A = K M$.

- $s^1$: $\tau A + B = 0  \Longrightarrow  B = -\tau A = -K M \tau$.

Therefore


$$
Y(s) = \frac{K M}{s} - \frac{K M \tau}{\tau s + 1}
$$


- **Invert term by term.** Use $L^{-1}\{1/s\} = 1$ and $L^{-1}\{1/(\tau s + 1)\} = (1/\tau) e^{-t/\tau}$:


$$
\begin{align}
y(t) &= L^{-1}\{ \frac{K M}{s} \} - K M \tau \cdot L^{-1}\{ \frac{1}{\tau s + 1} \} \\
&= K M - K M \tau \cdot \frac{1}{\tau} e^{-t/\tau} \\
&= K M - K M e^{-t/\tau}
\end{align}
$$


Factoring the common $K M$:

$$
y(t) = K M ( 1 - e^{-t/\tau} )    \text{(Equation 1)}
$$

```


### Interpreting Equation 1 Graphically

```{note}
**Five Landmarks on the Step Response**
The exponential approach to the new steady state has five reference points worth memorizing:


- **At $t = 0$:** $y(0) = K M (1 - 1) = 0$. The output is unchanged from the reference steady state at the instant of the step.

- **At $t = \tau$:** $y(\tau) = K M (1 - e^{-1}) = 0.632 K M$. This is the **63.2% landmark**  -  the time constant equals the time required to reach 63.2% of the eventual change. It is the universal definition by which $\tau$ is read from experimental data.

- **At $t = 2\tau$:** $y/y(\infty) = 1 - e^{-2} = 0.865$.

- **At $t = 3\tau$:** $y/y(\infty) = 1 - e^{-3} = 0.950$. "Settled to within 5%."

- **At $t = 5\tau$:** $y/y(\infty) = 1 - e^{-5} = 0.993$. Practically at steady state.

- **As $t \to \infty$:** $e^{-t/\tau} \to 0$, so $y(\infty) = K M$. The ultimate deviation equals gain times step magnitude.

A second cross-check: the slope at the origin is $y'(0) = K M / \tau$, so the initial-slope line intersects the asymptote $y = K M$ at time $t = \tau$. This is the classical "tangent-at-origin" method for graphically reading $\tau$ from a plot.
```


```{note}
**Sign of the Gain**
The same Equation 1 applies for any sign of $K$. Three cases:


- $K > 0$: output rises to a new positive deviation. Most level, temperature, pressure loops.

- $K < 0$: output falls (the curve is reflected through $y=0$). Common in heat exchangers where increasing cooling-water flow lowers process temperature, or in distillation where increasing reflux lowers a high-purity-product impurity.

- $K = 0$: no steady-state response to the input. Either a wrong model choice or a process with integral action (then the model is not strictly first-order).
```


### Worked Example: Level Tank with Linear Outflow

```{prf:example} Step Response of a Surge Tank
:label: instrumentationandcontrol-example-0

A surge tank has the first-order transfer function $H(s)/Q_i(s) = 10/(50 s + 1)$ where $H$ is liquid level [m] and $Q_i$ is inlet flow [m³/s], so $K = 10$ m per m³/s and $\tau = 50$ s. At the initial steady state, $Q_i = 0.40$ m³/s and $H = 3.0$ m. The inlet is suddenly stepped to $0.41$ m³/s. Find:


- the level 100 s after the step,

- the new steady-state level,

- the time at which the level reaches 63.2% of its ultimate change.
```


```{dropdown} Solution Steps
- **Switch to deviation variables.** The input deviation is


$$
q_i(t) = Q_i(t) - Q_i = 0.41 - 0.40 = 0.01 \text{m}^3/\text{s for } t > 0
$$


so the step magnitude is $M = 0.01$. The output deviation is $h(t) = H(t) - 3.0$, with $h(0) = 0$.


- **Apply Equation 1 with $K = 10$, $\tau = 50$, $M = 0.01$:**


$$
h(t) = K M ( 1 - e^{-t/\tau} ) = (10)(0.01)(1 - e^{-t/50}) = 0.10(1 - e^{-t/50}) \text{m}
$$


- **(a) Evaluate at $t = 100$ s.** Note $100/50 = 2$, so $e^{-100/50} = e^{-2} = 0.1353$.


$$
h(100) = 0.10 (1 - 0.1353) = 0.10 (0.8647) = 0.0865 \text{m}
$$


Convert back to absolute level:


$$
H(100) = H + h(100) = 3.000 + 0.0865 = 3.087 \text{m}
$$


A common student error is to read $h(100) = 0.0865$ m and *report it* as the answer; the absolute level is what an instrument actually shows.


- **(b) Steady-state level ($t \to \infty$).** As $t \to \infty$, $e^{-t/\tau} \to 0$, so


$$
h(\infty) = K M = (10)(0.01) = 0.10 \text{m}  \Longrightarrow  H(\infty) = 3.10 \text{m}
$$


- **(c) Time to reach 63.2% of the ultimate change.** By the landmark property of $\tau$,


$$
t_{63.2\%} = \tau = 50 \text{s}
$$


Verify by solving $1 - e^{-t/\tau} = 0.632$:


$$
e^{-t/\tau} = 0.368  \Longrightarrow  t/\tau = -\ln(0.368) = 1.0  \Longrightarrow  t = \tau = 50 \text{s} \checkmark
$$


- **Cross-check by material balance.** A sustained extra $0.01$ m³/s inflow must, at steady state, be matched by an extra $0.01$ m³/s outflow. If the outlet flow is linear in head, $Q_o = h/R$, then $R = K = 10$ s/m². The extra head needed to drive $0.01$ extra m³/s through resistance $R$ is $\Delta h = R \cdot \Delta Q = 10 \times 0.01 = 0.10$ m. ✓ Matches the transfer-function answer exactly.
```


### Worked Example: Negative-Gain Heat Exchanger

```{prf:example} Step Response with Negative Gain
:label: instrumentationandcontrol-example-1

A heat exchanger's process-outlet temperature is described by $T(s)/Q_{cw}(s) = -3.0/(8 s + 1)$ where $T$ is in $^\circ$F and $Q_{cw}$ is cooling-water flow in gpm. At the initial steady state, $Q_{cw} = 12.0$ gpm and $T = 175^\circ$F. The cooling-water flow is stepped to $14.0$ gpm. Find $T(t)$ at $t = 4$ s and at steady state.
```


```{dropdown} Solution Steps
- **Deviation step:** $M = 14.0 - 12.0 = +2.0$ gpm. Process gain $K = -3.0$ $^\circ$F/gpm (negative because more cooling lowers outlet $T$).


- **Apply Equation 1:**


$$
t(t) = K M (1 - e^{-t/\tau}) = (-3.0)(2.0)(1 - e^{-t/8}) = -6.0(1 - e^{-t/8}) ^\circ\text{F}
$$


- **Evaluate at $t = 4$ s.** $e^{-4/8} = e^{-0.5} = 0.6065$.


$$
t(4) = -6.0 (1 - 0.6065) = -6.0 (0.3935) = -2.36^\circ\text{F}
$$


Absolute temperature:


$$
T(4) = 175 + (-2.36) = 172.64^\circ\text{F}
$$


- **Steady state:** $t(\infty) = K M = -6.0^\circ$F, so $T(\infty) = 175 - 6.0 = 169.0^\circ$F.


- **Verification:** The temperature *decreases* (consistent with negative gain and positive step). At $t = \tau = 8$ s the deviation should be $0.632 \times (-6) = -3.79^\circ$F, giving $T(8) = 171.2^\circ$F. At $t = 5\tau = 40$ s the response is at 99.3%  -  effectively done. The exponential shape is the same; only the asymptotic level is signed.
```


```{note}
**Exam Tips  -  First-Order Step Response**
- Equation 1 is in *deviation* variables. Always add the prior steady state back before quoting the answer.

- The four memorized fractions are $0.632, 0.865, 0.950, 0.993$ at $1\tau, 2\tau, 3\tau, 5\tau$. Many exam questions can be answered by inspection if you know these.

- The slope at $t=0$ is $K M / \tau$, not zero. A first-order response starts moving immediately  -  there is no initial flatness. If you see a flat region at the beginning of a trace, the system has dead time (covered next).

- For *negative* gain, the response goes down. Sign of $K$ is preserved through Equation 1.
```


## First-Order Plus Dead Time (FOPDT) Identification
Real industrial processes almost always show a measurable delay between the moment a manipulated variable is changed and the moment the controlled variable begins to move. This delay  -  the **dead time**, $\theta$ (also called transportation lag)  -  comes from finite-velocity transport in piping, from analyzer cycle times, from sampling intervals in digital controllers, and from any pure-delay element in the loop. The FOPDT model adds this dead time to the first-order model and is the foundation of nearly every classical PID tuning rule.

### The FOPDT Transfer Function

```{note}
The First-Order Plus Dead Time (FOPDT) transfer function in standard form is


$$
G(s) = \frac{K e^{-\theta s}}{\tau s + 1}
$$


The factor $e^{-\theta s}$ is the Laplace-domain representation of a pure delay of $\theta$ time units. Three parameters: the steady-state gain $K$, the dominant time constant $\tau$, and the dead time $\theta$. Two reasons we love this model:


- It is the simplest model that captures both the speed of a process ($\tau$) and the time-to-first-response ($\theta$). The two together determine virtually every tuning constant.

- Most higher-order processes (cascades of two or more first-order lags) can be approximated by an equivalent FOPDT whose tuning rules give acceptable closed-loop behavior. This is why dozens of textbook tuning recipes (Ziegler-Nichols, Cohen-Coon, Tyreus-Luyben, IMC, lambda) all start from a FOPDT fit.
```


### The FOPDT Step Response
Subjecting $G(s)$ to a step input of magnitude $M$:


$$
Y(s) = \frac{K e^{-\theta s}}{\tau s + 1} \cdot \frac{M}{s} = e^{-\theta s} \frac{K M}{s(\tau s + 1)}
$$


The factor $e^{-\theta s}$ is a pure time-shift operator: when we invert, the time-domain answer is the first-order step response delayed by $\theta$. Using Equation 1 of the previous section and the time-shift theorem:


$$
y(t) = \begin{cases} 0, & t < \theta \\ K M (1 - e^{-(t-\theta)/\tau}), & t \geq \theta \end{cases}
$$


Graphically: a flat region from 0 to $\theta$, then an exponential rise. Reading $\theta$ and $\tau$ from a step-test trace is the central practical task of FOPDT identification.

### Method 1: Tangent-and-Inflection (Smith / Ziegler-Nichols Original)

```{note}
**Tangent-and-Inflection Construction**
- Draw the experimental step response.

- Find the inflection point  -  where the slope is steepest. For a pure first-order trace the inflection is at $t = \theta$ itself; for higher-order processes it shifts later.

- Draw a tangent line at the inflection. Extend it to (a) the original baseline and (b) the new asymptote.

- The tangent's intersection with the baseline gives $\theta$ (apparent dead time).

- The tangent's intersection with the asymptote gives $t_{\text{intercept}} = \theta + \tau$. So $\tau = t_{\text{intercept}} - \theta$.

This is fast on a graph but sensitive to where the eye places the tangent. We will not use it for numerical work; it is included because the original Ziegler-Nichols tuning rules were derived assuming this construction.
```


### Method 2: Sundaresan-Krishnaswamy Two-Point Fit
The two-point fit, developed by Sundaresan and Krishnaswamy in the late 1970s, is much more reproducible than the tangent method because it uses fixed reference fractions rather than a hand-drawn line. It is the method the transcript uses, and it is the method most often expected on the PE exam.

```{important}
**Sundaresan-Krishnaswamy Two-Point Formulas**
Read off the times $t_{35.3\%}$ and $t_{85.3\%}$ at which the response reaches 35.3% and 85.3% of its ultimate change. Then


$$
\begin{align}
\theta &= 1.3 t_{35.3\%} - 0.29 t_{85.3\%} \\
\tau   &= 0.67 (t_{85.3\%} - t_{35.3\%}) \\
K      &= \frac{\Delta y_{ss}}{\Delta x}
\end{align}
$$


The fractions 35.3% and 85.3% are not arbitrary  -  they are chosen so that the two-point fit exactly reproduces $\tau$ and $\theta$ for a pure FOPDT process. For higher-order processes, the fit minimizes least-squares error in the dominant pole.
```


### Why 35.3% and 85.3%?  -  A Quick Derivation Sketch
For a true FOPDT signal, $y(t) = KM(1 - e^{-(t-\theta)/\tau})$ for $t \geq \theta$. The time at which the response reaches a fraction $f$ of the ultimate is


$$
y/y(\infty) = f  \Longrightarrow  1 - e^{-(t-\theta)/\tau} = f  \Longrightarrow  t - \theta = -\tau \ln(1 - f)
$$


So


$$
t_f = \theta + \tau [-\ln(1-f)]
$$


For two fractions $f_1$ and $f_2$, the two times are


$$
\begin{align}
t_{f_1} &= \theta + \tau \cdot a,   a \equiv -\ln(1-f_1) \\
t_{f_2} &= \theta + \tau \cdot b,   b \equiv -\ln(1-f_2)
\end{align}
$$


Solving for $\tau$ and $\theta$:


$$
\begin{align}
\tau   &= \frac{t_{f_2} - t_{f_1}}{b - a} \\
\theta &= \frac{a t_{f_2} - b t_{f_1}}{a - b}
\end{align}
$$


The Sundaresan-Krishnaswamy fractions $f_1 = 0.353, f_2 = 0.853$ give $a = -\ln(0.647) = 0.4357$ and $b = -\ln(0.147) = 1.9173$, so $b - a = 1.4816$ and $1/(b - a) = 0.675 \approx 0.67$, and $b/(b-a) - a/(b-a) \cdot (\text{rearranged}) \to$ the textbook constants 1.3 and 0.29. The 0.67 and 1.3/0.29 numbers in the formulas are direct consequences of these two chosen levels.

### Worked Example: Heat-Exchanger Cooling-Water Step

```{prf:example} Fitting a FOPDT to a Cooling-Water Step Test
:label: instrumentationandcontrol-example-2

A heat exchanger's process-outlet temperature is monitored during a step in cooling-water flow. Initial steady state: cooling water $= 8.0$ gpm, outlet $T = 55.0^\circ$F. Step: cooling-water flow stepped to $9.2$ gpm at $t = 0$. New steady state (after sufficient time): $T = 53.2^\circ$F. From the recorded trace, the time at which $T = 54.36^\circ$F (i.e. 35.3% of the change) is 6.3 min, and the time at which $T = 53.5^\circ$F (85.3% of the change) is 9.5 min. Fit a FOPDT model.
```


```{dropdown} Solution Steps
- **Steady-state gain $K$.**


$$
K = \frac{\Delta y_{ss}}{\Delta x} = \frac{T_{\text{new}} - T_{\text{old}}}{Q_{cw,\text{new}} - Q_{cw,\text{old}}} = \frac{53.2 - 55.0}{9.2 - 8.0} = \frac{-1.8}{1.2} = -1.5 \frac{^\circ\text{F}}{\text{gpm}}
$$


Negative as expected (more cooling water lowers process outlet temperature).


- **Identify the 35.3% and 85.3% target temperatures.**


- 35.3% mark: $T_{35.3\%} = 55.0 + 0.353(53.2 - 55.0) = 55.0 + 0.353(-1.8) = 55.0 - 0.635 = 54.365^\circ$F.

- 85.3% mark: $T_{85.3\%} = 55.0 + 0.853(-1.8) = 55.0 - 1.535 = 53.465^\circ$F.

Read from the graph: $t_{35.3\%} = 6.3$ min, $t_{85.3\%} = 9.5$ min.


- **Apply the Sundaresan-Krishnaswamy formulas.**


$$
\begin{align}
\theta &= 1.3 (6.3) - 0.29 (9.5) = 8.19 - 2.755 = 5.435 \approx 5.4 \text{min} \\
\tau   &= 0.67 (9.5 - 6.3) = 0.67 (3.2) = 2.144 \approx 2.14 \text{min}
\end{align}
$$


- **Write the fitted FOPDT model.**

$$
G(s) = \frac{-1.5 e^{-5.4 s}}{2.14 s + 1}  \frac{^\circ\text{F}}{\text{gpm}}   (\theta, \tau \text{ in min})
$$

```


```{dropdown} Solution Steps
- **Controllability check.**


$$
\frac{\theta}{\tau} = \frac{5.4}{2.14} = 2.52
$$


This is a dead-time-dominant process ($\theta/\tau > 1$). PI control alone will be sluggish  -  the controller cannot see any effect of its own action for $\theta = 5.4$ min after the action. Strategies for dead-time-dominant processes:


- **Smith Predictor:** a model-based scheme that effectively cancels the dead time inside the loop, allowing the controller to be tuned as if for a pure first-order process.

- **Feedforward control:** measure the disturbance and counter-act before it propagates through the dead time.

- **Model Predictive Control (MPC):** explicitly accounts for dead time over a finite horizon.


- **Verification by reconstructing one point.** Predict the time at which $T$ reaches 50% of the change:


$$
\begin{align}
T_{50\%} &= 55.0 + 0.5(-1.8) = 54.10^\circ\text{F} \\
1 - e^{-(t - \theta)/\tau} &= 0.50  \Longrightarrow  t - \theta = \tau \ln(2) = 2.14 (0.693) = 1.485 \text{min} \\
t &= 5.4 + 1.485 = 6.88 \text{min}
\end{align}
$$


Compare to the graphical reading at $T = 54.1^\circ$F. If the graph gives $t \approx 7$ min, the fit is consistent.
```


### Worked Example: Higher-Order Process Fit to FOPDT

```{prf:example} Two-Lag Process Approximated as FOPDT
:label: instrumentationandcontrol-example-3

A second-order overdamped process has the true transfer function $G_{\text{true}}(s) = 1/[(5s+1)(s+1)]$ (gain 1, two time constants 5 and 1). A step test of magnitude 1 is run. From the resulting trace, the 35.3% time is 2.6 and the 85.3% time is 8.0 (dimensionless). Fit an apparent FOPDT and comment on the quality.
```


```{dropdown} Solution Steps
- **Gain:** since $\lim_{s\to 0} G_{\text{true}}(s) = 1$, $K = 1$ as expected.

- **Apparent FOPDT parameters:**


$$
\begin{align}
\theta_{\text{app}} &= 1.3 (2.6) - 0.29 (8.0) = 3.38 - 2.32 = 1.06 \\
\tau_{\text{app}}   &= 0.67 (8.0 - 2.6) = 0.67 (5.4) = 3.62
\end{align}
$$


- **Interpretation:** The dominant true time constant is 5, the secondary is 1. The fit recovers $\tau_{\text{app}} = 3.62$ (an underestimate of the dominant pole because the secondary pole hides behind it) and gives a nonzero $\theta_{\text{app}} = 1.06$ that mimics the secondary lag with an equivalent dead time. The empirical rule of thumb is $\theta_{\text{app}} \approx$ the smaller time constant, $\tau_{\text{app}} \approx$ the larger one  -  here $\theta_{\text{app}} = 1.06 \approx 1$ ✓, and $\tau_{\text{app}} = 3.62$ (within $\sim$30% of 5).

- **Engineering takeaway:** FOPDT *fits* a higher-order process. The tuning constants computed from the apparent FOPDT will give acceptable, if not optimal, closed-loop behavior. This is the universal industrial practice.
```


```{note}
**Exam Tips  -  FOPDT Identification**
- The Sundaresan-Krishnaswamy method (35.3% / 85.3%) is the standard. Memorize the formulas $\theta = 1.3 t_{35.3} - 0.29 t_{85.3}$, $\tau = 0.67(t_{85.3} - t_{35.3})$.

- Always state $K$ *with its sign.* Direct/reverse acting controller selection depends on it.

- Diagnostic: $\theta/\tau$


- $< 0.1$: tight control with PI is easy.

- $0.1$-$1.0$: classical PID territory.

- $> 1$: dead-time dominant. Plain PI/PID is sluggish; use Smith predictor, feedforward, or MPC.


- Cohen-Coon tuning (covered later) is more accurate than Ziegler-Nichols when $\theta/\tau > 0.3$.
```


## Second-Order Systems: Damping Coefficient
Two first-order processes in series, or a process plus controller, or many intrinsic mechanical and pneumatic devices, produce **second-order** dynamics. Second-order systems are the first family in which the response shape itself  -  monotonic vs. oscillatory  -  depends on a parameter, the **damping coefficient** $\zeta$ (zeta). Understanding $\zeta$ is what lets you predict whether a control loop will be sluggish, snappy, or wildly oscillating.

### Standard Form of the Second-Order Transfer Function

```{note}
The standard form of a second-order transfer function in process control is


$$
G(s) = \frac{Y(s)}{X(s)} = \frac{K}{\tau^2 s^2 + 2 \zeta \tau s + 1}
$$


Three parameters:


- $K$  -  steady-state (process) gain.

- $\tau$  -  the natural period parameter (units of time). The undamped natural frequency is $\omega_n = 1/\tau$.

- $\zeta$  -  the dimensionless damping coefficient (sometimes called the damping ratio).

The denominator constant term is normalized to 1; if you encounter a denominator $a s^2 + b s + c$ with $c \neq 1$, divide numerator and denominator by $c$ first.
```


```{note}
**Putting an Arbitrary Second-Order ODE Into Standard Form**
Given $a y + b y + c y = d x$, take the Laplace transform with $y(0) = y(0) = 0$ and divide through by $c$:


$$
\frac{Y(s)}{X(s)} = \frac{d/c}{(a/c) s^2 + (b/c) s + 1}
$$


Identify


$$
\begin{align}
K           &= d/c \\
\tau^2      &= a/c  \Longrightarrow  \tau = \sqrt{a/c} \\
2\zeta\tau  &= b/c  \Longrightarrow  \zeta = \frac{b}{2 c \tau} = \frac{b}{2 \sqrt{a c}}
\end{align}
$$


The last expression $\zeta = b/(2\sqrt{ac})$ is the form most often used for quick numerical work.
```


### The Five Response Regimes of $\zeta$

```{tip}
**Classification by Damping Coefficient**
For a step input, the second-order time-domain response takes one of five shapes depending on $\zeta$:


- $\zeta > 1$: **overdamped.** Two distinct real poles, monotonic approach to steady state (no oscillation). Like two first-order responses in series. Sluggish.

- $\zeta = 1$: **critically damped.** Two equal real poles. Fastest non-oscillatory response.

- $0 < \zeta < 1$: **underdamped.** Complex-conjugate poles in the left half-plane. Damped oscillations decaying to steady state. The normal target for control tuning.

- $\zeta = 0$: **undamped.** Pure imaginary poles. Sustained sinusoidal oscillation at $\omega_n = 1/\tau$ forever.

- $\zeta < 0$: **unstable.** At least one pole in the right half-plane. Oscillations (if $|\zeta| < 1$) or exponentials (if $|\zeta| > 1$) grow without bound.
```


### Derivation of the Underdamped Step Response
For completeness, here is the path from $G(s)$ to $y(t)$ for the underdamped case ($0 < \zeta < 1$).

```{dropdown} Solution Steps
- **Output transform for a step of magnitude $M$:**


$$
Y(s) = \frac{K}{\tau^2 s^2 + 2\zeta\tau s + 1} \cdot \frac{M}{s} = \frac{K M}{s (\tau^2 s^2 + 2 \zeta \tau s + 1)}
$$


- **Factor the denominator quadratic.** The roots of $\tau^2 s^2 + 2\zeta\tau s + 1 = 0$ are


$$
s = \frac{-2\zeta\tau \pm \sqrt{4\zeta^2\tau^2 - 4\tau^2}}{2\tau^2} = \frac{-\zeta \pm \sqrt{\zeta^2 - 1}}{\tau}
$$


For $\zeta < 1$ the discriminant is negative; write $\sqrt{\zeta^2 - 1} = j\sqrt{1 - \zeta^2}$:


$$
s = -\frac{\zeta}{\tau} \pm j \frac{\sqrt{1 - \zeta^2}}{\tau}
$$


Define the damped frequency $\omega_d = \sqrt{1-\zeta^2}/\tau$ and the decay rate $\alpha = \zeta/\tau$. The poles are $s = -\alpha \pm j \omega_d$.

- **Partial-fraction decomposition.** Write


$$
Y(s) = \frac{KM}{\tau^2} \frac{1}{s (s+\alpha-j\omega_d)(s+\alpha+j\omega_d)} = \frac{A}{s} + \frac{B s + C}{(s+\alpha)^2 + \omega_d^2}
$$


Multiplying through and matching coefficients (standard algebra; details suppressed for compactness) gives


$$
A = K M,   B = -K M,   C = -2 \alpha K M
$$


- **Inverse transform.** Using the damped-sine and damped-cosine pairs from the toolbox:


$$
\begin{align}
L^{-1}\{\frac{s + \alpha}{(s+\alpha)^2 + \omega_d^2}\} &= e^{-\alpha t}\cos(\omega_d t) \\
L^{-1}\{\frac{\omega_d}{(s+\alpha)^2 + \omega_d^2}\} &= e^{-\alpha t}\sin(\omega_d t)
\end{align}
$$


After algebraic recombination,

$$
y(t) = K M [ 1 - \frac{1}{\sqrt{1-\zeta^2}} e^{-\zeta t/\tau}\sin (\frac{\sqrt{1-\zeta^2}}{\tau} t + \phi)]    (0 < \zeta < 1)
$$

where the phase $\phi = \tan^{-1} (\sqrt{1-\zeta^2}/\zeta) = \cos^{-1}(\zeta)$.
```


### Performance Metrics of the Underdamped Response

```{important}
**Closed-Form Metrics in Terms of $\zeta$ and $\tau$**
- **Period of oscillation:** $T = \dfrac{2\pi\tau}{\sqrt{1-\zeta^2}}$. The damped period; the undamped period is $2\pi\tau$.

- **Time to first peak (rise to peak):** $t_p = \dfrac{\pi\tau}{\sqrt{1-\zeta^2}}$ (half the damped period).

- **Overshoot** (fractional excess over the final value at the first peak):


$$
OS = \exp (-\frac{\pi \zeta}{\sqrt{1-\zeta^2}})
$$


- **Decay ratio** (ratio of the second peak height to the first):


$$
DR = OS^{ 2} = \exp (-\frac{2\pi \zeta}{\sqrt{1-\zeta^2}})
$$


- **Quarter-decay target (Ziegler-Nichols target):** $DR = 1/4$ corresponds to $\zeta \approx 0.215$.

- **Settling time (within $\pm$2% of final):** $t_s \approx \dfrac{4\tau}{\zeta}$.
```


### Worked Example: Determining the Damping Coefficient from an ODE

```{prf:example} Stability and Oscillation from a Second-Order ODE
:label: instrumentationandcontrol-example-4

A process is governed by the ODE


$$
\frac{d^2 y}{dt^2} + K \frac{dy}{dt} + 4 y = x(t)
$$


with $y(0) = y'(0) = 0$. The coefficient $K$ (here a real parameter of the process, not a controller gain) can vary. Determine:


- the range of $K$ for which the response is oscillatory,

- the range of $K$ for which the response is overdamped (monotonic and stable).
```


```{dropdown} Solution Steps
- **Laplace transform the ODE.** With zero initial conditions, $L\{y\} = s^2 Y$ and $L\{y\} = s Y$:


$$
s^2 Y + K s Y + 4 Y = X
$$


Factor out $Y$:


$$
Y (s^2 + K s + 4) = X  \Longrightarrow  \frac{Y(s)}{X(s)} = \frac{1}{s^2 + K s + 4}
$$


- **Reduce to standard form.** The denominator constant term is 4; divide numerator and denominator by 4:


$$
\frac{Y(s)}{X(s)} = \frac{1/4}{\tfrac{1}{4} s^2 + \tfrac{K}{4} s + 1}
$$


Match against $\dfrac{K_p}{\tau^2 s^2 + 2\zeta\tau s + 1}$:


$$
\begin{align}
K_p          &= \frac{1}{4} \\
\tau^2       &= \frac{1}{4}  \Longrightarrow  \tau = \frac{1}{2}   (\text{positive root}) \\
2 \zeta \tau &= \frac{K}{4}  \Longrightarrow  \zeta = \frac{K}{8 \tau} = \frac{K}{8 \cdot (1/2)} = \frac{K}{4}
\end{align}
$$


```


```{dropdown} Solution Steps
- **(a) Oscillatory range.** A second-order system oscillates if $|\zeta| < 1$:


$$
|\frac{K}{4}| < 1  \Longrightarrow  -4 < K < 4
$$


*However,* $\zeta < 0$ ($K < 0$) gives unstable, growing oscillations. The transcript's stated answer is the full range $-4 < K < 4$ (oscillatory in form), but for a stable, decaying oscillation you need $0 < K < 4$. The PE-exam convention is to state the full range and then comment on stability separately, so:


$$
-4 < K < 4    \text{oscillatory (any decay direction)}
$$


$$
0 < K < 4    \text{stable, decaying oscillation}
$$


- **(b) Overdamped range.** Overdamped means $\zeta \geq 1$ (and stable):


$$
\frac{K}{4} \geq 1  \Longrightarrow   K \geq 4
$$


At exactly $K = 4$, $\zeta = 1$ (critically damped  -  the boundary).


- **Verification by limit cases.**


- $K = 0$: $\zeta = 0$, undamped. Sustained oscillation at $\omega_n = 1/\tau = 2$ rad/s, period $T_0 = 2\pi/\omega_n = \pi$ s. Consistent with the boundary of oscillatory behavior.

- $K = 4$: $\zeta = 1$, critically damped. Fastest non-oscillatory response. Boundary between (a) and (b).

- $K = 8$: $\zeta = 2$, heavily overdamped. Two real poles at $s = -\alpha \pm \sqrt{\alpha^2 - \omega_n^2}$ with $\alpha = \zeta/\tau = 4$; the slow pole dominates with effective $\tau_{\text{slow}} = 1/(s_{\text{slow}})$.

- $K = -2$: $\zeta = -0.5$, unstable underdamped. Oscillations grow exponentially. Physically, the closed-loop process is unstable.
```


### Worked Example: Quarter-Decay from a Step Test

```{prf:example} Computing $\zeta$ and $\tau$ from an Underdamped Step Response
:label: instrumentationandcontrol-example-5

A pressure-control loop's underdamped step response shows a first peak that overshoots the new steady state by 50% of the step. The second peak overshoots by $50\% \times 50\% = 25\%$ of the step ($DR = 1/4$). The time between the first peak and the next zero-crossing of the deviation is 12 s. Determine $\zeta$ and $\tau$.
```


```{dropdown} Solution Steps
- **Get $\zeta$ from $DR = 1/4$.**


$$
DR = e^{-2\pi\zeta/\sqrt{1-\zeta^2}} = 0.25  \Longrightarrow  -\frac{2\pi\zeta}{\sqrt{1-\zeta^2}} = \ln(0.25) = -1.386
$$


$$
\frac{\zeta}{\sqrt{1-\zeta^2}} = \frac{1.386}{2\pi} = 0.2206
$$


Squaring: $\zeta^2/(1-\zeta^2) = 0.0487$, so $\zeta^2 = 0.0487(1-\zeta^2)$, i.e. $\zeta^2(1+0.0487) = 0.0487$, giving $\zeta^2 = 0.0464$, $\zeta = 0.215$. ✓ The well-known "$\zeta \approx 0.215$ for quarter-decay" result.


- **Get $\tau$ from the period.** The time from one peak to the next zero crossing is a quarter-period:


$$
T/4 = 12  \Longrightarrow  T = 48 \text{s}
$$


Solve $T = 2\pi\tau/\sqrt{1-\zeta^2}$ for $\tau$:


$$
\tau = \frac{T \sqrt{1-\zeta^2}}{2\pi} = \frac{48 \sqrt{1-0.0464}}{2\pi} = \frac{48 \times 0.9766}{6.283} = 7.46 \text{s}
$$


- **Verification.** $\omega_d = \sqrt{1-\zeta^2}/\tau = 0.9766/7.46 = 0.131$ rad/s. Damped period $T = 2\pi/\omega_d = 48$ s. ✓
```


```{note}
**Exam Tips  -  Second-Order Systems**
- Always normalize the denominator so its constant term is 1 *before* reading $\tau$ and $\zeta$. Skipping this step is the most common error.

- For a polynomial $a s^2 + b s + c$, $\zeta = b/(2\sqrt{ac})$, $\tau = \sqrt{a/c}$.

- Quarter-decay ($DR = 1/4$) $\Leftrightarrow \zeta = 0.215$. Memorize.

- Two limiting cases that come up: $\zeta = 1$ (critical damping, fastest non-oscillatory) and $\zeta = 0$ (sustained oscillation at $\omega_n$).

- The Routh-Hurwitz criterion generalizes the stability test to higher-order polynomials. For a second-order $a s^2 + b s + c$ with $a > 0$, the system is stable iff $b > 0$ and $c > 0$  -  equivalent to $\zeta > 0$ in standard form.
```


## Control Valves: The Final Control Element
The control valve is the physical device on the pipe that the controller's output actually moves. Without an adequately-sized control valve with the right characteristic, no amount of clever controller tuning will produce smooth control. The PE exam consistently tests three things: sizing (the $C_v$ equation), characteristic selection (linear vs. equal percentage), and fail-safe action.

### The ISA/ANSI Valve-Sizing Equation for Incompressible Liquids

```{note}
For an incompressible liquid (constant density), the volumetric flow rate through a control valve is


$$
q = C_v \cdot f(\ell) \cdot \sqrt{\frac{\Delta P_v}{G_s}}   \text{(Equation 2)}
$$


- $q$  -  volumetric flow rate. US customary units: US gpm. Metric: m³/h with $K_v$ instead of $C_v$ (see conversion below).

- $C_v$  -  valve flow coefficient. *Definition:* the volumetric flow of water (specific gravity 1) in US gpm that passes through a fully open valve when the pressure drop across the valve is exactly 1 psi. So $C_v$ has units of $\text{gpm}/\sqrt{\text{psi}}$.

- $f(\ell)$  -  the valve characteristic, a dimensionless function of the lift $\ell$ (fraction open, $0 \leq \ell \leq 1$). The three classical forms are presented below.

- $\Delta P_v$  -  the pressure drop across the valve *only* (not the whole system) in psi. This is the single most error-prone variable in valve sizing because students confuse $\Delta P_v$ with the total system $\Delta P$.

- $G_s$  -  specific gravity of the liquid (dimensionless, water = 1).

Limitations: Equation 2 is valid for incompressible liquids only. For gases, the equation must be modified with an expansion factor $Y$ and a choked-flow check. For two-phase flow, use the Sheldon-Schnelle or Diehl-Lockhart-Martinelli correlations.
```


```{important}
**Unit Conversions**
US: $C_v$ in gpm/$\sqrt{\text{psi}}$, $q$ in gpm, $\Delta P_v$ in psi.

Metric: $K_v$ in m³/h/$\sqrt{\text{bar}}$, $q$ in m³/h, $\Delta P_v$ in bar.


$$
K_v \approx 0.865 C_v   C_v \approx 1.156 K_v
$$


A third coefficient $A_v$ in SI (m²) is sometimes used: $A_v = 2.4 \times 10^{-5} C_v$.
```


### The Three Classical Valve Characteristics

```{tip}
**$f(\ell)$ for Inherent Characteristics**
"Inherent" means measured at constant $\Delta P_v$  -  as if the valve were on a test bench, not installed in a system.


- **Linear:** $f(\ell) = \ell$. Equal increments of lift produce equal increments of flow. Slope $df/d\ell = 1$, constant.

- **Equal percentage:** $f(\ell) = R^{ \ell - 1}$ where $R$ is the **rangeability** or rangeability ratio (typical values 20-50; common is 50). Slope $df/d\ell = R^{ \ell - 1} \ln R = f \cdot \ln R$. *Equal fractional* increments of lift produce equal fractional increments of flow  -  hence the name.

- **Quick opening:** $f(\ell) \approx \sqrt{\ell}$ or similar. Most of the flow appears at small lift, with diminishing returns at high lift. Slope $df/d\ell$ is largest near $\ell = 0$. Used for safety-shutoff and bypass valves *only*, never for modulating control.

At $\ell = 0$ all three give $f \to 0$; at $\ell = 1$ all give $f = 1$. The shapes between those endpoints differ dramatically.
```


### Inherent vs. Installed Characteristic

```{note}
**Why the Installed Characteristic Differs from the Inherent One**
On a real plant, the control valve is in series with a long run of piping, fittings, possibly heat exchangers, and other equipment. The total system pressure drop from a fixed-pressure source to a fixed-pressure sink is fixed, but how it is divided between the valve and the rest of the system depends on flow rate:


$$
\Delta P_{\text{total}} = \Delta P_v(q) + \Delta P_{\text{piping}}(q)
$$


$\Delta P_{\text{piping}}$ grows roughly as $q^2$ (Darcy-Weisbach friction). As $q$ increases, $\Delta P_{\text{piping}}$ rises and $\Delta P_v = \Delta P_{\text{total}} - \Delta P_{\text{piping}}$ falls. Therefore:


- At low $q$ (valve mostly throttled), $\Delta P_v \approx \Delta P_{\text{total}}$.

- At high $q$ (valve wide open), $\Delta P_v$ may be only a small fraction of $\Delta P_{\text{total}}$.

This shifts the apparent $f$-versus-$\ell$ relationship. The *installed* characteristic is what you actually get when the valve is in service; the *inherent* characteristic is what the manufacturer's catalogue tells you.
```


```{tip}
**Two Key Consequences for Valve Selection**
- A **linear** inherent valve becomes **nonlinear** (concave-down) when installed  -  the slope $dq/d\ell$ drops at high flow, so the loop gain decreases at high flow.

- An **equal-percentage** inherent valve becomes **more linear** when installed  -  the natural curvature of the equal-percentage characteristic partially cancels the curvature introduced by the piping.

This is the *reason* equal-percentage is the dominant industrial choice: it gives a more constant loop gain over the operating range when the valve is in a system with significant fixed piping.

**Design rule of thumb (Hutchinson):** Let $\beta = \Delta P_v / \Delta P_{\text{total}}$ at maximum design flow.


- $\beta > 0.5$ (valve takes the majority of system $\Delta P$): use **linear**.

- $\beta < 0.5$ (piping takes the majority): use **equal percentage**.

The crossover $\beta = 0.25$-$0.33$ is often a useful target for new designs.
```


### Worked Example: Linear vs. Equal-Percentage Lift Calculation

```{prf:example} Required Lift for Two Pressure-Drop Scenarios
:label: instrumentationandcontrol-example-6

A control valve with $C_v = 110$ gpm/$\sqrt{\text{psi}}$ must pass 200 gpm of water ($G_s = 1$). Find the required lift for (a) inherent conditions with constant $\Delta P_v = 10$ psi, and (b) installed conditions with $\Delta P_v = 10 - 0.03 q$ psi. Repeat the analysis for an equal-percentage valve with rangeability $R = 40$.
```


```{dropdown} Solution Steps
- **Solve Equation 2 for the valve characteristic value $f$ regardless of valve type:**


$$
f(\ell) = \frac{q}{C_v} \sqrt{\frac{G_s}{\Delta P_v}}
$$


- **Linear inherent, (a) $\Delta P_v = 10$ psi, $f = \ell$:**


$$
\ell_{a,\text{lin}} = \frac{200}{110} \sqrt{\frac{1}{10}} = 1.818 \times 0.3162 = 0.575
$$


- **Linear installed, (b) compute the actual $\Delta P_v$ at the design flow:**


$$
\Delta P_v(q=200) = 10 - 0.03(200) = 10 - 6 = 4 \text{psi}
$$


*Note: less valve pressure drop because the rest of the system is taking 6 psi at this flow.* Then


$$
\ell_{b,\text{lin}} = \frac{200}{110} \sqrt{\frac{1}{4}} = 1.818 \times 0.500 = 0.909
$$


The installed linear valve is at 91% lift  -  close to fully open. Little upward authority remains.


- **Equal percentage, (a):** the $f$ value is the same as the linear case (0.575) because $f$ depends only on $q$, $C_v$, $G_s$, $\Delta P_v$. Solve $R^{\ell - 1} = f$:


$$
\ell = 1 + \frac{\log_{10} f}{\log_{10} R} = 1 + \frac{\log_{10}(0.575)}{\log_{10}(40)} = 1 + \frac{-0.2403}{1.6021} = 1 - 0.150 = 0.850
$$


- **Equal percentage, (b):** $\Delta P_v = 4$ psi so $f = 200/110 \cdot \sqrt{1/4} = 0.909$ (same as the linear installed case in step 3, because $f$ doesn't depend on the valve type). Then


$$
\ell = 1 + \frac{\log_{10}(0.909)}{\log_{10}(40)} = 1 + \frac{-0.0414}{1.6021} = 1 - 0.026 = 0.974
$$


```


```{dropdown} Solution Steps
- **Summary table:**


- Linear inherent: $\ell = 0.575$

- Linear installed: $\ell = 0.909$

- Equal-pct inherent: $\ell = 0.850$

- Equal-pct installed: $\ell = 0.974$


- **Engineering interpretation.**


- For the linear valve, the lift jumps from 0.575 (inherent) to 0.909 (installed) at the same flow. A real plant operator would see a valve that is 91% open and would conclude there is little room to handle an upset that demands even more flow.

- For the equal-pct valve, both lifts (0.850 and 0.974) are also near full open  -  but importantly, the slope $df/d\ell = f \ln R$ at the high-$f$ end is much steeper than the linear-valve slope, so a small lift change produces a large flow change. This means *this $C_v$ is too large* or the design flow is too high a fraction of the valve's range.

- **Designer's response:** pick a valve with a smaller $C_v$ so that at design flow the lift falls in the recommended 0.30-0.75 range (some references say 0.20-0.80). Re-do the calculation. The valve must have enough $C_v$ to pass the maximum required flow ($\sim$1.2-2.0 $\times$ design) at $\ell \approx 0.9$, and not so much $C_v$ that the minimum required flow drives the valve below $\ell = 0.1$ (poor controllability near the seat).


- **Verification of the equal-pct algebra.** Direct check: with $R = 40$ and $\ell = 0.850$, $f = 40^{0.850 - 1} = 40^{-0.15} = e^{-0.15 \ln 40} = e^{-0.5527} = 0.575$. ✓
```


### Loop Gain and Why Constant Loop Gain Matters

```{note}
**Valve Gain  -  The Slope of the Installed Characteristic**
The **valve gain** $K_v(\ell) \equiv dq/d\ell$ is the local sensitivity of the flow to a lift change. The overall **loop gain** of a control loop is the product of the process gain, the controller proportional gain, the sensor gain, and the valve gain:


$$
K_{\text{loop}} = K_p \cdot K_c \cdot K_s \cdot K_v
$$


For stable, well-damped control, this product should be approximately constant over the operating range. The process gain is set by physics, the sensor gain by calibration, and the controller gain is fixed by the tuning. So the only knob the valve designer has to keep the loop gain constant is the valve characteristic. An equal-percentage valve gives $K_v \propto f \propto q$ (in inherent form), which is constant on a logarithmic scale  -  exactly the property needed to compensate for a process whose gain decreases with throughput (most processes).
```


### Choked Flow  -  The Upper Limit on Equation 2

```{note}
**Liquid Choking (Cavitation and Flashing)**
Equation 2 predicts that flow rises indefinitely as $\Delta P_v$ rises. In reality, when the pressure at the valve's vena contracta falls below the liquid's vapor pressure $P_v$, vapor bubbles form (cavitation) or the bulk liquid flashes. Past this point, additional $\Delta P_v$ does not increase the flow.

The ISA-defined choked-flow limit:


$$
\Delta P_{\text{choked}} = F_L^2 (P_1 - F_F P_v)
$$


where $F_L$ is the liquid-recovery factor (typical 0.6-0.9), $F_F$ is the liquid critical-pressure ratio factor $\approx 0.96 - 0.28\sqrt{P_v/P_c}$. If $\Delta P_v < \Delta P_{\text{choked}}$ flow scales with $\sqrt{\Delta P_v}$ (Equation 2); if $\Delta P_v > \Delta P_{\text{choked}}$ flow saturates at $C_v\sqrt{\Delta P_{\text{choked}}/G_s}$.

Cavitation is destructive  -  the imploding bubbles erode trim. If predicted in service, specify anti-cavitation trim (multistage, drilled, or path-trim valves).
```


### Compressible (Gas) Flow Through Control Valves

```{important}
**ISA Gas-Sizing Equation (Subcritical)**
For a compressible gas with upstream pressure $P_1$, downstream pressure $P_2$, ratio of specific heats $k = c_p/c_v$:


$$
q_{\text{std}} = 1360 C_v F_p P_1 Y \sqrt{\frac{x}{M T_1 Z}}
$$


where $q_{\text{std}}$ is in scfh, $P_1$ in psia, $T_1$ in $^\circ$R, $M$ is molecular weight, $Z$ is compressibility, $x = (P_1 - P_2)/P_1$ is the pressure-ratio drop, and $Y$ is the expansion factor


$$
Y = 1 - \frac{x}{3 F_k x_T}
$$


with $F_k = k/1.40$ and $x_T$ a valve-style modifier (0.6-0.8 typical).

**Choked-flow limit for gases:** when $x \geq F_k x_T$, $Y = 2/3$ and flow saturates; further $\Delta P$ has no effect (the flow at the vena contracta has reached sonic velocity). For air, $k = 1.40$ so $F_k = 1$; choked when $P_2/P_1 \leq 0.53$ (typical valve).
```


```{note}
**Exam Tips  -  Control-Valve Sizing**
- Memorize the liquid sizing equation and its US units (gpm, psi, gpm/$\sqrt{\text{psi}}$). The conversion to metric $K_v$ ($0.865 C_v$) is testable.

- $\Delta P_v$ is the drop *across the valve* alone, never the total system $\Delta P$.

- Equal-percentage valves are the default for processes with significant piping pressure drop; linear valves are used only when the valve takes more than half the total system $\Delta P$.

- Design lift should land between 0.3 and 0.75 (some say 0.2-0.8) at normal flow. Outside that band, replace with a more appropriately sized valve.

- Cavitation predicted in service requires anti-cavitation trim.
```


## Fail-Safe Valve Action
Every control valve in a chemical plant must be specified with a **fail-safe action**  -  the position the valve assumes when its motive power (typically instrument air, 3-15 psi or 4-20 mA via I/P converter) is lost. This is a safety decision driven by the worst-case consequences of loss-of-power. Both local and downstream consequences must be considered.

### The Two Failsafe Modes

```{tip}
**Failsafe Modes and Their Aliases**
- **Fail-Open (FO).** Synonym: **Air-To-Close (ATC)**. On loss of air, the valve drives *open*. To close it, the controller must *supply* air pressure  -  hence "air to close."

- **Fail-Closed (FC).** Synonym: **Air-To-Open (ATO)**. On loss of air, the valve drives *closed*. To open it, the controller must supply air  -  hence "air to open."

The fail-direction is set mechanically by the spring inside the diaphragm actuator. A direct-acting actuator has the spring pushing the stem up (fail-down for a globe valve with flow-to-open); a reverse-acting actuator does the opposite. A solenoid in the air line provides additional failsafe enforcement for shutdown valves (SDVs).
```


### Sign Convention and Controller Direct/Reverse Action

```{note}
The valve's mechanical fail-direction determines the sign of the *valve gain* as seen by the controller. By convention:


- **Fail-Closed (ATO):** valve gain $K_v > 0$. Increasing controller output (4 $\to$ 20 mA) increases lift and increases flow.

- **Fail-Open (ATC):** valve gain $K_v < 0$. Increasing controller output decreases lift and decreases flow.

For the closed loop to have stable negative feedback, the product of all gains (process, sensor, valve, controller) must be positive. The controller's *direct/reverse* switch is set to make this so:


- Controller **reverse acting** ($K_c > 0$ conventional): output *decreases* when measurement rises.

- Controller **direct acting** ($K_c < 0$): output *increases* when measurement rises.

The combination is dictated by "negative feedback always."
```


```{important}
**Quick Action-Selection Table**
For a temperature loop heating with steam (FC valve, $K_v > 0$, process gain $K_p > 0$ since more steam = more temperature):


- Measurement rises $\to$ want to close the valve $\to$ controller output should fall $\to$ **reverse acting**.

For a temperature loop cooling with cooling water (FO valve, $K_v < 0$, process gain $K_p < 0$):


- Two negatives multiply to positive overall. Use **reverse acting** again.

The simple rule: if the product $K_p \cdot K_v > 0$, use **reverse**; if $< 0$, use **direct**.
```


### Fail-Safe Selection Heuristics

```{tip}
**Rule-of-Thumb Fail-Safe Decisions**
- Cooling water on an exothermic reactor or hot heat exchanger: **Fail-Open**. (Loss of cooling could cause runaway; keep coolant flowing.)

- Steam to a reboiler, heater, or jacketed reactor: **Fail-Closed**. (Loss of cooling water + hot steam = bad. Cut the heat source.)

- Reactor feed when downstream cannot handle off-spec: **Fail-Closed**.

- Fuel gas to a furnace: **Fail-Closed**. (Avoid feeding fuel into a furnace with a possibly extinguished flame.)

- Combustion air to a furnace: **Fail-Open**. (Avoid fuel-rich, explosive mixture.)

- Vent or relief: **Fail-Open**. (Always vent when uncertain.)

- Drain on a containment vessel: **Fail-Closed**. (Maintain containment.)

- Chemical injection of a hazardous reagent: **Fail-Closed**. (Stop adding hazard when uncertain.)

These are heuristics  -  the actual decision is made in a HAZOP study weighing local and global consequences.
```


### Worked Example: Two Service Scenarios

```{prf:example} Selecting Fail-Safe Action for Two Valves
:label: instrumentationandcontrol-example-7

**(a)** A control valve regulates cooling water flow to a shell-and-tube exchanger that cools a 220°C exothermic reactor effluent before downstream separation.

**(b)** A control valve regulates the discharge from a wastewater pH-neutralization tank to a downstream biological treatment plant.

Select the fail-safe action for each and justify both locally and globally.
```


```{dropdown} Solution Steps
- **(a) Cooling-water valve.**


- *Loss-of-air scenario A1: valve fails closed.* Cooling water stops. Reactor effluent enters the exchanger hot and exits hotter. Heat exchanger tubes may exceed their design temperature; if the process fluid has organic peroxide or other thermal-decomposition risk, runaway can ensue. Downstream: hot process fluid reaching a low-temperature-rated distillation column tray, a fired heater knockout drum, or a polishing tank could vaporize, pressurize, or boil. **Unacceptable.**

- *Loss-of-air scenario A2: valve fails open.* Cooling water flows at maximum. Worst case: process fluid is cooled below its design lower limit (possible freeze-up of high-pour-point streams, viscosity rise, or undesirable phase change). Generally tolerable for a short time; the reactor's protective interlocks have time to intervene.

- **Selection: Fail-Open (ATC).** Keep coolant flowing on power loss.


- **(b) Wastewater discharge valve.**


- *Scenario B1: valve fails closed.* Wastewater is held in the neutralization tank. The tank capacity may be exceeded if the inflow continues for a long outage  -  a high-level alarm and operator response are required, but the local consequence is bounded by tank volume.

- *Scenario B2: valve fails open.* Wastewater of possibly off-spec pH (the neutralization control loop is also lost during a power outage) flows continuously to the bio-treatment plant. The biological organisms can be killed by a pH shock or by a slug of toxic substance; the bio-plant takes days to repopulate. Regulatory permit violation is likely.

- **Selection: Fail-Closed (ATO).** Contain the wastewater until controls are restored.


- **The general lesson:** "fail safe" does not mean "fail in the direction of the normal operating point." It means "fail in the direction of lower consequence," which is determined by what can go wrong downstream, not by what is comfortable now. HAZOP studies systematically test each control valve against each possible failure scenario; the fail-safe decision is one of the outputs of HAZOP.


- **Verification consistency check.** Note that in both examples the fail-safe state moves the process toward the lower-consequence direction:


- (a) Default to cooling = always erring on the side of cooler-and-safer.

- (b) Default to containment = always erring on the side of not-releasing-anything-bad.

Memorize the heuristic "protect people first, equipment second, product third."
```


```{note}
**Exam Tips  -  Fail-Safe Selection**
- Read the entire scenario before answering. The PE-exam fail-safe questions almost always have a hidden downstream consequence. Don't fixate on the immediate unit operation.

- Memorize the alias pairs: FO = ATC, FC = ATO. A controller asking for "air to open" is FC, not FO.

- Sign convention: FC valve has $K_v > 0$, FO has $K_v < 0$. Match to process gain to choose direct/reverse controller action.

- The default for hydrocarbon service is FC; for cooling-utility-supply service, FO.
```


## Inherent vs. Installed Characteristics: Deep Dive and Graphical Interpretation
We touched on inherent vs. installed in the control-valve section; this section gives the complete graphical and algebraic treatment that the transcript walks through and that the PE exam expects.

### Setup: A Valve in a System

```{note}
Imagine a pipe segment from a fixed-pressure source $P_{\text{source}}$ to a fixed-pressure sink $P_{\text{sink}}$. In series: piping + fittings + a control valve. The system mechanical-energy balance is


$$
P_{\text{source}} - P_{\text{sink}} = \Delta P_{\text{piping}}(q) + \Delta P_v(q)
$$


where $\Delta P_{\text{piping}}$ scales roughly as $f \cdot L_e \cdot \rho v^2/(2D)$, i.e. approximately quadratically in $q$. The valve drop is whatever is left over.
```


```{note}
**Two Limiting Cases**
- **Valve dominates ($\beta \to 1$):** the valve takes nearly all the system $\Delta P$. The installed characteristic essentially equals the inherent one. Choose linear.

- **Piping dominates ($\beta \to 0$):** the piping takes nearly all the system $\Delta P$. The valve sees only a tiny $\Delta P_v$ at high flow. The installed characteristic is heavily distorted from the inherent one. Choose equal percentage.

where $\beta = \Delta P_v / \Delta P_{\text{total}}$ at design flow.
```


### Graphical Interpretation: Four Curves on One Plot
On a standard "flow vs. lift" plot, four curves can be drawn for a given valve and system:

- Linear inherent: straight line from (0, 0) to (1, $q_{\max}^{\text{inh}}$).
- Linear installed: concave-down curve  -  starts steep, flattens at high lift.
- Equal-pct inherent: convex-up curve  -  starts flat, steepens at high lift.
- Equal-pct installed: nearly straight line in the middle range, the curvatures partially cancel.

The fact that the equal-pct installed curve is the straightest of the four is the central practical reason equal-pct dominates industry use.

### Worked Example: Valve Gain as a Function of Lift

```{prf:example} Comparing $dq/d\ell$ for Linear and Equal-Pct at Two Operating Points
:label: instrumentationandcontrol-example-8

For the system in the previous worked example ($C_v = 110$, water, design flow 200 gpm), compute the valve gain $dq/d\ell$ at $\ell = 0.5$ and $\ell = 0.9$ for both characteristics. Use the installed pressure-drop relationship $\Delta P_v = 10 - 0.03 q$.
```


```{dropdown} Solution Steps
- **Setup.** For each characteristic and lift, solve $q = C_v f(\ell) \sqrt{(10 - 0.03 q)/1}$ implicitly for $q$, then approximate $dq/d\ell \approx [q(\ell + 0.01) - q(\ell - 0.01)]/0.02$.

- **Linear, $\ell = 0.5$.** $q = 55 \sqrt{10 - 0.03 q}$. Iterate:


- Guess $q = 150$: RHS $= 55\sqrt{10 - 4.5} = 55\sqrt{5.5} = 55(2.345) = 129$. Lower.

- Try $q = 130$: RHS $= 55\sqrt{10 - 3.9} = 55\sqrt{6.1} = 55(2.470) = 136$.

- Try $q = 136$: RHS $= 55\sqrt{10 - 4.08} = 55\sqrt{5.92} = 55(2.433) = 134$.

- Converged at $q \approx 135$.

Repeat for $\ell = 0.51, 0.49$ to get gain $\approx 270$ gpm/lift.

- **Linear, $\ell = 0.9$.** $q = 99 \sqrt{10 - 0.03 q}$. Iterate:


- Guess $q = 200$: RHS $= 99\sqrt{4} = 198$. Converged.

Compute gain near $\ell = 0.9$: $\approx 130$ gpm/lift (much smaller).

- **Equal-pct, $\ell = 0.5$, $R = 40$.** $f = 40^{-0.5} = 1/\sqrt{40} = 0.158$. Then $q = 110(0.158)\sqrt{10 - 0.03 q}$:


- Iterate around $q = 55$: $q = 17.4\sqrt{10 - 1.65} = 17.4\sqrt{8.35} = 17.4(2.89) = 50.3$. Iterate to convergence $\approx 51$.

Gain near $\ell = 0.5$: small (because $f$ is small).

- **Equal-pct, $\ell = 0.9$.** $f = 40^{-0.1} = 0.692$. $q = 110(0.692)\sqrt{10 - 0.03 q} = 76.1\sqrt{...}$:


- Iterate around $q = 180$: $76.1\sqrt{10 - 5.4} = 76.1\sqrt{4.6} = 163$. Try $q = 165$: $76.1\sqrt{5.05} = 171$. Converged at $\approx 170$.

Gain near $\ell = 0.9$: large (because $f$ is large and equal-pct has $df/d\ell = f \ln R$).

- **Comparison.** The linear valve's gain *drops* from 270 to 130 across the operating range  -  the loop becomes sluggish at high flow. The equal-pct valve's gain *rises* across the same range  -  but the multiplication by the falling process gain (which usually decreases with throughput) tends to cancel, giving more constant loop gain overall. This is the algebraic statement of the heuristic that equal-pct is preferred in installed conditions.
```


```{note}
**Exam Tips  -  Inherent vs. Installed**
- "Inherent" = constant $\Delta P_v$; "installed" = variable $\Delta P_v$ that decreases as flow rises.

- Linear $\to$ nonlinear (concave-down) when installed; equal-pct $\to$ more linear.

- The choice between linear and equal-pct hinges on $\beta = \Delta P_v/\Delta P_{\text{total}}$ at design flow. Above $\sim$0.5: linear OK. Below: equal-pct.

- Aim for design lift between 0.3 and 0.75 with the valve sized so it doesn't bottom out near the seat at low flow or saturate near full open at high flow.
```


## Sensors and Transmitters
The sensor (or primary element) physically detects the process variable; the transmitter converts the raw sensor signal into a standardized current (4-20 mA) or pneumatic (3-15 psi) signal that the controller can read.

### Direct vs. Indirect Sensors

```{note}
- **Direct sensors** measure the controlled variable itself. A thermocouple measures temperature directly through the Seebeck thermoelectric effect.

- **Indirect sensors** infer the controlled variable from a related measurable quantity. A Venturi or orifice flowmeter measures the pressure drop across a constriction and computes flow from Bernoulli's equation. A binary-system distillation tray-temperature sensor uses the $T$-$x$-$y$ equilibrium diagram to infer composition from temperature plus pressure.
```


### Sensor Vocabulary

```{tip}
- **Range:** the low and high values to which the sensor is calibrated (e.g. 50-250 psi or $-50$ to $+100^\circ$C).

- **Zero:** the low end of the range. *Not necessarily 0.* In the examples above, the zeros are 50 psi and $-50^\circ$C respectively.

- **Span:** the difference high $-$ low. For the examples: 200 psi and 150°C.

- **Turndown (rangeability):** the ratio of the highest reliably-readable value to the lowest. A Coriolis flowmeter with turndown 100:1 can read accurately from 1% to 100% of full scale; an orifice plate with turndown 4:1 is only reliable from 25% to 100%.

- **Accuracy:** closeness to true value. Usually quoted as $\pm$% of span (e.g. "$\pm$0.5% of span") or $\pm$% of reading.

- **Resolution:** smallest detectable change.

- **Time constant $\tau_s$:** the sensor itself has dynamics, modeled (for slow sensors) as first-order. For thermowells, $\tau_s$ can be 10-60 s; for direct thermocouples in fluid, 1-5 s; for pressure transmitters, $< 0.1$ s. When $\tau_s$ is small compared to the process $\tau$, the sensor block in the loop diagram is approximated as zero-order (instantaneous).

- **Dead time $\theta_s$:** from sample-line transport, analyzer cycle time (gas chromatograph), or digital scan rate.
```


### Common Sensor Types by Variable

```{tip}
**Sensor Catalogue**
**Temperature:**


- *Thermocouple* (T, J, K, E, etc.): junction of two dissimilar metals; voltage proportional to $T$. Robust, cheap, wide range, lower accuracy ($\pm$1-2°C).

- *RTD (Pt-100, Pt-1000):* platinum resistance increases linearly with $T$. Accurate ($\pm$0.1°C), slower than TC.

- *Thermistor:* semiconductor with strongly nonlinear $R(T)$; high sensitivity, narrow useful range (typ. $-50$ to $+150^\circ$C).

- *Infrared pyrometer:* non-contact, used above 500°C or where touching is impractical.

- *Bimetallic thermometer:* on-board mechanical readout; no electrical output unless modified.

**Pressure:**


- *Bourdon tube:* mechanical, local-readout gauge.

- *Diaphragm with strain gauge:* electronic transmitter. Standard.

- *Capacitance cell:* very-low-pressure measurement (inches H$_2$O).

- *Piezoelectric:* transient pressure (combustion, shock).

**Flow:**


- *Orifice plate:* cheap, ubiquitous, $\sim$\$ vs. Coriolis but high permanent loss; turndown $\sim$4:1.

- *Venturi:* similar idea, lower permanent loss (5-15% of $\Delta P$).

- *Coriolis:* mass-flow, very accurate ($\pm$0.1%), works on any fluid including slurries, expensive.

- *Magnetic (mag meter):* conductive liquids only; no obstruction; high turndown.

- *Turbine:* rotor-spin counting; clean liquids; moderate accuracy.

- *Ultrasonic transit-time:* clamp-on for retrofits; clean liquids best.

- *Vortex shedding:* bluff body sheds vortices at frequency proportional to flow; rangeability 20:1.

**Level:**


- *Differential pressure (DP):* the classical method. Measure $\Delta P$ between a tap at the bottom and a tap at the top (or atmosphere); $h = \Delta P / (\rho g)$.

- *Guided-wave radar:* sends a microwave pulse down a probe; reflection from liquid surface gives level. Independent of $\rho$.

- *Ultrasonic:* echo from liquid surface, top-mounted.

- *Capacitance:* probe acts as one plate of a capacitor, liquid as the dielectric.

- *Float:* mechanical, the oldest reliable method.

- *Load cells on the vessel:* weigh the contents; gives mass, not level.

**Composition:**


- *Gas chromatograph (GC):* accurate, broad, slow (cycle time 2-30 min). Adds dead time to the loop.

- *IR/UV/NIR analyzer:* continuous, fast, specific to a molecular bond.

- *Mass spectrometer:* fast, accurate, expensive.

- *pH electrode:* potentiometric; needs frequent calibration.

- *Conductivity probe:* dissolved-ion concentration.
```


### The 4-20 mA Standard

```{note}
The industry-standard transmitter output is a current loop ranging from 4 mA at the low end of the sensor range to 20 mA at the high end. Two design reasons for the 4 mA "live zero" (rather than 0 mA):


- A broken wire or dead transmitter shows 0 mA  -  distinguishable from a real low-end reading. The controller knows the loop is dead and can alarm.

- The transmitter can be loop-powered (the 4-20 mA current carries power as well as signal), removing the need for a separate power line.
```


```{important}
**Calibration Equations**
Linear map between measurement and 4-20 mA current:


$$
I [\text{mA}] = 4 + 16 \cdot \frac{\text{measurement} - \text{zero}}{\text{span}}
$$


$$
\text{measurement} = \text{zero} + \text{span} \cdot \frac{I - 4}{16}
$$


**Percent of span (%TO):**


$$
\%\text{TO} = 100 \cdot \frac{\text{measurement} - \text{zero}}{\text{span}} = \frac{I - 4}{16} \cdot 100
$$


```


### Worked Example: 4-20 mA Loop Calibration

```{prf:example} Reading and Setting Alarms on a 4-20 mA Loop
:label: instrumentationandcontrol-example-9

A pressure transmitter has range 50-250 psi. The controller's analog input reads 12.8 mA.


- What is the measured pressure?

- The operator wants a high-pressure alarm at 200 psi. What is the alarm trip in mA?

- The operator wants the controller to issue a low-pressure shutdown at 75 psi. What is the trip in mA?
```


```{dropdown} Solution Steps
- **Range, zero, span.** Range = 50-250 psi. Zero = 50 psi. Span = 250 - 50 = 200 psi.

- **(a) 12.8 mA $\to$ pressure.**


$$
\%\text{TO} = \frac{12.8 - 4}{16} \times 100 = \frac{8.8}{16} \times 100 = 55.0\%
$$


$$
P = 50 + 0.55(200) = 50 + 110 = 160 \text{psi}
$$


- **(b) 200 psi $\to$ mA.**


$$
\%\text{TO} = \frac{200 - 50}{200} \times 100 = 75.0\%
$$


$$
I = 4 + 16(0.75) = 4 + 12 = 16.0 \text{mA}
$$


- **(c) 75 psi $\to$ mA.**


$$
\%\text{TO} = \frac{75 - 50}{200} \times 100 = 12.5\%
$$


$$
I = 4 + 16(0.125) = 4 + 2 = 6.0 \text{mA}
$$


- **Verification by midpoint.** Mid-range pressure 150 psi $\to$ %TO $= 50\%$ $\to$ $I = 4 + 8 = 12$ mA. ✓ Linear calibration confirmed.


- **Practical note on alarm settings.** A 6 mA low-trip is close to the 4 mA live zero  -  if the loop opens, the controller would also see $< 6$ mA. Modern DCS systems distinguish "signal within range, low alarm" from "signal failure" by checking for $I < 3.8$ mA or $> 20.5$ mA (out-of-range diagnostic).
```


```{note}
**Exam Tips  -  Sensors and Transmitters**
- Zero is the *low end of the range*, not the absolute zero of the measurement scale.

- Span = high $-$ low.

- 4 mA = 0% TO = low end of range. 20 mA = 100% TO = high end.

- Span is what divides the 16 mA of signal range, not the absolute high value.

- Direct sensors measure the controlled variable; indirect sensors infer it from a related variable (e.g. orifice $\Delta P$ $\to$ flow via Bernoulli).

- Dead time from analyzers (especially GC) is a major control-design driver. A GC with 5-min cycle introduces 5-min sample delay into the loop.
```


## Closed-Loop Block Diagrams and Block-Diagram Algebra
Up to this point we have studied processes, valves, and sensors in isolation. In a real plant, they are wired together with a controller into a *closed loop*: the sensor feeds the controller, which manipulates the valve, which changes the process, which changes what the sensor reads. The standard tool for analyzing closed loops is the **block diagram** and the algebra for combining and reducing such diagrams.

### Building Blocks

```{note}
**Anatomy of a Single Feedback Loop**
A typical feedback control loop consists of these blocks connected in series with one feedback path:


- **Setpoint $r(t)$:** the operator's desired value.

- **Comparator (sum junction):** computes the error $e(t) = r(t) - y_m(t)$, where $y_m$ is the measured value.

- **Controller $G_c(s)$:** computes the manipulated-variable signal $u(t)$ from $e(t)$. For a PID controller, $G_c(s) = K_c(1 + 1/(\tau_I s) + \tau_D s)$.

- **Valve $G_v(s)$:** converts the controller signal to a process input (flow, heat, mass).

- **Process $G_p(s)$:** the physical transformation from input to controlled variable.

- **Disturbance path $G_d(s)$:** an exogenous disturbance $d(t)$ enters at some point in the process.

- **Sensor/transmitter $G_m(s)$:** converts the controlled variable to a measurement signal.
```


```{important}
**Closed-Loop Transfer Functions**
For a unit-feedback loop with forward path $G(s) = G_c G_v G_p$ and feedback path $H(s) = G_m$:


$$
\text{Setpoint response:}   \frac{Y(s)}{R(s)} = \frac{G_c G_v G_p}{1 + G_c G_v G_p G_m}
$$


$$
\text{Load response:}   \frac{Y(s)}{D(s)} = \frac{G_d}{1 + G_c G_v G_p G_m}
$$


The denominator $1 + G_{OL}(s)$, with $G_{OL} = G_c G_v G_p G_m$, is the **characteristic equation**. Its roots are the closed-loop poles. The loop is stable if and only if all roots have negative real parts (Routh-Hurwitz).
```


### The Sensor/Transmitter as a Block

```{note}
The sensor/transmitter is typically modeled as zero-order (instantaneous, gain only) for fast measurements (flow, pressure, level via DP) or as first-order ($K_m / (\tau_m s + 1)$) for slower measurements (thermowell-protected temperature, dissolved oxygen, conductivity). Composition analyzers add dead time $e^{-\theta_m s}$. For block-diagram reduction, the sensor block sits in the feedback path and contributes its own dynamics to the characteristic equation.
```


## PID Controllers  -  Algorithms and Tuning
The Proportional-Integral-Derivative (PID) controller is responsible for an estimated 90%+ of all single-loop control in the world's chemical plants. The PE exam tests three things: knowing what each mode does, knowing when to use which combination, and being able to apply a tuning rule (typically Ziegler-Nichols or Cohen-Coon) from a FOPDT identification.

### The Ideal Continuous PID Algorithm

```{note}
The most common form is the *parallel* or *textbook* form:


$$
u(t) = u_{\text{bias}} + K_c e(t) + \frac{K_c}{\tau_I}\int_0^t e(\tau) d\tau + K_c \tau_D \frac{de(t)}{dt}
$$


where $e(t) = r(t) - y(t)$ is the error. The Laplace-domain transfer function is


$$
G_c(s) = \frac{U(s)}{E(s)} = K_c(1 + \frac{1}{\tau_I s} + \tau_D s)
$$


Three tuning parameters:


- **Controller gain $K_c$:** dimensional (units of MV per CV). Larger $K_c$ = faster response, more overshoot, more risk of instability.

- **Integral time $\tau_I$ (also reset time):** units of time. Smaller $\tau_I$ = faster offset elimination, but more overshoot.

- **Derivative time $\tau_D$ (also rate time):** units of time. Larger $\tau_D$ = more anticipation, but more noise amplification.

Two alternative forms: *series* (interacting) PID, and *ISA standard form*. Conversions exist but are not exam-testable.
```


```{note}
**What Each Mode Does**
- **Proportional ($K_c$):** reacts to the *current* error. Cannot, by itself, eliminate steady-state offset  -  a sustained nonzero $u_{\text{bias}}$ requires a sustained nonzero $e$.

- **Integral ($\tau_I$):** reacts to the *accumulated* error. Drives steady-state offset to zero. Adds phase lag (slows the loop) and can cause windup if the manipulated variable saturates.

- **Derivative ($\tau_D$):** reacts to the *rate of change* of the error. Adds phase lead (speeds the loop). Amplifies measurement noise (high-frequency noise has a large derivative).
```


### Mode-Selection Guidelines

```{tip}
- **P only:** the simplest and most tolerant; leaves offset proportional to the load. Used on noncritical level loops where some offset is acceptable.

- **PI:** the workhorse. Eliminates offset. Used on virtually all flow, pressure, most level, and most temperature loops. Probably 75% of all industrial loops.

- **PID:** adds derivative to PI. Used on slow temperature loops with low noise (large $\tau$). *Never* use on flow loops  -  they are too noisy and the derivative action amplifies the noise dramatically.

- **PD:** rare. Acceptable when offset is tolerable, the process is fast and noise is low. Used in some servomechanism applications.
```


### Ziegler-Nichols Open-Loop (Step-Test) Tuning Rules

```{important}
**Ziegler-Nichols Tuning from a FOPDT Identification**
Given an FOPDT model with gain $K$, time constant $\tau$, dead time $\theta$:


- **P only:** $K_c = \dfrac{1}{K} \dfrac{\tau}{\theta}$.

- **PI:** $K_c = \dfrac{0.9}{K} \dfrac{\tau}{\theta}$,   $\tau_I = 3.33 \theta$.

- **PID:** $K_c = \dfrac{1.2}{K} \dfrac{\tau}{\theta}$,   $\tau_I = 2.0 \theta$,   $\tau_D = 0.5 \theta$.

These rules give a *quarter-decay* closed-loop response (decay ratio $\approx 0.25$, $\zeta \approx 0.215$), which is aggressive and on the boundary of acceptability. For smoother response, use Cohen-Coon (next) or IMC tuning.

Sign of $K_c$: use the magnitude formula and *set the controller direct/reverse switch to give negative feedback*. A negative-gain process needs a direct-acting controller, and vice versa.
```


### Cohen-Coon Tuning Rules

```{important}
**Cohen-Coon Tuning Rules (more accurate when $\theta/\tau > 0.3$)**
- **P only:** $K_c = \dfrac{1}{K} \dfrac{\tau}{\theta}(1 + \dfrac{\theta}{3\tau})$

- **PI:** $K_c = \dfrac{1}{K} \dfrac{\tau}{\theta}(0.9 + \dfrac{\theta}{12\tau})$,   $\tau_I = \theta \dfrac{30 + 3 \theta/\tau}{9 + 20 \theta/\tau}$

- **PID:** $K_c = \dfrac{1}{K} \dfrac{\tau}{\theta}(1.35 + \dfrac{\theta}{4\tau})$,   $\tau_I = \theta \dfrac{32 + 6 \theta/\tau}{13 + 8 \theta/\tau}$,   $\tau_D = \theta \dfrac{4}{11 + 2 \theta/\tau}$
```


### IMC (Lambda) Tuning

```{important}
**IMC/Lambda Tuning for an FOPDT**
Internal Model Control assumes an inverse-process controller filtered by a first-order lag with closed-loop time constant $\lambda$. The resulting PI parameters are


$$
K_c = \frac{1}{K} \cdot \frac{\tau}{\lambda + \theta},   \tau_I = \tau
$$


$\lambda$ is the user's choice. Aggressive: $\lambda \approx \theta$; moderate: $\lambda \approx \tau$; conservative: $\lambda \approx 3\tau$. IMC gives a stable, smooth, no-overshoot setpoint response.
```


### Worked Example: PI Tuning from a FOPDT Fit

```{prf:example} ZN, Cohen-Coon, and IMC Tuning for the Cooling-Water Loop
:label: instrumentationandcontrol-example-10

Continuing the previous FOPDT example, $K = -1.5$ $^\circ$F/gpm, $\tau = 2.14$ min, $\theta = 5.4$ min. Compute PI tuning by (a) Ziegler-Nichols, (b) Cohen-Coon, (c) IMC with $\lambda = \tau$. Compare.
```


```{dropdown} Solution Steps
- **(a) Ziegler-Nichols PI.**


$$
\begin{align}
K_c &= \frac{0.9}{|K|} \frac{\tau}{\theta} = \frac{0.9}{1.5} \frac{2.14}{5.4} = 0.60 \times 0.396 = 0.238 \text{gpm}/^\circ\text{F} \\
\tau_I &= 3.33 \theta = 3.33 \times 5.4 = 18.0 \text{min}
\end{align}
$$


- **(b) Cohen-Coon PI.** With $\theta/\tau = 5.4/2.14 = 2.524$:


$$
\begin{align}
K_c &= \frac{1}{1.5} \frac{2.14}{5.4} (0.9 + \frac{5.4}{12 \times 2.14}) = 0.667 \times 0.396 \times (0.9 + 0.210) = 0.293 \text{gpm}/^\circ\text{F} \\
\tau_I &= 5.4 \cdot \frac{30 + 3(2.524)}{9 + 20(2.524)} = 5.4 \cdot \frac{37.57}{59.48} = 5.4 \times 0.632 = 3.41 \text{min}
\end{align}
$$


- **(c) IMC PI with $\lambda = \tau = 2.14$ min.**


$$
\begin{align}
K_c &= \frac{1}{|K|} \frac{\tau}{\lambda + \theta} = \frac{1}{1.5} \frac{2.14}{2.14 + 5.4} = \frac{1}{1.5} \times 0.284 = 0.189 \text{gpm}/^\circ\text{F} \\
\tau_I &= \tau = 2.14 \text{min}
\end{align}
$$


- **Controller action sign.** $K < 0$ for this process, so the controller is **direct-acting** (controller output rises when measurement rises) to maintain negative feedback. The magnitudes $K_c$ from each method are entered into the controller and the direct/reverse switch is set to "direct."


- **Comparison.**


- ZN gives moderate $K_c$ and slow integral; will produce overshoot.

- Cohen-Coon gives somewhat larger $K_c$ and much faster integral; will respond faster but with more overshoot. CC is the recommended choice for dead-time-dominant processes ($\theta/\tau > 0.3$).

- IMC gives the smallest $K_c$ and a very fast integral ($\tau_I = \tau$); produces a smooth, no-overshoot response at the cost of speed.

For a process this delay-dominant, none of these will be snappy  -  consider Smith predictor for dramatically better performance.


- **Sanity check.** The dimensionless loop gain at the chosen $K_c$ is $|K_c \cdot K| \approx$ 0.36 (ZN), 0.44 (CC), 0.28 (IMC). All are well below 1.0, so the loop is comfortably stable. ZN's value (0.36) is closest to the quarter-decay target gain, consistent with its more aggressive tuning intent.
```


### Ultimate-Gain (Closed-Loop) Tuning

```{note}
**The Ziegler-Nichols Closed-Loop (Ultimate) Method**
An alternative to the step-test method: with integral and derivative disabled, increase $K_c$ until the loop oscillates at a constant amplitude (the limit of stability). Record:


- Ultimate gain $K_u$  -  the $K_c$ value at sustained oscillation.

- Ultimate period $P_u$  -  the period of the oscillation.

Then:


- P only: $K_c = 0.5 K_u$.

- PI: $K_c = 0.45 K_u$, $\tau_I = P_u/1.2$.

- PID: $K_c = 0.6 K_u$, $\tau_I = P_u/2$, $\tau_D = P_u/8$.

Practical issue: deliberately bringing a real plant to its limit of stability is disruptive and not safe. The relay-feedback method (*Åström-Hägglund*) gives the same $K_u, P_u$ from a small relay-induced oscillation and is much safer.
```


### Anti-Windup

```{note}
When the manipulated variable saturates (valve fully open or closed) and the error persists, the integral term keeps accumulating without producing any further action. When the error eventually reverses, the controller takes a long time to "unwind" the accumulated integral and the loop is sluggish. This is **integral windup**. Mitigations:


- *Conditional integration:* freeze the integrator when the MV is saturated.

- *Back-calculation:* compute the controller output assuming the integrator is whatever it needs to be to give the actual (saturated) MV.

- *Velocity-form algorithm:* most modern DCS implementations use a velocity-form (incremental) PID that is inherently windup-free.

All commercial controllers have built-in anti-windup; the engineer must verify it is enabled and that the saturation limits are set correctly.
```


### Worked Example: Routh-Hurwitz Stability of a PI Loop

```{prf:example} Find the Stability Boundary $K_c$ for a Simple PI Loop
:label: instrumentationandcontrol-example-11

A PI controller $G_c(s) = K_c(1 + 1/(2 s))$ controls a process $G_p(s) = 1/[(s+1)(s+2)]$ with unit sensor. Find the range of $K_c$ for closed-loop stability.
```


```{dropdown} Solution Steps
- **Open-loop transfer function:**


$$
G_{OL}(s) = G_c G_p = K_c \frac{1}{(s+1)(s+2)}\cdot \frac{2s + 1}{2s} = \frac{K_c (2s + 1)}{2 s (s+1)(s+2)}
$$


- **Characteristic equation:** $1 + G_{OL} = 0$, i.e.


$$
2 s (s+1)(s+2) + K_c (2s + 1) = 0
$$


Expand:


$$
2 s (s^2 + 3s + 2) + 2 K_c s + K_c = 2 s^3 + 6 s^2 + 4 s + 2 K_c s + K_c = 2 s^3 + 6 s^2 + (4 + 2 K_c) s + K_c = 0
$$


- **Routh array** for $a_3 s^3 + a_2 s^2 + a_1 s + a_0$ with $a_3 = 2$, $a_2 = 6$, $a_1 = 4 + 2 K_c$, $a_0 = K_c$:


| $s^3$ | $2$ | $4 + 2 K_c$ |
| --- | --- | --- |
| $s^2$ | $6$ | $K_c$ |
| $s^1$ | $b_1$ | 0 |
| $s^0$ | $K_c$ |  |


where $b_1 = [6(4 + 2 K_c) - 2 K_c]/6 = [24 + 12 K_c - 2 K_c]/6 = (24 + 10 K_c)/6$.
```


```{dropdown} Solution Steps
- **Stability requires all first-column entries positive:**


- $6 > 0$: always.

- $b_1 > 0$: $24 + 10 K_c > 0 \Rightarrow K_c > -2.4$.

- $K_c > 0$.

Combining: stability iff $K_c > 0$.


- **Ultimate gain.** As $K_c \to \infty$, all entries stay positive; the loop is stable for any positive $K_c$. (The process by itself is overdamped and has plenty of phase margin; PI control with the chosen $\tau_I = 2$ does not destabilize it.) For a process with more lag (e.g. three first-order in series), there would be a finite $K_u$ at which the loop oscillates.


- **Verification.** At $K_c = 0$ (open loop), the characteristic equation is $2s(s+1)(s+2) = 0$, with poles 0, $-1$, $-2$. The pole at the origin is marginal (open-loop integrator). Adding any $K_c > 0$ moves the marginal pole into the left half-plane. ✓
```


```{note}
**Exam Tips  -  PID and Tuning**
- Memorize the ZN PI rule: $K_c = 0.9 \tau/(K\theta)$, $\tau_I = 3.33 \theta$. PID rule: $K_c = 1.2 \tau/(K\theta)$, $\tau_I = 2 \theta$, $\tau_D = 0.5 \theta$.

- Direct vs. reverse: choose to keep the loop in negative feedback. For positive process gain $\to$ reverse-acting controller; for negative gain $\to$ direct-acting.

- Never use derivative action on flow loops (noise).

- Anti-windup is required on any loop whose MV can saturate (most temperature, level, and pressure loops with large operating ranges).

- Routh-Hurwitz is the algebraic stability test for polynomial characteristic equations.
```


## Advanced Control Structures
The single-loop PID is the workhorse, but many process challenges  -  significant dead time, measurable disturbances, multiple competing constraints, or interacting variables  -  call for richer control structures. The PE exam expects you to recognize these structures and to know when each is justified.

### Cascade Control

```{note}
**When and Why to Use Cascade**
**Cascade control** uses a faster *inner* loop nested inside a slower *outer* loop. The outer controller's output becomes the setpoint of the inner controller. The inner loop catches and rejects disturbances close to their source before they propagate to the outer variable.

**Justification:** cascade is appropriate when


- there is a measurable intermediate variable between the manipulated variable and the slow controlled variable,

- a significant disturbance enters between the MV and the slow output (so the inner loop sees it first),

- the inner loop is at least 3$\times$ faster than the outer loop (so the inner loop's dynamics look "instantaneous" to the outer).

**Classic pairings:**


- Reactor temperature (outer) $\to$ jacket-fluid temperature (inner) $\to$ jacket flow valve.

- Distillation tray temperature (outer) $\to$ steam flow to reboiler (inner) $\to$ steam valve.

- Furnace tube-skin temperature (outer) $\to$ fuel-gas flow (inner) $\to$ fuel valve.
```


### Feedforward Control

```{note}
**Feedforward Algebra**
**Feedforward** measures the disturbance directly, predicts its effect on the controlled variable from a model, and pre-compensates by adjusting the manipulated variable before the disturbance reaches the output. The ideal feedforward controller is


$$
G_{ff}(s) = -\frac{G_d(s)}{G_p(s)}
$$


where $G_d$ is the disturbance-to-output transfer function and $G_p$ is the manipulated-to-output. This perfectly cancels the disturbance in the limit of a perfect model. Practical considerations:


- Feedforward is open-loop: it cannot correct for unmeasured disturbances or for model mismatch. Always combine with feedback PI/PID.

- Steady-state feedforward (static gain only) is often sufficient. Dynamic feedforward includes a lead-lag block.

- If $G_p$ has more dead time than $G_d$, the ideal feedforward is non-causal  -  you would need to act before the disturbance arrives. The fix is to drop the dead-time inversion and accept imperfect cancellation.
```


### Override (Selective) Control

```{note}
**Override control** has two (or more) controllers competing to drive a single manipulated variable, with a low/high selector choosing which controller's output reaches the valve. Used when one variable must stay within a safety limit while a normal variable is being controlled.

**Example:** compressor discharge pressure is controlled normally, but suction pressure overrides (low-select) to prevent compressor surge. As suction pressure drops near the surge line, the surge controller takes over the valve.
```


### Ratio Control

```{note}
**Ratio control** sets the setpoint of one flow as a fixed ratio of another measured flow. The classic application is air/fuel ratio in combustion:


$$
\text{Air setpoint} = R \times \text{Fuel flow}
$$


The implementation is a multiplier block ahead of a flow PI controller. Care is needed during transients: the air loop must lead the fuel loop on increases (avoid fuel-rich, smoke) and lag on decreases (avoid lean blowout).
```


### Smith Predictor for Dead-Time-Dominant Processes

```{note}
**The Smith Predictor Structure**
For a process with severe dead time, the **Smith Predictor** surrounds a standard PI controller with two model branches:


- One branch contains the full model $G(s) = K e^{-\theta s}/(\tau s + 1)$.

- The other branch contains the no-delay portion $G_0(s) = K/(\tau s + 1)$.

The controller effectively sees the no-delay process, so it can be tuned for that process. The predictor structure cancels the dead time in the model. In the limit of a perfect model, the closed loop responds as if the process had no dead time at all.

**Caveat:** the Smith Predictor is exquisitely sensitive to model error. A 10% error in $\theta$ or $\tau$ can destabilize the loop. Use only when the model is good and reliable.
```


### Multivariable Control: Interactions and the RGA

```{note}
**Pairing Loops to Minimize Interaction**
When a process has multiple controlled and manipulated variables (e.g. a distillation column with reflux and reboiler manipulated, distillate and bottoms compositions controlled), the choice of which manipulated variable pairs with which controlled variable matters. The **Relative Gain Array (RGA)** quantifies the interaction:


$$
\Lambda = G(0) \otimes [G(0)^{-1}]^T   \text{(Hadamard product of }G\text{ and the transpose of its inverse, evaluated at }s=0\text{)}
$$


- $\lambda_{ij} = 1$: no interaction; perfect pairing.

- $0 < \lambda_{ij} < 1$: some interaction; acceptable.

- $\lambda_{ij} = 0$: this MV has no effect on this CV; do not pair.

- $\lambda_{ij} < 0$: pairing this MV-CV inverts the apparent process gain; closed-loop response will be unstable. Do not pair.

- $\lambda_{ij} > 1$: pairing exists but interactions amplify. Use with caution.

Rule of thumb: pair on RGA entries closest to 1 (and positive). For severely interacting systems, consider decoupling or model predictive control.
```


```{note}
**Exam Tips  -  Advanced Structures**
- Cascade: two summing junctions, two PID blocks in series with outer feeding inner setpoint. Used for slow-variable outer, fast-variable inner, with disturbance entering near the inner variable.

- Feedforward: a measured-disturbance block computes a correction added to (not replacing) the feedback controller's output.

- Override: a selector block (LSS or HSS) between multiple controllers and one valve.

- Ratio: a multiplier block ahead of a flow controller; the multiplier's input comes from another flow measurement.

- Smith predictor: extra model blocks around a PI controller; effective only with a good plant model.

- RGA: pairing tool for multivariable problems; pair on entries near 1.
```


## Summary: A Single-Page Reference Sheet
This last section gathers the most exam-relevant formulas and decisions in one place. Use it for last-minute review.

```{tip}
**Time- and Laplace-Domain Identities You Should Know Cold**
- Step $M$: $L\{M u(t)\} = M/s$.

- Exponential decay: $L\{e^{-at}\} = 1/(s+a)$.

- Dead time: $L\{f(t-\theta)u(t-\theta)\} = e^{-\theta s} F(s)$.

- First-derivative rule (zero IC): $L\{f'(t)\} = s F(s)$.

- Final-value theorem: $\lim_{t\to\infty} f(t) = \lim_{s\to 0} s F(s)$.
```


```{tip}
**First-Order Step Response**


$$
y(t) = K M (1 - e^{-t/\tau})
$$


Landmarks: 63.2% at $\tau$; 86.5% at $2\tau$; 95.0% at $3\tau$; 99.3% at $5\tau$. Slope at $t=0$ is $KM/\tau$. Add back $y$ before quoting absolute value.
```


```{tip}
**FOPDT and Sundaresan-Krishnaswamy**


$$
G(s) = \frac{K e^{-\theta s}}{\tau s + 1}
$$


$$
\theta = 1.3 t_{35.3\%} - 0.29 t_{85.3\%},   \tau = 0.67(t_{85.3\%} - t_{35.3\%}),   K = \Delta y_{ss}/\Delta x
$$


Controllability: $\theta/\tau < 0.1$ easy; $0.1$-$1$ classical; $> 1$ requires Smith predictor or feedforward.
```


```{tip}
**Second-Order Damping**


$$
\zeta = \frac{b}{2\sqrt{ac}},   \tau = \sqrt{a/c}   \text{(for }ay+by+cy = dx\text{)}
$$


$\zeta > 1$ overdamped; $\zeta = 1$ critical; $0 < \zeta < 1$ underdamped; $\zeta = 0$ undamped; $\zeta < 0$ unstable. Quarter-decay ($DR = 1/4$) at $\zeta \approx 0.215$.


$$
OS = e^{-\pi\zeta/\sqrt{1-\zeta^2}},   DR = OS^2,   T = 2\pi\tau/\sqrt{1-\zeta^2}
$$


```


```{tip}
**Control-Valve Sizing**


$$
q = C_v f(\ell) \sqrt{\Delta P_v / G_s}   (\text{liquid, gpm, psi, gpm}/\sqrt{\text{psi}})
$$


Linear $f = \ell$; Equal-pct $f = R^{\ell-1}$; Quick-opening $f = \sqrt{\ell}$.
$\beta = \Delta P_v/\Delta P_{\text{total}}$: $\beta > 0.5$ linear; $\beta < 0.5$ equal-pct.
$K_v$ (metric) $\approx 0.865 C_v$. Target lift $0.3$-$0.75$ at design.
```


```{tip}
**Fail-Safe**
FO = ATC; FC = ATO. FC has $K_v > 0$, FO has $K_v < 0$.
Cooling water: FO. Steam: FC. Vent: FO. Drain on inventory: FC. Hazardous reagent: FC. Combustion air: FO. Fuel: FC.
```


```{tip}
**4-20 mA Calibration**


$$
I = 4 + 16 \frac{\text{measurement} - \text{zero}}{\text{span}},   \%TO = (I-4)/16 \times 100
$$


Zero = low end of range; Span = high $-$ low. Live zero (4 mA) distinguishes broken loop from low reading.
```


```{tip}
**PID Tuning**
**Ziegler-Nichols PI:** $K_c = 0.9\tau/(K\theta)$, $\tau_I = 3.33\theta$.
**Ziegler-Nichols PID:** $K_c = 1.2\tau/(K\theta)$, $\tau_I = 2\theta$, $\tau_D = 0.5\theta$.
**Cohen-Coon PI:** $K_c = (1/K)(\tau/\theta)(0.9 + \theta/(12\tau))$, $\tau_I = \theta(30 + 3\theta/\tau)/(9 + 20\theta/\tau)$.
**IMC PI:** $K_c = \tau/[K(\lambda+\theta)]$, $\tau_I = \tau$. $\lambda \approx \tau$ for moderate.
**ZN closed-loop PI:** $K_c = 0.45 K_u$, $\tau_I = P_u/1.2$.
Direct/reverse: keep loop in negative feedback. Match controller sign to process gain sign.
```


```{tip}
**Mode Selection**
P: noncritical level. PI: flow, pressure, most level, most temperature (the workhorse, 75%+ of all loops). PID: slow temperature loops with low noise. Never use D on flow.
```


```{tip}
**Advanced Structures**
- Cascade: outer setpoint $\to$ inner setpoint; inner $> 3\times$ faster than outer.

- Feedforward: measure disturbance, $G_{ff} = -G_d/G_p$. Always combine with feedback.

- Override: selector chooses among controllers for one valve.

- Ratio: multiplier ahead of flow PI.

- Smith predictor: model-cancels dead time; sensitive to model error.

- RGA: pair MV-CV on entries near 1; avoid negative entries.
```
