import disnake
from disnake.ext import commands
import sqlite 

intents = disnake.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='+', intents=intents)

conn = sqlite3.connect('/data/bot.db')
cursor = conn.cursor()

@bot.event 
async def on_ready():
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        id BIGINT 
        cash INT )""")
    conn.commit()
    print(f'{bot.user.name} ready!')

@bot.command()
async def ping(ctx):
    await ctx.reply(f'Понг! {round(bot.latency * 1000)} мс')