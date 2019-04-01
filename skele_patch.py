#changes to ./Prusa-Firmware/Firmware/Marlin_main.cpp
s = open('./Prusa-Firmware/Firmware/Marlin_main.cpp', 'r').read()
s = s.replace('current_position[E_AXIS] += 30;', 'current_position[E_AXIS] += 20;')
f = open('./Prusa-Firmware/Firmware/Marlin_main.cpp', 'w')
f.write(s)
f.close()
#changes to ./Prusa-Firmware/Firmware/ultralcd.cpp
s = open('./Prusa-Firmware/Firmware/ultralcd.cpp', 'r').read()
s = s.replace('current_position[E_AXIS] -= 45;', 'current_position[E_AXIS] -= 32;')
s = s.replace('current_position[E_AXIS] -= 15;\n\tplan_buffer_line(current_position[X_AXIS], current_position[Y_AXIS], current_position[Z_AXIS], current_position[E_AXIS], 1000 / 60, active_extruder);', 'current_position[E_AXIS] -= 10;\n\tplan_buffer_line(current_position[X_AXIS], current_position[Y_AXIS], current_position[Z_AXIS], current_position[E_AXIS], 100 / 60, active_extruder);')
f = open('./Prusa-Firmware/Firmware/ultralcd.cpp', 'w')
f.write(s)
f.close()
#changes to ./Prusa-Firmware/Firmware/variants/1_75mm_MK3-EINSy10a-E3Dv6full.h, current and microstep for .9 commented out
s = open('./Prusa-Firmware/Firmware/variants/1_75mm_MK3-EINSy10a-E3Dv6full.h', 'r').read()
s = s.replace('#define DEFAULT_AXIS_STEPS_PER_UNIT   {100,100,3200/8,280}', '#define DEFAULT_AXIS_STEPS_PER_UNIT   {100,100,3200/8,980}')
s = s.replace('#define Z_MAX_POS 210', '#define Z_MAX_POS 220')
s = s.replace('#define DEFAULT_MAX_FEEDRATE                {200, 200, 12, 120}      // (mm/sec)   max feedrate (M203)', '#define DEFAULT_MAX_FEEDRATE                {400, 400, 12, 320}      // (mm/sec)   max feedrate (M203)')
s = s.replace('#define DEFAULT_MAX_ACCELERATION            {1000, 1000, 200, 5000}  // (mm/sec^2) max acceleration (M201)', '#define DEFAULT_MAX_ACCELERATION            {4000, 1000, 200, 5000}  // (mm/sec^2) max acceleration (M201)')
#uncomment for .9 motor
#s = s.replace('#define TMC2130_USTEPS_E    32        // microstep resolution for E axis', '#define TMC2130_USTEPS_E    16        // microstep resolution for E axis')
#uncomment to lower motor current
#s = s.replace('#define TMC2130_CURRENTS_H {16, 20, 35, 30}  // default holding currents for all axes', '#define TMC2130_CURRENTS_H {20, 20, 35, 26}  // default holding currents for all axes')
#s = s.replace('#define TMC2130_CURRENTS_R {16, 20, 35, 30}  // default running currents for all axes', '#define TMC2130_CURRENTS_R {20, 20, 35, 26}  // default running currents for all axes')
f = open('./Prusa-Firmware/Firmware/variants/1_75mm_MK3-EINSy10a-E3Dv6full.h', 'w')
f.write(s)
f.close()
#disable forced selftest in ./Prusa-Firmware/Firmware/variants/1_75mm_MK3-EINSy10a-E3Dv6full.h
f = open('./Prusa-Firmware/Firmware/variants/1_75mm_MK3-EINSy10a-E3Dv6full.h', 'a+')
f.write('#define DEBUG_DISABLE_FORCE_SELFTEST //disable force selftest')
f.close
quit()