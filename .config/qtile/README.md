# Qtile

# Table of Contetents
- [Dependences and Defaults](#dependences)
    - [Terminal Emulator](#terminal-emulator)
    - [Fonts](#fonts)
        - VictorMono
        - UbuntuMono
    - [Shell](#shell)
    - [Nitrgoen](#nitrgoen)
    - [LXAppearance](#lxappearance)
    - [Transparency](#transparency)
    - [Rofi](#rofi)
    - [Dbus](#dbus)
- [Keys](#keys)

# Dependences 
Required apps and defaults of my preferences linked by key binds:
## Terminal Emulator
Terminal used: [Kitty](https://sw.kovidgoyal.net/kitty/) \
Font: Victor Mono Nerd Font \
For colorschemes: [Kitty Themes](https://github.com/dexpota/kitty-themes)
Actual Colorscheme: [Argonaut](https://github.com/dexpota/kitty-themes/blob/master/themes/Argonaut.conf)
**Instalation**: \
- Arch-Based: `sudo pacman -S kitty`
- Debian-Based: `sudo apt install kitty`
## Fonts
[Nerd Fonts](https://www.nerdfonts.com/#home) are required. Several special symbols are used among the config.
There are two main fonts used:
- [VictorMono](https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/VictorMono.zip)
- [UbuntuMono](https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/UbuntuMono.zip)
## Shell
Shell used: [Fish](https://fishshell.com/).
**Instalation**: \
- Arch-Based: `sudo pacman -S fish`
- Debian-Based: `sudo apt install fish`

## Nitrgoen
Nitrgoen is an app to manage wallpapers. At starting the command ´nitrgoen --restore´ is executed.
**Instalation**: \
- Arch-Based: `sudo pacman -S nitrogen`
- Debian-Based: `sudo apt install nitrogen`

## Lxappeareance
[Lxappeareance](https://wiki.lxde.org/es/LXAppearance) is an app to set system themes .
**Instalation**: \
- Arch-Based: `sudo pacman -S lxappearance`
- Debian-Based: `sudo apt install lxappearance`

## Transparency
Transparency compositor used: [picom](https://github.com/yshui/picom). In some cases is needed to create an empty file named `picom.conf` or set the backend as `xrender`.
**Instalation**: \
- Arch-Based: `sudo pacman -S picom`
- Debian-Based: `sudo apt install picom`

## Rofi
[Rofi](https://github.com/davatorium/rofi) is a menu used to start apps and navegate through workspaces.
Theme: [Material-Ocean](https://github.com/material-ocean/rofi-Theme)
config.rasi:
```rasi
configuration {
    modi: "window,drun,ssh,combi";
    font: "VictorMono Nerd Font 11";
    theme: "material-ocean";
    show-icons: true;
}
```
**Instalation**: \
- Arch-Based: `sudo pacman -S rofi dmenu`
- Debian-Based: `sudo apt install rofi dmenu`
    ```
    mkdir ~/.config/rofi
    wget https://raw.githubusercontent.com/material-ocean/rofi-Theme/master/material-ocean.rasi
    echo "configuration {
    modi: "window,drun,ssh,combi";
    font: "VictorMono Nerd Font 11";
    theme: "material-ocean";
    show-icons: true;
    }" >> config.rasi
    
    ```

## Dbus
In order to set the spotify controls and names in the bar is needed to install an `Mpris2` dependence named `dbus-next`. \
`pip install dbus-next`.

# Keys
| Keys                 | Action                                    |
| -------------------- | ----------------------------------------- |
| super+w              | Close window                              |
| super+control+q      | Shutdown Qtile                            |
| super+Alt+r         | Restart Qtile                             |
| super+Alt+q         | Shutdown PC                               |
| super+h              | Focus the left window                     |
| super+l              | Focus the right window                    |
| super+j              | Focus the down window                     |
| super+k              | Focus the up window                       |
| super+c              | Focus the next window                     |
| super+shift+h        | Swap with the left window                 |
| super+shift+l        | Swap with the right window                |
| super+shift+j        | Swap with the down window                 |
| super+shift+k        | Swap with the up window                   |
| super+i              | Grow actual window                        |
| super+shift+i        | Shink actual window                       |
| super+control+h      | Grow left                                 |
| super+control+l      | Grow right                                |
| super+control+j      | Grow down                                 |
| super+control+k      | Grow up                                   |
| super+Tab            | Next Layout                               |
| super+shift+f        | Toggle Floating                           |
| super+o              | Maximize window acording to layout config |
| super+shift+space    | Flip windows - Monad                      |
| super+n              | Normalize widnow sizes                    |
| super+m              | Set actual window to fullscreen           |
| super+Alt+j         | Go to screen 1                            |
| super+Alt+k         | Go to screen 2                            |
| super+space          | Open an app                               |
| control+space        | Show opened apps                          |
| super+b              | Browser                                   |
| super+shift+e        | Study                                     |
| super+shift+a        | Anime                                     |
| control+Alt+t       | Terminal                                  |
| XF86AudioRaiseVolume | Volume Up                                 |
| XF86AudioLowerVolume | Volume Down                               |
| XF86AudioPlay        | Spotify Play/Pause                        |
| XF86AudioNext        | Spotify Next                              |
| XF86AudioPrev        | Spotify Prev                              |
| Print                | Full ScreenShot                           |
| shift+super+s        | Section ScreenShot                        |
| super+v              | Diodon                                    |
