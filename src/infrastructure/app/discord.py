from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, override

from src.application.app import Bot

if TYPE_CHECKING:
    from src.bot import DiscordBot


@dataclass(frozen=True)
class EMSFormBot(Bot):
    _discord: DiscordBot

    @override
    async def run(self) -> None:
        await self._discord.start()
