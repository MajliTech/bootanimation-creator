# ---------------------------------------------------------------------
# BootAnimation Creator
# By MajliTech
# You should have a LICENSE file attached to this project
# If not, please see https://spdx.org/licenses/LGPL-3.0-or-later.html
# This project is possible by https://android.googlesource.com/platform/frameworks/base/+/master/cmds/bootanimation/FORMAT.md
# They are providing some instructions on how to configure you BootAnimation ZIP
# ---------------------------------------------------------------------


#Libraries
import colorama
import os
import easygui
import libba
import time

#Initalize
colorama.init()
Fore = colorama.Fore
Back = colorama.Back
Style = colorama.Style
part = 0
INFO = "INFO"
QUES = "QUES"
ERR = "ERR"
WARN = "WARN"
def add_part():
    # The specs say that there are 3 types of parts:
    """
    p -- this part will play unless interrupted by the end of the boot
    c -- this part will play to completion, no matter what
    f -- same as p but in addition the specified number of frames is being faded 
    out while continue playing. Only the first interrupted f part is faded out, 
    other subsequent f parts are skipped
    """
    # Since this is a basic tool for now, we are only interested in the first 2.
    # So let's provide this for our user:
    part = {}
    typecor = False
    prform(INFO, "The possible types are:")
    while True:
        print(" - p - This part wil play, but will stop when boot ended")
        print(" - c - this part will play, no matter what happens")
        typ = prinp(QUES, "What type the first part should be?")
        if typ=="c" or typ=="p": break
        prform("ERR"," Invalid type! Try using the tips below.")    
    part["type"] = typ
    while True:
        cnt = prinp(QUES, "How many times should this part be repeated?")
        try:
            cnt = int(cnt)
            break
        except:
            prform("ERR"," Invalid count!")   
    part["count"] = cnt 
    while True:
        dela = prinp(QUES, "How many FRAMES should be delayd after this part?")
        try:
            dela = int(dela)
            break
        except:
            prform("ERR"," Invalid count!")   
    part["delay"] = dela 
    part["part"] = 0
    prform("INFO","Possible media types are:")
    while True:
        print(Fore.LIGHTRED_EX+" - png (soon): a series of PNG images. They must be named number by number (0000.png, 0001.png, 0002.png, ...)"+Fore.RESET)
        print(" - ffmpeg: Files will be decoded from ffmpeg to png and audio format. You can specify whatever file as long as FFmpeg supports it.")
        med = prinp(QUES, "Which type of media do you want to add to your boot animation?")
        if med=="ffmpeg": break
        prform("ERR","Invalid media type! Use the tips bellow.")
    if med=="ffmpeg":
        part["ffmpeg"] = True
        if tk: p = easygui.fileopenbox()
        else: p = prinp(QUES,"Please provide a path to the video:")
        part["path"] = [p,p]
    else:
        prform(ERR, "Soon!")
    #     part["ffmpeg"] = False
    #     if tk: p = easygui.diropenbox()
    #     else: p = prinp(QUES,"Please provide a path to the folder:")
    #     if prinp("QUES","Would you also like to include WAV for this part? (Y/N)").lower()=="y":
    #         if tk: a = easygui.fileopenbox(filetypes=["*.wav"])
    #         else: p = prinp(QUES,"Please provide a path to the audio:")
    #         part["path"] = [p,a]
    #     else:
    #         prform(INFO,"Not including audio for this part.")
    #         part["path"] = [p,None]
    return part
# Clean terminal for us
print("\n"*os.get_terminal_size()[1])
print (u"{}[2J{}[;H".format(chr(27), chr(27)), end="")
# print("\033c",end="")
# clear()
#A simple function which prints out formatted string with color and what is it.
def prform(which:str, string:str):
    INFO = Fore.BLUE+"i "+Fore.WHITE
    QUES = Fore.MAGENTA+"? "+Fore.WHITE
    ERR = Fore.RED+"X "+Fore.WHITE
    WARN = Fore.YELLOW+"! "+Fore.WHITE
    CONG = Fore.LIGHTGREEN_EX+"✓ "+Fore.WHITE
    if which=="INFO":
        print(INFO+string)
        return INFO+string
    elif which=="QUES":
        print(QUES+string)
        return QUES+string
    elif which=="ERR":
        print(ERR+string)
        return ERR+string
    elif which=="WARN":
        print(WARN+string)
    elif which=="CONG":
        print(CONG+string)
def prinp(which:str, string:str):
    INFO = Fore.BLUE+"i "+Fore.WHITE
    QUES = Fore.MAGENTA+"? "+Fore.WHITE
    if which=="INFO":
        return input(INFO+Style.BRIGHT+string+Style.NORMAL+" >> ")
    elif which=="QUES":
        return input(QUES+Style.BRIGHT+string+Style.NORMAL+" >> ")
# This should look something like this:
# {"width": 1080, "height": 1920, "fps":30}
specs = {}
animations = []
# Sample object in animations:
# {'type': 'p', 'count': 0, 'delay': 0, 'part': 0, 'ffmpeg': True, 'path': ['/home/majlitech/Downloads/y2mate.com - konczysz technikum idziesz na studia D_360p.mp4', '/home/majlitech/Downloads/y2mate.com - konczysz technikum idziesz na studia D_360p.mp4']}
try:
    import tkinter as tk
except ImportError:
    tk = None

print(Fore.RED+"❊ BootAnimation Creator")
print(Fore.GREEN+"❊ by MajliTech")
if not libba.check_ffmpeg(): 
    prform(WARN, "ffmpeg was not detected. Please CTRL+C in 10 seconds to cancel program's startup.")
    prform(INFO, "FFmpeg is being used when converting videos to boot animations. \n   - If you already have your animation in PNG series you can safely ignore this warning.")
    try:
        time.sleep(10)
    except:
        print("\r",end="")
        prform("ERR", "CTRL+C detected! Exiting...")
        raise SystemExit()
prform("INFO","We will now go through setup procedure")
prform(INFO,"Value below should be declared like this: WIDTHxHEIGHT, for example: 1080x1920")
correct = False
#Handle ^C 
try:
    # Let's initalize the ZIP's desc.txt file
    while not correct:
        res = prinp(QUES,"What resolution is your animation?")
        try:
            res = res.split("x")
            int(res[1])
            if len(res)==2:
                for i in enumerate(res):
                    res[i[0]] = int(i[1])
                correct = True
        except:
            prform("ERR", "Invalid resolution! Try again:")
    while True:
        fps = prinp(QUES, "At what FPS is your boot animation?")
        try:
            fps = int(fps)
            break
        except:
            prform("ERR","This isn't vaild FPS number.")
    # We're done here. Let's add it to the specs:
    specs["width"] = res[1]
    specs["height"] = res[0]
    specs["fps"] = fps

    # The string says it all.
    prform("INFO","Now we will add the first part of your boot animation.")
    animations.append(add_part())
    prform("CONG","Congrats! You have your first BootAnimation part!")
    yea = prinp(QUES, "Do you want to add more parts?")
    if yea.lower()=="y":
            animations.append(add_part())
    if tk: loc = easygui.filesavebox(default="bootanimation",msg="Save ZIP (without .zip, this will be automatically added)")
    else: loc = prinp(QUES,"Enter location of ZIP (without .zip, this will be automatically added)")
    prform(INFO,"Starting animation creation...")
    prform(INFO,"1/3: Generate desc.txt")
    libba.gen_desc(animations,specs)
    prform(INFO,"2/3: Copy media to bc-tmp (or decode to PNGs)")
    libba.decode_media(animations,specs)
    prform(INFO,"3/3: Pack to zip and remove Temp Folder")
    libba.pack_zip(loc)
    prform("CONG", "Your boot animations is complete!")
    prform(INFO,"It was saved under "+loc+".zip")
except KeyboardInterrupt:
    print()
    prform("ERR", "CTRL+C detected! Exiting...")

