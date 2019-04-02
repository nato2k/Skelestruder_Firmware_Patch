#!/bin/bash
if [ -d Prusa-Firmware ]
then
	rm -rf Prusa-Firmware
	echo "removing old directory"
fi
git clone https://github.com/prusa3d/Prusa-Firmware
python3 skele_patch_v2.py
rc=$?
if [ $rc = 1 ]
then
	echo "failed updating... exiting"
else
	echo "compiling firmware"
	./Prusa-Firmware/build.sh
	echo "complete!"
fi
