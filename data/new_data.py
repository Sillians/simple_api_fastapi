from __future__ import absolute_import
import json
import os
from pathlib import Path


root_folder = Path(__file__).parents[1]
new_path = root_folder / "sample"


filename = "sample.json"
data = os.path.join(new_path, filename)


def get_new_data():
    with open(data) as file:
        new_data = json.load(file)
    return new_data
