# Scripts

This repo is a collection of scripts.

## Set Wallpaper

This script enables you to change the desktop wallpaper on OSX.

### Use Case

My primary use case is that I like to cycle through specific wallpapers at certain hours of the day, e.g. morning, afternoon, evening and night.

### Structure

- The image name can be passed as an argument when running the script.
- The default image extension is set to jpg.
- The wallpaper images should be in a specific folder.

### Cron Job

In order to run the script at given hours of the day, I've set up cronjobs.

```
0 06 * * * python ~/Repos/bcsnipes/public/scripts/set_wallpaper.py 01_morning
0 14 * * * python ~/Repos/bcsnipes/public/scripts/set_wallpaper.py 02_afternoon
0 19 * * * python ~/Repos/bcsnipes/public/scripts/set_wallpaper.py 03_evening
0 22 * * * python ~/Repos/bcsnipes/public/scripts/set_wallpaper.py 04_night
```
