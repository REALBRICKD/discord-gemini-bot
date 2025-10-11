import discord
from discord.ext import commands
from google import genai
import os
from src.database.databaseClient import DatabaseClient

MAX_LEN = 2000
API_KEY = os.getenv("GEMINI_API_KEY")
botid = os.getenv("BOT_ID")

class Chat(commands.Cog):
    client = None
    def __init__(self, bot):
        self.bot = bot
        self.client = genai.Client(api_key=API_KEY)
        self.db_helper = DatabaseClient()

    @commands.command(name="chat", help="Will respond to anything you ask it.")
    async def chat(self, ctx):
        user_message = ctx.message.content
        # respond with Gemini API
        history = self.db_helper.get_msg_history(ctx.author.id)
        response = self.client.models.generate_content(model = "gemini-2.5-pro", 
                                                       contents = [user_message] + ["previous interactions: "] + history)
        reply = response.candidates[0].content.parts[0].text
        # save to db
        self.db_helper.save_message(ctx.author.id, user_message, reply)
        if len(reply) > MAX_LEN:
            for i in range(0, len(reply), MAX_LEN):
                await ctx.send(reply[i:i+MAX_LEN])
        else:
            await ctx.send(reply)

async def setup(bot):
    await bot.add_cog(Chat(bot))
