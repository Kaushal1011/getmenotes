# GMN _Notes
Author: Kaushal
## Pyo
-  Pyo Uses its own server to manage audio operations  
-  Notein class of Pyo is used to
 Receive midi notes, convert pitch to Hz and manage 10 voices of polyphony.
  
```python
                self.note = Notein(poly=10, scale=1, first=0, last=127)
       
```
-  Notein.keyboard() is used to display a gui keyboard on screen which mimics a virtual keyboard
  
```python
        self.note.keyboard()
        
```
-  Handle pitch and velocity (Notein outputs normalized amplitude (0 -> 1)).
 
```python
        self.pit = self.note['pitch'] * self.transpo
        
```
## S3Synth
-  S3Synth is a class that makes an audio processing based on certain defined routes
 <rgm> ![](routes.png) </rgm>
  
-  This handles the enveloping mechanism of this synthesiser
  
```python
        self.amp = MidiAdsr(0.5 * self.note['velocity'],
                            attack=0.1,
                            decay=1,
                            sustain=.5,
                            release=2,
                            mul=.4)
        
```
-  Create Oscilattor
 self.scope1=Scope(Mix([-1*self.osc1,-1*self.osc2]))
 self.scope1.g
 Selector takes multiple inputs and interpolates
 between them to generate a single output.
 Stereo mix using Band-limited Low Frequency Oscillator
 with different wave shapes.
 Mix audio streams
 
```python
        self.osc1 = Osc(table=self.t, freq=self.pit, mul=self.amp)
        self.osc2 = Osc(table=self.t2, freq=self.pit, phase=0.25, mul=self.amp)
        self.osc22 = Osc(table=self.t2,
                         freq=self.pit + np.pi / 2,
                         mul=self.amp)
                
                        self.osccos = Selector([self.osc2, self.osc22], voice=0.15)
        self.osccos.ctrl(title="Shift modulation amount")

                        self.osc3 = LFO(self.pit, sharp=0.5, type=2, mul=self.amp)
        self.osc3.ctrl(
            title=
            'Osc3 type 0=saw u 1=saw d 2=sq 3=tri 4=pulse 5=bipulse 6=s&h 7=Sine'
        )

        self.osc4 = LFO(self.pit, sharp=0.5, type=0, mul=self.amp)
        self.osc4.ctrl(
            title=
            "Osc4 type 0=saw u 1=saw d 2=sq 3=tri 4=pulse 5=bipulse 6=s&h 7=Sine"
        )

        self.extrasel = Selector(
            [self.osc3.mix(1), self.osc4.mix(1)], mul=0.05, voice=0.5)
        self.mainsel = Selector(
            [self.osc1.mix(1), self.osccos.mix(1)], mul=1, voice=0.5)
        self.mainsel.ctrl(title="Main Oscillator Volume")
        self.extrasel.ctrl(title="Extra Oscillator Volume Ctrl")

                self.mix = Mix([self.mainsel.mix(1), self.extrasel.mix(1)], voices=2)
        
```
