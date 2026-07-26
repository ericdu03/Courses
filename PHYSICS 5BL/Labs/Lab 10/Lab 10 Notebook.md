# Lab 10 Notebook

## Experiment 1a: Measuring RC Time Constant
* Interesting to note that when the connections were flipped then the oscilloscope didn't measure anything. Not entrely sure why. 
* Other than that, connections went well and we got to measuring. Apparently there's a way to export the oscilloscope data to .csv directly, and in the interest of more accurate data measurements we think we'll do that instead. 
* A bit too much data and we found that Tektronix doesn't have a very consistent .csv file format so we decided to take the data manually instead.
  * We still have the .csv files so there is still the option to go back 

* Current seemed to roll over really slowly but after waiting a couple of seconds we can see it:

Image of the setup below:

<img src = "IMG_8107.png">



## Table of Data 

Referencepoint is set at: 4.96V at -2.68 seconds. Relative voltage of 0V and 0 seconds.

The data is as follows:

| Channel| Max (V)| Min (V) | 
|-| -| -|
Channel 1 | 5| -5
Channel 2| 4.96| -4.96

**Minimum Voltage: -4.88 V**

**NOTE:** We were measuring a discharge.

| Absolute Voltage (V) | Voltage Difference (V) | Time Difference (seconds) |
| ----------- | ----------- | --------- |
|  4.96|    0| 0 |
| 0.64| 4.32 | 0.3 |
| -1.28 | 6.24| 0.6 |
|-2.64| 7.60| 0.9 |
-3.36 | 8.32 | 1.2
-4.00 | 8.96 | 1.6
-4.24 | 9.20 | 1.8
-4.48 | 9.44 | 2.1
-4.56 | 9.52 | 2.4
-4.72 | 9.68 | 2.7
-4.88 | 9.84 | 4.9

## Experiment 1c: Handcrafting a Capacitor

* Capacitor was created using two sheets of aluminum foil and paper. The areas of the foils had to be different in order to prevent shorting the capacitor. We decided that when we calculate capcatance $\frac{\varepsilon_0A}{d}$, we will use the smaller of the two foils to do so.

* There was a lot of noise in our capacitance measurement, but upon adjusting the frequency and amplitude values we were able to get a signal that wasn't just noise.
  * This was done with the 10M$\Omega$ resistor.

We found that we got a good curve when the resistor attached was $100 k\Omega$, with DC coupling in the oscilloscope.

| Absolute Voltage (V) | Voltage Difference (V) | Time Difference (seconds) |
| ----------- | ----------- | --------- |
| 2.12| 0 | 0|
|-0.04| 2.16 | 0.52|
|-0.76| 2.88 | 1.0|
|-1.24|3.36|1.5
|-1.48| 3.6| 2.0|
|-1.56|3.68|2.5|
|-1.72|3.84|3.0|
|-1.80|3.92|3.5|
|-1.88|4.0|4.0|
|-1.9| 4.02 | 4.5|
|-1.94| 4.06| 5.0|

* Source voltage was 10 Volts $V_{pp}$, whereas the net voltage drop for the capacitor was 5 volts. <!-- try to verify whether this value is right--> The frequency was $100 \ \text{mHz}$.

**Resistance of inductor:** 70.8 $\Omega$.

## Experiment 2b: RLC Overdampted Transient Response

| Absolute Voltage (V) | Voltage Difference (V) | Time Difference (seconds) |
| ----------- | ----------- | --------- |
5.68 | 0 | 0
1.2 | 4.48 | 1
0.32| 5.36| 2.0
0.16| 5.52|3
0.08 | 5.6 | 4|
0.08 |5.6 | 5

When we fit this we an find the $V_{pp}$ via a curve fit and finding where it asymptotes