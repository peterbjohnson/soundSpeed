# soundSpeed
Demonstrate a simple measurement of the speed of sound

# Using the code

The Python script reads and plots sounds from a sound card, i.e. it works like an oscilloscope. 
  
You can customise the sample duration, frequency, and interval
  
Example application on the command line:
`python soundSpeed_a.py --duration .1 --fs 44100 --interval 300 --device 1`
  
In the above example, a 0.1 s sample, at 44.1 kHz, is plotted every 300 ms, using device 1
  
To select a device, run `listDevices.py` to see which devices are available

# Conducting the experiment

Create a periodic sound, e.g. using a smart phone or by singing

Place two microphones at different distances from the sound source

Changing the distance between the microphones will change the relative phase of their measurements. 

Play with the distance until you the phase difference is one, or another integer number of wavelengths. 

Given the wavelength, $\lambda$, and the frequency $f$ of the source, you can calculate the speed of sound

$$c=f\lambda$$
