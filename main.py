import disnake
from disnake.ext import commands
from TOKEN import TOKEN

intents = disnake.Intents.default()
intents.message_content = True

bot = commands.Bot()

@bot.event
async def on_ready():
  print("бот готов!")

@bot.slash_command(guild_ids=[1234, 5678])  
async def ping(inter):
  await inter.response.send_message("Понг!")

bot.run(TOKEN)


