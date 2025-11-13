import disnake
from disnake.ext import commands

class hello(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # создаём slash-команду
    @commands.slash_command(description="Приветствие")
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message("Йо братан салам как там дела брат", ephemeral=True)  # ответ только виден тебе

def setup(bot):
    bot.add_cog(hello(bot))