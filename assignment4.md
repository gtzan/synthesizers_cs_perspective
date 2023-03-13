

# Assignment 3 

Modal synthesis, filters, spectral analysis and FM synthesis 
------------------------------------------------------------

In this assignment we will explore some fundamental DSP concepts 
to better understand the concepts we covered in class. In addition, 
we will look into the MIDI communication protocol and file format for 
controlling synthesizers and storing performance information. 

Similarly to the first assignment I will use the term familiar programming 
language to refer to the ones that you probably have encountered during your 
studies: Python, C, C++, Java, and Javascript. As you probably can guess I will use the
term unfamiliar programming language to refer to any other programming
language such as: Haskell, OCaml, Prolog, Rust, Go, Julia, Ruby, C#, F#
R, etc. I will use the term computer music textual languages to refer to languages 
that have extensive support and primitives for sound and music manipulation such as 
Chuck, Supercollider, Csound, Nyquist, and Faust and visual programming languages 
for languages such as PureData and Max/MSP. 

Unless explicitly stated you can use any programming languages for implementing 
the questions. Using a computer music language moves the degree of difficulty down and using an unfamiliar programming language moves it up. For example if you implement question 6 in Max/MSP or Chuck it counts as basic rather than expected. If you implement question 6 in an unfamiliar programming languages it can count as advanced. In general, I am flexible so if you want to adjust things just let me know. Also if you 
think of a question of comparable difficulty that you would like do again let me know and most likely 
it should be ok. 

If you need access to devices ask me via email or through Discord for access to ECS602. 

1. (Basic) Watch one of the videos listed under [Resources](resources.md). Select a short part of the video (something like 15-30 seconds) and make an explicit connection to any of the concepts we have covered in the course. Write a short paragraph describing the connection and provide the timing of the excerpt you considered. 

2. (Basic) Watch one of the interviews listed under [Resources](resources.md). Select a short part of the interview (something like 30-60 seconds) and make an explicit connection to any of the concepts we have covered in the course. Write a short paragraph describing the connection and provide the timing of the excerpt you considered. 

3. (Basic) Get two different coffee mugs and record the sound of hitting them with a pen. Plot the corresponding magnitude spectra (there is some code for plotting magnitude spectra in Python in the FM synthesis notebook) - you are welcome to use other tools. 

4. (Basic) Create two additive synthesis models of the coffee mug recordings from question 3. Each model should consist of 4 sinusoidal oscillators and associated envelopes. Listen to the resulting sound and comment on whether you can recognize which coffee mug is which from the additive synthesis approximation. You can use any language (including computer music languages) for this question. 

5. (Expected) Create two modal synthesis models of the coffee mug recordings from question 3. Each model should consist of 4 BiQuad filters with appropriate associated center frequencies and resonances excited by an impulse function. Listen to the resulting sound and comment on whether you can recognize which coffee mug is which from the modal synthesis approximation. You can use any language (including computer music languages) for this question.  

6. (Expected) Compare the mangitude spectra of the original mug recordings, the additive synthesis approximation, and the modal synthesis approximation. Describe what you observe and comment on whether it corresponds to what you hear. 

7. (Expected) Synthesize a percussive sound using FM synthesis. The attack should be short and there should be many frequencies (i.e a high modulation index). Experiment with the amplitude and modulation index envelope shape until you have a good percussive sound. 

8. (Expected) Implement the parametric two pole filter used in the water bottle modal synthesis paper and described in this publication - create two audio examples showing how it can be used: https://ccrma.stanford.edu/~jos/smac03maxjos/smac03maxjos.pdf

9. (Advanced) Use the parametric two-pole filter mentioned in question 8 to create another modal synthesis approximation for the two coffee mugs of questions 5,6. Repeat the comparison between the different models both in terms of magnitude spectrums and in terms of listening. The water bottle modal synthesis paper (https://dafx2020.mdw.ac.at/proceedings/papers/DAFx2020_paper_24.pdf) describes a process for estimating the mode decay that you can follow for the coffee mug recordings. 

10. (Advanced) Implemented a real-time version of any of the synthesis models you developed in this assignments. You can use any language/programming environment for this question. 

