# BootAnimations Creator 
Simplicity.

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
1. Install Python 3 with PIP (optionally Tkinter).

Debian:
```bash
apt install python3 python3-pip
# Optional
apt install python3-tk
```
macOS:
    To fill in

Windows:
    Download a package from https://www.python.org/

2. Install git

Debian:
```sh
sudo apt install git
```
macOS:
```sh
brew install git
```
Windows:
    Take a look at https://git-scm.com/download/win

3. `git clone` this repository and `cd` into it
```sh
git clone https://github.com/MajliTech/bootanimation-creator.git
#or, with ssh if you prefer
git clone git@github.com:MajliTech/bootanimation-creator.git
cd bootanimation-creator
```
4. Create a venv (optional, if you plan on building then this will make binaries lighter)
```sh
#on ubuntu, you need to install python3-venv
sudo apt install python3-venv
pip install pyvenv
python3 -m venv .
#On windows, you might need to remove the 3 extension in case it is asking for install from MS Store
```
5. Download requirements
```
python3 -m pip install -r src/requirements.txt
```
6. Run!
```sh
python3 src/main.py
#Again, on windows, you might need to remove the 3 extension in case it is asking for install from MS Store
```
### Build an executable
1. Follow steps 1-5 from previous guide
2. If you have created a venv for this build, install Pyinstaller: `pip install pyinstaller`
3. Build
```
pyinstaller src/main.spec
```
4. The executable will be placed in the `src/dist` folder, go pick it up and run it!
## FAQ
### What is this?
This is a simple Python script that turns an ffmpeg video or png series into an Android boot animation. 
### Why was this created?
I didn't discover any tools that would do this, so I decided to make one.


