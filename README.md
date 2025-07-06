# BootAnimations Creator 
Simplicity.
### What is this?
This is a simple Python script that turns a ffmpeg video or png series into an Android boot animation. 
### Why was this created?
I didn't discover any tools that would do this, so I decided to make one.

[![Build executables](https://github.com/MajliTech/bootanimation-creator/actions/workflows/build.yml/badge.svg)](https://github.com/MajliTech/bootanimation-creator/actions/workflows/build.yml)

## Dependencies
FFmpeg if you plan on decoding video files. If you already have a WAV file and series of PNGs you don't need anything.

## Running
### From releases
You can download a binary for your system.
currently supported OSes are:
 - Windows x64
 - Linux x64 (may or may not also run on macOS x64)

### Running from source
If you want to run this from source, you can!  
1. Install requirements first:

#### Debian:
```bash
sudo apt install python3 python3-pip git
# Optional
sudo apt install python3-tk
```

#### Fedora:
```bash
sudo dnf install python3 python3-tkinter git
```

#### Windows:
Download Python from: https://www.python.org/  
Download git from: https://git-scm.com/download/win

#### macOS:
```commandline
brew install git
```
To be done.

2. Clone:
```bash
git clone https://github.com/MajliTech/bootanimation-creator.git
# Or, with ssh if you prefer
git clone git@github.com:MajliTech/bootanimation-creator.git
cd bootanimation-creator
```

3. Create a venv (optional, if you plan on building then this will make binaries lighter):
```bash
# On Ubuntu, you need to install python3-venv
# On Windows, you might need to use python instead of python3 in case it is asking for install from MS Store.
sudo apt install python3-venv
python3 -m venv .
```

4. Download requirements:
```bash
# On Windows, you might need to use python instead of python3 in case it is asking for install from MS Store.
python3 -m pip install -r src/requirements.txt
# On Windows you also need:
python3 -m pip install --upgrade pywin32
```
5. Run:
```bash
# On Windows, you might need to use python instead of python3 in case it is asking for install from MS Store.
python3 src/main.py
```

### Build an executable
1. Follow steps 1-5 from previous guide
2. If you have created a venv for this build, install Pyinstaller: `pip install pyinstaller`
3. Build
```
pyinstaller src/main.spec
```
4. The executable will be placed in the `src/dist` folder, go pick it up and run it!
