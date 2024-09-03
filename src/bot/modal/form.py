from discord import Interaction, ui


class EMSForm(ui.Modal, title="Форма"):
    username = ui.TextInput(label="Ник")
    static_id = ui.TextInput(label="Static ID")

    async def on_submit(self, interaction: Interaction) -> None:
        await interaction.response.send_message("Отправлена", ephemeral=True)
