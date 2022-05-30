# Import Color Scheme
from os.path import isfile, join
from os import listdir
import json
from random import sample
import sys
# from settings.themes import nord as colors
from settings.path import def_path, themes_path
from settings.theme_loader import load_theme
# from settings.themes import material_ocean as colors

#
# mod = "mod4"
# browser = 'brave'
# terminal = "kitty"
# font = "UbuntuMono Nerd Font"
#


def load_defaults():
    with open(def_path, 'r') as f:
        defaults = json.load(f)
    return defaults


defaults = load_defaults()
mod = defaults["mod"]
browser = defaults["browser"]
terminal = defaults["terminal"]
font = defaults["font"]
# random_cs()
colors = load_theme(defaults["colors"])
