from mind import bot 


@bot.command()
async def move(ctx, channel : discord.VoiceChannel, *members : discord.Member):
    for member in members:
        await member.move_to(channel)

    print(f"{members} foi movido para {channel}!")

@bot.event
async def on_ready():
        print(f"ready")
   



