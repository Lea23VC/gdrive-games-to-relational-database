import os
from classes.GameConfig import GameConfig
from typing import List
# Define a list to store the games configuration
games_config: List[GameConfig]  = [
    {
        "name": "gb",
        "fullname": "Game Boy",
        "id": os.getenv("ID_FOLDER_GB")
    },
    {
        "name": "gbc",
        "fullname": "Game Boy Color",
        "id": os.getenv("ID_FOLDER_GBC")
    },
    {
        "name": "gba",
        "fullname": "Game Boy Advance",
        "id": os.getenv("ID_FOLDER_GBA")
    },
    {
        "name": "nes",
        "fullname": "Nintendo Entertainment System",
        "id": os.getenv("ID_FOLDER_NES")
    },
    {
        "name": "snes",
        "fullname": "Super Nintendo Entertainment System",
        "id": os.getenv("ID_FOLDER_SNES")
    },
    {
        "name": "64",
        "fullname": "Nintendo 64",
        "id": os.getenv("ID_FOLDER_64")
    },
    {
        "name": "gamecube",
        "fullname": "Nintendo Gamecube",
        "id": os.getenv("ID_FOLDER_GAMECUBE"),
        "nasos": True
    },
    {
        "name": "ds",
        "fullname": "Nintendo DS",
        "id": os.getenv("ID_FOLDER_DS")
    },
    {
        "name": "3ds",
        "fullname": "Nintendo 3DS",
        "id": os.getenv("ID_FOLDER_3DS")
    },
    {
        "name": "psx",
        "fullname": "Play Station",
        "id": os.getenv("ID_FOLDER_PSX")
    },
    {
        "name": "ps2",
        "fullname": "Play Station 2",
        "id": os.getenv("ID_FOLDER_PS2")
    },
    {
        "name": "psp",
        "fullname": "Play Station Portable",
        "id": os.getenv("ID_FOLDER_PSP")
    },
    {
        "name": "dreamcast",
        "fullname": "Sega Dreamcast",
        "id": os.getenv("ID_FOLDER_DREAMCAST")
    },
    {
        "name": "wii",
        "fullname": "Nintendo Wii",
        "id": os.getenv("ID_FOLDER_WII"),
        "nasos": True
    },
    {
        "name": "switch",
        "fullname": "Nintendo Switch",
        "id": os.getenv("ID_FOLDER_SWITCH")
    },
    {
        "name": "genesis",
        "fullname": "Sega Genesis",
        "id": os.getenv("ID_FOLDER_GENESIS")
    }
]

