import discord
from discord.ext import commands,tasks
import datetime
import math
import random
from discord.ext.commands.errors import CommandNotFound
import youtube_dl
from discord_minesweeper import *

recomendacoes = []

with open('lista de _filmes.txt','r') as recomendacao:
    for linha in recomendacao:
        recomendacoes.append(linha)

bot = commands.Bot("!",online=True)


@bot.event
async def on_ready():
    print("Nelson")
    current_time.start()


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "Nelson" in message.content or "NELSON" in message.content:
        await message.channel.send(f"Nelson, {message.author.name}")
    if "torroio" in message.content or "TORROIO" in message.content or "Torroio" in message.content or "torr0io" in message.content or "T0rr010" in message.content:
        await message.channel.send(f"é proibido falar esse nome nesse servidor, {message.author.name}")
        await message.delete()
    await bot.process_commands(message)



@bot.command(name = "nelson")
async def send_nelson(ctx):
    name = ctx.author.name
    awnser = "Nelson, " + name
    await ctx.send(awnser)

@bot.command(name = "ping")
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command(name= "calcula")
async def calcula(ctx,expression):
    try:
        if expression[-1] == '!':
            resp = math.factorial(float(expression[0:len(expression)-1]))
            embed = discord.Embed(
                title = 'FATORIAL',
                description = "pai é cranio nelsin porra",
                color = 0x0000FF
            )     
            embed.set_author(name= bot.user.name)
            embed.add_field(name = "Resposta", value = resp, inline = False)
            await ctx.send(embed=embed)
        if expression[0:3] == 'cos':
            resp = math.cos((float(expression[3:])*math.pi)/180) 
            embed = discord.Embed(
                title = 'COSSENO',
                description = "pai é cranio nelsin porra é o angulo",
                color = 0x0000FF
            )     
            embed.set_author(name= bot.user.name)
            embed.add_field(name = "Resposta", value = resp, inline = False)
            await ctx.send(embed=embed)
        if expression[0:3] == 'sen':
            resp = math.sin((float(expression[3:])*math.pi)/180)      
            embed = discord.Embed(
                title = 'SENO',
                description = "pai é cranio nelsin porra é o angulo",
                color = 0x0000FF
            )     
            embed.set_author(name= bot.user.name)
            embed.add_field(name = "Resposta", value = resp, inline = False)
            await ctx.send(embed=embed)
        if expression[0:3] == 'tan':
            resp = math.tan((float(expression[3:])*math.pi)/180)      
            embed = discord.Embed(
                title = 'TANGENTE',
                description = "pai é cranio nelsin porra é o angulo",
                color = 0x0000FF
            )     
            embed.set_author(name= bot.user.name)
            embed.add_field(name = "Resposta", value = resp, inline = False)
            await ctx.send(embed=embed)
        if expression[0:2] == 'pi':
            resp = math.pi
            embed = discord.Embed(
                title = 'PI',
                description = "pai é cranio nelsin porra é PIKKKKAS",
                color = 0x0000FF
            )     
            embed.set_author(name= bot.user.name)
            embed.add_field(name = "Resposta", value = resp, inline = False)
            await ctx.send(embed=embed)
        else:
            resp = eval(expression)
            embed = discord.Embed(
                title = 'OPERAÇÃO',
                description = "pai é cranio nelsin porra",
                color = 0x0000FF
            )     
            embed.set_author(name= bot.user.name)
            embed.add_field(name = "Resposta", value = resp, inline = False)
            msg = await ctx.send(embed=embed)
            await msg.add_reaction('👍')
            while 1:
                print(msg.reactions)
    except discord.ext.commands.errors.CommandNotFound:
        await ctx.send("caraio nelsin ta burro")

@bot.command()
async def recomendacao(ctx):
    tipo = ['Filme','Série']
    recomendacao = random.choice(recomendacoes)
    tipo_choice = random.choice(tipo)
    await ctx.send(f"Nelsin Recomenda :sunglasses: - {tipo_choice}: {recomendacao}")

@bot.command()
async def entrar(ctx):
    try:
        canal = ctx.author.voice.channel
        await canal.connect()
    except:
        await ctx.send('Já to dentro po kkkkk ta me fazendo de otario')

@bot.command()
async def sair(ctx):
    try:
        server = ctx.message.guild.voice_client
        await server.disconnect()
    except AttributeError:
        await ctx.send(f"Ta querendo tirar sem botar po kkkkk")


GRID = None

@bot.command()
async def campo(ctx,comando):
    if comando == 'start':
        grid = generate_grid()  
        GRID = grid
        for linha in grid:
            for elemento in linha:
                print(elemento, end = ' ')
            print()
        resposta = ''
        for i in range(len(player_grid)):
            for j in range(len(player_grid)):
                if player_grid[i][j] == DESCONHECIDO or player_grid[i][j]== BANDEIRA:
                    resposta+=(":asterisk:" + '   ')
                else:
                    resposta+=(str(player_grid[i][j]) + '   ')
            resposta+='\n\n'
        await ctx.send(resposta)
    elif comando[0:5] == 'click':
        click(int(comando[6]),int(comando[8]),grid,player_grid)
        resposta = ''
        for i in range(len(grid)):
            for j in range(len(grid)):
                if player_grid[i][j] == DESCONHECIDO or player_grid[i][j]== BANDEIRA:
                    resposta+=(":asterisk:" + '   ')
                else:
                    resposta+=(str(player_grid[i][j]) + '   ')
            resposta+='\n\n'
        await ctx.send(resposta)
        


@tasks.loop(seconds= 1)
async def current_time():
    now = datetime.datetime.now()
    now = now.strftime("%d/%m/%y às %H:%M:%S")
    channel = bot.get_channel(702789054244061197)
    if now[12] == '0' and now[13] == '2' and now[15] == '1' and now[16] == '1':
        await channel.send("HORA DE VAZAR :grimacing:")
    if now[12] == '0' and now[13] == '2' and now[15] == '1' and now[16] == '1' and now[18]== '5' and now[19] == '9':
        await channel.send("E que esteja avisado...")


bot.run("OTEzMTg1NTEyMTc5NzgxNjkz.YZ60SA.Y8KAB5gvQeSpuyVMU3kfrx9qgAA")
