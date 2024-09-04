from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, override

from discord import Intents, Interaction, utils
from discord.ext.commands import Bot

from src.bot.bot.base import DiscordBot
from src.bot.modal.form import EMSForm

if TYPE_CHECKING:
    from src.core.config.base import FileConfig


@dataclass
class EMSBot(DiscordBot):
    _config: FileConfig
    _api: Bot = field(
        default_factory=lambda: EMSBot._with_default_intents(),
    )

    @classmethod
    def _with_default_intents(cls) -> Bot:
        intents = Intents.default()
        intents.message_content = True
        return Bot(command_prefix="!", intents=intents)

    @override
    async def start(self) -> None:
        await self.__init_commands()
        utils.setup_logging()
        await self._api.start(token=self._config.discord().token)

    async def __init_commands(self) -> None:
        @self._api.event
        async def on_ready() -> None:
            await self._api.tree.sync()

        @self._api.tree.command(name="form", description="Отправить заявку")
        async def form(interaction: Interaction) -> None:
            await interaction.response.send_modal(EMSForm(self._config))
