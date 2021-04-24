# import discord
import discord
import os
import random
from discord.ext import commands
from keep_alive import keep_alive

# Constants
cmds = list("><^v?#_|" + "+-*%/" + "\\.@" + "0123456789")

bot = commands.Bot(command_prefix = '%')
p1 = ""
p2 = ""
turn = ""
pieces = ""
gameOver = True
board = []

def grid():
  return "```\n"+"\n".join(["".join(i) for i in board])+ "\n```"


@bot.command(name='play', help='Starts a game with another person, given board size.')
async def play(ctx,pl1:discord.Member,pl2:discord.Member,w:int,h:int):
  global p1
  global p2
  global turn
  global gameOver
  global pieces
  if(w<1 or h<1 or  w>10 or h>10):
    await ctx.send("Invalid dimensions/Dimensions too high.")
  elif(gameOver): # Start the game
    global board
    board = [['.' for i in range(w)] for i in range(h)]
    gameOver = False
    count = 0
    p1 = pl1 # Player A
    p2 = pl2 # Player B

    # Assign player positions
    board[random.randint(1,h-1)][random.randint(0,w-1)] = 'A'
    Bx,By=random.randint(0,w-1),random.randint(1,h-1)
    while(board[By][Bx]=='A'):
      Bx,By=random.randint(0,w-1),random.randint(1,h-1)
    board[By][Bx] = 'B'

    await ctx.send("Starting Board: \n" + grid()) 
    if(random.randint(0,1)):
      turn = p1
    else:
      turn = p2
    pieces = random.sample(cmds,k=4)
    await ctx.send("<@" + str(turn.id) + ">'s turn") 
    await ctx.send("Pieces: `"+",".join(pieces)+"`")
  else:
    await ctx.send("A game is in progress. Please wait.")


@bot.command(name='move', help='places char at the given coordinates.')
async def move(ctx,char,x:int,y:int):
  global p1
  global p2
  global turn
  global board
  global gameOver
  global pieces
  if gameOver:
    await ctx.send("There is no game in progress. Type %play to start!")
  else:
    if turn == ctx.author:
      if(abs(y)<len(board) and abs(x)<len(board[0]) and char in pieces):
        board[y][x] == char
        await ctx.send("Current Board:\n"+grid())
      else:
        await ctx.send("Invalid move. Try again.")
    else:
      await ctx.send("Sorry, it is not your turn.")

@bot.command(name='execute', help='executes the board and determines the result. Ends the game as well.')
async def execute(ctx):
  await ctx.send("Executing")

@bot.command(name='end', help='ends the game without deciding a result.')
def endGame(ctx):
  if(gameOver):
    await ctx.send("There is no game to end.")
  else:
    gameOver = True
    await ctx.send("Game ended.")





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