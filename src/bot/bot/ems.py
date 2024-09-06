from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, override

from discord import Embed, Intents, Interaction, utils
from discord.ext.commands import Bot

from src.bot.bot.base import DiscordBot
from src.bot.modal.form import EMSForm
from src.bot.view.agree import AgreeOrDeclineView

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

        @self._api.tree.command(name="запись", description="Отправить заявку")
        async def form(interaction: Interaction) -> None:
            embed = Embed(title="Форма")
            embed.add_field(name="Тег", value=f"<@{interaction.user.id}>")
            embed.add_field(name="", value=f"<@&{self._config.discord().role_id}>")
            await interaction.response.send_message(
                embeds=(embed,),
                view=AgreeOrDeclineView(self._config),
            )

        @self._api.tree.command(name="secret")
        async def secret(interaction: Interaction) -> None:
            await interaction.response.send_message("Алия пиздюк")
