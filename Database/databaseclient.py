import discord
from discord.ext import commands
import sqlite3

database = sqlite3.connect('messagehistory.db')
cursor = database.cursor()
database.execute("CREATE TABLE IF NOT EXISTS messages(user_id INT, message_content STRING)")

class db(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.event
    async def on_message(message):
        if message.auuthor == bot.user:
            return
