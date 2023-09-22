import discord
import asyncio
import os

TOKEN = os.environ.get('TOKEN')

CHANNEL_ID = 1153046777952481420

client = discord.Client()

@client.event
async def on_ready():
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("Бот запущен!")

client.run(TOKEN)
