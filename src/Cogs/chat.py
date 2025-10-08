import discord
from discord.ext import commands
import sqlite3
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
botid = os.getenv("BOT_ID")
database = sqlite3.connect('messagehistory.db')
cursor = database.cursor()
database.execute("CREATE TABLE IF NOT EXISTS messages(user_id INT, message_content STRING)")

class CogChat(commands.Cog):
    client = None
    def __init__(self, bot):
        self.bot = bot
        self.client = genai.Client(api_key=API_KEY)

    @commands.command(name="chat", help="UNDER CONSTRUCTION: just says hi for now")
    async def chat(self, ctx):
        self.storeMessage(ctx.author.id, ctx.message.content)
        # respond with Gemini API
        response = self.client.models.generate_content(model = "gemini-2.5-pro", contents = ctx.message.content)
        reply = response.candidates[0].content.parts[0].textdatabase
        self.storeMessage(botid, reply)
        await ctx.send(reply)

    def storeMessage(self, id, content):
        query = "INSERT INTO messages (user_id, message_content) VALUES (?, ?)"
        cursor.execute(query, (id, content))
        database.commit()

    # get key data
    def getMessageHistory(self, id):
        query = "SELECT message_content FROM messages WHERE user_id = ?"
        cursor.execute(query, (id, ))
        rows = cursor.fetchall()
        history = [row[0] for row in rows]
        return history

class db(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    await bot.add_cog(CogChat(bot))