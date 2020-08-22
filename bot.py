import discord, jishaku, os
from discord.ext import commands

bot = commands.Bot(command_prefix="g!")
bot.remove_command("help")
bot.load_extension("jishaku")

@bot.event
async def on_ready():
    print("yes online now")

bot.run(str(os.environ.get("TOKEN")))
