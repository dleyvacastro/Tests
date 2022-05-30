from libqtile import widget, qtile
from settings.default_globals import font, colors
#from settings.themes import material_ocean as colors

# widget_defaults = dict(
#     font=font + " Bold",
#     fontsize=12,
#     padding=3,
# )


def base(fg='text', bg='dark'):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        # text="",  # Icon: nf-oct-triangle_left
        text="",
        fontsize=37,
        font=font,
        padding=-3
    )


def separator():
    return widget.Sep(**base(), linewidth=1, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        font=font + ' Bold',
        text=text,
        padding=3
    )


def widget_defaults(font=font, sz=12, b=0, padding=3):
    if b:
        font += ' Bold'
    return {
        'font': font,
        'fontsize': sz,
        'padding': padding
    }


def workspace():
    return [widget.GroupBox(font=font,
                            fontsize=16,
                            **base(bg='dark'),
                            highlight_method='block',
                            inactive='505050',
                            disable_drag=True
                            ),
            widget.CurrentScreen(
                **widget_defaults(),
                active_text=" 蘒 ",
                inactive_text=" 﨡 ",
                **base(bg='dark')
    ),
        separator(),
        widget.WindowName(
                format='{name}',
                **base(bg='dark', fg='active'),
                max_chars=15
    )
    ]


def MusicPayer(fb='text', bg='dark'):
    events = [
        'dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous',
        'dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause',
        'dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next'
    ]
    return [
        widget.TextBox(
            **base(fb, bg),
            text='玲',
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(events[0])},
            **widget_defaults(sz=17, b=1, padding=10)

        ),
        widget.TextBox(
            **base(fb, bg),
            text='懶',
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(events[1])},
            **widget_defaults(sz=17, b=1, padding=10)
        ),
        widget.TextBox(
            **base(fb, bg),
            text='怜',
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(events[2])},
            **widget_defaults(sz=17, b=1, padding=10)
        ),

    ]


primary_widgets = [
    *workspace(),
    powerline('color4', 'dark'),


    widget.PulseVolume(**base(bg='color4'),
                       **widget_defaults(sz=15, b=1, padding=5),
                       fmt='墳 {}',
                       ),
    *MusicPayer(bg='color4'),
    widget.Mpris2(
        **base(bg='color4'),
        **widget_defaults(sz=15, b=1),
        max_chars=12,
        name='spotify',
        objname="org.mpris.MediaPlayer2.spotify",
        display_metadata=['xesam:title'],
        stop_pause_text='',
        scroll_wait_intervals=2000
    ),

    # icon(bg="color4", text=' '),
    # widget.Net(
    #    **base(bg='color4'),
    #    font=font,
    #    fontsize=15,
    #    format='Claro Caremonda: {down}↓↑{up}'
    # ),
    powerline('color3', 'color4'),
    # widget.Notify(**base(bg='color3'), font=font, max_chars=20),
    # widget.Pomodoro(
    #     **base(bg='color3'),
    #     padding=17,
    #     fontsize=18,
    #     font=font, prefix_inactive="",
    #     prefix_active="  ",
    #     prefix_long_break=" 鬒 ",
    #     prefix_paused="  ",
    #     prefix_break="  ",
    #     color_inactive='#000000',
    #     color_active='#000000',
    #     color_break='dcfb7f'
    # ),

    icon(bg="color3", text=' '),
    widget.CheckUpdates(
        **base(bg='color3'),
        colour_have_updates=colors['text'],
        colour_no_updates=colors['text'],
        no_update_string='0',
        display_format='{updates}',
        update_interval=1800,
        custom_command='checkupdates',
        **widget_defaults(sz=17, b=1)
    ),
    widget.Sep(**base(bg='color3'), linewidth=1, padding=5),
    icon(bg='color3', text='﬙'),
    widget.CPU(
        **base(bg='color3'),
        **widget_defaults(b=1),
        format='{freq_current}GHz - {load_percent}%'
    ),

    powerline('color2', 'color3'),
    widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),
    widget.CurrentLayout(**base(bg='color2'),
                         **widget_defaults(b=1),
                         ),
    # Icon: nf-mdi-calendar_clock
    powerline('color1', 'color2'),
    icon(bg="color1", fontsize=17, text=' '),

    widget.Clock(**base(bg='color1'),
                 format='%d/%m/%Y - %I:%M %p ',
                 **widget_defaults(b=1)),

    powerline('dark', 'color1'),
    widget.Systray(background=colors['dark'], padding=4, icon_size=15),
    # widget.QuickExit(default_text=" ⏻ ",
    #                  countdown_format='[{}]', background=colors['dark'],
    #                  **widget_defaults(sz=15)
    #                  ),
    separator()
]
secondary_widgets = [
    *workspace(),
    powerline('color2', 'dark'),
    widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),
    widget.CurrentLayout(**base(bg='color2'),
                         **widget_defaults(b=1)
                         ),
    # Icon: nf-mdi-calendar_clock
    powerline('color1', 'color2'),
    icon(bg="color1", fontsize=17, text=' '),

    widget.Clock(**base(bg='color1'),
                 format='%d/%m/%Y - %I:%M %p ',
                 **widget_defaults(b=1)),
    # widget.Sep(**base(bg='color1'), linewidth=1, padding=5)

]

extension_defaults = widget_defaults().copy()
