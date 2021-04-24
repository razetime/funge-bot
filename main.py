# import discord
import discord
import os
import random
from discord.ext import commands
from keep_alive import keep_alive

# Constants
commands = "><^v?_|" + "+-*%/" + "\\.@" + "0123456789"

bot = commands.Bot(command_prefix = '%')
p1 = ""
p2 = ""
turn = ""
gameOver = True
board = []

# client =  discord.Client()

# @bot.event
# async def on_ready(ctx):
#   print("Logged in as {0.user}".format(ctx))

@bot.command(name='play', help='Starts a game with another person, given board size.')
async def play(ctx,pl1:discord.Member,pl2:discord.Member,w:int,h:int):
  global p1
  global p2
  global turn
  global gameOver
  if(w>10 or h>10):
    await ctx.send("Dimensions above 10x10 are not allowed.")
  elif(gameOver): # Start the game
    global board
    board = [['.' for i in range(w)] for i in range(h)]
    gameOver = False
    count = 0
    p1 = pl1
    p2 = pl2
    await ctx.send("Start Board: \n"+"\n".join(["".join(i) for i in board])) 
    if(random.randint(0,1)):
      turn = p1
    else:
      turn = p2
    await ctx.send("@<" + str(turn.id)+ ">'s turn'") 
  else:
    await ctx.send("A game is in progress. Please wait.")


@bot.command(name='move', help='places char at the given coordinates(0-indexed).')
async def move(ctx,char,x:int,y:int):
  await ctx.send("Doing move")

@bot.command(name='execute', help='executes the board and determines the result.')
async def execute(ctx):
  await ctx.send("Executing")



# @bot.command(name='help')
# async def help(ctx):
#   await ctx.send("""Full list of rules and commands:
# https://github.com/razetime/funge-bot/blob/main/README.md""")
# # @client.event
# # async def on_message(message):
# #   if message.author == client.user:
# #     return
# #   if message.content.startswith("$hello"):
# #     await message.channel.send("Hello!")




keep_alive()
bot.run(os.environ['TOKEN'])