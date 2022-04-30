import re
from dataclasses import dataclass
from time import sleep
from typing import Optional

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


def input(valid_inputs: Optional[list[str]] = None) -> str:
    options_prompt = ""
    options = []

    if valid_inputs:
        options = _get_input_options(valid_inputs)
        options_prompt = f"[info]Please select from '{', '.join([option['label'] for option in options])}'"
        print(options_prompt, delay=0, pause=0)

    value = console.input("")

    if not valid_inputs:
        return value
    else:
        selected_option = None

        for option in options:
            if option["shortcut"].lower() == value.lower():
                selected_option = option
                break

        if selected_option:
            return selected_option["text"]
        else:
            print(
                f"[info]Hmm sorry, not valid. {options_prompt}",
                delay=0,
                pause=0,
            )
            return input(valid_inputs)


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

    
def _get_input_options(option_strings: list[str]) -> dict:
    options_map = {}

    for option_string in option_strings:
        for index, char in enumerate(option_string):
            shortcut = option_string[:index + 1]

            if not options_map.get(shortcut):
                options_map[shortcut] = {
                    "shortcut": shortcut,
                    "label": f"({shortcut}){option_string[index+1:]}",
                    "text": option_string
                }
                break

    return list(options_map.values())



def _print_content(content: Content, delay: float):
    for char in content.text:
        console.print(f"{content.style}{char}", end="")
        sleep(delay)
