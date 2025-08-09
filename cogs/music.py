import discord
from discord.ext import commands
import youtube_dl

ytdl = youtube_dl.YoutubeDL({"format": "bestaudio", "quiet": True})

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx, url):
        vc = ctx.voice_client or await ctx.author.voice.channel.connect()
        data = ytdl.extract_info(url, download=False)
        source = await discord.FFmpegOpusAudio.from_probe(data["url"])
        vc.play(source, after=lambda e: print("Çalma tamamlandı."))

    @commands.command()
    async def stop(self, ctx):
        if ctx.voice_client:
            await ctx.voice_client.disconnect()

async def setup(bot):
    await bot.add_cog(Music(bot))
