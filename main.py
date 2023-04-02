from dotenv import load_dotenv
import discord, os
from discord.ext import commands
from translate import *

bot = discord.Bot()
load_dotenv('mytoken.env')

@bot.slash_command()
async def hello(ctx, name: str = None):
    name = name or ctx.author.name
    await ctx.respond(f"Hello {name}!")

@bot.slash_command()
async def help(ctx):
    embed = discord.Embed(
        title='About Me',
        description="This bot is a translator bot from English to Spanish and Spanish to English\n\n Use /listcoms for listing commands for bot.",
        colour=0xFF5733
    )
    embed.set_thumbnail(url='https://joshtronic.com/images/arch-linux-meme.jpg')
    await ctx.respond(embed=embed)

@bot.slash_command()
async def listcoms(ctx):
    embed = discord.Embed(
        title="The List of Commands",
        description='/hello -> this is a command that greets you or anybody else if you @ someone\n\n /translatees -> translates from English to Spanish\n /translateen -> translates from Spanish to English',
        colour=0x3498db
    )
    embed.set_thumbnail(url="http://www.clipartbest.com/cliparts/nTX/oM7/nTXoM7knc.jpeg")
    await ctx.respond(embed=embed)

@bot.slash_command()
async def translatees(ctx, text: str=None):
    text = text or ctx.author.name
    if text:
        text = argostranslate.translate.translate(text, from_code, to_code)
        embed = discord.Embed(
            title="English to Spanish",
            description=text,
            colour=0xFF5733
        )
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Bandera_de_Espa%C3%B1a.svg/1920px-Bandera_de_Espa%C3%B1a.svg.png")
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        await ctx.respond(embed=embed)

@bot.slash_command()
async def translateen(ctx, texte: str=None):
    texte = texte or ctx.author.name
    if texte:
        from_code = 'es'
        to_code = 'en' 

        texte = argostranslate.translate.translate(texte, from_code, to_code)
        embed = discord.Embed(
            title="El español al inglés",
            description=texte,
            colour=0xe74c3c
        )
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/en/thumb/b/be/Flag_of_England.svg/1920px-Flag_of_England.svg.png")
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        await ctx.respond(embed=embed)

def yepToken():
    bot.run(os.getenv('TOKEN'))
yepToken()