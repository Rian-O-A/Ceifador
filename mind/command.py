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
    for member in members:
        await member.move_to(channel)

   
    

@bot.command()
async def centralizar(ctx):
    # PEGAR o canal de voice de origem 
    canal = ctx.author.voice.channel
    user = ctx.author.discriminator

    
    for na in ctx.guild.voice_channels:
         if na.members != []:
            for men in na.members:
                await men.move_to(canal)
        
    if  user == '5754':
        await ctx.send("Tarefa concluida meu senhor!")
    else:
        await ctx.send("Atenderei seu pedido, mas não abuse!")


@bot.command()
async def clear(ctx):
    channel = ctx.channel
    messages = []
    await ctx.send("Sim meu senhor, limparei toda essa imundice!")
    async for message in channel.history(limit=200):
        messages.append(message.id)
    
    for id in messages:
        message = await channel.fetch_message(id)
        await message.delete()

       
@bot.command()
async def muteall(ctx):
    # Verifica se o autor do comando está em um canal de voz
    user = ctx.author.discriminator
    if  user == '5754':
        await ctx.send("Todos calem a boca seus mortais, meu senhor irá se pronunciar!")
    else:
        await ctx.send("Verme insolente!\nAtenderei seu pedido, mas não ouse abusar da sorte!")
    if ctx.author.voice is None:
        if  user == '5754':
            await ctx.send("Meu senhor, você precisa está em algum canal de voice!")  
        else:
            await ctx.send("Mortal ignorante, para que eu possa agraciar com meus poderes você precisa está em algum chat de voice!")

        return

    # Obtém o canal de voz em que o autor do comando está
    voice_channel = ctx.author.voice.channel

    # Percorre todos os usuários no canal de voz e os muta
    for member in voice_channel.members:
        await member.edit(mute=True)     

@bot.command()
async def desmute(ctx):
    # Verifica se o autor do comando está em um canal de voz
    user = ctx.author.discriminator
    if  user == '5754':
        await ctx.send("Devolverei suas vozes novamente, como meu senhor ordenou!")
    else:
        await ctx.send("Irei abrir um exceção e devolverei suas vozes, mas não abusem!")
    if ctx.author.voice is None:
        if  user == '5754':
            await ctx.send("Meu senhor, você precisa está em algum canal de voice!")  
        else:
            await ctx.send("Mortal ignorante, para que eu possa agraciar com meus poderes você precisa está em algum chat de voice!")

        return

    # Obtém o canal de voz em que o autor do comando está
    voice_channel = ctx.author.voice.channel

    # Percorre todos os usuários no canal de voz e os muta
    for member in voice_channel.members:
        await member.edit(mute=False)        

@bot.command()
async def info(ctx):
    
    
    for na in ctx.guild.voice_channels:
         print(na.members)
         



