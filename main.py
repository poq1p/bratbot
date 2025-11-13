import disnake
from disnake.ext import commands
from TOKEN import TOKEN

bot = commands.InteractionBot()

@bot.event
async def on_ready():
    print(f"Бот запущен как {bot.user}")

bot.load_extension("cogs.ping")
bot.load_extension("cogs.hello")

bot.run(TOKEN)

