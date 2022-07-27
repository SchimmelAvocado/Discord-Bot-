from datetime import datetime
import discord
from discord.ext import commands
import pytz
import os
import aiosqlite

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix=".",help_command=None, intents=intents)


@client.event
async def on_message(msg):
        print(msg)
        if 'a' in msg.content:
            print('Message received!')
async def on_ready():
    print(f'BotName: {client.user.name}')
    await client.change_presence(activity=discord.Game(name=".man"))  
    async with aiosqlite.connect("kaisabot.db") as db:
        async with db.cursor() as cursor:
            await cursor.execute('CREATE TABLE IF NOT EXISTS anime (name TEXT, picture BLOB)')
        await db.commit()


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run("nice try ;)")

