- make a large block, 20 micron central line trace, 100 micron ground separated by 7.5
microns. 
- Either use a lump port or wave port
- What would be the metal property of the metal film, and what property of the
  silicon? 
- Simulate 1-10GHz, 10GHz = 3cm
    - If the entire length of the model is 20cm, we find the transmission to be worse
      than a 2cm width. 
    - threshold is roughly the threshold where we can sustain a full wavelength.
    - so the width should be less than a wavelength for you to get good transmission
- will run into things like precision and time, more technical things in HFSS
    - It will take infinitely long to simulate if you don't set up the mesh property
      correctly

- Look up S matrix 
    - S11 = 1 means full reflection 
    - For perfect transmission, you want S21 to be 1, and S11 to be 0. 
    - S11 + S21 does not need to be 100%, because you can have dissipation along the
      way
    - S12 should equal S21? 
    - S21 = send energy from 1 and observe at 2
    - S12 = send energy from 2, and observe at 1

- Try different conductivity values and also try different lengths.  
# Questions

- When I try to do the lumped port thing, it asks me for an "integration line", what
  is this supposed to be?

