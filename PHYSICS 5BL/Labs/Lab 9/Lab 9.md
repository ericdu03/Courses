# Lab 9 Journal

* Oscilloscope works properly, managed to connect the function generator with the oscilloscope using a BNC-BNC wire, and it worked out nicely as well.
* Figured out how all the knobs work, and was able to measure the maximum and minimum voltage using the oscilloscope
* Oscilloscope actually takes a snapshot (as long as the setting is on "stop"), otherwise it is continuously reading the signal.
* Some interesting things about the oscilloscope were observed:
  * the trigger position only holds one of the inputs in place, while the other one is allowed to vary 


## Peak to peak measurements from manual
* Divisions (vertical) for sine wave: 4 major, 20 minor
* Divisions (vertical) for whole window: 8 major, 40 minor

* Divisions (horizontal) for sine wave: 5 major, 25 minor
* Divisions (horizontal) for whole window: 10 major, 50 minor 


## Trigger stuff

The location of peaks and trophs switch places (i.e. a peak becomes a troph and vice versa). The sine wave doesn't appear to be shifted by a certain amount but instead just flipped. The trigger level probably refers to the edge of the oscilloscope; when we change from positive to negative slope the leading edge (left) goes from positive to negative too.

Changing the level causes the left edge of the sine wave to move accordingly so that the leading edge begins at that level. When we set the level to be greater than the amplitude of the oscilloscope, the reading starts going crazy.

