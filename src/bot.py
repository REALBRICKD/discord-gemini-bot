import os
import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
from src.database.databaseClient import DatabaseClient

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="/", intents=intents)

# Database initialization         
db_helper = DatabaseClient()

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

