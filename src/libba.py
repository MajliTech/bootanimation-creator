# ---------------------------------------------------------------------
# BootAnimation Creator
# By MajliTech
# You should have a LICENSE file attached to this project
# If not, please see https://spdx.org/licenses/LGPL-3.0-or-later.html
# ---------------------------------------------------------------------
import os
import subprocess
import shlex
import json
import zipfile
import shutil


try:
    os.mkdir("bc-tmp")
    os.mkdir("bc-tmp/bootanim")
except:
    pass
def check_ffmpeg():
    if shutil.which('ffmpeg') == None: return False 
    else: return True
    # return False # for testing purposes

# {
#     "type": "p",
#     "count": 0,
#     "delay": 0,
#     "part": 0,
#     "ffmpeg": True,
#     "path": [
#         "/home/majlitech/Downloads/y2mate.com - konczysz technikum idziesz na studia D_360p.mp4",
#         "/home/majlitech/Downloads/y2mate.com - konczysz technikum idziesz na studia D_360p.mp4",
#     ],
# }

# {"width": 1080, "height": 1920, "fps":30}
def gen_desc(animations: list, specs: dict):
    header = f"{specs['width']} {specs['height']} {specs['fps']}\n"
    parts = ""
    for i in animations:
        appe = f"{i['type']} {i['count']} {i['delay']} part{i['part']}\n"
        parts += appe
    with open("bc-tmp/bootanim/desc.txt","w") as f:
        f.write(header)
        f.write(parts)
        f.close()
def decode_media(animations: list, specs: dict):
    for i in animations:
        if i["ffmpeg"] == True:
            res = find_vid_res(i["path"][0])
            if not res[0] == specs["width"]:
                raise ValueError("Video size mismatch")
            if not res[1] == specs["height"]:
                raise ValueError("Video size mismatch")
            try:
                os.mkdir("bc-tmp/bootanim/part{}".format(i["part"]))
            except:
                shutil.rmtree("bc-tmp/bootanim/part{}".format(i["part"]))
                os.mkdir("bc-tmp/bootanim/part{}".format(i["part"]))
            cmd = "ffmpeg -i \"{0}\" bc-tmp/bootanim/part{1}/%04d.png".format(
                i["path"][0], i["part"]
            )
            s = subprocess.getstatusoutput(cmd)
            if s[0] != 0:
                raise OSError("Error executing ffmpeg command: Exited with code {}".format(s[0]))
            cmd = "ffmpeg -i \"{0}\" bc-tmp/bootanim/part{1}/audio.wav".format(i["path"][0], i["part"]            )
            s = subprocess.getstatusoutput(cmd)
def pack_zip(file: str,deltemp: bool = True):
    zip = zipfile.ZipFile(file,mode="w")
    for i in os.walk("bc-tmp/bootanim"):
        zip.write(i)
    zip.close()
    # shutil.make_archive("bc-temp/bootanim", 'zip', "bc-tmp")
    if deltemp: shutil.rmtree("bc-tmp")
def find_vid_res(pathToInputVideo):
    cmd = "ffprobe -v quiet -print_format json -show_streams"
    args = shlex.split(cmd)
    args.append(pathToInputVideo)
    # run the ffprobe process, decode stdout into utf-8 & convert to JSON
    ffprobeOutput = subprocess.check_output(args).decode("utf-8")
    ffprobeOutput = json.loads(ffprobeOutput)

    # find height and width
    height = ffprobeOutput["streams"][0]["height"]
    width = ffprobeOutput["streams"][0]["width"]

    return [int(height), int(width)]



if __name__ == "__main__":
    print("! Please do not run this as a standalone.")
    # shutil.rmtree("bc-tmp")
