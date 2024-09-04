import uvloop

from src.bot import EMSBot
from src.core.config.toml import TomlConfig
from src.infrastructure.app.discord import EMSFormBot


async def main() -> None:
    await EMSFormBot(EMSBot(TomlConfig.from_file())).run()


if __name__ == "__main__":
    uvloop.run(main())
