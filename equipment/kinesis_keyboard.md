# Kinesis Keyboard Advantage2 Setup

1. Update to the latest firmware here if needed:
   https://www.kinesis-ergo.com/advantage2-resources/currently
   (current firmware: 1.0.521.us (2MB), 06/25/2020)

2. Here is a link to the User Manual if needed:
   https://www.kinesis-ergo.com/support/technical-support/manuals-drivers/

3. Turn on Power User Mode: Progm + Shift + Esc (LED's should flash 4 times)

4. Mount the `KINESIS KB` drive: Progm + F1

5. Edit the `KINESIS KB/active/state.txt` file to be:
```
startup_file=qwerty.txt
thumb_mode=MAC
key_click_tone=OFF
toggle_tone=ON
macro_disable=OFF
macro_speed=9
status_play_speed=3
power_user=false
program_key_lock=OFF
```

1. Edit the `KINESIS KB/active/qwerty.txt` file to be:
```
[kp=]>[kp=mac]
[lctrl]>[lwin]
[kp-lctrl]>[kp-lwin]
[rctrl]>[rwin]
[kp-rctrl]>[kp-rwin]
[rwin]>[rctrl]
[kp-rwin]>[kp-rctrl]
[prtscr]>[mute]
[scroll]>[vol-]
[pause]>[vol+]
[delete]>[enter]
[end]>[space]
[home]>[F13]
[caps]>[escape]
```

1. Unmount the drive: Program + F1

2. Turn off Power User Mode: Progm + Shift + Esc (LED's should flash 2 times)
