import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason: str | None = None):
        await ctx.defer()
        await member.kick(reason=reason)
        await ctx.send(f"{member} sunucudan atıldı.")

    @commands.hybrid_command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason: str | None = None):
        await ctx.defer()
        await member.ban(reason=reason)
        await ctx.send(f"{member} sunucudan yasaklandı.")

    @commands.hybrid_command(name="temizle")
    @commands.has_permissions(manage_messages=True)
    async def temizle(self, ctx, amount: int):
        await ctx.defer()
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f"{amount} mesaj silindi.", delete_after=5)

async def setup(bot):
    await bot.add_cog(Moderation(bot))
