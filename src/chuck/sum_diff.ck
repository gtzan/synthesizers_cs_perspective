

// In modulation, a carrier is modulated (multiplied) by a modulator 

.1 => dac.gain; 

SinOsc carrier => Gain g => dac;
SinOsc modulator => g => dac;

// default operation is addition 
1 => g.op;
320.0 => carrier.freq;
440.0 => modulator.freq; 
2::second => now;

// multiplication results in ring modulation 
3 => g.op;
2::second => now;

1 => g.op;
0.5 => g.gain;
760 => carrier.freq;
760 => modulator.freq;
2::second => now;

120 => carrier.freq;
120 => modulator.freq;
2::second => now;
