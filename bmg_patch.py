#!/usr/bin/env python3
#changes to ./Prusa-Firmware/Firmware/Marlin_main.cpp
import sys
num1 = sys.argv[1]
num2 = sys.argv[2]
num1 = int(num1)
num2 = int(num2)

if num1 == 8:
    num1 = ' 8'

def strreplace(replacefile, sfind, sreplace):
    s = open(replacefile, 'r').read()
    e = s.find(sfind)
    if e == -1:
        print('string (' + sfind + ') not found...exiting')
        sys.exit(1)
    else:
        s = s.replace(sfind, sreplace)
        print('replacing: ' + sfind + ' with: ' + sreplace)
        f = open(replacefile, 'w')
        f.write(s)
        f.close()

#changes to ./Prusa-Firmware/Firmware/variants/1_75mm_MK3S-EINSy10a-E3Dv6full.h comment .9 line if you have 1.8 and uncomment current line for 1.8
replacefile = './Prusa-Firmware/Firmware/variants/1_75mm_MK3S-EINSy10a-E3Dv6full.h'
s = open(replacefile, 'r').read()
sfind = '#define DEFAULT_AXIS_STEPS_PER_UNIT   {100,100,3200/8,280}'
sreplace = '#define DEFAULT_AXIS_STEPS_PER_UNIT   {100,100,3200/8,%d}' % (num1)
strreplace(replacefile, sfind, sreplace)

#.9 motor.  comment if using 1.8
sfind = '#define TMC2130_USTEPS_E    32        // microstep resolution for E axis'
sreplace = '#define TMC2130_USTEPS_E   %d        // microstep resolution for E axis' % (num2)
strreplace(replacefile, sfind, sreplace)

#BMG unload fix
sfind = '#define UNLOAD_FILAMENT_1 "G1 E-80 F7000"'
sreplace = '#define UNLOAD_FILAMENT_1 "G1 E-100 F7000"'
strreplace(replacefile, sfind, sreplace)

#BMG load fix
sfind = '#define LOAD_FILAMENT_2 "G1 E40 F100"'
sreplace = '#define LOAD_FILAMENT_2 "G1 E50 F100"'
strreplace(replacefile, sfind, sreplace)

#BMG unload fix2
sfind = '#define FILAMENTCHANGE_FINALRETRACT -80'
sreplace = '#define FILAMENTCHANGE_FINALRETRACT -100'
strreplace(replacefile, sfind, sreplace)

#BMG load fix2
sfind = '#define FILAMENTCHANGE_FINALFEED 25'
sreplace = '#define FILAMENTCHANGE_FINALFEED 35'
strreplace(replacefile, sfind, sreplace)

#BMG xyz
#sfind = '#define Z_MAX_POS_XYZ_CALIBRATION_CORRECTION 9.0'
#sreplace = '#define Z_MAX_POS_XYZ_CALIBRATION_CORRECTION 2.0'
#strreplace(replacefile, sfind, sreplace)

#name change
sfind = '#define CUSTOM_MENDEL_NAME "Prusa i3 MK3S"'
sreplace = '#define CUSTOM_MENDEL_NAME "Prusa i3 Nate Ed."'
strreplace(replacefile, sfind, sreplace)

#Bed temp increase
sfind = '#define BED_MAXTEMP 125'
sreplace = '#define BED_MAXTEMP 135'
strreplace(replacefile, sfind, sreplace)


#uncomment to lower motor current consider changing 20 to 36 for 800 mah
# sfind = '#define TMC2130_CURRENTS_H {16, 20, 35, 30}  // default holding currents for all axes'
# sreplace = '#define TMC2130_CURRENTS_H {16, 20, 35, 25}  // default holding currents for all axes'
# if num2 < 16:
#     strreplace(replacefile,sfind,sreplace)

# sfind = '#define TMC2130_CURRENTS_R {16, 20, 35, 30}  // default running currents for all axes'
# sreplace = '#define TMC2130_CURRENTS_R {16, 20, 35, 25}  // default running currents for all axes'
# if num2 < 16:
#     strreplace(replacefile,sfind,sreplace)

#disable forced selftest in ./Prusa-Firmware/Firmware/variants/1_75mm_MK3S-EINSy10a-E3Dv6full.h
f = open('./Prusa-Firmware/Firmware/variants/1_75mm_MK3S-EINSy10a-E3Dv6full.h', 'a+')
f.write('#define DEBUG_DISABLE_FORCE_SELFTEST //disable force selftest\n\t#define Z_MAX_POS_XYZ_CALIBRATION_CORRECTION 2.0')
f.close
print('finished!')
quit()
