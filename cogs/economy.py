from discord.ext import commands

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.balances = {}

    @commands.hybrid_command()
    async def balance(self, ctx):
        await ctx.defer()
        bal = self.balances.get(ctx.author.id, 0)
        await ctx.send(f"{ctx.author.mention}, bakiyen: {bal} coin.")

    @commands.hybrid_command()
    async def daily(self, ctx):
        await ctx.defer()
        bal = self.balances.get(ctx.author.id, 0)
        bal += 100
        self.balances[ctx.author.id] = bal
        await ctx.send(f"Günlük ödül: 100 coin. Yeni bakiyen: {bal} coin.")

async def setup(bot):
    await bot.add_cog(Economy(bot))
