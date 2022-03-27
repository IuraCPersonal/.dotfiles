#  _   ___      ___   _ 
# | | | \ \ /\ / / | | |
# | |_| |\ V  V /| |_| |
#  \__,_| \_/\_/  \__,_|
#                           
# Config by s1mpi  


# Import Libraries

import os
import re
import socket
import subprocess

from libqtile.dgroups import simple_key_binder
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from typing import List

mod = "mod4"
terminal = "alacritty"
browser = "google-chrome-stable"

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # The essentials
    Key([mod], "Return", lazy.spawn(terminal + " -e zsh"), desc="Launch Terminal"),
    Key([mod], "b", lazy.spawn(browser), desc="Launch Browser"),
    Key([mod], "Tab", lazy.next_layout(), desc='Toggle through layouts'),
    Key([mod], "q", lazy.window.kill(), desc='Kill active window'),
    Key([mod, "shift"], "r", lazy.restart(), desc='Restart Qtile'),
    Key([mod], "x", lazy.spawn("arcolinux-logout"), desc='Power Menu'),
    Key([mod], "F12", lazy.spawn("rofi -show"), desc='Rofi Show'),
    Key([mod], "F11", lazy.spawn("rofi -show drun"), desc='Rofi Drun'),
    Key([mod, "shift"], "Return", lazy.spawn("rofi -no-lazy-grab -show drun -modi drun -theme ~/.config/rofi/launchers/colorful/style_1"), desc="Spawn Rofi")
]

groups = [
    Group("MAIN", layout="monadtall"),
    Group("WEB", layout="monadtall"),
    Group("CODE", layout="monadtall"),
    Group("TERM", layout="monadtall"),
    Group("CHAT", layout="monadtall"),
    Group("MUS", layout="monadtall"),
]

# Allow MODKEY+[0 through 9] to bind to groups, see https://docs.qtile.org/en/stable/manual/config/groups.html
# MOD4 + index Number : Switch to Group[index]
# MOD4 + shift + index Number : Send active window to another Group
dgroups_key_binder = simple_key_binder("mod4")

layout_theme = {
    "border_width": 0,
    "margin": 8, 
    "border_focus": '#7dcfff',
}

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Floating(**layout_theme)
]

# Tokyo Night Color Scheme
colors = [
    ["#f7768e", "#f7768e"],
    ["#ff9e64", "#ff9e64"],
    ["#e0af68", "#e0af68"],
    ["#9ece6a", "#9ece6a"],
    ["#73daca", "#73daca"],
    ["#b4f9f8", "#b4f9f8"],
    ["#2ac3de", "#2ac3de"],
    ["#7dcfff", "#7dcfff"],
    ["#7aa2f7", "#7aa2f7"],
    ["#bb9af7", "#bb9af7"],
    ["#c0caf5", "#c0caf5"],
    ["#a9b1d6", "#a9b1d6"],
    ["#9aa5ce", "#9aa5ce"],
    ["#cfc9c2", "#cfc9c2"],
    ["#565f89", "#565f89"],
    ["#414868", "#414868"],
    ["#24283b", "#24283b"],
    ["#1a1b26", "#1a1b26"],
]

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

widget_defaults = dict(
    font = "mononoki Bold",
    fontsize = 9,
    padding = 3, 
)

extension_defaults = widget_defaults.copy()


def init_widgets_list():
    widgets_list = [
        widget.Sep(
            linewidth = 0,
            foreground = colors[2],
            background = None
        ),
        widget.TextBox(
            text = "",
            foreground = colors[-4],
            fontsize = 21
        ),
        widget.TextBox(
            text = "",
            foreground = colors[-4],
            fontsize = 12
        ),
        widget.GroupBox(
            # margin_y = 3,
            # margin_x = 1,
            # padding_y = 5,
            # padding_x = 3,
            fontfamily = "mononoki Bold",
            active = colors[0],
            inactive = colors[-4],
            background = None,
            borderwidth = 3,
            highlight_color = colors[-1],
            highlight_method = "text",
            this_current_screen_border = colors[7],
            this_screen_border = colors[1],
            other_current_screen_border = colors[1],
            other_screen_border = colors[3],
            foreground = colors[2],
            center_aligned = True
        ),
        widget.TextBox(
            text = "",
            foreground = colors[-4],
            fontsize = 12
        ),
        widget.TextBox(
            text = ' ',
            foreground = colors[4],
            fontsize = 21
        ),
        widget.WindowName(
            fontsize = 11,
            foreground = colors[-4],
            padding = 0
        ),
        widget.Sep(
            linewidth = 0
        ),
        widget.Sep(
            linewidth=0,
            foreground=colors[0],
        ),
        widget.TextBox(text = ""),
        widget.Systray(),
        widget.TextBox(
            text = "",
            foreground = colors[-4],
            fontsize = 12 
        ),
        widget.TextBox(
            text = "",
            foreground = colors[0],
            fontsize = 21
        ),
        widget.CheckUpdates(
            no_update_string='Up to Date',
            update_interval=1800,
            distro="Arch_checkupdates",
            display_format="{updates} updates",
            foreground = colors[-5],
            colour_have_updates = colors[-5],
            colour_no_updates = colors[-5],
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(
                    terminal + ' -e sudo pacman -Syu')},
            fontsize = 12
        ),
        widget.TextBox(
            text = "",
            foreground = colors[-4],
            fontsize = 12 
        ),
        widget.TextBox(
            text = '',
            foreground = colors[3],
            fontsize = 21
        ),
        widget.Memory(
            fontsize = 12,
            foreground = colors[-5],
            format = "{MemUsed:.0f} MB",
        ),
        widget.Sep(
            linewidth = 12,
            background = None, 
            foreground = colors[-1]
        ),
        widget.TextBox(
            text = '',
            foreground = colors[1],
            fontsize = 21
        ),
        widget.CPU(
            fontsize = 12,
            foreground = colors[-5],
            format = "{load_percent} %",
        ),
        widget.Sep(
            linewidth = 12,
            background = None, 
            foreground = colors[-1]
        ),

        widget.TextBox(
            text = '墳',
            foreground = colors[9],
            fontsize = 20
        ),
        widget.Volume(
            fontsize = 12,
            foreground = colors[-5],
            fmt = "{}",
        ),
        widget.TextBox(
            text = "",
            foreground = colors[-4],
            fontsize = 12
        ),
        widget.TextBox(
            text = '',
            foreground = colors[7],
            fontsize = 20
        ),
        widget.Clock(
            fontsize = 12,
            foreground = colors[-5],
            format = "%H:%M %p"
        ),
        widget.CurrentLayoutIcon(
            custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
            padding = 0,
            scale = 0.5
        ),
        widget.Sep(
            linewidth=0,
            foreground=colors[2],
            background=None
        ),

    ]
    return widgets_list


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    del widgets_screen1[9:10]
    return widgets_screen1


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2


def init_screens():
    return [
        Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=30, background=colors[-1])),
        Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=0.1, size=20)),
        Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=0.1, size=20))
    ]


if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()


def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)


def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)


def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)


mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    *layout.Floating.default_float_rules,
    Match(title='Confirmation'),      # tastyworks exit box
    Match(title='Qalculate!'),        # qalculate-gtk
    Match(wm_class='kdenlive'),       # kdenlive
    Match(wm_class='pinentry-gtk-2'),  # GPG key password entry
])

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True

@hook.subscribe.startup
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
