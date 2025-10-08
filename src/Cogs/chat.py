import discord
from discord.ext import commands
import sqlite3

database = sqlite3.connect('messagehistory.db')
cursor = database.cursor()
database.execute("CREATE TABLE IF NOT EXISTS messages(user_id INT, message_content STRING)")

class CogChat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="chat", help="UNDER CONSTRUCTION: just says hi for now")
    async def chat(self, ctx):
        #Database        
        query = "INSERT INTO messages (user_id, message_content) VALUES (?, ?)"
        cursor.execute(query, (ctx.author.id, ctx.message.content))
        database.commit()
        await ctx.send("hi")


class db(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    await bot.add_cog(CogChat(bot))