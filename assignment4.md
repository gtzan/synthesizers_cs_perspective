

# Assignment 4 

Synthesizer software emulation and implementing research papers 
--------------------------------------------------------------- 

This assignment comes in two versions. The first version focuses on real-time implementation and software simulation of an existing synthesizer (the Yamaha DX21) and is heavier in terms of programming. The second version looks at the implementation of some synthesis techniques from research papers and is more focused on coding and presenting algorithms so it is less heavy in terms of programming but requires more math understanding. It will be easier if you work on one version or the other but if you decide to mix questions that is fine. As usual I will use the term familiar programming 
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

## VERSION 2 - Research paper implementation 

1. (Basic) 

2. (Basic) 

3. (Basic) 

4. (Basic) 

5. (Expected) 

6. (Expected) 

7. (Expected) 

8. (Expected) 

9. (Advanced) 

10. (Advanced) 
