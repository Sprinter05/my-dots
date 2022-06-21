# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess
import socket
from spotify import Spotify
from libqtile import *
from libqtile import hook
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile import widget
#from libqtile.utils import guess_terminal

@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])

mod = "mod4"
terminal = "xfce4-terminal"
browser = "firefox"
explorer = "thunar"
sound = "pavucontrol"
clipboard = "gpaste-client ui"
screenlock = "xfce4-terminal -e /home/sprinter/.bin/scripts/lock.sh"
updates = "xfce4-terminal -e /home/sprinter/.bin/scripts/updates.sh"
applist = os.path.expanduser('~/.bin/scripts/applet.sh')
alttab = "bash /home/sprinter/.bin/scripts/applet2.sh"
time = os.path.expanduser('~/.config/rofi/applets/applets/time.sh')
powermenu = os.path.expanduser('~/.config/rofi/applets/applets/powermenu.sh')
network = os.path.expanduser('~/.config/rofi/applets/applets/network.sh')
battery = os.path.expanduser('~/.config/rofi/applets/applets/battery.sh')
volume = os.path.expanduser('~/.config/rofi/applets/applets/volume.sh')

def window_name(text):
    for string in [" - Mozilla Firefox"]:
        text = text.replace(string, "")
    return text

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),

    Key(["mod1"], "Tab", lazy.layout.next(), desc="Move window focus to next window"),
    #Key(["mod1"], "Tab", lazy.spawn(alttab), desc="Alt+Tab menu"),
    # Key(["mod1", "shift"], "Tab", lazy.layout.prev(), desc="Move window focus to previous window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "mod1"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "mod1"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "mod1"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "mod1"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn(browser), desc="Launch browser"),
    Key([mod], "e", lazy.spawn(explorer), desc="Launch file explorer"),
    Key([mod], "s", lazy.spawn(sound), desc="Launch sound mixer"),
    Key([mod], "z", lazy.spawn(screenlock), desc="Lock Screen"),
    Key([mod], "a", lazy.spawn(applist), desc="App Launcher"),
    Key([mod], "v", lazy.spawn(clipboard), desc="Clipboard"),


    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "Tab", lazy.prev_layout(), desc="Toggle between layouts"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # Move windows to x group
    Key([mod, "shift"], "1", lazy.window.togroup("1"), desc="Move window to group 1"),
    Key([mod, "shift"], "2", lazy.window.togroup("2"), desc="Move window to group 2"),
    Key([mod, "shift"], "3", lazy.window.togroup("3"), desc="Move window to group 3"),
    Key([mod, "shift"], "4", lazy.window.togroup("4"), desc="Move window to group 4"),
    #Key([mod, "shift"], "5", lazy.window.togroup("5"), desc="Move window to group 5"),
    #Key([mod, "shift"], "6", lazy.window.togroup("6"), desc="Move window to group 6"),

    # Move to x group
    Key([mod], "1", lazy.group["1"].toscreen(), desc="Move to group 1"),
    Key([mod], "2", lazy.group["2"].toscreen(), desc="Move to group 2"),
    Key([mod], "3", lazy.group["3"].toscreen(), desc="Move to group 3"),
    Key([mod], "4", lazy.group["4"].toscreen(), desc="Move to group 4"),
    #Key([mod], "5", lazy.group["5"].toscreen(), desc="Move to group 5"),
    #Key([mod], "6", lazy.group["6"].toscreen(), desc="Move to group 6"),
]

groups =[
        Group("1", label = ""),
        Group("2", label = ""),
        Group("3", label = ""),
        Group("4", label = ""),
        ]


"""for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )
"""

colors = [
          ["#2c2f36", "#2c2f36"], #gray
          ["#1B1B2F", "#1B1B2F"], #dark

          ["#ff8886", "#ff8886"], #light red
          ["#E43F5A", "#E43F5A"], #red

          ["#51afef", "#51afef"], #light blue
          ["#004d98", "#004d98"], #blue

          ["#0eb016", "#0eb016"], #gree
          ["#ed822b", "#ed822b"], #orange

          ["#ffffff", "#ffffff"], #white
          ["#9c9fa6", "#9c9fa6"], #light gray
         ]

layouts = [
    layout.Columns(
        border_focus = '#E43F5A',
        border_normal = '#111111',
        border_width = 1,
        margin = 8,
        border_on_single = False
    ),
    layout.Stack(
        border_width = 1,
        border_focus = '#E43F5A',
        border_normal = '#111111',
        margin = 8,
        border_on_single = False
    ),
    layout.Spiral(
        border_focus = '#E43F5A',
        border_normal = '#111111',
        border_width = 1,
        margin = 8,
        border_on_single = False,
        new_client_position = 'bottom'
    ),
    layout.Zoomy(
        border_focus = '#E43F5A',
        border_normal = '#111111',
        border_width = 1,
        margin = 8,
        border_on_single = False
    ),
    layout.Max(
        margin = 8
    ),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="saucecodepro nf",
    fontsize=14,
    padding=3,
    background=colors[0],
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    linewidth = 0,
                    padding = 4,
                    background = colors[3],
                ),
                widget.CurrentLayoutIcon(
                    font = "Source Code Pro Bold",
                    scale=0.8,
                    background = colors[3],
                    foreground = colors[1],
                    fontshadow = colors[1],
                    custom_icon_paths = ['/home/sprinter/.config/qtile/layout-icons/']
                ),
                widget.TextBox(
                    text = '◣',
                    font = "Ubuntu Mono",
                    padding = -6,
                    #margin_y = 10,
                    fontsize = 45,
                    foreground = colors[3]
                ),
                #widget.Sep(
                #    linewidth = 0,
                #    padding = 1,
                #),
                widget.GroupBox(
                    font = "saucecodepro nf",
                    fontsize = 18,
                    margin_y = 3,
                    margin_x = 1,
                    padding_y = -0,
                    padding_x = 1,
                    borderwidth = 3,
                    active = colors[7],
                    inactive = colors[9],
                    rounded = False,
                    highlight_color = colors[3],
                    highlight_method = "text",
                    this_current_screen_border = colors[3],
                    this_screen_border = colors [2],
                    #other_current_screen_border = colors[4],
                    #other_screen_border = colors[4],
                    foreground = colors[1],
                    background = colors[0],
                    disable_drag = True,
                    center_aligned = True
                ),
                widget.Sep(
                    linewidth = 0,
                    padding = 3,
                ),
                widget.Prompt(
                    background=colors[1],
                    foreground=colors[0],
                    fontsize=16,
                    cursor_color='1c1f24',
                    prompt='➦Run:',
                    center_aligned = True
                ),
                widget.Sep(
                    linewidth = 0,
                    padding = 2,
                ),
                widget.TextBox(
                    text = '',
                    font = "saucecode pro nf",
                    #padding = 2,
                    margin_y = 10,
                    fontsize = 16,
                    foreground = colors[4],
                ),
                widget.Sep(
                    linewidth = 0,
                    padding = 2,
                ),
                widget.WindowName(
                    fontsize=16,
                    max_chars=50,
                    margin_y=-10,
                
                    center_aligned = True,
                    for_current_screen = True,
                    parse_text = window_name
                ),
                widget.TextBox(
                    text = '',
                    font = "saucecodepro nf",
                    #padding = -5,
                    #margin_y = 10,
                    fontsize = 20,
                    foreground = colors[8],
                    #background = colors[1]
                    mouse_callbacks = {'Button1': lazy.spawn(updates)}
                ),
                widget.CheckUpdates(
                    font = "Source Code Pro",
                    padding = 1,
                    fontsize = 16,
                    update_interval = 1800,
                    distro = "Ubuntu",
                    display_format = " {updates} ",
                    colour_have_updates = colors[8],
                    colour_no_updates = colors[8],
                    mouse_callbacks = {'Button1': lazy.spawn(updates)}
                ),
                widget.Systray(),
                widget.TextBox(
                    text = '◢',
                    font = "Ubuntu Mono",
                    padding = -6,
                    #margin_y = 10,
                    fontsize = 45,
                    foreground = colors[1]
                ),
                #Spotify(
                #    font = "Source Code Pro Bold",
                #    fontsize = 16,
                #    foreground = colors[3],
                #    background = colors[1],
                #    max_chars = 25,
                #    format = "{icon} {track}:{album} - {artist}",
                #    play_icon = ""
                #),
                widget.TextBox(
                    text = '',
                    font = "saucecodepro nf",
                    #padding = -5,
                    #margin_y = 10,
                    fontsize = 28,
                    foreground = colors[3],
                    background = colors[1]
                ),
                widget.CapsNumLockIndicator(
                    font = "Source Code Pro Bold",
                    #padding = -5,
                    #margin_y = 10,
                    fontsize = 16,
                    foreground = colors[3],
                    background = colors[1],
                    padding = 5
                ),
                widget.TextBox(
                    text = '◢',
                    font = "Ubuntu Mono",
                    padding = -5,
                    #margin_y = 10,
                    fontsize = 45,
                    foreground = colors[3],
                    background = colors[1]
                ),
                widget.TextBox(
                    text = '',
                    font = "saucecodepro nf",
                    #padding = -5,
                    #margin_y = 10,
                    fontsize = 22,
                    foreground = colors[1],
                    background = colors[3]
                ),
                widget.CPU(
                    font = "Source Code Pro Bold",
                    fontsize =16,
                    foreground = colors[1],
                    background = colors[3],   
                    format = ' {load_percent}%',
                    padding = 1
                ),
                widget.Sep(
                    linewidth = 0,
                    padding = 12,
                    background = colors[3]
                ),
                widget.TextBox(
                    text = '龍',
                    font = "saucecodepro nf",
                    #padding = -5,
                    #margin_y = 10,
                    fontsize = 26,
                    foreground = colors[1],
                    background = colors[3]
                ),
                widget.Memory(
                    font = "Source Code Pro Bold",
                    fontsize =16,
                    foreground = colors[1],
                    background = colors[3],   
                    #fmt = '{}',
                    format = ' {MemUsed:.0f} MiB',
                    padding = 1
                ),
                widget.TextBox(
                    text = '◢',
                    font = "Ubuntu Mono",
                    padding = -5,
                    #margin_y = 10,
                    fontsize = 45,
                    foreground = colors[1],
                    background = colors[3]
                ),
                widget.TextBox(
                    text = '說',
                    font = "saucecodepro nf",
                    #padding = -5,
                    #margin_y = 10,
                    fontsize = 25,
                    foreground = colors[3],
                    background = colors[1],
                    mouse_callbacks = {'Button1': lazy.spawn(network)}
                ),
                widget.Sep(
                    linewidth = 0,
                    padding = 10,
                    background = colors[1]
                ),
                widget.TextBox(
                    text = '',
                    font = "saucecodepro nf",
                    #padding = -5,
                    #margin_y = 10,
                    fontsize = 28,
                    foreground = colors[3],
                    background = colors[1],
                    mouse_callbacks = {'Button1': lazy.spawn(battery)}
                ),
                widget.Sep(
                    linewidth = 0,
                    padding = 10,
                    background = colors[1]
                ),
                widget.TextBox(
                    text = '墳',
                    font = "saucecodepro nf",
                    #padding = -5,
                    #margin_y = 10,
                    fontsize = 24,
                    foreground = colors[3],
                    background = colors[1],
                    mouse_callbacks = {'Button1': lazy.spawn(volume)}
                ),
                widget.PulseVolume(
                    font = "saucecodepro nf",
                    #padding = -5,
                    #margin_y = 10,
                    fontsize = 15,
                    foreground = colors[3],
                    background = colors[1],
                    #emoji = True
                    volume_app = "pavucontrol",
                    mouse_callbacks = {'Button1': lazy.spawn(volume)}
                    #emoji = True
                    #theme_path='/home/docs/checkouts/readthedocs.org/user_builds/qtile/checkouts/stable/test/data/ss_temp'
                ),
                widget.TextBox(
                    text = '◤',
                    font = "Ubuntu Mono",
                    padding = -5,
                    #margin_y = 10,
                    fontsize = 45,
                    foreground = colors[1],
                    background = colors[3]
                ),
                widget.TextBox(
                    text = '',
                    font = "saucecodepro nf",
                    #padding = -4,
                    #margin_y = 30,
                    fontsize = 22,
                    foreground = colors[1],
                    background = colors[3],
                    mouse_callbacks = {'Button1': lazy.spawn(time)}
                ),
                widget.Clock(
                    font = 'Source Code Pro Bold',
                    fontsize = 16,
                    format="%a, %d/%m/%y ",
                    foreground = colors[1],
                    background = colors[3],
                    padding=3,
                    mouse_callbacks = {'Button1': lazy.spawn(time)}
                ),
                widget.Sep(
                    linewidth = 0,
                    padding = 2,
                    background = colors[3]
                ),
                widget.TextBox(
                    text = '',
                    font = "saucecodepro nf",
                    #padding = -4,
                    #margin_y = 30,
                    fontsize = 22,
                    foreground = colors[1],
                    background = colors[3],
                    mouse_callbacks = {'Button1': lazy.spawn(time)}
                ),
                widget.Clock(
                    font = 'Source Code Pro Bold',
                    fontsize = 16,
                    format="%H:%M ",
                    foreground = colors[1],
                    background = colors[3],
                    padding=3,
                    mouse_callbacks = {'Button1': lazy.spawn(time)}
                ),
                widget.TextBox(
                    text = '◤',
                    font = "Ubuntu Mono",
                    padding = -7,
                    #margin_y = 10,
                    fontsize = 45,
                    foreground = colors[3],
                    background = colors[1]
                ),

                widget.TextBox(
                    text = '',
                    font = "saucecodepro nf",
                    margin_y = 5,
                    fontsize = 24,
                    padding = 4,
                    foreground = colors[3],
                    background = colors[1],
                    mouse_callbacks = {'Button1': lazy.spawn(powermenu)}
                ),
                
                #widget.QuickExit(
                #    font = "saucecodepro nf",
                #    margin_y = 5,
                #    fontsize = 24,
                #    padding = 6,
                #    foreground = colors[3],
                #    background = colors[1],
                #    default_text = '',
                #    countdown_start = 6,
                #    countdown_format = '{}'
                #),
                
                widget.Sep(
                    linewidth = 0,
                    padding = 4,
                    background = colors[1]
                ),
            ],
            size = 24,
            margin = 8
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
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
    ]
)
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
