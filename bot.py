import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.bans = True

bot = commands.Bot(command_prefix='+', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='ban')
async def ban(ctx, member: discord.Member):
    # Your code for the ban command here
    await ctx.send(f'Banned {member.mention}')

@bot.command(name='kick')
async def kick(ctx, member: discord.Member):
    # Your code for the kick command here
    await ctx.send(f'Kicked {member.mention}')

@bot.command(name='mute')
async def mute(ctx, member: discord.Member):
    # Your code for the mute command here
    await ctx.send(f'Muted {member.mention}')

@bot.command(name='purge')
async def purge(ctx, amount: int):
    # Your code for the purge command here
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f'{amount} messages purged.')

@bot.command(name='aide')
async def help_command(ctx):
    # List of commands and their descriptions
    help_message = (
        "```\n"
        "+ban @user - Banir un user\n"
        "+kick @user - Kick un user\n"
        "+mute @user - Mute un user\n"
        "+purge <amount> - suprime le nombre de msg indique\n"
        "+aide - montre tout les commandes\n"
        "```"
    )
    await ctx.send(help_message)

# Replace 'YOUR_DISCORD_BOT_TOKEN' with your actual bot token
async def login():
    try:
        await client.login('process.env.TOKEN')
        print(f'Logged in as {bot.user}')
    except Exception as e:
        print(f'Failed to log in: {e}')
        raise e
