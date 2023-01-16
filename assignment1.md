SIMPLE SYNTHESIZER 
------------------

In this assignment we will mostly explore the basic sine wave
oscillator and playing simple melodies using it. A reasonable "hello
world" of sound synthesis can be a tuning note i.e creating 3 seconds
a sine wave at 440Hz sampled at a typical audio sampling rate such as
44100 or 48000 samples per second.

Similarly to "hello world" this program does not do anything particularly
interesting but completing it ensures that you are able to compile and
interpret your code, generate an audio signal, and hear it which at
the end of the day is all you need to experiment with sound synthesis using
software.

I will use the term familiar programming language to refer to the ones
that you probably have encountered during your studies: Python, C,
C++, Java, and Javascript. As you probably can guess I will use the
term unfamiliar programming language to refer to any other programming
language such as: Haskell, OCaml, Prolog, Rust, Go, Julia, Ruby, C#, F#
R, etc.

For all basic questions (1,2,3,4) use a familiar programming language. 

1. (Basic)

Create an array of digital samples corresponding to 3
seconds of a 440Hz sinusoid with a sampline rate of 44100 samples per
second. Either play the resulting tone directly if your language
supports it (feel free to use a library if one is available) or write
a sound file that you can listen to using some external program such
as the Audacity audio editor. You are allowed to use a soundfile
reading/writing library if you can find one for the language you are
using or you can write one yourself (there are many resources
documenting the .wav file format for example
https://docs.fileformat.com/audio/wav/ - you don't need to implement
all possible options just get one basic one working. Use a familiar
programming language. 

2. (Basic)

Using the code you wrote in question 1 create a function that
takes as arguments a MIDI note number and a duration and similarly
generates a sinusoidal sound. Use this function to create a simple
recognizable melody by concatenating the corresponding arrays with
appropriate pitches and durations. If you can't think of a melody
Bicycle made for two (Daisy, Daisy) or the star wars theme or
happy birthday are common choices. 


3. (Basic)

Now generalize your code to take as input a simple score language.
The score language should specifiy pitches and durations and include
rests (silent duration). You can choose how you represent pitches
in terms of relative or absolute encoding or similarly how your represent
durations (absolute time or as a fractions of measures at a specified tempo)
or using NoteOn and NoteOff events. You can use a subset of SKINI
(https://ccrma.stanford.edu/software/stk/skini.html)
if you don't want to make up your own format.  


4. (Basic) 

Implement the following oscillators: Sawtooh, Pulse, Triangle and Noise
There are different ways to implement some of them - any reasonable
implementation is fine. 

5. (Expected)

Software that processes digital audio typically operates using buffers
of samples. Re-implement questions 1,2,3,4 but using buffers. For
example, to create a sinusoid for 1 second your oscillator function
will be called multiple times to generate a user-provided number of
samples (256, 512, 1024 are common buffer sizes). You will need to
keep track of where you are in terms of the signal so that no
discontinuities are created. If you are using a software library for
playing audio that is based on call-backs you can implement your
buffered oscillators as call-back functions.

6. (Expected)

Extend the monophonic synthesizer you created in the previous
questions to support polyphony and multiple oscillators. You can
implement polyphony using a fixed number of oscillators (one for each
voice) and do not need to deal with any smart voice allocation. Check
to see what level of polyphony you can support with your
implementation on your computer by increasing the number of
oscillators gradually until you can not keep up with real time.

7. (Expected)

Implement some of the basic functionality (questions 1,2)
using a visual programming language (Max/MSP or PureData or feel free
to suggest other ones)

8. (Expected)

Implement all of the basic functionality (questions
1,2,3,4) using a textual programming language that is designed for
sound and music (Csound, Nyquist, Chuck, Supercollider, Faust). Only
one language implementation is required for full marks.


There are 4 advanced questions. You only need to implement 2 of them
for full marks.


9. (Advanced)

Implement all functionality of the simple synthesizer (questions
1,2,3,4,5,6) using an unfamiliar programming language.


10. (Advanced)

Look into how one can implement the sin/cos function without using
built-in library implementations. Typically implementation use a
combination of polynomial approximations (Taylor Series, Chebyshev
polynomials) and wavetable interpolation. Implement the sine function
using 3 different approaches (different polynomial orders can be
considered different approaches) and compare them in terms of time and
memory requirements. Any programming language can be used for this
question.


11. (Advanced) 

Implement all functionality of the simple synthesizer (questions
1,2,3,4,5,6) as a AudioUnit/VST plugin using the JUCE software
framework in C++.  - you don't need to directly implement the score
but can respond to MIDI input.

12. (Advanced) 

Implement all the functionity of the simple synthesizer (questions
1,2,3,3,4,5,6) as a VCV Rack modular component.
