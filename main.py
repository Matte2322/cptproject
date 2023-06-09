from dotenv import load_dotenv
import discord, os
from discord.ext import commands
from discord.commands import Option
from translate import *

bot = discord.Bot()
load_dotenv('mytoken.env')

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(description='Tests the bot\'s latency')
async def ping(ctx):
    await ctx.respond('The ping rn: {0} ms'. format((bot.latency)))

@bot.slash_command(description='Waves hello :)')
async def hello(ctx, name: str = None):
    name = name or ctx.author.name
    await ctx.respond(f"Hello {name}!")

@bot.slash_command(description='says something')
async def dosomething(ctx, typesomethingout: Option(str, "Type something here and the bot will output")):
    typesomethingout = typesomethingout or ctx.author.name
    if typesomethingout:
        await ctx.respond(typesomethingout)

@bot.slash_command(description='Tells you the "about me" for the bot')
async def help(ctx):
    embed = discord.Embed(
        title='About Me',
        description="This bot is a translator bot from English to Spanish and Spanish to English\n\n Use /listcoms for listing commands for bot.",
        colour=0xFF5733
    )
    embed.set_thumbnail(url='https://joshtronic.com/images/arch-linux-meme.jpg')
    await ctx.respond(embed=embed)

@bot.slash_command(description='Lists all commands')
async def listcoms(ctx):
    embed = discord.Embed(
        title="The List of Commands",
        description='/ping -> tests the bot\'s ping \n /dosomething -> outputs something out if you input something \n /hello -> this is a command that greets you or anybody else if you @ someone\n\n /translatees -> translates from English to Spanish\n /translateen -> translates from Spanish to English',
        colour=0x3498db
    )
    embed.set_thumbnail(url="http://www.clipartbest.com/cliparts/nTX/oM7/nTXoM7knc.jpeg")
    await ctx.respond(embed=embed)

@bot.slash_command(description="Translates from Spanish to English (Se traduce del español al inglés)")
async def translateen(ctx, texte: Option(str, "Type something in Spanish")):
    texte = texte or ctx.author.name
    if texte:
        texte = argostranslate.translate.translate(texte, from_code, to_code)
        embed = discord.Embed(
            title="El español al inglés",
            description=texte,
            colour=0x992d22
        )
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/en/thumb/b/be/Flag_of_England.svg/1920px-Flag_of_England.svg.png")
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        await ctx.respond(embed=embed)


@bot.slash_command(description='Translates from English to Spanish (Se traduce del inglés al español)')
async def translatees(ctx, text: Option(str, "Type something in English")):
    text = text or ctx.author.name
    if text:
        from_code = 'en'
        to_code = 'es' 

        text = argostranslate.translate.translate(text, from_code, to_code)
        embed = discord.Embed(
            title="English to Spanish",
            description=text,
            colour=0xf1c40f
        )
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Bandera_de_Espa%C3%B1a.svg/1920px-Bandera_de_Espa%C3%B1a.svg.png")
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        await ctx.respond(embed=embed)

def yepToken():
    bot.run(os.getenv('TOKEN'))
yepToken()