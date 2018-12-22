#DutchNitro by JulesJulicher#9096
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import os

Client = discord.Client
bot = commands.Bot(command_prefix="dt!")
bot.remove_command('help')

async def loop():
    while True:
        await bot.change_presence(game=discord.Game(name="prefix = dt!", type=2))
        await asyncio.sleep(15)
        await bot.change_presence(game=discord.Game(name="vergeet niet te cappen", type=2))
        await asyncio.sleep(15)
        await bot.change_presence(game=discord.Game(name="happy runescaping", type=2))
        await asyncio.sleep(15)
        await bot.change_presence(game=discord.Game(name="fijne kerstdagen", type=2))
        await asyncio.sleep(15)


@bot.event
async def on_ready():
    print("this bot is ready to go and have a test run")
    print(bot.user.name)
    print(bot.user.id)
    print(discord.__version__)
    await loop()

@bot.event
async def on_command_error(message, error):
    embed=discord.Embed(title="Command Not Found", description="Whoops! kan dat niet vinden probeer `dt!help`", color=0xFF0000)
    await bot.send_message(error.message.channel, embed=embed)
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------

@bot.command(pass_context=True)
async def invite(ctx):
    embed = discord.Embed(colour = 0xff0000)
    embed.add_field(title="invite", value="invite van bot")
    await bot.say("https://discordapp.com/api/oauth2/authorize?client_id=520988858700005386&permissions=8&scope=bot")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def cookie(ctx,):
    await bot.say(":cookie:")
    
@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here is what i could find.", color=0xFF0000)
    embed.add_field(name="name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role, inline=True)
    embed.add_field(name="Joined at", value=user.joined_at, inline=True )
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(description="Here's what I could find:", color=0xff0000)
    embed.add_field(name="Name", value=ctx.message.server.name)
    embed.add_field(name="Owner", value=ctx.message.server.owner)
    embed.add_field(name="Region", value=ctx.message.server.region)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles))
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.add_field(name="Channels", value=len(ctx.message.server.channels))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def talk(ctx):
    await bot.say("hello whats your name?")
#-----------------------------------------------------------------------------------------------------------------
@bot.command(pass_context=True)
async def remove_cmd(ctx, cmd):
    if not (ctx.message.author.id == '266540652865519617' or ctx.message.author.id == '343013889283457025'):
        return await bot.say("No perms from developers")
    await bot.say("cmd has bin removed :ok_hand:")
    bot.remove_command(cmd)
#-----------------------------------------------------------------------------------------------------------------
@bot.command(pass_context=True)
async def serverlist(ctx):
    if ctx.message.author.server_permissions.administrator:
        embed = discord.Embed(title="All servers", description="lists all servers the bot is in.", color=0xff0000)
        tmp = 1
        for i in bot.servers:
            embed.add_field(name=str(tmp), value=i.name, inline=True)
            tmp += 1
        await bot.say(embed=embed)
#----------------------------------------------------------------------------------------------------------------
@bot.command(pass_context=True)
async def reboot(ctx):
    if not (ctx.message.author.id == '266540652865519617' or ctx.message.author.id == '343013889283457025'):
        return await bot.say(":x: You **Must** Be Bot Owner Or Developer or someone who has acces")
    await bot.say("ay okay :ok_hand:")
    await bot.logout()
    #werkt
    
@bot.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await bot.say("ay okay :ok_hand:")
    await bot.join_voice_channel(channel)

@bot.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_bot = bot.voice_client_in(server)
    await bot.say(":ok_hand: :dash:")
    await voice_bot.disconnect()
    
@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(colour = 0xff0000)
    embed.set_author(name="help")
    embed.add_field(name="serverinfo", value="geeft informatie over de server", inline = False)
    embed.add_field(name="info", value="geeft informatie over een persoon. gebruik dt!info @persoon", inline = False)
    embed.add_field(name="ping", value="pong", inline=False)
    embed.add_field(name="cookie", value="tegen de honger", inline=False)
    embed.add_field(name="join", value="de bot joint de voice channel waar je in zit", inline=False)
    embed.add_field(name="leave", value="bot verlaat je voice channel", inline=False)
    #_____________________________________
    embed.add_field(name="reboot", value="precies wat het zegt, **mod only**", inline=False)
    embed.add_field(name="remove_cmd", value="verwijdert een cmd, **mod only**", inline=False)
    await bot.send_message(author, embed=embed)
    
bot.run(os.environ.get('TOKEN'))
