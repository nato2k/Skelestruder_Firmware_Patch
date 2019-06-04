#!/usr/bin/env python3
#changes to ./Prusa-Firmware/Firmware/Marlin_main.cpp
import sys

def strreplace(replacefile, sfind, sreplace):
    s = open(replacefile, 'r').read()
    e = s.find(sfind)
    if e == -1:
        print('string not found...exiting')
        sys.exit(1)
    else:
        s = s.replace(sfind, sreplace)
        print('replacing: ' + sfind + ' with: ' + sreplace)
        f = open(replacefile, 'w')
        f.write(s)
        f.close()

replacefile = './Prusa-Firmware/Firmware/Marlin_main.cpp'
sfind = 'current_position[E_AXIS] += 30;'
sreplace = 'current_position[E_AXIS] += 20;'

strreplace(replacefile, sfind, sreplace)

#changes to ./Prusa-Firmware/Firmware/ultralcd.cpp
replacefile = './Prusa-Firmware/Firmware/ultralcd.cpp'
sfind = 'current_position[E_AXIS] -= 45;'
sreplace = 'current_position[E_AXIS] += 5;\n\tplan_buffer_line(current_position[X_AXIS], current_position[Y_AXIS], current_position[Z_AXIS], current_position[E_AXIS], 500 / 60, active_extruder);\n\tst_synchronize();\n\tcurrent_position[E_AXIS] -= 45;'
strreplace(replacefile, sfind, sreplace)

sfind = 'current_position[E_AXIS] -= 15;'
sreplace = 'current_position[E_AXIS] += 10;\n\tplan_buffer_line(current_position[X_AXIS], current_position[Y_AXIS], current_position[Z_AXIS], current_position[E_AXIS], 500 / 60, active_extruder);\n\tst_synchronize();\n\tcurrent_position[E_AXIS] -= 15;'
strreplace(replacefile, sfind, sreplace)

#changes to ./Prusa-Firmware/Firmware/variants/1_75mm_MK3-EINSy10a-E3Dv6full.h comment .9 line if you have 1.8 and uncomment current line for 1.8
replacefile = './Prusa-Firmware/Firmware/variants/1_75mm_MK3-EINSy10a-E3Dv6full.h'
s = open(replacefile, 'r').read()

sfind = '#define DEFAULT_AXIS_STEPS_PER_UNIT   {100,100,3200/8,280}'
sreplace = '#define DEFAULT_AXIS_STEPS_PER_UNIT   {100,100,3200/8,490}'
strreplace(replacefile, sfind, sreplace)

sfind = '#define Z_MAX_POS 210'
sreplace = '#define Z_MAX_POS 220'
strreplace(replacefile, sfind, sreplace)

sfind = '#define DEFAULT_MAX_FEEDRATE                {200, 200, 12, 120}      // (mm/sec)   max feedrate (M203)'
sreplace = '#define DEFAULT_MAX_FEEDRATE                {400, 400, 12, 320}      // (mm/sec)   max feedrate (M203)'
strreplace(replacefile, sfind, sreplace)

sfind = '#define DEFAULT_MAX_ACCELERATION            {1000, 1000, 200, 5000}  // (mm/sec^2) max acceleration (M201)'
sreplace = '#define DEFAULT_MAX_ACCELERATION            {4000, 1000, 200, 5000}  // (mm/sec^2) max acceleration (M201)'
strreplace(replacefile, sfind, sreplace)

#.9 motor.  comment if using 1.8
sfind = '#define TMC2130_USTEPS_E    32        // microstep resolution for E axis'
sreplace = '#define TMC2130_USTEPS_E    8        // microstep resolution for E axis'
strreplace(replacefile, sfind, sreplace)

#uncomment to lower motor current consider changing 20 to 36 for 800 mah
sfind = '#define TMC2130_CURRENTS_H {16, 20, 35, 30}  // default holding currents for all axes'
sreplace = '#define TMC2130_CURRENTS_H {20, 20, 35, 26}  // default holding currents for all axes'
#strreplace(replacefile,sfind,sreplace)

sfind = '#define TMC2130_CURRENTS_R {16, 20, 35, 30}  // default running currents for all axes'
sreplace = '#define TMC2130_CURRENTS_R {20, 20, 35, 26}  // default running currents for all axes'
#strreplace(replacefile,sfind,sreplace)

#disable forced selftest in ./Prusa-Firmware/Firmware/variants/1_75mm_MK3-EINSy10a-E3Dv6full.h
f = open('./Prusa-Firmware/Firmware/variants/1_75mm_MK3-EINSy10a-E3Dv6full.h', 'a+')
f.write('#define DEBUG_DISABLE_FORCE_SELFTEST //disable force selftest')
f.close
print('finished!')
quit()
