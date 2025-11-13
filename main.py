import disnake
from disnake.ext import commands
from TOKEN import TOKEN

intents = disnake.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
  print("бот готов!")

bot.load_extension("cogs.ping")

bot.load_extension("cogs.hello")


bot.run(TOKEN)


