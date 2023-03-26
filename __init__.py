import os
import sys
from typing import List

import yaml

languages = {}
commands = {}


languages_present = {}


def get_command(value: str) -> List:
    return commands["command"][value]


def get_string(lang: str):
    return languages[lang]


for filename in os.listdir(r"./"):
    if filename.endswith(".yml"):
        language_name = filename[:-4]
        commands[language_name] = yaml.safe_load(
            open(r"./" + filename, encoding="utf8")
        )


for filename in os.listdir(r"./"):
    if "en" not in languages:
        languages["en"] = yaml.safe_load(
            open(r"en.yml", encoding="utf8")
        )
        languages_present["en"] = languages["en"]["name"]
    if filename.endswith(".yml"):
        language_name = filename[:-4]
        if language_name == "en":
            continue
        languages[language_name] = yaml.safe_load(
            open(r"./" + filename, encoding="utf8")
        )
        for item in languages["en"]:
            if item not in languages[language_name]:
                languages[language_name][item] = languages["en"][item]
    try:
        languages_present[language_name] = languages[language_name][
            "name"
        ]
    except:
        print(
            "There is some issue with the language file inside bot. Please report it to the owner at @No_me_no_no on Telegram."
        )
        sys.exit()