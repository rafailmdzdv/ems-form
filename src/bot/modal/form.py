from discord import Embed, Interaction, ui

from src.core.config.base import FileConfig


class EMSForm(ui.Modal, title="Форма"):
    date = ui.TextInput(label="Дата")

    def __init__(self, config: FileConfig) -> None:
        self._config = config
        super().__init__()

    async def on_submit(self, interaction: Interaction) -> None:
        embed = Embed(title="Форма")
        embed.add_field(name="Тег", value=f"<@{interaction.user.id}>")
        embed.add_field(name="Дата", value=self.date)
        embed.add_field(name="", value=f"<@&{self._config.discord().role_id}>")
        await interaction.response.send_message(embeds=(embed,))
