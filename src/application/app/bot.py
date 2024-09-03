from typing import Protocol


class Bot(Protocol):
    async def run() -> None:
        ...
