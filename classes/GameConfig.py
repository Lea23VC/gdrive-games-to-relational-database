from typing import TypedDict

# Define a TypedDict for the games configuration
class GameConfig(TypedDict):
    name: str
    fullname: str
    id: str
    nasos: bool