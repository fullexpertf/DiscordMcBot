import json
import asyncio
import discord
from discord.ext import commands

with open("config.json", encoding="utf-8") as f:
    config = json.load(f)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=config["prefix"], intents=intents)

initial_extensions = [
    "cogs.moderation",
    "cogs.economy",
    "cogs.levels",
    "cogs.music",
    "cogs.minecraft"
]

@bot.event
async def on_ready():
    print(f"{bot.user} olarak giriş yapıldı.")

async def load_extensions():
    for ext in initial_extensions:
        await bot.load_extension(ext)

async def main():
    async with bot:
        await load_extensions()
        await bot.start(config["token"])

if __name__ == "__main__":
    asyncio.run(main())
