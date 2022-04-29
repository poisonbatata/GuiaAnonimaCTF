import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

bot = commands.Bot(command_prefix='c!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


# -=-=-=-=- Comandos -=-=-=-=-

@bot.command()
# c!start : Verifica se o BOT está on.
async def start(ctx):
    await ctx.send('Tamo on :sunglasses:')


@bot.command(name="newctf", help='Cria um embed sobre o novo ctf.\nUso: c!ctfon --name Expertum --difficulty Easy --flags 3 --time "1 Semana (28 abr 2022 18:00 até 05 mai 2022 18:00)" --hints 3 --delay 2d', brief="Cria um embed sobre o novo ctf.")
# c!newctf : Manda a mensagem embed sobre o novo ctf
async def embedCtf(ctx):
    nome="Expertum"
    dificuldade="Easy"
    flags=3
    descricao=f'Neste desafio você tem que capturar {flags} FLAGS! Temos uma plataforma para ver os desafios, hints, pontuar as flags e muito mais! Basta você se registrar na plataforma para jogar e clicar na aba "Challenges" para ver os desafios.'
    duracao="1 Semana (28 abr 2022 18:00 até 05 mai 2022 18:00)"
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
    embedVar.add_field(name="឵឵឵", value=mensagemFinal, inline=False) # Coloquei um caractere (Unicode: U+17B5) que não renderiza no discord para conseguir enviar a mensagem sem o name aparecer.
    
    await ctx.channel.send(embed=embedVar)
    await ctx.channel.send('||<@&824041124728799302>||')


@bot.command(name="say", help='Faz o bot "falar" a mensagem desejada.\nUso: c!say Olá!', brief="Exibe a mensagem desejada no chat")
@commands.has_permissions(administrator=True)
# c!say msg : Faz o bot falar a msg
async def say(ctx, *, arg):
    await ctx.channel.send(arg)


"""
@bot.command()
@commands.has_permissions(administrator=True)
async def fala(ctx, *args):
    response = ""
    for arg in args:
        response = response + " " + arg
    await ctx.channel.send(response)
"""


# -=-=-=-=- Erros -=-=-=-=-
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send(f'{ctx.message.author}, você não tem permissão para executar o comando "{ctx.command}".')









load_dotenv()
bot.run(os.getenv('TOKEN'))




"""TODO
c!ctfon --name Expertum --difficulty Easy --flags 3 --time 1 semana
c!hint1 Veja o ftp

Comandos{
    - endctf
    - 
    - 
    - 
}

Permissões{
    - @commands.has_role('admin')
    - @commands.has_permissions(administrator=True)
    - 
    - 
    - 
}

"""

