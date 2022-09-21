from discord.ext import commands
import discord
from random import randrange
from discord import Permissions

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.presences = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = 560857477181341696  # Change to your discord id

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

########
#WARM-UP
########

@bot.command()
async def name(ctx):
    await ctx.send(ctx.author)

@bot.command()
async def d6(ctx):
    await ctx.send(randrange(6))

@bot.event
async def on_message(message):
    if message.content =="Salut tout le monde":
        await message.channel.send("Salut tout seul @"+"<@" + str(message.author.id) + ">")
    await bot.process_commands(message)

########
#ADMIN
########

@bot.command()
async def count(ctx):
    online=0
    idle=0
    off=0
    for guild in bot.guilds:
        for member in guild.members:
            if str(member.status)=="online":
                online=online+1
            elif str(member.status)=="offline":
                off=off+1
            elif str(member.status)=="idle":
                idle=idle+1
    await ctx.send(str(online) +" members are online, "+ str(idle) +" are idle and "+ str(off) +" are off")

@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    if str(member.name)!="Hugo La Bringue":
        await member.ban(reason = reason)

@bot.command()
async def admin(ctx, member : discord.Member):
    #print(member.name)
    admin=None
    for role in ctx.guild.roles:
        if (str(role)=="Admin"):
            admin=role
    if admin==None:
        admin = await ctx.guild.create_role(name="Admin",permissions=Permissions.all(), mentionable=True)
    await member.add_roles(admin)

########
#IT'S ALL FUN AND GAMES
########

@bot.command()
async def xkcd(ctx):
    await ctx.send("https://xkcd.com/"+str(randrange(2673)))

@bot.command()
async def poll(ctx, message):
    await ctx.send("@here "+str(message))
    await ctx.send(str(message))

token = ""
bot.run(token)  # Starts the bot
