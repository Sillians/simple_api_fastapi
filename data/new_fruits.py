from __future__ import absolute_import
import json
import os
from pathlib import Path


root_folder = Path(__file__).parents[1]
new_path = root_folder / "new_fruits"


filename = "new_fruits.json"
data = os.path.join(new_path, filename)


def get_new_fruits_data():
    with open(data) as file:
        new_fruit_data = json.load(file)
    return new_fruit_data

