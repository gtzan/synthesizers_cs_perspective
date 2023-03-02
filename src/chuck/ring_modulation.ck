

SinOsc osc1 => Gain ring_multiplier => dac;
SinOsc osc2 => Gain dc_offset;
Step offset => dc_offset;
dc_offset => ring_multiplier;

0.5 => ring_multiplier.gain;
3 => ring_multiplier.op;

// carrier 
320.0 => osc1.freq;
// modulator 
440.0 => osc2.freq;
3::second => now;

  