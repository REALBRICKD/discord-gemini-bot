import discord
from discord.ext import commands
import requests

# Here by popular demand. Uses Inspirobot API to generate "inspirational" posters.
class Inspirobot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # Fetches data directly from the Inspirobot site and sends output as a discord message.
    @commands.command(name="inspirobot", help="Provides encouragement in your time of need")
    async def inspiroBot(self, ctx):
        url = "https://inspirobot.me/api?generate=true"
        response = requests.get(url)
        await ctx.send(response.text)

# Add cog to bot directory, enabling the command to be called
async def setup(bot):
    await bot.add_cog(Inspirobot(bot))
