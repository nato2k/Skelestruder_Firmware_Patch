#!/bin/bash
if [ -d Prusa-Firmware ]
then
	rm -rf Prusa-Firmware
	echo "removing old directory"
fi
git clone https://github.com/prusa3d/Prusa-Firmware
python3 skele_patch.py
rc=$?
if [ $rc = 1 ]
then
	echo "failed updating... exiting"
else
	if [ ! -d Hex-files ]
    then
        mkdir Hex-files
        echo "adding Hex-files directory to avoid build script bug"
    fi
    echo "compiling firmware"
	./Prusa-Firmware/build.sh
	echo "complete!"
fi
