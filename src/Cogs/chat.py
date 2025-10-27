import discord
from discord.ext import commands
from google import genai
import os
from src.database.databaseClient import DatabaseClient

MAX_LEN = 2000
API_KEY = os.getenv("GEMINI_API_KEY")
botid = os.getenv("BOT_ID")

# This is a simple command that allows the user to converse with the Gemini API directly.
class Chat(commands.Cog):
    client = None
    # Initialize the cog
    def __init__(self, bot):
        self.bot = bot
        self.client = genai.Client(api_key=API_KEY)
        self.db_helper = DatabaseClient()

    # Factors both previous messages and the current message into the response.
    @commands.command(name="chat", help="Will respond to anything you ask it.")
    async def chat(self, ctx):
        user_message = ctx.message.content
        history = self.db_helper.get_msg_history(ctx.author.id) # Gather message history from db to provide additional context
        response = self.client.models.generate_content(model = "gemini-2.5-pro", 
                                                       contents = [user_message] + ["previous interactions: "] + history) # respond with Gemini API
        reply = response.candidates[0].content.parts[0].text
        self.db_helper.save_message(ctx.author.id, user_message, reply) # save to db
        await ctx.send(reply)

async def setup(bot):
    await bot.add_cog(Chat(bot))
