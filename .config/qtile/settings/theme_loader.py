import json
try:
    from settings.path import *
except:
    from path import *

from os import listdir
from os.path import join
from random import sample


themes_list = [f for f in listdir(themes_path) if f.endswith('.json')]


def get_json_file(name: str) -> dict:
    with open(def_path, 'r') as f:
        def_file = json.load(f)
    return def_file


def load_theme(theme):

    selected = join(themes_path, theme)
    with open(selected, 'r') as f:
        colors = json.load(f)
    return colors


def dict_enum(l: list) -> dict:
    return {i: l[i] for i in range(len(l))}


def switch_theme(theme: str, file: dict = {}) -> None:
    if not file:
        file = get_json_file(def_path)

    file["colors"] = theme
    with open(def_path, 'w') as f:
        f.write(json.dumps(file, indent=4))


def list_themes():
    themes_dict = dict_enum(themes_list)
    def_file = get_json_file(def_path)
    print(f'Actual theme: {def_file["colors"][:-5]}.')

    for i in themes_dict:
        print(f'{i +1}: {themes_dict[i][:-5]}')
    # if sel_id not in range(len(themes_list)):
    try:
        sel_id = int(input('Select a theme to be aplied: ')) - 1
        selection = themes_dict[sel_id]
        print(f'Actual theme: {selection[:-5]}')
    # else:
    except:
        selection = random_cs()
        print(f'Wrong Input. Random choise: {selection[:-5]}')

    return [selection, def_file]


def random_cs():
    selected = sample(themes_list, 1)[0]
    return selected


def main():
    switch_theme(*list_themes())


if __name__ == '__main__':
    main()
