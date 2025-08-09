import aiohttp
from discord.ext import commands

API = "https://api.mcsrvstat.us/2"

class Minecraft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mcstatus(self, ctx, address: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{API}/{address}") as resp:
                data = await resp.json()
        if data.get("online"):
            players = data.get("players", {}).get("online", 0)
            await ctx.send(f"Sunucu aktif! Online oyuncu sayısı: {players}")
        else:
            await ctx.send("Sunucu kapalı ya da ulaşılamıyor.")

async def setup(bot):
    await bot.add_cog(Minecraft(bot))
