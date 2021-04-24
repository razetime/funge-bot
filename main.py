# import discord
import os
from discord.ext import commands
from keep_alive import keep_alive

bot = commands.bot(command_prefix = '%')

# client =  discord.Client()

@bot.event
async def on_ready():
  print("Logged in as {0.user}".format(client))

@bot.command(name='play', help='Starts a game with another person.')
async def play(ctx):
  await ctx.send("Starting game..")

@bot.command(name='move', help='places char at the given coordinates(0-indexed).')
async def move(ctx,char,x:int,y:int):
  await ctx.send("Doing move")

@bot.command(name='execute', help='executes the board and determines the result.')
async def execute(ctx):
  await ctx.send("Executing")



@bot.command(name='help')
async def help(ctx):
  await ctx.send("""Full list of rules and commands:
https://github.com/razetime/funge-bot/blob/main/README.md""")
# @client.event
# async def on_message(message):
#   if message.author == client.user:
#     return
#   if message.content.startswith("$hello"):
#     await message.channel.send("Hello!")




keep_alive()
bot.run(os.environ['TOKEN'])