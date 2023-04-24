import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents,command_prefix='$')
token = "MY-TOKEN"

@bot.command()
async def move(ctx, channel : discord.VoiceChannel, *members : discord.Member):
    for member in members:
        await member.move_to(channel)

    print(f"{members} foi movido para {channel}!")

@bot.event
async def on_ready():
        print(f"ready")
   

bot.run(token)

