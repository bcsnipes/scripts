import datetime
import os
import sys

def change_filenames(path, prefix, extension = ".jpg"):
  for file_name in os.listdir(path):
    birthtime = os.stat(f"{path}/{file_name}").st_birthtime
    converted_datetime = datetime.datetime.fromtimestamp(birthtime)

    formatted = (converted_datetime.strftime(f'{prefix}_%y%m%d_%H%M%S'))
    source = f"{path}/{file_name}"
    destination = f"{path}/{formatted}.{extension}"

    os.rename(source, destination)

if __name__ == "__main__":
  change_filenames(sys.argv[1], sys.argv[2], sys.argv[3])

