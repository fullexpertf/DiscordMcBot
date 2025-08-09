import discord
from discord.ext import commands
import youtube_dl

ytdl = youtube_dl.YoutubeDL({"format": "bestaudio", "quiet": True})

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    async def play(self, ctx, url: str):
        await ctx.defer()
        vc = ctx.voice_client or await ctx.author.voice.channel.connect()
        data = ytdl.extract_info(url, download=False)
        source = await discord.FFmpegOpusAudio.from_probe(data["url"])
        vc.play(source, after=lambda e: print("Çalma tamamlandı."))
        await ctx.send("Çalma başladı.")

    @commands.hybrid_command()
    async def stop(self, ctx):
        await ctx.defer()
        if ctx.voice_client:
            await ctx.voice_client.disconnect()
            await ctx.send("Ses bağlantısı sonlandırıldı.")
        else:
            await ctx.send("Herhangi bir ses kanalında değilim.")

async def setup(bot):
    await bot.add_cog(Music(bot))
