import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix='!/')


@bot.event
async def on_ready():
        print(f"Ceifador ON")


@bot.command()
async def move(ctx, channel : discord.VoiceChannel, *members : discord.Member):
    canal = ctx.author.voice.channel
    
    print(f"Estou no canal de voz: {canal.name}")
   
    for member in members:
        await member.move_to(channel)

   
    print(f"{members} foi movido para {channel}!")

@bot.command()
async def centralizar(ctx,*members : discord.Member):
    canal = ctx.author.voice.channel
    
    print(ctx.guild.voice_channels[0].members)
   
    for member in members:
        await member.move_to(canal)

   
    print(f"{members} foi movido para {canal.name}!")

@bot.command()
async def info(ctx):
    
    print(ctx.guild.voice_channels)
    for na in ctx.guild.voice_channels:
         print(na)
         
   



