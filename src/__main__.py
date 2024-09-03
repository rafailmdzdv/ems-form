import uvloop

from src.bot import EMSBot
from src.infrastructure.app.discord import EMSFormBot


async def main() -> None:
    await EMSFormBot(EMSBot()).run()


if __name__ == "__main__":
    uvloop.run(main())
