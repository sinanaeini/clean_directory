import json


def read_json(path):
    with open(path) as f:
        reader = json.load(f)
        return reader
