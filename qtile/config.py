# By Sprinter05

# Imports
import os
import subprocess
import socket
from datetime import datetime

# qtile base
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

# qtile extras (https://github.com/elParaguayo/qtile-extras)
from qtile_extras import widget as extrawidget
from qtile_extras.widget import modify
from qtile_extras.popup.toolkit import PopupRelativeLayout, PopupText, PopupWidget
from qtile_extras.widget.mixins import ExtendedPopupMixin
from qtile_extras import *

# Files with data
from colors import *
from decors import *

@hook.subscribe.startup_once
def autostart_once():
    subprocess.run('/home/sprinter/.config/qtile/autostart.sh')

# Define my applications for shortcuts
mod = "mod4"
terminal = "alacritty"
browser = "firefox"
explorer = "thunar"
screenshot = "flameshot gui"
pulsemix = "alacritty -e pulsemixer"
taskmanager = "alacritty -e btop"
gputaskmanager = "alacritty -e nvtop"
fastmusic = "/home/sprinter/Scripts/mpc.sh"
musicplayer = "alacritty -e ncmpcpp"
screenlock = "betterlockscreen -l"
applauncher = "rofi -show drun"
clipboard = 'rofi-gpaste'
confedit = '/home/sprinter/Scripts/confedit.sh'
#alttab = "/home/sprinter/alt.sh"
emojipick = 'rofimoji --max-recent 0 --selector-args "-config ~/.config/rofi/emoji.rasi"'
calculator= f'= --dmenu="dmenu -sb {colors_fg[9]} -sf {colors_bg[1]} -nb {colors_bg[1]} -nf {colors_bg[0]} -fn JetBrainsMono-20"'

# Keyboard keys
keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Cheat sheet at https://github.com/qtile/qtile/blob/master/libqtile/backend/x11/xkeysyms.py

    # Window management
    Key([mod, "control"], "Down", lazy.window.toggle_minimize(), desc="Minimize window"),
    Key([mod, "control"], "Up", lazy.window.toggle_maximize(), desc="Maximize window"),
    Key([mod, "control"], "Left", lazy.layout.client_to_previous(), desc="Change to left stack"),
    Key([mod, "control"], "Right", lazy.layout.client_to_next(), desc="Change to right stack"),
    Key([mod], "u", lazy.window.toggle_floating()),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack",),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    # Window switching
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    # Replaced with "alttab" (https://github.com/sagb/alttab)
    #Key(["mod1"], "Tab", lazy.group.next_window(), desc="Move window focus to next window"),
    #Key(["mod1", "shift"], "Tab", lazy.group.previous_window(), desc="Move window focus to next window"),

    # Window placement
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Window sizing
    Key([mod, "mod1"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "mod1"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "mod1"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "mod1"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "shift"], "a", lazy.layout.shrink_main(), desc="Grow main to the left"), # For monadtall
    Key([mod, "shift"], "d", lazy.layout.grow_main(), desc="Grow main to the right"), # For monadtall

    # Keyboarc Shortcuts
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([], "Print", lazy.spawn(screenshot), desc="Take a screenshot"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Space", lazy.spawn(calculator), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn(browser), desc="Launch browser"),
    Key([mod], "e", lazy.spawn(explorer), desc="Launch file explorer"),
    Key([mod], "s", lazy.spawn(pulsemix), desc="Launch sound mixer"),
    Key([mod], "m", lazy.spawn(fastmusic), desc="Launch mpc rofi selector"),
    Key([mod, "shift"], "m", lazy.spawn(musicplayer), desc="Launch mpd music player"),
    Key([mod, "shift"], "c", lazy.spawn(confedit), desc="Edit a config folder with code"),
    Key([mod], "t", lazy.spawn(taskmanager), desc="Launch task top"),
    Key([mod, "shift"], "t", lazy.spawn(gputaskmanager), desc="Launch GPU top"),
    Key([mod], "l", lazy.spawn(screenlock), desc="Lock Screen with i3lock"),
    Key([mod], "a", lazy.spawn(applauncher), desc="App Launcher with rofi"),
    Key([mod], "v", lazy.spawn(clipboard), desc="Clipboard with rofi and greenclip"),
    Key([mod], "period", lazy.spawn(emojipick), desc="Pick emojis with rofi"),

    # Layout management
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "Tab", lazy.prev_layout(), desc="Toggle between layouts"),

    # Qtile management
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    #Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Move windows between groups
    Key([mod, "shift"], "1", lazy.window.togroup("1"), desc="Move window to group 1"),
    Key([mod, "shift"], "2", lazy.window.togroup("2"), desc="Move window to group 2"),
    Key([mod, "shift"], "3", lazy.window.togroup("3"), desc="Move window to group 3"),
    Key([mod, "shift"], "4", lazy.window.togroup("4"), desc="Move window to group 4"),
    Key([mod, "shift"], "5", lazy.window.togroup("5"), desc="Move window to group 5"),
    Key([mod, "shift"], "6", lazy.window.togroup("6"), desc="Move window to group 6"),

    # Move between groups
    Key([mod], "1", lazy.group["1"].toscreen(), desc="Move to group 1"),
    Key([mod], "2", lazy.group["2"].toscreen(), desc="Move to group 2"),
    Key([mod], "3", lazy.group["3"].toscreen(), desc="Move to group 3"),
    Key([mod], "4", lazy.group["4"].toscreen(), desc="Move to group 4"),
    Key([mod], "5", lazy.group["5"].toscreen(), desc="Move to group 5"),
    Key([mod], "6", lazy.group["6"].toscreen(), desc="Move to group 6"),
]

# Mouse keys
mouse = [
    # Floating window management
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

# Qtile groups
groups =[
    Group("1", label = ""),
    Group("2", label = ""),
    Group("3", label = ""),
    Group("4", label = ""),
    Group("5", label = ""),
    Group("6", label = ""),
]

# Layouts that I use
layouts = [
    layout.Columns(
        border_focus = colors_fg[2],
        border_normal = colors_bg[7],
        border_width = 3,
        margin = 4,
        border_on_single = False,
    ),
    layout.MonadTall(
        border_focus = colors_fg[2],
        border_normal = colors_bg[7],
        border_width = 3,
        margin = 4,
        align = 0,
        ratio = 0.6,
        new_client_position = 'bottom',
    ),
    layout.Stack(
        border_focus = colors_fg[2],
        border_normal = colors_bg[7],
        border_width = 3,
        margin = 4,
        border_on_single = False,
    ),
    layout.Zoomy(
        border_focus = colors_fg[2],
        border_normal = colors_bg[7],
        border_width = 3,
        margin = 4,
        border_on_single = False,
    ),
    layout.Max(
        margin = 4
    ),
]

# Define rules for floating windows
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    border_focus = colors_fg[6],
    border_normal = colors_bg[7],
    border_width = 3,
    border_on_single = False,
)

# Default widget settings
widget_defaults = dict(
    font="JetBrainsMono NF",
    fontsize=14,
    padding=8,
    background=colors_bg[1],
)
extension_defaults = widget_defaults.copy()

# JetBrains Nerd Font
fonts = {
    "regular": "JetBrainsMono NF",
    "bold": "JetBrainsMono NF Bold",
    "italic": "JetBrainsMono NF Italic",
    "bolditalic": "JetBrainsMono NF Bold Italic"
}

# Qtile Bar that I designed
screens = [
    Screen( 
        top=bar.Bar(
            [
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
                    font=fonts["bold"],
                    center_aligned = True,
                    for_current_screen = True,
                ),

                # SPACE HERE #

                # System Tray
                widget.Systray(
                    background=colors_bg[2],
                    padding=4,
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
                    step=1,
                ),
                widget.PulseVolume(
                    **dectext,
                    foreground=colors_bg[5],
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
                    ethernet_interface='eno4',
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
                ),
            ],
            size = 26,
            margin=4,
        ),
    ),
]

# Other Qtile stuff
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
