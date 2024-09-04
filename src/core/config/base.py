from typing import Protocol

from src.core.config.sections.discord import DiscordSection


class FileConfig(Protocol):
    @classmethod
    def from_file(cls) -> "FileConfig":
        ...

    def discord(self) -> DiscordSection:
        ...
