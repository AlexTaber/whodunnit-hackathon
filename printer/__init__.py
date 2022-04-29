import re
from dataclasses import dataclass
from time import sleep

from rich.console import Console

from printer.theme import custom_theme

console = Console(theme=custom_theme)


@dataclass
class Content:
    style: str
    text: str


def print(content: str, end="\n", delay=0.02, pause=0.5) -> None:
    content_arr = _get_content_array(content)

    for content in content_arr:
        _print_content(content, delay)

    sleep(pause)
    console.print("", end=end)


def _get_content_array(content: str) -> list[Content]:
    content_arr = content.split("$")

    return [_get_content_from_string(content_string) for content_string in content_arr]


def _get_content_from_string(content: str) -> Content:
    style = _get_style_from_string(content)
    text = re.sub("\[.*?\]", "", content)
    return Content(style, text)


def _get_style_from_string(content: str) -> str:
    if content.find("[") > -1:
        return content[content.find("[") : content.find("]") + 1]
    else:
        return ""


def _print_content(content: Content, delay: float):
    for char in content.text:
        console.print(f"{content.style}{char}", end="")
        sleep(delay)
