import os
import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import sqlite3

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="/", intents=intents)

# Database initialization         
database = sqlite3.connect('messagehistory.db')
cursor = database.cursor()
database.execute("CREATE TABLE IF NOT EXISTS messages(user_id INT, message_content STRING, bot_response STRING)")        

@bot.event
async def on_ready():
    for filename in os.listdir("src/Cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"src.Cogs.{filename[:-3]}")
    await bot.tree.sync()
    print("Bot is ready!")

if __name__ == "__main__":
    print(os.getcwd())
    
bot.run(token, log_handler=handler, log_level=logging.DEBUG)

