#!/usr/bin/env bash 
dir="~/.config/rofi/launchers/colorful"

confirm() {
    rofi -dmenu\
        -i\
        -no-fixed-num-lines\
        -p "Are you sure? "\
        -theme $dir/confirm.rasi
}


answer=$(confirm &)
if [[ $answer == "Yes" || $answer == "y" || $answer == "Y" || $answer == "uwu" ]]; then
    systemctl suspend
    betterlockscreen -l
elif [[ $answer == "No" || $answer == "n" ]]; then
    exit 0
fi
