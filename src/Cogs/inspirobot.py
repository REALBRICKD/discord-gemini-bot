import discord
from discord.ext import commands
import requests

# Here by popular demand
class Inspirobot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="inspirobot", help="Provides encouragement in your time of need")
    async def inspiroBot(self, ctx):
        url = "https://inspirobot.me/api?generate=true"
        response = requests.get(url)
        await ctx.send(response.text)

async def setup(bot):
    await bot.add_cog(Inspirobot(bot))