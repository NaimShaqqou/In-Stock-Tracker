import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix='')

discord.Intents.all()


@client.event
async def on_ready():
    print('Bot is ready.')


@client.event
async def on_member_join(ctx, member):
    await ctx.send(f'{member}, welcome to my server!')


@client.event
async def on_member_remove(ctx, member):
    await ctx.send(f'{member}, goodbye!')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)


@client.command()
async def roll(ctx):
    await ctx.send(f'Roll: {random.randint(1, 6)}')




client.run('OTA5MTc3OTQwMzk3NDEyMzky.YZAf8A.neUkaL_TepA-jiRIjJB3khUIPWQ')
