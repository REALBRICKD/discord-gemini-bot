import os
import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import sys
import os
# Ensure database is ported correctly.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.database.databaseClient import DatabaseClient

# Load environment variables from .env file
load_dotenv()
token = os.getenv("DISCORD_TOKEN")

# Configure intents and logging - intents are essentially bot permissions.
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# All commands will be preceded with a /
bot = commands.Bot(command_prefix="/", intents=intents)

# Database initialization         
db_helper = DatabaseClient()

# Load cogs. Think of them as command modules.
@bot.event
async def on_ready():
    for filename in os.listdir("src/cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"src.cogs.{filename[:-3]}")
    await bot.tree.sync()
    print("Bot is ready!")

if __name__ == "__main__":
    print(os.getcwd()) # ensures correct working directory
    
bot.run(token, log_handler=handler, log_level=logging.DEBUG) #runs bot

