from typing import Protocol


class DiscordBot(Protocol):
    async def start(self) -> None:
        ...
