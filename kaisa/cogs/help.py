import datetime
from http import client
import discord
from discord.ext import commands
import pytz

class Hilfe(commands.Cog):


    @commands.Cog.listener()
    async def on_ready(self):
        print('.help command loaded')


    @commands.command()
    async def man (self, ctx):
        de = pytz.timezone('Europe/Berlin')
        embed = discord.Embed(title=f'> **Basic Commands**',
                            description=f'.userinfo *[@user]*\n'
                                        f'.say *[Inhalt]*\n'
                                        f'.joe\n',
                            color=0x8854d0,
                            timestamp=datetime.datetime.now().astimezone(tz=de))

        embed2 = discord.Embed(title=f'> **Music Commands**',
                            description=f'.join\n'
                                        f'.play *[YT-URL]*\n'
                                        f'.pause\n'
                                        f'.resume\n'
                                        f'.disconnect\n',
                            color=0x8854d0,
                            timestamp=datetime.datetime.now().astimezone(tz=de))

        await ctx.send(embed=embed)
        await ctx.send(embed=embed2)


def setup(client):
    client.add_cog(Hilfe(client))