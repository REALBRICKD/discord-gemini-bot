import discord
from discord.ext import commands
import sqlite3
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

MAX_LEN = 2000
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
botid = os.getenv("BOT_ID")
database = sqlite3.connect('messagehistory.db')
cursor = database.cursor()

class Chat(commands.Cog):
    client = None
    def __init__(self, bot):
        self.bot = bot
        self.client = genai.Client(api_key=API_KEY)

    @commands.command(name="chat", help="Will respond to anything you ask it.")
    async def chat(self, ctx):
        # respond with Gemini API
        history = self.getMsgHistory(ctx.author.id)
        response = self.client.models.generate_content(model = "gemini-2.5-pro", 
                                                       contents = [ctx.message.content] + ["previous interactions: "] + history)
        reply = response.candidates[0].content.parts[0].text
        self.storeMessage(ctx.author.id, ctx.message.content, reply)
        for chunk in [reply[i:i+MAX_LEN] for i in range(0, len(reply), MAX_LEN)]:
            await ctx.send(chunk)

    def storeMessage(self, id, content, reply):
        query = "INSERT INTO messages (user_id, message_content, bot_response) VALUES (?, ?, ?)"
        cursor.execute(query, (id, content, reply))
        database.commit()
    # get key data
    def getMsgHistory(self, user_id):
        query = "SELECT message_content, bot_response FROM messages WHERE user_id = ?"
        cursor.execute(query, (user_id,))
        rows = cursor.fetchall()
        # Returns a list of (user_message, bot_response) tuples
        return rows

async def setup(bot):
    await bot.add_cog(Chat(bot))