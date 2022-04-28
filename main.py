import discord
import os
from dotenv import load_dotenv

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # c!start : Verifica se o BOT está on.
    if message.content.startswith('c!start'):
        await message.channel.send('Tamo on :sunglasses:')



load_dotenv()
client.run(os.getenv('TOKEN'))

