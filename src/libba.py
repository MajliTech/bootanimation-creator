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
            cmd = "ffmpeg -i \"{0}\" bc-tmp/bootanim/part{1}/%04d.png".format(i["path"][0], i["part"])
            s = subprocess.getstatusoutput(cmd)
            if s[0] != 0:
                raise OSError("Error executing ffmpeg command: Exited with code {}".format(s[0]))
            cmd = "ffmpeg -i \"{0}\" bc-tmp/bootanim/part{1}/audio.wav".format(i["path"][0], i["part"])
            s = subprocess.getstatusoutput(cmd)
        else:
            try:
                shutil.rmtree("bc-tmp/bootanim/part{}".format(i["part"]))
            except:
                pass
            shutil.copytree(i["path"][0],f"bc-tmp/bootanim/part{i['part']}")
            if str(i['path'][1]).endswith(".wav"):
                shutil.copy(i["path"][1],f"bc-tmp/bootanim/part{i['part']}/audio.wav")
            else: 
                if i['path']['1']: print(f"libba: The specified audio file for part {i['part']} is invalid ({i['path'][1]}). Please choose a file ending with .wav.\nlibba: Skipping audio file for part nr {i['part']}")
def pack_zip(file, deltemp=True):
    with zipfile.ZipFile(file, "w", compresslevel=zipfile.ZIP_DEFLATED) as zip_file:
        for root, dirs, files in os.walk("bc-tmp/bootanim"):
            base_dir = os.path.relpath(root, "bc-tmp/bootanim")
            for filename in files:
                file_path = os.path.join(root, filename)
                arcname = os.path.join(base_dir, filename)
                zip_file.write(file_path, arcname=arcname)
    if deltemp:
        shutil.rmtree("bc-tmp/bootanim")

    if deltemp: shutil.rmtree("bc-tmp")
def find_vid_res(pathToInputVideo):
    cmd = "ffprobe -v quiet -print_format json -show_streams"
    args = shlex.split(cmd)
    args.append(pathToInputVideo)
    ffprobeOutput = subprocess.check_output(args).decode("utf-8")
    ffprobeOutput = json.loads(ffprobeOutput)
    height = ffprobeOutput["streams"][0]["height"]
    width = ffprobeOutput["streams"][0]["width"]

    return [int(height), int(width)]



if __name__ == "__main__":
    print("! Please do not run this as a standalone.")
