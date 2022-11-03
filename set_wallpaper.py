import os
import pathlib
import random
import subprocess

FOLDER = 'test'

OSA_SCRIPT = """/usr/bin/osascript<<END 
tell application "System Events"
    tell every desktop
        set picture to "{}"
    end tell
end tell
END"""

def set_wallpaper():
    os.chdir('/Users/eme/Wallpapers+')
    files = os.listdir(FOLDER)
    random.shuffle(files)
    first_file = files[0]

    path = os.path.join(
        pathlib.Path().absolute(),
        FOLDER,
        first_file
    )

    subprocess.Popen(OSA_SCRIPT.format(
        path), shell=True)

set_wallpaper()