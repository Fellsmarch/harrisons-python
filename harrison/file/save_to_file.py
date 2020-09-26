from pathlib import Path
from typing import Any


def save_to_file(object: Any, output_path: str) -> None:
    """
    Saves an object to the given output path.
    """
    path = Path(output_path)
    with open(path, "w") as file:
        file.write(object)
