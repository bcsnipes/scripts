import subprocess
import sys

OSA_SCRIPT = """/usr/bin/osascript<<END 
tell application "System Events"
    tell every desktop
        set picture to "{}"
    end tell
end tell
END"""

def change_wallpaper(path):
    subprocess.Popen(OSA_SCRIPT.format(
        path), shell=True)

if __name__ == "__main__":
    change_wallpaper(sys.argv[1])


