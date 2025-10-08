import discord
from discord.ext import commands
import sqlite3

database = sqlite3.connect('messagehistory.db')
cursor = database.cursor()
database.execute("CREATE TABLE IF NOT EXISTS messages(user_id INT, message_content STRING, bot_response STRING)")

class Purge_Message_History(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="purgemessagehistory", help="Purges message history.")
    async def purge_message_history(self, ctx):
        query = "DELETE FROM messages WHERE user_id = ?"
        cursor.execute(query, (ctx.author.id, ))
        database.commit()
        await ctx.send("Your message history has been purged.")

async def setup(bot):
    await bot.add_cog(Purge_Message_History(bot))