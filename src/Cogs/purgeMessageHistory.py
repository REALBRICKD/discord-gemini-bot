import discord
from discord.ext import commands
from src.database.databaseClient import DatabaseClient

class Purge_Message_History(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db_helper = DatabaseClient()

    @commands.command(name="purgemessagehistory", help="Purges message history.")
    async def purge_message_history(self, ctx):
        self.db_helper.delete_user_messages(ctx.author.id)
        await ctx.send("Your message history has been purged.")

async def setup(bot):
    await bot.add_cog(Purge_Message_History(bot))