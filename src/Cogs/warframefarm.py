# Testing a specialized search function
import discord
from discord.ext import commands
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

MAX_LEN = 2000
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

class WarframeFarm(commands.Cog):
    client = None
    def __init__(self, bot):
        self.bot = bot
        self.client = genai.Client(api_key=API_KEY)

    @commands.command(name="warframefarm", help="Tells you where best to farm whatever...maybe.")
    async def chat(self, ctx):
        # respond with Gemini API
        prompt = """
        You are given an item or mod in the game Warframe. 
        You will also be given a list of official sources to pull data from and perform queries within. 
        If it is a site with a search function, utilize that.
        DO NOT PULL DATA FROM ANYWHERE EXCEPT FROM THESE SOURCES.
        Condense all the information into accurate, concise, and actionable steps.
        No blank lines, emotes, italics, or bolding or other such formatting unless it is done in the sources.
        Analyze all numbers/data carefully. Explain briefly how you arrived at your conclusion.
        Ensure every topic and subtopic is relevant and important. Cut all irrelevant information.
        You must remain as objective as possible, and as current as possible with the information you have.
        Avoid explanatory or essay-style paragraphs - rather, opt for concise, markdown-based technical writing if possible.
        If an item is not available built, return results for the blueprint instead.
        Avoid blank lines for the sake of spacing.
        Avoid vaulted relics unless there are no other current options or the item in question is in resurgence.
        Pay special attention to what any relics drop if applicable, be 100% certain the item in question can be among those items - 80/20 is **NOT** enough.
        If there is ever any uncertainty, giving multiple strong options is okay - this is a last resort.
        If you decide on a relic, search for it on Digital Extremes' official droptable
        (https://warframe-web-assets.nyc3.cdn.digitaloceanspaces.com/uploads/cms/hnfvc0o3jnfvc873njb03enrf56.html) to ensure the relic exists and drops the item. Otherwise, pick again.
        Do **NOT** mix up your relic eras.
        Here are the sources:
        https://warframe-web-assets.nyc3.cdn.digitaloceanspaces.com/uploads/cms/hnfvc0o3jnfvc873njb03enrf56.html
        https://warframe.market/
        https://wiki.warframe.com/
        """ + ctx.message.content
        response = self.client.models.generate_content(model = "gemini-2.5-pro", contents = prompt)
        reply = response.candidates[0].content.parts[0].text
        for chunk in [reply[i:i+MAX_LEN] for i in range(0, len(reply), MAX_LEN)]:
            await ctx.send(chunk)

class db(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    await bot.add_cog(WarframeFarm(bot))