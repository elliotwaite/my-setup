# Kinesis Keyboard Advantage2 Setup

1. Update to the latest firmware here if needed: https://www.kinesis-ergo.com/advantage2-resources/ (I'm currently using version 1.0.210.us)

2. Here is a link to the User Manual if needed: https://www.kinesis-ergo.com/support/technical-support/manuals-drivers/

3. Turn on Power User Mode: Progm + Shift + Esc

4. Mount the `KINESIS KB` drive: Progm + F1

5. Edit the `KINESIS KB/active/state.txt` file to be:
    ```
    startup_file=qwerty.txt
    thumb_mode=MAC
    key_click_tone=OFF
    toggle_tone=ON
    macro_disable=OFF
    macro_speed=9
    status_play_speed=0
    power_user=true
    ```

6. Edit the `KINESIS KB/active/qwerty.txt` file to be:
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
    [caps]>[F20]
    ```

7. Unmount the drive: Program + F1
