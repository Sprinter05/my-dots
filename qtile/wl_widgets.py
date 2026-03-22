from libqtile import bar, widget
from libqtile.config import Screen
from colors import *
from decors import *
from qtile_extras import widget as extrawidget
from qtile_extras import *
import constants

defaultbar = top=bar.Bar([   
    # Arch Linux logo
    widget.Sep(
        linewidth = 0,
        padding = 6,
        background=colors_fg[2],
    ),
    widget.TextBox(
        text='󰣇',
        foreground=colors_bg[1],
        background=colors_fg[2],
        fontsize=24, 
        padding=8,        
    ),
    widget.Sep(
        linewidth = 0,
        padding = 5,
        background=colors_fg[2],
        **powerline_left,
    ),
    # Current layout
    widget.Sep(
        linewidth = 0,
        padding = 6,
    ),
    extrawidget.CurrentLayoutIcon(
        **declayout,
        use_mask = True,
        scale=0.65,
        foreground = colors_bg[1],
    ),
    widget.CurrentLayout(
        **dectext,
        colors=colors_fg[5],
    ),
    # Group Boxes
    widget.Sep(
        linewidth = 0,
        padding = 6,
    ),
    widget.GroupBox(
        **powerline_left,
        fontsize = 16,
        margin_x = 1,
        padding_x = 1,
        borderwidth = 3,
        foreground = colors_bg[1],
        active = colors_bg[0],
        inactive = colors_bg[3],
        highlight_color = colors_bg[1],
        this_current_screen_border = colors_fg[6],
        rounded = False,
        disable_drag = True,
        center_aligned = True,
        highlight_method = "text",
    ),
    # Run command
    widget.Prompt(
        **powerline_left,
        foreground=colors_bg[5],
        fontsize=16,
        prompt='➦ Run:',
        cursor_color=colors_bg[0],
    ),
    # Window name
    widget.WindowName(
        background=colors_bg[2],
        fontsize=14,
        max_chars=50,
        fmt=' {}',
        font=constants.fonts["bold"],
        center_aligned = True,
        for_current_screen = True,
    ),
    # SPACE HERE #
    # Do Not Disturb
    widget.DoNotDisturb(
        enabled_icon="󰂛",
        disabled_icon="󰂚",
        fontsize=17,
        background=colors_bg[2],
        update_interval = 0.5,
        padding = 4
    ),
    widget.StatusNotifier(
        background=colors_bg[2],
        icon_size = 19,
        padding = 5
    ),
    widget.Sep(
        linewidth = 0,
        padding = 6,
        background=colors_bg[2],
        **powerline_right,
    ),
    # Keylock Indicator
    widget.TextBox(
        **deckeyboard,
        text='󰌌',
        fontsize=18,
        foreground=colors_bg[1],
    ),
    widget.CapsNumLockIndicator(
        **dectext,
    ),
    widget.Sep(
        linewidth = 0,
        padding = 6,
    ),
    # Volume management (Pulseaudio)
    widget.PulseVolume(
        **decvol,
        emoji=True,
        emoji_list=['󰝟', '󰕿', '󰖀', '󰕾'],
        fontsize=18,
        foreground=colors_bg[1],
        padding=6,
        device='default',
        step=1,
    ),
    widget.PulseVolume(
        **dectext,
        foreground=colors_bg[5],
        channel='Master',
        step=1,
    ),
    widget.Sep(
        linewidth = 0,
        padding = 6,
    ),
    # Brightness control for intel
    widget.TextBox(
        **declight,
        text='󰃠',
        fontsize=18,
        foreground=colors_bg[1]
    ),
    widget.Backlight(
        **dectext,
        backlight_name='intel_backlight',
        change_command='backlight_control {0}',
        foreground=colors_bg[5],
        step=5,
    ),
    widget.Sep(
        linewidth = 0,
        padding = 6,
    ),
    # Battery report
    widget.Battery(
        **decbattery,
        format='{char}',
        empty_char = '󰂃',
        charge_char='󰂄',
        discharge_char='󰁹',
        full_char='󱟢',
        unknown_char = '󱉝',
        show_short_text=False,
        fontsize=18,
        padding=8,
        foreground=colors_bg[1],
        low_foreground="d20f39",
    ),
    widget.Battery(
        **dectext,
        format='{percent:2.0%}',
        show_short_text=False,
        foreground=colors_bg[5],
        low_foreground=colors_bg[5],
        padding=6,
    ),
    widget.Sep(
        linewidth = 0,
        padding = 6,
    ),
    # Wifi display
    # NOTE: The ethernet stuff is from a custom implementation I did (PR here: https://github.com/qtile/qtile/pull/4569)
    widget.Wlan(
        **decwifi,
        format='󰖩',
        foreground=colors_bg[1],
        disconnected_message='󰖪',
        ethernet_message='󰈀',
        fontsize=16,
        interface='wlan0',
        use_ethernet=True,
        ethernet_interface='eno1',
        update_interval=5,
    ),
    widget.Wlan(
        **dectext,
        foreground=colors_bg[5],
        format='{essid}',
        interface='wlan0',
        ethernet_interface='eno1',
        disconnected_message='Disconnected',
        use_ethernet=True,
        ethernet_message='Ethernet',
        update_interval=5,
    ),
    widget.Sep(
        linewidth = 0,
        padding = 6,
    ),
    # Time and date
    widget.TextBox(
        **decdate,
        text='󰃭',
        foreground=colors_bg[1],
        fontsize=18,                   
    ),
    widget.Clock(
        **dectext,
        format='%b %d, %H:%M',
        foreground=colors_bg[5],
    ),
    widget.Sep(
        linewidth = 0,
        padding = 2,
    ),
    # Exit Qtile
    widget.Sep(
        **powerline_right,
        linewidth=0,
        padding=6,
    ),
    widget.QuickExit(
        fontsize = 24,
        foreground = colors_bg[1],
        background = colors_fg [2],
        default_text = '󰗽',
        countdown_start = 4,
        countdown_format = '{}'
    ),
    widget.Sep(
        linewidth = 0,
        padding = 5,
        background=colors_fg[2],
    )],
    size = 26,
    margin = constants.mar_g,
    background=colors_bg[2]
)