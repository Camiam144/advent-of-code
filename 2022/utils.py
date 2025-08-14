import inspect
from pathlib import Path


def get_script_name():
    """
    Retrieves the name of the currently running script.
    """
    return Path(inspect.stack()[1].filename.split(".")[0]).name


def get_data(script_name: str) -> str:
    data_name = script_name + ".txt"
    with Path.open(
        "/Users/camerongross/Documents/Programming/adventofcode/2022/data/" + data_name,
        "r",
    ) as f:
        data = f.read()
    return data
