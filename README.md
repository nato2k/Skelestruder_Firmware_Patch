# Skelestruder_Firmware_Patch
Python script to patch Prusa firmware for Skelestruder

This pulls the latest firmware from Prusa and patches it for Skelestruder.  There are a couple commented lines in skele_patch.py for reducing the extruder motor current, uncomment if you wish to update.

Use build.sh for linux/mac and build_wsl.sh for Windows subsystem for linux

Needs requirements listed on https://github.com/prusa3d/Prusa-Firmware

In order to make sure the firmware changes are loaded, you need to send M502 and then M500 to your printer after the update.  This recalls defaults from firmware and saves them to EEPROM
