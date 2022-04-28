import discord
import os
from dotenv import load_dotenv

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # c!start : Verifica se o BOT está on.
    if message.content.startswith('c!start'):
        await message.channel.send('Tamo on :sunglasses:')


    # c!ctfon : Manda a mensagem embed sobre o novo ctf
    if message.content.startswith('c!ctfon'):
        nome="Expertum"
        dificuldade="Easy"
        flags=3
        descricao=f'Neste desafio você tem que capturar {flags} FLAGS! Temos uma plataforma para ver os desafios, hints, pontuar as flags e muito mais! Basta você se registrar na plataforma para jogar e clicar na aba "Challenges" para ver os desafios.'
        duracao="1 semana"
        hints="""1º Hint: {hint1}
        2º Hint: {hint2}
        3º Hint: {hint3}"""

        mensagemFinal="Qualquer duvida ou problema mande sua mensagem no canal <#719675854149517372> ou para os ADMs <@!248535350891380736> e <@!339396162543157248>"

        embedVar = discord.Embed(title="Novo CTF na área!", description=descricao, color=0xFFFFFF)
        embedVar.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/1255/1255407.png")
        embedVar.add_field(name="Nome: ", value=nome, inline=True)
        embedVar.add_field(name="Dificuldade:", value=dificuldade, inline=True)
        embedVar.add_field(name="Flags:", value=flags, inline=True)
        embedVar.add_field(name="Duração:", value=duracao, inline=True)
        embedVar.add_field(name="Plataforma para pontuação:", value="https://ctf.guiaanonima.com/", inline=False)
        embedVar.add_field(name="Dia das Hints:", value=hints, inline=False)
        embedVar.add_field(name="឵឵឵", value=mensagemFinal, inline=False)
        
        await message.channel.send(embed=embedVar)
        await message.channel.send('||<@&824041124728799302>||')






load_dotenv()
client.run(os.getenv('TOKEN'))



"""TODO
c!ctfon --name Expertum --difficulty Easy --flags 3 --time 1 semana
c!hint1 Veja o ftp

"""


