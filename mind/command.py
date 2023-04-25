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
    # PEGAR o canal de voice de origem 
    canal = ctx.author.voice.channel

    for member in members:
        await member.move_to(channel)

   
    

@bot.command()
async def centralizar(ctx):
    canal = ctx.author.voice.channel
    
    for na in ctx.guild.voice_channels:
         if na.members != []:
            for men in na.members:
                await men.move_to(canal)


@bot.command()
async def clear(ctx):
    channel = ctx.channel
    messages = []
    async for message in channel.history(limit=200):
        messages.append(message.id)
    
    for id in messages:
        message = await channel.fetch_message(id)
        await message.delete()
        
          
   



