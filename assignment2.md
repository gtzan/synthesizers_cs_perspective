# Assignment 2 

DSP AND MIDI 
------------------

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
the questions. If you need access to devices ask me via email or through Discord for 
access to ECS602. 


1. (Basic)

Connect directly using MIDI two hardware devices without going through a computer (sometimes 
this is termed a DAWLESS setup). Write a short text description of which devices you connected 
and what issues you had to figure out. You will need to read a bit about MIDI input, output, and cables. 
A classic example could be connecting a MIDI keyboard and generating sound in a different keyboard or rack-mount synthesizer but it does not have to be a keyboard or synthesizers as long as it is clear you have 
two devices communicating with each other. 

2. (Basic) 

Show using a figure, programming, and math what is the result multiplying the complex number $(2+j)$ with $j$. For programming, represent the complex number as an array, list, or tuple and directly implement the complex number multiplication in terms of real and imaginary parts without using any built-in libraries or types for complex numbers. 

3. (Basic) 

Connect a hardware MIDI device to your laptop or desktop. Write code that prints out MIDI messages whenever they are received. Some devices can connect directly through USB, there are cheap USB to MIDI converters or you can go through an audio interface that has MIDI functionality. Similarly to question 1, just document your experience, what challenges you encountered, and what you learned. 


4. (Basic) Create one second of audio by summing the following sinusoidal frequencies ($100Hz, 200Hz, 300Hz$) all with the same phase, and three random amplitudes between $0.0$ and $1.0$. Listen to the generated sound and create 4 plots one for each individual sinusoid and one for the resulting mixed sound. Each plot should correspond to the time duration of one period of the lowest sinusoid ($100Hz$). Show how you can estimate these three random amplitudes by taking the dot product of the mixture with basis sinusoids of amplitude 1 for the three frequencies ($100Hz, 200Hz, 300Hz$). 


5. (Expected) This is an extension of question 4. Extend your code from question 4 so that the three sinusoidal components have random phases in addition to random amplitudes. Listen to the generated sound and create 4 plots one for each individual sinusoid and one for the resulting mixed sound. Each plot should correspond to the time duration of one period of the lowest sinusoid ($100Hz$). Show how the amplitudes and phases can be estimated for this sound in two ways: 



