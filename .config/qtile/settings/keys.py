from libqtile.config import Key
from libqtile.lazy import lazy
# from default_globals import mod, browser, terminal
from libqtile.log_utils import logger
from settings.default_globals import mod, browser, terminal


def open_pages(pages: str):
    return f'{browser} --new-window {pages}'


key_list = [
    # Window Managment
    # # Control
    ([mod], "w", lazy.window.kill()),
    ([mod, "shift"], "w", lazy.spawn('xkill')),
    ([mod, "control"], "q", lazy.shutdown()),
    ([mod, "mod1"], "r", lazy.restart()),
    ([mod, "mod1"], "q", lazy.spawn(
        'rofi -show power-menu -modi power-menu:~/.local/bin/rofi-power-menu')),
    # # Navegation - Switching
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "c", lazy.layout.next()),
    # # Swaping
    ([mod, "shift"], "h", lazy.layout.shuffle_left()),
    ([mod, "shift"], "l", lazy.layout.shuffle_right()),
    ([mod, "shift"], "j", lazy.layout.shuffle_down(),),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),
    # # Re-Sizing
    ([mod], "i", lazy.layout.grow()),
    ([mod, "shift"], "i", lazy.layout.shrink()),
    ([mod, "control"], "h", lazy.layout.grow_left()),
    ([mod, "control"], "l", lazy.layout.grow_right()),
    ([mod, "control"], "j", lazy.layout.grow_down()),
    ([mod, "control"], "k", lazy.layout.grow_up()),
    # # Layouts modes
    # # # Layout swap
    ([mod], "Tab", lazy.next_layout()),
    # # # Toggle floating window
    ([mod, "shift"], "f", lazy.window.toggle_floating()),
    # # # Layout & widows
    ([mod], "o", lazy.layout.maximize()),
    ([mod, "shift"], "space", lazy.layout.flip()),
    ([mod], "n", lazy.layout.normalize()),
    ([mod], "m", lazy.window.toggle_fullscreen()),

    # Screen movment
    # ([mod, "mod1"], "j", lazy.next_screen()),
    # ([mod, "mod1"], "k", lazy.prev_screen()),
    ([mod], "comma", lazy.next_screen()),
    ([mod], "period", lazy.prev_screen()),
    # Apps
    ([mod], "space", lazy.spawn('rofi -show drun')),
    (["control"], "space", lazy.spawn('rofi -show')),
    ([mod], "b", lazy.spawn(browser)),
    ([mod, "shift"], "e", lazy.spawn(open_pages(
        'https://e-aulas.urosario.edu.co/ lofi.cafe https://es.symbolab.com/'))),
    ([mod, "shift"], "a", lazy.spawn(open_pages(
        'https://www3.animeflv.net/ https://www.mangatigre.com/ https://manganyaa.com/es https://www.youtube.com/'))),
    # (["control", "mod1"], "t", lazy.spawn(terminal)),
    ([mod], "Return", lazy.spawn(terminal)),
    # # Media
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        'pactl set-sink-volume @DEFAULT_SINK@ +5%')),
    ([], "XF86AudioLowerVolume", lazy.spawn(
        'pactl set-sink-volume @DEFAULT_SINK@ -5%')),
    ([], 'XF86AudioPlay', lazy.spawn(
        'dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause'
    )),
    ([], 'XF86AudioNext', lazy.spawn(
        'dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next'
    )),
    ([], 'XF86AudioPrev', lazy.spawn(
        'dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous'
    )),
    # # ScreenShot
    ([], "Print", lazy.spawn(
        "scrot '/tmp/%F_%T_$wx$h.png' -e 'xclip -selection clipboard -target image/png -i $f'")),
    (["shift", mod], "s", lazy.spawn(
        "scrot -s '/tmp/%F_%T_$wx$h.png' -e 'xclip -selection clipboard -target image/png -i $f && rm $f'")),
    ([mod], "v", lazy.spawn('/usr/bin/diodon')),
]

keys = [Key(*i) for i in key_list]
