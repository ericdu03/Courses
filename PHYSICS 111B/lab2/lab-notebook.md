# Turning on Experiment
- current in multimeter: 10mV/1A, use the multimeter reading over the power supply
  reading
- frequencies:
    - 2.059 MHz for Rb85
    - 3.087 MHz for Rb87
- Berkeley magnetic field: 47649 nT, or 0.47 gauss
- 

## Section 6.2
- Couldn't get a good image of trace b/c 10Hz was too low of a measurement
- Dropoff peaks widen as you increase the coil current, this is again 
a qualitative measurement.  
- DC voltage on the shunt resistor: 10.239 mV, or 1.0239A. 

- Varying other parameters:
    - If sweep period is too fast (>=1Hz), then you get overlap bc the 
    secondary peak doesn't die down fast enough. 
    - Changing RF voltage changes the resonant peak height. 
        - makes sense, because reducing downpumping amplitude 
        = keeping more atoms in excited
          state (m = +1), 
          so the number of atoms that can be pumped up are 
          less --> lower amplitude signal. 
    - increasing rubidium current increases the resonance peak
        - also makes sense, current in the lamp corresponds directly to how many
          atoms are being pumped up. 
    - not very precise lol. 
        - can try starting the sweep near one of the resonance peaks to measure it,
          but overall not very accurate. 
    - shrunk the sweep window so that you only see one of the peaks, the Rb85 is at
      ~1.8 MHz and Rb87 is at 2.8MHz. 

FUCK 

- could not figure out how to take the measruement setting the RF 
- Lissajous curves
  - Curves came out pretty good
  - tempreature changed a lot during measurements, statistical noise within the bulb --> any variatinon will have an amplified effect bc of the amplifier adds 500x
  - varied the supply voltage (current) instead of frequency, probably should have done the latter bc of higher precision
  - visually determined resonance; inherently bad
  - we didn't figure out how to get the zero field properly, but we learned we can extrapolate the data we already have (should have taken data from 0 to 1A current)
  - unfortunately data is at 1A but should be ok
- Zeeman resonance worked well, timescales were quite annoying
  - took good recordings for the characteristic time 