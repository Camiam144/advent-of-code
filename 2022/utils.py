import inspect
import os


def get_script_name():
    """
    Retrieves the name of the currently running script.
    """
    return os.path.basename(inspect.stack()[1].filename.split(".")[0])


def get_data(script_name: str) -> str:
    data_name = script_name + ".txt"
    with open(
        "/Users/camerongross/Documents/Programming/adventofcode/2022/data/" + data_name,
        "r",
    ) as f:
        data = f.read()
    return data
