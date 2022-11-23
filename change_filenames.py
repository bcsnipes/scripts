import datetime
import os
import sys

def change_filenames(path, prefix):
  for file_name in os.listdir(path):
    # Extract
    birthtime = os.stat(path).st_birthtime
    converted_datetime = datetime.datetime.fromtimestamp(birthtime)

    # Format
    formatted = (converted_datetime.strftime(f'/{prefix}_%y%m%d%H:%M%S'))
    source = path + "/" + file_name
    destination = path + formatted + '.jpg'

    # Rename
    os.rename(source, destination)

    # print(destination)


if __name__ == "__main__":
  change_filenames(sys.argv[1], sys.argv[2])

