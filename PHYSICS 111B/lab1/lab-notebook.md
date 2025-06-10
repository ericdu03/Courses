# Questions before Lab
- Prelab mentions something about an "embedding dimension", why does the lab 
choose n = 3 as the appropriate dimension? 
- Section 10.1 does things in LabView, do we have to do this, or can we 
do it in python instead? 
# Notes 
- Had to take a function generator from another lab station because we didn't have one
:skull:
- Labview connected properly, wiring things were a bit annoying to work with 
but overall it was ok.
- Don't really know what waveform and waveform chart 2 are there for.
- x-axis in the power spectrum shows Time but it should be frequency, for all 
plots 

## Cobweb VI
- Interleaved array has (m0, m0, ..., m_n, m_n) elements, then we truncate the first 
two (start at index 2, to 51) to get (m1, m1, ..., m_n), which we then append 0 to 
get the y-values. The x-values we truncate the law two (index 0 to 50). Finally 
we interleave to get the desired x-y plot.  

- Plot looks very good 
- turns out we flipped x and y so that's why things weren't working.   
- not sure how to exactly distinguish between order and chaos 

## Liapunov Exponent
- Made a new circuit, and used function nodes this time to make our lives easier
- had some trouble naming the variables and stuff but overall it was ok
- Graph turned out great! Noticed that the Liapunov exponent increases after 3.57, 
a marker for chaos. 

## NLSim.vi
- approaches a line because it's capturing the rise and fall of the cos wave perfectly
- increase sampling rate = higher accuracy on the curve. 
- get a few points when we sample at a multiple, because we sample only at 
specific points (this makes sense)
    - we see aliasing in frequency domain, because we're sampling at discrete 
     points in time that all happen to overlap with each other 

- to see a cycloid we want f1, and f2 to be a multiple of each other, and not a multiple 
of the sampling rate. 
- the torus does either point in the y = x or y = -x direction, can't figure out what 
causes the flip 
- With A = 0, it's not chaotic. 


## Henon Map
- As we move from A=0 - A=1.4, we see more and more points form on the return map. 
This equation is similar to a logistic map, at least, it looks like that when we plot 
the bifurcation plot as a function of A. 
- We’re able to confirm if we zoom into the bifurcation map at 1.25, we see 7 branches(?)
and we confirm that’s how many points we see when we plot the return map, 
7 return points at the cooresponding value of A

## Strobe Pulse 
- to read the plot, each fixed point counts as a point where the curve "bounces"
- 1 --> 2 cycle: 0.007
- 2 --> 4 cycle: 0.786
- 4 --> 8 cycle: 2.394
- 8 --> 16 cycle: 3.092

- still don't know what the gain is lol 

## Bouncing Ball 
- frequencies (Hz) @ 10V: 30, 50, 60, 70, 110 for the images taken of the path to chaos
- Driving amplitude (V) @ 80Hz: 3 (circle), 4 (stable, not oval), 5 (pseudostable) .6 (pseudo-stable), 7 (unstable), 8 (stable)

## Information Dimension
- computer crashed LOL

### Bouncing Ball

30, 60, 90Hz, driving frequencies (V): 2, 5, 8
  - 30 Hz, 2V: 6 dimensions but only 5 columns?
- 120 Hz, 4 V was pseudostable
- 120 Hz, 5 V, pseudostable
- 120 Hz, 6V chaotic
- 120 Hz, 8V chaotic

### PN Junction
- 3000 to 5000 Hz, at intervals of 500 Hz
- 5, 7, 10 volts

Slider was set to 4.729, not sure if that's relevant at all for both experiments

At 9V, 3600 Hz, there's some weird "notches" on the oscilloscope that I can't really explain. 