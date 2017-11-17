import discord
from discord.ext import commands
from discord.voice_client import VoiceClient

startup_extensions = ["Music"]
bot = commands.Bot(".")

@bot.event
async def on_ready():
    print("I am the Demon Archer Nobunaga, the Demon King of the Sixth Heaven!!")
    print("Very well... I shall offer you my assistance!")

class mainCommands():
    def __init__(self, bot):
        self.bot = bot

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("Washija!!")

@bot.command(pass_context=True)
async def hello(ctx):
    await bot.say("ＷＡＳＨＩＪＡ！！！")
    await bot.say("I am the Demon Archer Nobunaga, the Demon King of the Sixth Heaven!!")
    await bot.say("Mmm, I am summoned by my Master SOTONAMI#9435 also known as Max.")

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
                exc = '{}: {}'.format(type(e).__name__,e)
                print('Failed to load extension {}\n{}'.format(extensions,exc))

bot.run("MzgwOTE3OTQ3Mjc2ODUzMjQ5.DO_lFw.ZEseiW2ehAA61t3VZU-0arOm5W8")
