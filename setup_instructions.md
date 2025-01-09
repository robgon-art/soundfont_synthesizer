Playing music from Python
=========================

You can play musical notes from a Python program using [FluidSynth](http://www.fluidsynth.org/), a free real-time software synthesizer.

Installing on Linux
-------------------

1\. Install the package containing the FluidSynth library. For example, on Ubuntu:

$ sudo apt install libfluidsynth3

2\. FluidSynth needs a file FluidR3\_GM.sf2 that contains waveforms for various musical instruments. Install the package contaning this soundfont file. For example, on Ubuntu:

$ sudo apt install fluid-soundfont-gm

On Ubuntu, the soundfont file will be located at `/usr/share/sounds/sf2/FluidR3_GM.sf2` .

3\. Install pyfluidsynth, which lets you access FluidSynth from Python:

    $ pip install pyfluidsynth

Installing on macOS
-------------------

1\. Install [Homebrew](https://brew.sh/) if you have not done so already.

2\. Use 'brew list' to see a list of all Homebrew packages that are installed on your machine. If you don't already have some version of the 'python' and 'python-tk' packages, then install them:

% brew install python
% brew install python-tk

3\. Be sure that you are running Python and pip from their Homebrew packages, **not** the versions that are preinstalled in macOS. You may need to [add a certain Homebrew directory to your PATH](https://stackoverflow.com/a/48101303/4034070).

4\. Install FluidSynth using brew:

% brew install fluid-synth

4\. FluidSynth needs a file FluidR3\_GM.sf2 that contains waveforms for various musical instruments. You can download this file from the page [The Fluid Release 3 General-MIDI Soundfont](https://member.keymusician.com/Member/FluidR3_GM/index.html). On that page, click the link 'Download FluidR3\_GM Soundfont'. Save the file in some directory.

5. Install pyfluidsynth, which lets you access FluidSynth from Python:

% pip install pyfluidsynth

Installing on Windows
---------------------

1\. Go to the [FluidSynth releases page](https://github.com/FluidSynth/fluidsynth/releases) and download the latest 64-bit release for Windows (e.g. fluidsynth-2.1.0-win64.zip). Extract this zip file into some directory, e.g. `c:\Users\``me``\install`.

2\. Add the `fluidsynth-x64\bin` subdirectory to your PATH. To do this, click in the search box on the task bar, run the command 'Edit the system environment variables', click 'Environment Variables…', select Path in the 'User variables' section, click 'Edit…', click New, then enter the path of the bin subdirectory, e.g. `c:\Users\``me``\install\fluidsynth-x64\bin`.

3\. FluidSynth needs a file FluidR3\_GM.sf2 that contains waveforms for various musical instruments. You can download this file from the page [The Fluid Release 3 General-MIDI Soundfont](https://member.keymusician.com/Member/FluidR3_GM/index.html). On that page, click the link 'Download FluidR3\_GM Soundfont'. Save the file in some directory.

4\. Install pyfluidsynth, which lets you access FluidSynth from Python:

pip install pyfluidsynth

pyfluidsynth API
----------------

Here are a few useful classes and methods. For more information, sees the [pyfluidsynth GitHub page](https://github.com/SpotlightKid/pyfluidsynth).

### fluidsynth.Synth class

A Synth is an instance of the FluidSynth synthesizer.

Synth()

Create a Synth.

.note\_off(_channel, key_)

Stop playing a note on the given channel. _key_ is a MIDI note number from 0 to 127.

.note\_on(_channel_, _key_, _velocity_)

Start playing a note on the given channel. _key_ is a MIDI note number from 0 to 127. _velocity_ is a value from 0 to 255.

.program\_select(_channel_, _soundfont\___id_, _bank_, _preset_)

Select a sound to play on the given channel (a number from 0 to 15), using the given soundfont. Usually _bank_ will be 0. For a general MIDI soundfont such as FluidR3\_GM.sf2, _preset_ will be a General MIDI instrument number.

.sfload(_filename_)

Load a soundfont into memory, returning an ID that references it.

.start(\[device = _name_\] \[driver = _name_\])

Start the synthesizer. On Linux, I recommend passing `device = 'hw:0'`. On Windows, I recommend passing `driver = 'dsound'`.

Example
-------

The following Python program will play a chord for a few seconds:

import time
import fluidsynth

fs = fluidsynth.Synth()
fs.start(device = 'hw:0')  \# on Windows, use "driver = 'dsound'"

sfid = fs.sfload('/usr/share/sounds/sf2/FluidR3\_GM.sf2')  \# replace path as needed
fs.program\_select(0, sfid, 0, 0)

fs.noteon(0, 60, 30)
fs.noteon(0, 67, 30)
fs.noteon(0, 76, 30)

time.sleep(3.0)

fs.noteoff(0, 60)
fs.noteoff(0, 67)
fs.noteoff(0, 76)

time.sleep(1.0)

Save this program to a file `chord.py`, and replace the path in the second commented line above with the full path to the FluidR3\_GM.sf2 file on your machine. Now run the program. You should hear a chord play.