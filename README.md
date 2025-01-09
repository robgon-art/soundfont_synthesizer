# SoundFont Synthesizer
A simple one-octave synthesizer using FluidSynth and a SoundFont

![A screenshot of the keyboard](keyboard.png)

## Installation Instructions

1. To run the app, you need to first download and install the FluidSynth library from here:</br>
  https://github.com/FluidSynth/fluidsynth/releases</br>
Download fluidsynth-2.4.2-win10-x64.zip, unzip the folder, put it someplace on your system and add an environment path to the bin folder.

2. Download or clone the repo to run the code, unzip it, and put it somewhere on your drive.

3. Download a sound font file, like this one, Dore Mark's NY S&S Model B-v5.2.sf2</br>
  https://drive.google.com/file/d/1nvTy62-wHGnZ6CKYuPNAiGlKLtWg9Ir9/view</br></br>
Place the SoundFont file in the soundfont_synthesizer folder.

4. Install these projects with pip:
   pygame pyfluidsynth

5. Run python soundfont_synthesizer.py, and you should see this and be able to play. Blue indicates the pressed notes.

## Acknowledgments
This project was made possible by the following resources:

- **FluidSynth**: A real-time software synthesizer based on the SoundFont 2 specifications.
- **PyGame**: A set of Python modules designed for writing video games, used here for the graphical interface and input handling.
- **pyFluidSynth**: A Python wrapper for the FluidSynth library, enabling seamless MIDI and SoundFont functionality integration into Python projects.
- **SoundFont Technology**: A file format and associated technology that uses sample-based synthesis to play MIDI files. 
- **Dore Mark** for his NY S&S Model B-v5.2 SoundFont: A high-quality SoundFont sampled by Dore Mark, providing the rich tones of a New York Steinway Model B piano.
- **Adam Dingle** for his FluidSynth installation instructions.
