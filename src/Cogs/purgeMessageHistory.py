import discord
from discord.ext import commands
from src.database.databaseClient import DatabaseClient

# A client command for delete_user_messages in the database client.
class Purge_Message_History(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db_helper = DatabaseClient()

    # calls the database client to delete user messages
    @commands.command(name="purgemessagehistory", help="Purges message history.")
    async def purge_message_history(self, ctx):
        self.db_helper.delete_user_messages(ctx.author.id)
        await ctx.send("Your message history has been purged.")

# Add cog to bot directory, enabling the command to be called
async def setup(bot):
    await bot.add_cog(Purge_Message_History(bot))
