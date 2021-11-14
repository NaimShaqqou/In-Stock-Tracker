import discord
import random
import notifier

from discord.ext import commands

# For security purposes, removed token for gitHub uploads
TOKEN = ''
tracking_list = []
valid_sites = ["amazon", "newegg", "ebay", "walmart", "bestbuy"]

client = commands.Bot(command_prefix='')
discord.Intents.all()


# client events represent actions the bot takes once it recognizes
# certain events have occured, EX: on_ready prints to console once
# the bot recognizes it has succesfully connected to discord
#######################################################################
# These events represent introductory functionality to get me
# acclimated to working with discord bots
@client.event
async def on_ready():
    print('Bot is ready.')


@client.event
async def on_member_join(ctx, member):
    await ctx.send(f'Welcome, {member}, to my server!')


@client.event
async def on_member_remove(ctx, member):
    await ctx.send(f'Goodbye, {member}!')

##########################################################################

# client commands represent additional functionality accessible
# to the discord users, EX: roll returns an int [1 - 6] inclusive

# track calls the check stock on a valid website for an input item
@client.command()
async def track(ctx, *, message):
    checklist = message.split(" ", 1)

    if checklist[0] in valid_sites:
        await ctx.send(f"Now searching for {checklist[1]} on {checklist[0]}.")
        tracking_list.append(checklist[1])
        notifier.check_stock(checklist[0], checklist[1])
    else:
        await ctx.send('Invalid input: please try again')


# price calls a possible check price method for an input item
@client.command()
async def price(ctx, *, message):
    for i in valid_sites:
        # await ctx.send(f'Site: {i} \nPrice: {check_price(i, message)}\n')
        print()


# list prints all input items currently being tracked
@client.command()
async def list(ctx):
    num = 1;
    for i in tracking_list:
        await ctx.send(f'{num}: {i}\n')
        num += 1


##############################################################
# these methods represent introductory functionality to get
# me acclimated to working with discord bots
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)


@client.command()
async def roll(ctx):
    await ctx.send(f'Roll: {random.randint(1, 6)}')

#############################################################

client.run(TOKEN)
