import json
import sys
from os import path

rofi_path = path.join(path.expanduser('~'), ".config", "rofi")
kitty_path = path.join(path.expanduser('~'), ".config", "kitty")
dg_path = path.join(path.expanduser('~'), '.config',
                    'qtile', 'settings', 'default_globals.json')
apthemes_path = path.join(path.expanduser('~'), '.config', 'apthemes')
look_path = path.join(apthemes_path, 'look.json')
test_path = path.join(apthemes_path, 'test.conf')


def rofi(cs):

    with open(path.join(rofi_path, 'config.rasi'), 'r') as f:
        rl = f.read().split('\n')

    for i in rl:
        if i.startswith('@theme'):
            tl = i
            break


def kitty(cs):
    config_file_path = path.join(kitty_path, 'kitty.conf')
    with open(config_file_path) as f:
        rl = f.read().split('\n')

    for i in rl:
        if i.startswith("include themes"):
            tl = i
            break
    rl[rl.index(tl)] = f"include themes/{cs}.conf"
    wt = '\n'.join(rl)
    with open(config_file_path, 'w') as f:
        f.write(wt)


def main():
    defaultcs = 'Argonaut'
    with open(dg_path, 'r') as f:
        dg = json.load(f)
    with open(look_path, 'r') as f:
        look = json.load(f)

    csk = look[dg["colors"][:-5]]["kitty"]
    if csk == "DEFAULT":
        csk = defaultcs

    kitty(csk)


main()
