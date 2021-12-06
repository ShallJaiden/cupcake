import discord
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.reply(left + right)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run('OTA5NzAwODgxMTA3MjU1MzA2.YZIG9w.B4UN_uzRyMfEy7P9dJ5WzM3wFjE')
