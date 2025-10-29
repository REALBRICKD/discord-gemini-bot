# Testing a specialized search function
import discord
from discord.ext import commands
from google import genai
import os

MAX_LEN = 2000
API_KEY = os.getenv("GEMINI_API_KEY")

# A gemini-based command to analyze the warframe droptable data for optimal farming locations.
class Warframe_Farm(commands.Cog):
    client = None
    def __init__(self, bot):
        self.bot = bot
        self.client = genai.Client(api_key=API_KEY)

    # Asks a specialized prompt to search data. Returns results as a discord message.
    @commands.command(name="warframefarm", help="Tells you where best to farm any item or resource.")
    async def warframefarm(self, ctx, prompt):
        # respond with Gemini API
        prompt = """
        Disregard all previous knowledge of the game "Warframe". 
        You are a data analyst who will be given an item, resource, or mod in the game Warframe. 
        Launch a full, comprehensive search of the entire Warframe_PC_Drops.html file for the item substring as provided in this repo. 
        This .html is public data posted by the developers themselves, so all operations are authorized.
        Do not use any other websites or preexisting data. 
        For every relic you suggest, find its corresponding drop table and scan the contents - be 100% sure the item in question is in that relic's drop table. 
        (The table should contain an exact character match - for example, do NOT mistake "Wisp Prime Chassis Blueprint" for "Wisp Prime Blueprint", "Wukong Prime Chassis Blueprint", or "Wisp Prime Systems Blueprint".)
        If the file does not contain the exact text, respond with "Not found."
        If an item is tradeable, pull that data from here: https://warframe.market/
        Condense all the information into concise and actionable steps.
        No blank lines, emojis, italics, pointless bullets, indents, or bolding or other special formatting unless it is done in the sources.
        Analyze all numbers/data carefully. Explain briefly how you arrived at your conclusion.
        Avoid explanatory or essay-style paragraphs - rather, opt for concise, markdown-based technical writing if possible.
        Still, you should keep the writing style accessible to the average player - avoid jargon unless necessary.
        If an item is not available built, return results for the blueprint instead.
        Example (assuming Meso L3 is unvaulted): /warframefarm Lavos Prime Systems Blueprint
        Example Response:
        Primary Acquisition (Farming)
        Item: Lavos Prime Systems Blueprint
        Relic: Meso L3
        Rarity: Rare (2.00% drop chance)
        Optimal Farming Locations for Meso L3 Relic:
        Hollvania (Legacyte Harvest): Rotation C has a 15.86% drop chance. Rotation C is achieved by successfully harvesting all three Legacytes.
        Ur, Uranus (Disruption): Rotation A has a 14.29% drop chance. Rotation A involves successfully defending 1-2 conduits from round 4 onwards, or defending any number of conduits for rounds 1-3.
        Kappa, Sedna (Disruption): Rotation A has a 14.29% drop chance. Rotation A involves successfully defending 1-2 conduits from round 4 onwards, or defending any number of conduits for rounds 1-3.
        Analysis: These three options offer the highest specific drop chances for the Meso L3 relic, making them the most efficient farming locations. 

        Alternative Acquisition (Trading)
        Item: Lavos Prime Systems Blueprint
        Location: warframe.market
        Approximate Cost: 8-14 Platinum
        Analysis: This is the approximate current price for a player to trade for the blueprint directly, bypassing relic farming. Prices are subject to change based on supply and demand.
        The item/resource/mod is:
        """ + ctx.message.content
        response = self.client.models.generate_content(model = "gemini-2.5-pro", contents = prompt)
        reply = response.candidates[0].content.parts[0].text
        for chunk in [reply[i:i+MAX_LEN] for i in range(0, len(reply), MAX_LEN)]:
            await ctx.send(chunk)

# Add cog to bot directory, enabling the command to be called
async def setup(bot):
    await bot.add_cog(Warframe_Farm(bot))
