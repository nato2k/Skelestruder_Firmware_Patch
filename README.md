# Skelestruder_Firmware_Patch
Python script to patch Prusa firmware for Skelestruder

This pulls the latest firmware from Prusa and patches it for Skelestruder.  There are a couple commented lines in skele_patch.py for reducing the extruder motor current, uncomment if you wish to update.

Use build_wsl.sh to build the firmware.

Now accepts arguments for E and uSteps.  For example ./build_wsl.sh 980 16 will use 980 esteps and 1/16 usteps.  Valid values for uSteps are 32, 16, and 8.  If 8 usteps are selected then extruder motor currents will be increased slightly.

Needs requirements listed on https://github.com/prusa3d/Prusa-Firmware

In order to make sure the firmware changes are loaded, you need to send M502 and then M500 to your printer after the update.  This recalls defaults from firmware and saves them to EEPROM
