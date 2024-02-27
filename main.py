import discord
from discord.ext import commands

from colorama import Back, Fore, Style
import time
import platform

GunmaxDex = commands.Bot(command_prefix="#", intents=discord.Intents.all())

@GunmaxDex.event
async def on_ready():
  prfx = (Back.BLACK + Fore.GREEN +
          time.strftime("%H:%M:%S UTC", time.gmtime()) + Back.RESET +
          Fore.WHITE + Style.BRIGHT)
  print(prfx + " Logged in as " + Fore.YELLOW + GunmaxDex.user.name)
  print(prfx + " Bot ID " + Fore.YELLOW + str(GunmaxDex.user.id))
  print(prfx + " Discord Version " + Fore.YELLOW + discord.__version__)
  print(prfx + " Python Version " + Fore.YELLOW +
        str(platform.python_version()))


@GunmaxDex.command()
async def hello(ctx):
  await ctx.send("Hello!")


GunmaxDex.run("MTE3MjYxNDgwOTcxMjMzMjgwMQ.GjE628.vRWn81L5yylVnz0mjDHgNPWjbM3iZ8Ca7jOj-s")


