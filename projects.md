
# Initial Projects Proposals 


1. Retro game sound engine - Cy 

   Old computers and game consoles included programmable sound generators which were chips that synthesized audio signals. These were used to create music for early video games and have similar architecture to synthesizers. Examples include the Commodore 64 and the Nintendo Entertainment System. The goal will be to have a software emulation of a chip like the MOS technology 6581 https://en.wikipedia.org/wiki/MOS_Technology_6581 and be able to render 8-bit game music using it. 
   
   https://github.com/crschung/vgm-audio-processor
   
   
   
   

3. Car engine modeling - Mitchell 

The goal of this project will be to analyze the sound of different car engines and create a parametric model that generates sound similar to the actual car engine that is controllable for example by increasing the rpm. 



5. Physical modeling of strings and bars - Robert 

   This project intends to explore the sounds of the Zimbabwean mbira through physical modelling synthesis techniques.
   See project github: https://github.com/rsmwood/mbira-modelling


6. Porting Music V compiler - Cameron 


7. Live coding environment - Grace 




8. Music programming language - Vicky 

This is a simple music programming language (see [github project link](https://github.com/iamvickynguyen/Synthtax)). The language will be something like this [examples](https://github.com/iamvickynguyen/Synthtax/tree/antlr/test). The goal is to create some sound synthesis without coding some basic stuff such as a sine wave, ADSR, adding sounds, etc.

Anyone with basic C++ and compiler knowledge is welcome!



9. Embedded tracker - Iain 


10. Oversampled and memory-heavy digital oscillators - Iain 




# Project Ideas (Please check regularly) 

This page is going to be evolving over the course of the term with more details as the projects get more fleshed out. Similarly to the assignments, the projects 
are labeled by their degree of difficulty (basic, expected, advanced). The total points for all project activity is 50. Membership in project is going to be fluid 
so for example you might decide to participate in multiple projects at different levels of engagement or focus on a single one on your own. 10 of the 50 
points are reserved for advanced projects, 20 of the 50 points have to be advanced or expected, and the remaining 20 can be advanced, expected, or basic. 
That way if you feel that particular level of difficulty is too easy, you can work on a higher level of difficulty. 

Each project has a number of allocated points. If you have a team and work equally on a project then the number of points is divided evenly. 
You can also contribute in smaller amounts. For example a project might be worth 10 points and by addings some document or fixing some bugs 
you could get 1 or 2 points. Projects at the same level of difficulty and same number of points should be approximately the same in terms of work involved although this could change depending on your background knowledge. Also the difficulty of the project can be adjusted based on the specifics of the implementation. For example a procedural sound generation engine is an expected project if you use a computer music language or environment but if you were to implement it in an unusual general programming language with few libraries from sound could be an advanced project. As the projects evolve we will iron out such details. 


## Basic Projects (sum up to 20) 

1. Implement a simple patch editor/library for a particular hardware synth. It does not need to cover all the available functionality but it should have enough functionality that it is useful. A simple GUI is sufficient or even command-line interface is sufficient. 
2. Create a simple sampling-based synthesizer for an instrument of your own choice. You will need to sample the instrument for a few different pitches and dynamics and then use interpolation and some logic to make your synthesizer able to play any pitch and dynamic. Your synthesizer should respond to MIDI and generate audio. Typically such as a software synthesizer is implemented as an audio plugin or it could also be a VCV rack module. (10 points) 
3. Implement a simple software MIDI sequencer. It should support simple recording, editing, and playback of MIDI events.  
4. Implement a simple drum machine using samples and a grid software interface. The drum machine should also respond to MIDI messages  
5. Simple audio effect with a few parameters (no fancy GUI or MIDI control needed). Examples could be a parametric filter, a simple equalizer, a simple reverb, or a compressor. Typically this would be a VST/Audio Plugin with JUCE or Faust being the recommended programming framework. 
6. Live coding performance 

## Expected Projects (sum up to 40) 

1. Implement a software emulator of a particular hardware synth. You should be able to interface with your software synthesizer using MIDI and generate audio. Typically such as software emulator is implemented as an audio plugin or it could also be a VCV rack module. For synthesizers of the 80s, you can cover most if not all of the functionality of the synthesizer but for more modern ones you might need to pick a subset (for example do not implement the sequencer) .  
2. Create a simple parser and sound synthesis engine for Music V - which is one of the first computer music programming languages. There is an existing working compiler that uses modern Fortran. With modern libraries and more flexible languages like Python writing a simple parser/sound synthesis engine is a reasonable project. (20 points) 
3. Procedural sound generation using a computer music framework or language (Chuck, SuperCollider, CSound, Faust, Max/MSP or PureData). This refers to generating sounds or textural that have characteristics that can be controlled. Examples include wind, rotor and motor sounds, footsteps, rain etc. 
4. Car engine modeling
6. Retro game audio engine 
7. Real-time phase vocoder  
8. Granular synthesizer 
9. Real-time audio effects processor - multiple effects, MIDI control, nicer GUI - extension of basic project 5. (20 points) 
10. Classic paper demonstration notebook  
11. Non-trivial contribution to existing open source codebase of computer music software (10 points) 
12. Stereo panning and delay effects 


## Advanced Projects (sum up to 50) 


1. Physical Modeling Synthesis - implement some sound synthesis technique that is based on modeling the physics of sound production and provide expressive controls 
2. Virtual analog synthesis 
3. Chip tunes 
4. Inverse sound matching   
5. Semantic patch browser  
6. New approaches to patching and programing (semi-modular, implicit, textual) (20 points)
7. New approaches to live coding 
8. Hardware/physical computing (10-20 points) installation, music robot, hyper-instrument, non-invasive sensing) 
10. Virtual and Augmented reality control interface 
11. Retargeting to webassembly/webaudio existing computer music languages/environments 
12. Music information retrieval analysis module to VCV voltage outputs 
13. 3D sound source placement for multiple synthesizers  
14. GPU sound syntheis (torch synth) 
15. Multi-computer network synthesis 

Total points: 50 

