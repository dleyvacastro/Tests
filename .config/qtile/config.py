# Qtile imports
from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.log_utils import logger
# Standard Imports
from typing import List  # noqa: F401
import os
import subprocess
# Config Imports
#from settings.themes import material_ocean as colors
from settings.default_globals import *
from settings.keys import keys
from settings.screens import screens
from settings.theme_loader import switch_theme, random_cs


@hook.subscribe.startup_once
def autostart():
    # xrandr = 'xrandr --output HDMI1 --above eDP1'
    # latam_keyboard = 'setxkbmap latam'
    # nitrogen = 'nitrogen --restore'
    # diodon = '/usr/bin/diodon &'
    # picom = 'picom -f &'
    # subprocess.run(xrandr, shell=True)
    # subprocess.run(latam_keyboard, shell=True)
    # subprocess.run(nitrogen, shell=True)
    # subprocess.run(diodon, shell=True)
    # subprocess.run(picom, shell=True)
    # subprocess.run(browser + ' &', shell=True)
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])


@hook.subscribe.shutdown
def randomize_cs_at_startup():
    switch_theme(random_cs())


# @hook.subscribe.startup_complete
# def startup_complete_tweeks():
#     subprocess.run('kill kdeconnect-app', shell=True)
#     subprocess.run('pactl set-sink-volume @DEFAULT_SINK@ 33% &', shell=True)


g = [
    # Group("   "),
    Group("   ", Match(wm_class=["Firefox", "Brave-browser"])),
    Group("   ", layout='monadtall'),
    Group("   ",
          Match(wm_class=["WhatSie", "discord",
                "TelegramDesktop", "whatsdesk", "rambox"])
          ),
    Group("   ", Match(wm_class=["spotify"])),
    Group("   "),
    Group("   ", Match(wm_class=["zoom"])),
    # Group("7", Match(wm_class=['kdeconnect-app']))
]
groups = g + [Group(i) for i in [
    "7", "8", "9",
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])
layout_conf = {
    'border_focus': colors['focus'][0],
    'border_width': 1,
    'margin': 2
}

layouts = [
    # layout.Columns(border_focus_stack=['#d75f5f', '#8f3d3d'], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    layout.MonadTall(**layout_conf),
    layout.MonadWide(**layout_conf),
    layout.RatioTile(**layout_conf),
    # layout.Bsp(**layout_conf),
    # layout.Matrix(**layout_conf),
    # layout.Tile(**layout_conf),

    # layout.TreeTab(
    #    font="Ubuntu",
    #    fontsize=10,
    #    sections=["FIRST", "SECOND", "THIRD", "FOURTH"],
    #    section_fontsize=10,
    #    border_width=2,
    #    bg_color="1c1f24",
    #    active_bg="c678dd",
    #    active_fg="000000",
    #    inactive_bg="a9a1e1",
    #    inactive_fg="1c1f24",
    #    padding_left=0,
    #    padding_x=0,
    #    padding_y=5,
    #    section_top=10,
    #    section_bottom=20,
    #    level_shift=8,
    #    vspace=3,
    #    panel_width=200
    # ),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]
# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]


dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
