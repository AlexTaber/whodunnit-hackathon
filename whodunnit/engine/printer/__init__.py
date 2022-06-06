import re
from dataclasses import dataclass
from time import sleep
from typing import Optional

from rich.console import Console

from whodunnit.engine.game import game
from whodunnit.engine.printer.theme import custom_theme

console = Console(theme=custom_theme)

state = {"current_char_width": 0}


@dataclass
class Content:
    style: str
    text: str


def print(content: str, end="\n", delay=0.02, pause=0.5) -> None:
    content_arr = _get_content_array(content)

    for content in content_arr:
        _print_content(content, delay)

    if not game.state.dev_mode:
        sleep(pause)

    if end == "\n":
        state["current_char_width"] = 0

    console.print("", end=end)


def input(valid_inputs: Optional[list[str]] = None) -> str:
    options = []

    if valid_inputs:
        options = _get_input_options(valid_inputs)
        select_options = "\n".join([option["label"] for option in options])
        options_prompt = f"[info]Please select:\n{select_options}"
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
                f"[danger]Invalid input",
                delay=0,
                pause=0,
            )
            return input(valid_inputs)


def _get_content_array(content: str) -> list[Content]:
    content_arr = content.split("|")

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
    for index, option_string in enumerate(option_strings):
        shortcut = str(index + 1)
        options_map[shortcut] = {
            "shortcut": shortcut,
            "label": f"|[primary]({shortcut})| {option_string}",
            "text": option_string,
        }

    return list(options_map.values())


def _print_content(content: Content, delay: float):
    for char in content.text:
        state["current_char_width"] += 1

        if state["current_char_width"] > 80 and char == " ":
            char = "\n"
            state["current_char_width"] = 0
        elif char == "\n":
            state["current_char_width"] = 0

        console.print(f"{content.style}{char}", end="")

        if not game.state.dev_mode:
            sleep(delay)
