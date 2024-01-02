from dataclasses import dataclass
from typing import Literal
import os


@dataclass
class FolderContent:
    root: str
    directories: list[str]
    files: list[str]


def file_browser(filepath: str = ".") -> list[FolderContent]:
    return [
        FolderContent(root, directories, files)
        for root, directories, files in os.walk(filepath)
    ]


def check_type(filepath: str) -> Literal["directory", "file", "link"]:
    if os.path.isdir(filepath):
        return "directory"
    elif os.path.isfile(filepath):
        return "file"
    elif os.path.islink(filepath):
        return "link"


def filesplit(filepath: str) -> tuple[str, str]:
    return os.path.splitext(filepath)


if __name__ == "__main__":
    print(file_browser())
