import discord
from discord.ext import commands

class Levels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.xp = {}

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        self.xp[message.author.id] = self.xp.get(message.author.id, 0) + 10
        await self.bot.process_commands(message)

    @commands.hybrid_command()
    async def level(self, ctx, member: discord.Member | None = None):
        await ctx.defer()
        member = member or ctx.author
        xp = self.xp.get(member.id, 0)
        lvl = xp // 100
        await ctx.send(f"{member.mention} seviye {lvl}, XP {xp}.")

async def setup(bot):
    await bot.add_cog(Levels(bot))
