

# Assignment 4 

Synthesizer software emulation and implementing research papers 
--------------------------------------------------------------- 

This assignment comes in three versions. The first version focuses on real-time implementation and software simulation of an existing synthesizer (the Yamaha DX21) and is heavier in terms of programming. The other two versions look at the implementation of some synthesis techniques from research papers and are more focused on coding and presenting algorithms so they less heavy in terms of programming but requires more math understanding. The expected answer for versions 2 and 3 is not expected to be real-time and is expected to be a Python/Jupyter notebook. It will be easier if you work on one version or the other but if you decide to mix questions that is fine. As usual I will use the term familiar programming 
language to refer to the ones that you probably have encountered during your  studies: Python, C, C++, Java, and Javascript. As you probably can guess I will use the term unfamiliar programming language to refer to any other programming language such as: Haskell, OCaml, Prolog, Rust, Go, Julia, Ruby, C#, F#
R, etc. I will use the term computer music textual languages to refer to languages 
that have extensive support and primitives for sound and music manipulation such as 
Chuck, Supercollider, Csound, Nyquist, and Faust and visual programming languages 
for languages such as PureData and Max/MSP. 

Unless explicitly stated you can use any programming languages for implementing 
the questions. Using a computer music language moves the degree of difficulty down and using an unfamiliar programming language moves it up. For example if you implement question 6 in Max/MSP or Chuck it counts as basic rather than expected. If you implement question 6 in an unfamiliar programming languages it can count as advanced. In general, I am flexible so if you want to adjust things just let me know. Also if you 
think of a question of comparable difficulty that you would like do again let me know and most likely 
it should be ok. 

If you need access to devices ask me via email or through Discord for access to ECS602. 

Fee free to suggest your own versions that follow a similar structure. For example if you have a different synthesizer that you would like to emulate using software - you can come up with similar questions to version 1 or if you find a paper you would like to implement you can come up with similar questions to version 2 and 3. 


## VERSION 1 - SOFTWARE SIMULATION OF THE YAMAHA DX 21 

Any programming language that can do real-time audio processing and show a graphical user interface can be used 
for this assignment. I would recommend implementing this either as a plugin using the JUCE software framework 
or as a VCV Rack module. 

1. (Basic) Watch a video on YoutTube about the DX 21 (some are listed under [Resources](resources.md) but you can use anything you find). Select a short part of the video (something like 15-30 seconds) and make an explicit connection to any of the concepts we have covered in the course. Write a short paragraph describing the connection and provide the timing of the excerpt you considered. 

2. (Basic) Record two notes (C4, G4) from two different patches of the Yamaha DX21. Ideally use the Yamaha DX21 that is in ECS602 but if needed you can also capture sound from YouTube or by any other means. Show the time domain plots and magnitude spectrograms of the four sounds you recorded using both linear amplitude and amplitude in dB (using Python or MATLAB is probably the easiest way to go) - you should analyze a short duration corresponding to a few pitch cycles of each note. 

3. (Basic) Find out what FM "algorithm" (the DX21 has four operators and 8 algorithms) is used for each patch sound you examined in the previous question. Describe in a short-paragraph how the operators are connected and which ones act as modulators and which ones act as carriers. The manual to the DX21 can be found online and a paper copy is also availabe in ECS602. 

4. (Basic) Either use one of the patches you examined or use init mode to start from a blank state and either make a significant change or create a new patch by editing some parameters of the sound but keeping the algorithm the same (for example you can change the ADSR, or experiment with the feedback amount). Using the code from question 2 show the time-domain waveform and magnitude spectrum before you make any changes and after you make the changes. 

5. (Expected) Create a basic hello-world real-time synth. Your synth should have a single sinusoidal oscillator and be controllable by MIDI. You don't need to support polyphony. 

6. (Expected) Extend the synthesizer from question 5 to support an ADSR envelope and two-operator FM synthesis. You don't need to support polyphony. 

7. (Expected) Implement one of the algorithms and try to approximate one patch sound. You will need to extend your implementation to 4 operators. Implement the frequency ratios and detune parameters (see DX21 manual) but ignore the LFO and Pitch envelopes. 

8. (Expected) Add the LFO and pitch envelopes to your implementation. Your synthesizer is still mono-phonic. Show how you can approximate an existing patch. 

9. (Advanced) Extend your synthesizer to support polyphony (first investigate how many voices you can have simultaneously without audio artifcats on your computer to decide the number of voices). Implement simple polyphony and voice allocation (http://msp.ucsd.edu/techniques/v0.05/book-html/node60.html). 

10. (Advanced) Add a graphical-user interface to your synthesizer. You can try to recreate closely the interface of the DX21 or come up with your own possibly more intuitive way of editing patches. 

## VERSION 2 - Research paper implementation - Virtual analog synthesis 

This version is based on the following paper: 

Oscillator and Filter Algorithms for Virtual Analog Synthesis - Vesa Välimäki and Antti Huovilainen
Source: Computer Music Journal , Summer, 2006, Vol. 30, No. 2 (Summer, 2006), pp. 19-31
(https://www.jstor.org/stable/pdf/3682001.pdf) - you will need to be at UVIc or using UVic VPN to 
access the paper. 

1. (Basic) Summarize the main contributions of the paper in your own words (about 1-2 paragraphs) 

2. (Basic) Explain in your own words Figure 4. More specifically explain what is the issue with the standard implementation of the sawtooth wave and how the "improved" version addresses that problem. 

3. (Basic) Recreate Figure 4a using your own code and a plotting library. 

4. (Basic) Recreate Figure 4b using your own code and a plotting library 

5. (Expected) Implement the DPW sawtooth waveform and recreate Figures 4c,4d,4e and 4f. 

6. (Expected) Implement the two-oscillator generation algorith for pulse waveform generation and recreate the corresponding figures. 

7. (Expected) Implement the triangular waveform generation algorithm proposed in the paper and recreate the corresponding figures. 

8. (Expected) Generate some audio examples with continuously changing pitch and pulse-width in the case of the pulse waveform that contrast the naive aliased oscillators with the proposed ones. 

9. (Advanced) Implement the digital moog filter part of the paper and re-create the associated figures. 

10. (Advanced) Compare the computational efficiency of the proposed oscillators with a wavetable implementation in which the samples of one cycle of each waveform are stored and linear-interpolation is used. 


## VERSION 3 - Research paper implementation - Bubble sound simulation 

This version is based on the following research paper: 

Physically Based Models for Liquid Sounds - Kees Van Den Doel 
ACM Transactions on Applied Perception (TAP) 2.4 (2005): 534-546
https://dl.acm.org/doi/pdf/10.1145/1101530.1101554

1. (Basic) Explain in your own words the basic idea for modeling the sound of an individual bubble (1-2 paragraphs) 

2. (Basic) Explain in your own owrds the basic idea for modeling the complex liquid sounds statistically (1-2 paragraphs) 

3. (Basic) Record the sound of an individual droplet and plot the time-domain plot of the sound. 

4. (Basic) Plot the magnitude spectrum and spectrogram using both linear and dB scaling for the y-axis. 

5. (Expected) Implement the decaying sinusoid model described in the paper for the sound generation of an individual bubble sound. 

6. (Expected) Recreate the sounds used in the user study based. 

7. (Expected) Implement and plot the output of the Poisson process for bubble creation described in the paper. This question just models the event times for the bubbles 

8. (Expected) Implement the full bubble simulator as described in the paper 

9. (Advanced) Create a few "presets" by adjusting the creation rates for different sized bubbles. The paper mentions: "An enormous variety of waterlike sounds can be created with the simulator, ranging from intimate
dripping sounds to torrential rains or waterfalls." Show audio examples of your simulator supporting this statement. 

10. (Advanced) Create a buffered implementation of your system suitable for real-time synthesis. You don't need to implement an actual real-time system with a GUI but your simulator should work by producing samples in short fixed buffer sizes without artifacts. Of course if can implement a real-time version if you choose to do so. 

