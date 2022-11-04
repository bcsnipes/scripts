import os
import pathlib
import subprocess
import sys

IMG_EXT = '.jpg'
IMG_FOLDER = 'dynamic'

OSA_SCRIPT = """/usr/bin/osascript<<END 
tell application "System Events"
    tell every desktop
        set picture to "{}"
    end tell
end tell
END"""

def set_wallpaper(time):
    os.chdir('/Users/eme/Wallpapers+')
    path = os.path.join(
        pathlib.Path().absolute(),
        IMG_FOLDER,
        time + IMG_EXT
    )
    subprocess.Popen(OSA_SCRIPT.format(
        path), shell=True)

if __name__ == "__main__":
    set_wallpaper(sys.argv[1])


