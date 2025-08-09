import discord
from discord.ext import commands
import asyncio
import yt_dlp

ytdl_opts = {"format": "bestaudio/best", "quiet": True, "noplaylist": True}
ytdl = yt_dlp.YoutubeDL(ytdl_opts)
ffmpeg_opts = {"options": "-vn"}

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    async def play(self, ctx, url: str):
        """Verilen YouTube URL'sinden müzik çalar."""
        if not ctx.author.voice:
            await ctx.send("Önce bir ses kanalına katılmalısın.")
            return

        await ctx.defer()
        vc = ctx.voice_client or await ctx.author.voice.channel.connect()
        loop = asyncio.get_running_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))
        stream_url = data["url"] if "url" in data else data["formats"][0]["url"]
        source = discord.FFmpegPCMAudio(stream_url, **ffmpeg_opts)
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
