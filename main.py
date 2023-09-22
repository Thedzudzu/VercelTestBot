import discord
import asyncio
import os

# Токен вашего бота. Замените его на свой собственный токен.
TOKEN = TOKEN = os.environ.get('TOKEN')

# ID канала, в который вы хотите отправить сообщение
CHANNEL_ID = 1153046777952481420

# Создание клиента Discord
client = discord.Client()

# Обработчик события "бот запущен"
@client.event
async def on_ready():
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("Бот запущен!")

# Запуск бота
client.run(TOKEN)
