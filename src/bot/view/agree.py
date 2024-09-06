from discord import ButtonStyle, Interaction
from discord.ui import Button, View, button

from src.core.config.base import FileConfig


class AgreeOrDeclineView(View):
    def __init__(self, config: FileConfig) -> None:
        self._config = config
        super().__init__()

    @button(label="Принять", style=ButtonStyle.green)
    async def agree(self, interaction: Interaction, _: Button) -> None:
        if await self._check_is_user_head(interaction):
            await interaction.message.add_reaction("✅")
            await interaction.message.edit(view=None)

    @button(label="Отклонить", style=ButtonStyle.red)
    async def decline(self, interaction: Interaction, _: Button) -> None:
        if await self._check_is_user_head(interaction):
            await interaction.message.add_reaction("❌")
            await interaction.message.edit(view=None)

    async def _check_is_user_head(self, interaction: Interaction) -> bool:
        role = interaction.guild.get_role(self._config.discord().role_id)
        return role in interaction.user.roles
