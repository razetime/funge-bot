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


@bot.command(name='play', help='[player1 player2 width height]: Starts a game with another person, given board size.')
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
    await ctx.send("<@" + str(p1.id) + "> -> A")
    await ctx.send("<@" + str(p2.id) + "> -> B")
    await ctx.send("<@" + str(turn.id) + ">'s turn") 
    await ctx.send("Pieces: `"+",".join(pieces)+"`")
  else:
    await ctx.send("A game is in progress. Please wait.")


@bot.command(name='move', help='[char x y]: places char at the given coordinates.')
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
      if(abs(y)<len(board) and abs(x)<len(board[0]) and char in pieces and board[y][x] == '.'):
        board[y][x] = char
        await ctx.send("Current Board:\n"+grid())
        pieces = random.sample(cmds,k=4)
        if(turn == p1):
          turn = p2
        else:
          turn = p1
        await ctx.send("<@" + str(turn.id) + ">'s turn")
        await ctx.send("Pieces: `"+",".join(pieces)+"`")
      else:
        await ctx.send("Invalid move. Try again.")
    else:
      await ctx.send("Sorry, it is not your turn.")

@bot.command(name='execute', help='executes the board and determines the result. Ends the game as well.')
async def execute(ctx):
  global board
  global gameOver
  if(gameOver):
    ctx.send("There is no running board to execute.")
    return
  if turn == ctx.author:
    r,c=0,0
    dr,dc=0,1
    stack = []
    curr = board[r][c]
    route = []
    stringMode = False
    string = ""
    while(1):
      curr = board[r][c]
      if([r,c] in route):
        ctx.send("Tie")
        gameOver = True
        return
      elif(curr == 'A'):
        ctx.send("<@" +str(p1.id) + "> wins")
        gameOver = True
        return
      elif(curr == 'B'):
        ctx.send("<@" +str(p2.id) + "> wins")
        gameOver = True
        return
      elif(stringMode and curr != '"'):
        string += curr
      elif(curr == '>'):
        dr,dc = 0,1
      elif(curr == '<'):
        dr,dc = 0,-1
      elif(curr == '^'):
        dr,dc = -1,0
      elif(curr == 'v'):
        dr,dc = 1,0
      elif(curr in '0123456789'):
        stack.append(int(curr))
      elif(curr in '+-%/*'):
        stack.append(eval(str(stack.pop()) + curr + str(stack.pop())))
      elif(curr == '?'):
        dr = random.randint(-1,1)
        dc = random.randint(-1,1)
      elif(curr == '#'):
        r += dr
        c += dc
      elif(curr == '"'):
        stringMode = not stringMode
        string = ""
      elif(curr == '@'):
        r += 2*dr
        c += 2*dc
      elif(curr == '|'):
        if(stack.pop()):
          dr = -1
          dc = 0
        else:
          dr = 1
          dc = 0
      elif(curr == '_'):
        if(stack.pop()):
          dr = 0
          dc = -1
        else:
          dr = 0
          dc = 1
      else:
        pass
      route.append([r,c])
      r += dr
      c += dc
      r = r % len(board[0])
      c = c % len(board)
  else:
    await ctx.send("You can execute the board on your turn.")

@bot.command(name='end', help='ends the game without deciding a result.')
async def endGame(ctx):
  global gameOver
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