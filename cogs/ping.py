import disnake
from disnake.ext import commands


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Проверить отклик бота")
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message("Pong!")

def setup(bot):
    bot.add_cog(Ping(bot))
