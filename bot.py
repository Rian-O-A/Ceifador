# This example requires the 'message_content' intent.

import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents,command_prefix='$')

class MyClient(discord.Client):
    

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
 

           

client = MyClient(intents=intents)
client.run('MTA1MDQ2MzA5MTk3ODE1ODA5MA.GrgeiY.pGsm5jzu36pkHdWFjxQ_eGZ1SMaZYK1daiEvR4')
