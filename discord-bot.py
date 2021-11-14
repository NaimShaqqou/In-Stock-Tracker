import discord
import random
import importlib
importlib.import_module('in-stock-notifier.py')
from discord.ext import commands

TOKEN = 'OTA5MTc3OTQwMzk3NDEyMzky.YZAf8A.uSI6IPdexRQfxPz5TMNYDQg70RU'
tracking_list = []
valid_sites = ["amazon", "newegg", "ebay", "walmart", "bestbuy"]

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
async def track(ctx, message):
    check = message.split(" ", 1)
    if check[0] in valid_sites:
        await ctx.send(f"Now tracking: {message}")
        tracking_list.append(check[1])
        check_stock(check[0], check[1])
    else:
        await ctx.send("Invalid input.")


@client.command()
async def price(ctx, message):
    for i in valid_sites:
        # await ctx.send(f'Site: {i} \nPrice: {check_price(i, message)}\n')
        print()


@client.command()
async def List(ctx):
    num = 1;
    for i in tracking_list:
        await ctx.send(f'{num}: {i}\n')
        num += 1


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)


@client.command()
async def roll(ctx):
    await ctx.send(f'Roll: {random.randint(1, 6)}')


client.run(TOKEN)
