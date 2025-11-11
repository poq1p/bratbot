import disnake
from disnake.ext import commands
import sqlite 

intents = disnake.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='+', intents=intents)

conn = sqlite3.connect('/data/bot.db')
cursor = conn.cursor()