#DutchNitro by JulesJulicher#9096
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import os
import youtube_dl

Client = discord.Client
bot = commands.Bot(command_prefix="dt!")
bot.remove_command('help')

players = {}

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
#info cmds
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
#--------------------------------------------------------------------------------------------------
#overige cmds
@bot.command(pass_context=True)
async def ping(ctx):
        t1 = time.perf_counter()
        tmp = await bot.say("pinging...")
        t2 = time.perf_counter()
        await bot.say("Ping: {}ms".format(round((t2-t1)*1000)))
        await bot.delete_message(tmp)

#music cmds___________________________________________________
@bot.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await bot.say("ay okay :ok_hand:")
    await bot.join_voice_channel(channel)
    
@bot.command(pass_context=True)
async def play(ctx, url):
	server = ctx.message.server
	voice_bot = bot.voice_client_in(server)
	player = await voice_bot.create_ytdl_player(url)
	players[server.id] = player
	player.start()
    
@bot.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_bot = bot.voice_client_in(server)
    await bot.say(":ok_hand: :dash:")
    await voice_bot.disconnect()

@bot.command(pass_context=True)
async def pause(ctx):
	id = ctx.message.server.id
	players[id].pause()

@bot.command(pass_context=True)
async def resume(ctx):
	id = ctx.message.server.id
	players[id].resume()
@bot.command(pass_context=True)
async def stop(ctx):
	id = ctx.message.server.id
	players[id].stop()
	await bot.say(":ok_hand: ay okay")
	
#_______________________________________
@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(colour = 0xff0000)
    embed.set_author(name="help")
    embed.add_field(name="serverinfo", value="geeft informatie over de server", inline = False)
    embed.add_field(name="info", value="geeft informatie over een persoon. gebruik dt!info @persoon", inline = False)
    embed.add_field(name="ping", value="x aantal ms vertraging", inline=False)
    embed.add_field(name="join", value="de bot joint de voice channel waar je in zit", inline=False)
    embed.add_field(name="leave", value="bot verlaat je voice channel", inline=False)
    embed.add_field(name="play", value="speelt een liedje van yt, gebruik play urlhere", inline=False)
    embed.add_field(name="pause", value="pauzeert het liedje", inline=False)
    embed.add_field(name="resume", value="liedje gaat verder", inline=False)
    embed.add_field(name="stop", value="stopt de muziek", inline=False)
    #admin cmds
    embed.add_field(name="serverlist", value="dev only", inline=False)
    embed.add_field(name="kick", value="kick de gementionde persoon **mod only**", inline=False)
    embed.add_field(name="reboot", value="precies wat het zegt, **dev only**", inline=False)
    embed.add_field(name="remove_cmd", value="verwijdert een cmd, **dev only**", inline=False)
    await bot.send_message(author, embed=embed)
#----------------------------------------------------------------------------------------------------------------
#admin cmds
#------------------------------------------------------
#ids
julesjulicher2 = "266540652865519617"
demon333 = "304335595637964811"
onheil = "210016781790740481"
freshness = "371390873889669120"
deadmau5= "272370438334578690"
optic = "261489812807090176"
Greyaligator = "125251854811660288"
gideon = "225615881009496064"
mast3beer = "325614257544757249"
ikayser = "268813802391207937"
lordhugo = "267061903035990017"
helpmai = "274953456085893121"
exia = "262731316615708683"
draynor = "311210142249123840"
heiligekip = "306437934838579200"
nneo = "146037858212249600"
thabaws = "344868565209448448"
jeffrey = "343013889283457025"
curious = "297725476821008384"
#____________________________________________-
@bot.command(pass_context = True)
async def kick(ctx, member: discord.Member):
    if ctx.message.author.id == julesjulicher2 or ctx.message.author.id == demon333 or ctx.message.author.id == onheil or ctx.message.author.id == freshness or ctx.message.author.id == deadmau5 or ctx.message.author.id == optic or ctx.message.author.id == Greyaligator or ctx.message.author.id == gideon or ctx.message.author.id == mast3beer or ctx.message.author.id == ikayser or ctx.message.author.id == lordhugo or ctx.message.author.id == helpmai or ctx.message.author.id == exia or ctx.message.author.id == draynor or ctx.message.author.id == heiligekip or ctx.message.author.id == nneo or ctx.message.author.id == thabaws or ctx.message.author.id == jeffrey or ctx.message.author.id == curious:
        try:
            await bot.say(":boot: bye!""{}".format(member.mention))
            await bot.kick(member)
        except discord.errors.Forbidden:
            await bot.say(":x: error kan niet doen!, controleer of de bot boven de rang staat van de gene die je kickt")
    else:
        await bot.say("geen toegang")

julesjulicher2 = "266540652865519617"
jeffrey = "343013889283457025"
@bot.command(pass_context=True)
async def reboot(ctx):
    if ctx.message.author.id == julesjulicher2 or ctx.message.author.id == jeffrey:
        return await bot.say(":x: geen toegang")
    await bot.say("ay okay :ok_hand:")
    await bot.logout()

julesjulicher2 = "266540652865519617"
jeffrey = "343013889283457025"
@bot.command(pass_context=True)
async def remove_cmd(ctx, cmd):
    if ctx.message.author.id == julesjulicher2 or ctx.message.author.id == jeffrey:
        return await bot.say("No perms from developers")
    await bot.say("cmd is verwijdert :ok_hand:")
    bot.remove_command(cmd)
julesjulicher2 = "266540652865519617"
@bot.command(pass_context=True)
async def serverlist(ctx):
    if ctx.message.author.id == julesjulicher2:
        embed = discord.Embed(title="All servers", description="lists alle servers waar de bot in is.", color=0xff0000)
        tmp = 1
        for i in bot.servers:
            embed.add_field(name=str(tmp), value=i.name, inline=False)
            tmp += 1
        await bot.say(embed=embed)

    
bot.run(os.environ.get('TOKEN'))
