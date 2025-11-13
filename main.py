import disnake
from disnake.ext import commands
from TOKEN import TOKEN

intents = disnake.Intents.default()
intents.message_content = True

bot = commands.Bot()

@bot.event
async def on_ready():
  print("бот готов!")

bot.load_extension("cogs.ping")


bot.run(TOKEN)


