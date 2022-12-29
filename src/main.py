# ---------------------------------------------------------------------
# BootAnimation Creator
# By MajliTech
# You should have a LICENSE file attached to this project
# If not, please see https://spdx.org/licenses/LGPL-3.0-or-later.html
# ---------------------------------------------------------------------


#Libraries
import colorama
#Initalize
colorama.init()
Fore = colorama.Fore
Back = colorama.Back
INFO = "INFO"
QUES = "QUES"
#A simple function which prints out formatted string with color and what is it.
def prform(which:str, string:str):
    INFO = Fore.BLUE+"i "+Fore.WHITE
    QUES = Fore.MAGENTA+"? "+Fore.WHITE
    ERR = Fore.RED+"! "+Fore.WHITE
    if which=="INFO":
        print(INFO+string)
        return INFO+string
    elif which=="QUES":
        print(QUES+string)
        return QUES+string
    elif which=="ERR":
        print(ERR+string)
        return ERR+string
def prinp(which:str, string:str):
    INFO = Fore.BLUE+"i "+Fore.WHITE
    QUES = Fore.MAGENTA+"? "+Fore.WHITE
    if which=="INFO":
        return input(INFO+string+" >> ")
    elif which=="QUES":
        return input(QUES+string+" >> ")
# This should look something like this:
# {"width": 1080, "height": 1920, "fps":30}
specs = {}
animations = {}
#Sample object for animations
# {"type":}

print(Fore.RED+"BootAnimation Creator")
print(Fore.GREEN+"by MajliTech")
prform("INFO","We will now go through setup procedure")
prform(INFO,"Value below should be declared like this: WIDTHxHEIGHT, for example: 1080x1920")
correct = False
#Handle ^C 
try:
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
            # pass
            prform("ERR", "Invalid resolution! Try again:")
    prform("INFO","Now we will add parts of your boot animation.")
except KeyboardInterrupt:
    print()
    prform("ERR", "CTRL+C detected! Exiting...")

