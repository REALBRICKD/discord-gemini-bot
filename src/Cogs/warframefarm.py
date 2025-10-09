# Testing a specialized search function
import discord
from discord.ext import commands
from google import genai
import os

MAX_LEN = 2000
API_KEY = os.getenv("GEMINI_API_KEY")

class Warframe_Farm(commands.Cog):
    client = None
    def __init__(self, bot):
        self.bot = bot
        self.client = genai.Client(api_key=API_KEY)

    @commands.command(name="warframefarm", help="Tells you where best to farm whatever...maybe.")
    async def warframefarm(self, ctx, prompt):
        # respond with Gemini API
        prompt = """
        You are an accurate data analyst who will be given an item, resource, or mod in the game Warframe. 
        You will also be given official sources to pull data from and perform queries within. 
        If it is a site with a search function, utilize that.
        DO NOT PULL DATA FROM ANYWHERE EXCEPT THESE SOURCES.
        Condense all the information into accurate, concise, and actionable steps.
        No blank lines, emotes, italics, pointless bullets, indents, or bolding or other special formatting unless it is done in the sources.
        Analyze all numbers/data carefully. Explain briefly how you arrived at your conclusion.
        Ensure every topic and subtopic is relevant and important. Cut all irrelevant information. If information is not mathematically supported by the droptable, cut it and try again.
        You must remain as objective as possible, and as current as possible with the information you have.
        Avoid explanatory or essay-style paragraphs - rather, opt for concise, markdown-based technical writing if possible.
        Still, you should keep the writing style accessible to the average player - avoid jargon unless necessary.
        If an item is not available built, return results for the blueprint instead.
        If an item can only be obtained from a vaulted relic, say so.
        If there are multiple strong options, name them all.
        If you must search for a relic, resource, or mod, search for it on Digital Extremes' official droptable
        (https://warframe-web-assets.nyc3.cdn.digitaloceanspaces.com/uploads/cms/hnfvc0o3jnfvc873njb03enrf56.html) to ensure the relic exists and drops the item. Otherwise, pick again.
        If you decide on a relic, search the relic in DE's official droptable - if the item is not dropped by that relic, try a different relic.
        If an item is tradeable, pull that data from here: https://warframe.market/
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

async def setup(bot):
    await bot.add_cog(Warframe_Farm(bot))