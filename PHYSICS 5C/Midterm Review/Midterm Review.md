# Statistics Review

- Discrete mean: $\langle x \rangle = \sum_i x_iP_i$
- Continuous mean $\langle x \rangle = \int xP(x) dx$
- Continuous Probability Distribution $\langle x\rangle = \int xP(x) dx$
- For independent variables, $P(u, v) \Delta u \Delta v = P(u) du \cdot P(v) dv$, and $\langle uv\rangle = \langle u\rangle \langle v \rangle$

# Chapter 5: Maxwell-Boltzmann Distribution

- Is one specific application of the Boltzmann Distribution

The Boltzmann distribution exists because of an $\ln T$ term that exists within the equation

$$ \frac{d\ln \Omega(E)}{dT} = \frac{1}{k_BT}$$
And the form of this equation also gives us the reason behind why the Boltzmann distribution looks like what it does. 

Boltzmann distribution tells us that the equilibrium state is the state in which there are the most nubmer of microstates. 

# Chapter 6: Pressure

## Ideal Gas Law

Introduces the ideal gas law $PV = nRT$ useful formula because it relates all three nice state variables (pressure, temperature, volume) together into one equation.

# Chapter 11: Energy 

## Functions of state

They are defined when a state is at equilibrium. The idea is that a variable is a function of state if we can *generate* a system which, at equilibrium, has a value as that function of state. 

## Heat Capacity 

A poor term to use becuase it's really a measure of "energy capacity". In an isothermal process, we write 

$$ C_V = \frac{dQ}{T}$$ 

since temperature is constant, otherwise we write it as 

$$ C_V = \left(\frac{dQ}{dT}\right)_V$$

And likewise 

$$ C_p = \left(\frac{dQ}{dT}\right)_p$$

The subscripted $V$ denotes the fact that we're holding $V$ constant. We also know that $C_p > C_V$ always, and that $\frac{C_p}{C_V} = \frac 53 \equiv \gamma$. To get specific heat capacites, divide by the mass of the material. 

# Chapter 12: Isothermal and Adiabatic Processes

## Reversibility

A system is reversible if there is a thermodynamic procses which allows us to return the system to its initial state from a different state. 

- irreversible and reversible are not strictly disjoint (they're fuzzy). You can ask what percentage of a process is reversible. 
- Reversible process does not respect equilbirium of state variables. Also, a cycle doesn't necessarily mean that the process is reversible. 
  - we only know whether a process is reversible if its total change in entropy is zero. 
- For a process to be reversible it must produce vertical lines in $T-S$ space, in other words an isothermal proces. 

## Isothermal Expansion 

Isothermal means that $\Delta T = 0$, so therefore $\Delta U = 0$ for it as well. Since $\Delta U = 0$, then $dW = dQ$. One way to identify isothermal expansion is to just imagine the system, and see whether the temperature changes or not. 

Therefore to calculate the $\Delta Q$: 

$$ \begin{align*}
  \Delta Q &= -\int dW\\
  &= \int_{V_1}^{V_2} p dV\\
  &= \int_{V_1}^{V_2} \frac{RT}{V} dV\\
  &= nR \ln \left(\frac{V_2}{V_1}\right)
\end{align*}$$
## Adiabatic Expansion

Adiabatic expansions have $\Delta Q = 0$, so therefore $\Delta U = \Delta W$. While this does imply that the system *only* does work on the system, it doesn't violate the second law of thermodynamics because the gas changes state during this process. 

In this expansion we have $TV^{\gamma -1} = \text{constant}$ ad $pV^\gamma = \text{constant}$, a useful relation. Isotherms and adiabats always have changing temperature and volume.

# Chapter 13: Heat Engines and Second Law
- **Clausius' Statement:** No process is possible whose sole result is the transfer of heat from cold to hot. 
- **Kelvin's Statement:**  No process is possible whose sole result is the complete conversion of work.
**These two statements are equivalent statements**

Carnot engine is an engine which consists of two isothermal processes and one adiabatic processes.

# Office Hours Questions
- OH Question: If an exact differential is one that can be written as a linear combination of other differentials, then what is the form of $dQ$ that makes it an inexact differential?
  - If we say $dg = y \ dx$
- Why is $p \ dV$ not an exact differential?
  - What are the forms of these (inexact) state variables that make them inexact?
- What is the formal definition of a reversible process?
- why can't we express a square as a bunch of mini carnot engines?
- how did we prove that the carnot engine is the most efficient?
  - Argument lies in the fact that 
- Is it always assumed that $n = 1$ in most equations?

# Agenda
- finish review doc, write up cheat sheet. Potentially if you have time, write up two versions - one with derivations and the other with just formulas. 



<!-- # Mathematical Facts

## Exact Differentials 
If the path integral of a process containing that variable is path independent, then the state variable is an *exact differential*. 

# Chapter 11: Energy 

## Functions of State 

Functions of state are defined when a state is at an equilibrium. It doesn't really matter during a *process*, but more the fact that we can generate a function of state.   

**Zeroth Law:** Whne two states $A$ and $B$ are simultaneously in equilibrium with a state $C$, then they are also in equilibrium with each other.  

# Office Hours Questions

## Exact Differentials 
- OH Question: If an exact differential is one that can be written as a linear combination of other differentials, then what is the form of $dQ$ that makes it an inexact differential?
  - If we say $dg = y \ dx$
- Why is $p \ dV$ not an exact differential?
- What are the forms of these (inexact) state variables that make them inexact?


$$\begin{align*}
  f(x) &= 1\\
  g(x) &= 2
\end{align*}$$ -->


