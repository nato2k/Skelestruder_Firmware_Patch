#!/bin/bash
if [ $# < 2 ]
  then
    num1=980
	num2=16
	echo "default steps selected 980/16"
  else
    num1=$1
	num2=$2
	echo "using $num1 esteps and $num2 usteps"
fi

if [ -d Prusa-Firmware ]
then
	rm -rf Prusa-Firmware
	echo "removing old directory"
fi
git clone https://github.com/prusa3d/Prusa-Firmware
python3 skele_patch.py $num1 $num2
rc=$?
if [ $rc = 1 ]
then
	echo "failed updating... exiting"
else
    if [ ! -d Hex-files ]
    then
        mkdir Hex-files
        echo "creating Hex-files directory to avoid Prusa build script bug"
	else
		echo "removing old Hex-files directory"
		rm -rf Hex-files
		mkdir Hex-files
    fi
	echo "compiling firmware"
	results=$(./Prusa-Firmware/PF-build.sh 1_75mm_MK3-EINSy10a-E3Dv6full.h EN_ONLY GOLD)
    fwdir=$(echo $results | sed -n -E -e 's/.*Hex-file Folder: ([^ ]+).*/\1/p')
	echo "copying hex file to builds directory"
	if [ ! -d complete_builds ]
		then
		mkdir complete_builds
	fi
	fwfile=$(ls $fwdir)
	fwfull=$fwdir'/'$fwfile
	fwnew=$(echo $fwfile | cut -d "-" -f 1-2)
	cp $fwfull complete_builds/$fwnew-MK3-E$num1-u$num2-$(date +%Y%m%d).hex
	echo "compiled file is located at: $(pwd)/complete_builds/$fwnew-MK3-$(date +%Y%m%d).hex"
	echo "complete!"
fi
