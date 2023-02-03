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

1. Implement a simple patch editor/library for a particular hardware synth. It does not need to cover all the available functionality but it should have enough functionality that it is useful. A simple GUI is sufficient or even command-line interface is sufficient. (10 points) 
2. Create a simple sampling-based synthesizer for an instrument of your own choice. You will need to sample the instrument for a few different pitches and dynamics and then use interpolation and some logic to make your synthesizer able to play any pitch and dynamic. Your synthesizer should respond to MIDI and generate audio. Typically such as a software synthesizer is implemented as an audio plugin or it could also be a VCV rack module. (10 points) 
3. Implement a simple software MIDI sequencer. It should support simple recording, editing, and playback of MIDI events.  (10 points) 
4. Implement a simple drum machine using samples and a grid software interface. The drum machine should also respond to MIDI messages (10 points) 
5. Simple audio effect with a few parameters (no fancy GUI or MIDI control needed). Examples could be a parametric filter, a simple equalizer, a simple reverb, or a compressor. Typically this would be a VST/Audio Plugin with JUCE or Faust being the recommended programming framework. (10 points) 
6. Live coding performance (10 points) 

## Expected Projects (sum up to 40) 

1. Implement a software emulator of a particular hardware synth. You should be able to interface with your software synthesizer using MIDI and generate audio. Typically such as software emulator is implemented as an audio plugin or it could also be a VCV rack module. For synthesizers of the 80s, you can cover most if not all of the functionality of the synthesizer but for more modern ones you might need to pick a subset (for example do not implement the sequencer) . (20 points) 
2. Create a simple parser and sound synthesis engine for Music V - which is one of the first computer music programming languages. There is an existing working compiler that uses modern Fortran. With modern libraries and more flexible languages like Python writing a simple parser/sound synthesis engine is a reasonable project. (20 points) 
3. Procedural sound generation using a computer music framework or language (Chuck, SuperCollider, CSound, Faust, Max/MSP or PureData). This refers to generating sounds or textural that have characteristics that can be controlled. Examples include wind, rotor and motor sounds, footsteps, rain etc. (20 points)
4. Car engine modeling (20 points) 
6. Retro game audio engine (20 points) 
7. Real-time phase vocoder (20 points) 
8. Granular synthesizer (20 points) 
9. Real-time audio effects processor - multiple effects, MIDI control, nicer GUI - extension of basic project 5. (20 points) 
10. Classic paper demonstration notebook (20 points) 
11. Non-trivial contribution to existing open source codebase of computer music software (10 points) 
12. Stereo panning and delay effects (20 points) 


## Advanced Projects (sum up to 50) 


1. Physical Modeling Synthesis - implement some sound synthesis technique that is based on modeling the physics of sound production and provide expressive controls (10-20 points) 
2. Virtual analog synthesis (10-20 points) 
3. Chip tunes (10-20 points)
4. Inverse sound matching (10-20 points)  
5. Semantic patch browser (10-20 points) 
6. New approaches to patching and programing (semi-modular, implicit, textual) (20 points)
7. New approaches to live coding (10-20 points)
8. Hardware/physical computing (10-20 points) installation, music robot, hyper-instrument, non-invasive sensing) (20 points)
9. Virtual and Augmented reality control interface (10-20 points)
10. Retargeting to webassembly/webaudio existing computer music languages/environments (10-20 points)
11. Music information retrieval analysis module to VCV voltage outputs (10-20 points)
12. 3D sound source placement for multiple synthesizers (10-20 points) 
13. GPU sound syntheis (torch synth) (10-20 points) 
14. Multi-computer network synthesis (10-20 points) 

Total points: 50 

