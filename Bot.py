import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='PCMB ', description='Bot that loves the PCMR. <3\nCreated by BLUENINJA')

@bot.event
async def on_ready():
    print("Sup world, it's the bot!")
    print(bot.user.name)

@bot.command()
async def info():
    await bot.say('Creator: BLUENINJA\nPurpose: Spread the Master Race to the masses.\n-----Commands-----\nHelp - This\nWhy - Explains the PCMR\nGoodbot - Self Explanatory')

@bot.command()
async def why():
    await bot.say('https://www.reddit.com/r/pcmasterrace/wiki/guide')

@bot.command()
async def goodbot():
    await bot.say('Thanks! You too')

@bot.command()
async def hey():
    await bot.say("Sup world, it's the bot!")

@bot.event
async def on_message(message):
	if str(message) == 'Hello':
		await bot.say("Sup.")
	else:
		await bot.say(str(message))
		
	
bot.run('NDIwODA1MzI0MTk5NjkwMjQx.DYEEQg.-NpWX2CKLA7i6Z_osEv-5UmhB8I')