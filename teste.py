import discord
import asyncio

# Define os intents padrão
intents = discord.Intents.default()

intents.message_content = True
# Cria um objeto Client com os intents
client = discord.Client(intents=intents)

# Define o prefixo para os comandos
prefix = '!'

@client.event
async def on_ready():
    print('Bot online e pronto para uso!')

@client.event
async def on_message(message):
    print(message.content)  # adiciona um print com o conteúdo da mensagem
    # Verifica se o comando começa com o prefixo desejado
    if message.content.startswith(prefix + 'move'):
        # Separa o comando dos argumentos
        command = message.content.split(' ')[0]
        args = message.content.split(' ')[1:]

        # Obtém o canal de voz alvo
        channel_name = ' '.join(args)
        channel = discord.utils.get(message.guild.voice_channels, name=channel_name)

        # Verifica se o canal de voz alvo existe
        if channel:
            # Move todos os membros do canal atual para o canal de voz alvo
            for member in message.guild.voice_channels[0].members:
                await member.move_to(channel)
            # Envia uma mensagem de confirmação
            await message.channel.send(f'Movi todos os membros para {channel_name}.')
        else:
            await message.channel.send('Canal de voz não encontrado.')

# Insira o token do seu bot do Discord
client.run('MY-TOKEN')
