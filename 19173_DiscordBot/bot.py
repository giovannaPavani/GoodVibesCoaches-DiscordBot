# bot.py
import os
import random
import discord
from discord import FFmpegPCMAudio
from discord.ext import commands, tasks
from datetime import datetime
from dotenv import load_dotenv
from discord.ext.commands import bot


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} se conectou ao Discord!')

@bot.command(name='lanse', help='Lansa a braba através de uma única frasezinea')
async def mande(ctx):
    msgs = ['😖zelão peidao😨',
            '💁‍♀️giovanna patroa💅',
            '👯‍♀️se me ataca eu vo ataca🤺✨',
            '👼labaxurias decantas amem🙏'
    ]

    response = random.choice(msgs)
    await ctx.send(response)

@bot.command(name='coach', help='Te envia uma frase motivacional e inspiradora')
async def mande(ctx):
    msgs = ['✨não seja fod*, desista✨',
            '✨nenhum obstáculo é grande para quem desiste✨',
            '✨os humilhados serão mais humilhados ainda✨',
            '✨o importante não é lutar sempre, mas perder todos os dias✨',
            '✨pode não dar certo, e você vai ter certeza quanto tentar✨',
            '✨dias de luta, dias de derrota✨',
            '✨o que for pra ser, nunca será✨',
            '✨primeiro eles riem dos seus sonhos...\n depois eles riem dos seus fracassos✨',
            '✨o não você já tem, o que você está procurando é a humilhação✨',
            '✨se você pode sonhar, você pode desistir✨',
            "✨I just can't✨",
            '✨O importante não é lutar sempre, mas fracassar todos os dias✨',
            '✨vai dar tudo errado✨',
            '✨vai. n\e se der medo, volta ✨',
            '✨só dara errado se você tentar✨',
            '✨não sabendo que era possível... foi lá e soube✨',
            '✨nunca é tarde para desistir✨',
    ]

    imgs=['1.jpg',
          '2.jpg',
          '3.jpg',
          '4.jpg',
          '5.jpg',
          '6.jpg',]
    img = random.choice(imgs)
    response = random.choice(msgs)

    await ctx.send(response)
    await ctx.send(file=discord.File(img))
    

@bot.command(name='niver', pass_context=True, help='Manda parabéns, pois hoje é um dia especial')
async def niver(ctx, pessoa):
    await ctx.send(f'Feliz aniversário, {pessoa}! 🎈🎉\n\nHoje é um dia especial 🥳, te dou um presente 🎁 você nunca viu nada igual 👀')
    # grab the user who sent the command
    user = message.author
    guild = ctx.guild
    voice_client  = discord.utils.get(bot.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('parabens.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)


@bot.command(name='lanse_dado', help='Lansa o dado. Use !lanse_dado [nº lançamentos] [nº lados do dado]')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name='canal', help="Admins podem criar um canal e escolher o nome")
@commands.has_role('admin')
async def create_channel(ctx, nome):
    guild = ctx.message.guild
    print(f'Creating a new channel: {nome}')
    await guild.create_text_channel(nome)

@bot.command(name='diario', help='Registra a anotação do diário de bordo formatadinho')
@commands.has_role('escrivã')
async def escrever(ctx, *args):
    meses=['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    now = datetime.now()
    dia = now.day
    mes = meses[(now.month)-1]
    print(now.hour)
    texto = ''
    for arg in args:
        texto = texto + arg + ' '
    response = (f'{dia} de {mes} - {now.hour}:{now.minute} às .. : .. \n\t {texto}')
    print (response)
    await ctx.send(response)

@bot.command(name="link", pass_context=True, help="Se houver, registra o titulo e link no canal de texto")
async def registrar(ctx, titulo, link):
    canal = bot.get_channel(830066192366436422)
    await canal.send(f'{titulo}: {link}')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('Você não é patroa o suficiente para executar esse comando.')

bot.run(TOKEN)