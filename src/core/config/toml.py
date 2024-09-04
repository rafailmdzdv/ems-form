from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import override

import tomllib

from src.core.config.base import FileConfig
from src.core.config.sections.discord import DiscordSection


@dataclass(frozen=True)
class TomlConfig(FileConfig):
    _discord: DiscordSection

    @classmethod
    @override
    def from_file(cls) -> FileConfig:
        config_file = Path(
            __file__,
        ).parent.parent.parent.parent / "config/config.toml"
        with config_file.open("rb") as file:
            toml = tomllib.load(file)
        return cls(
            DiscordSection(
                token=toml["discord"]["token"],
                role_id=toml["discord"]["role_id"],
            ),
        )

    @override
    def discord(self) -> DiscordSection:
        return self._discord
