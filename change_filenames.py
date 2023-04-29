import datetime
import os
import sys

def change_filenames(path):
    for entry in os.scandir(path):
        if entry.is_file():
            source = entry.path
            birthtime = entry.stat().st_birthtime
            converted_datetime = datetime.datetime.fromtimestamp(birthtime)
            formatted = converted_datetime.strftime(f"%y%m%d_%H%M%S")
            extension = os.path.splitext(source)[1]
            destination = os.path.join(path, f"{formatted}{os.path.splitext(source)[1]}")
            if source != destination:
                os.rename(source, destination)

if __name__ == "__main__":
    change_filenames(sys.argv[1])


