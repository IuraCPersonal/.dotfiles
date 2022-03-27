#!/usr/bin/env bash 

lxsession &
picom  &
# volumeicon &
nm-applet &
feh --bg-fill $HOME/.config/qtile/wall.jpg &

