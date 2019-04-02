# Skelestruder_Firmware_Patch
Python script to patch Prusa firmware for Skelestruder
This pulls the latest firmware from Prusa and patches it for Skelestruder.  There are a couple commented lines in skele_patch.py for reducing the extruder motor current, uncomment if you wish to update.
Use build.sh for linux/mac and build_wsl.sh for Windows subsystem for linux
Needs requirements listed on https://github.com/prusa3d/Prusa-Firmware
There appears to be a bug in the provided script from Prusa on Windows that requires you to run it twice
