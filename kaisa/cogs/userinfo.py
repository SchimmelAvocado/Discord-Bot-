import datetime
from http import client
import discord
from discord.ext import commands
import pytz

class Userinfo(commands.Cog):


    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print('.userinfo command loaded')


    @commands.command()
    async def userinfo(self, ctx, member: discord.Member):
        de=pytz.timezone('Europe/Berlin')
        embed = discord.Embed(title=f'> Userinfo für {member.display_name}',
                                description='',
                                color=0x8854d0,
                                timestamp=datetime.datetime.now().astimezone(tz=de))

        embed.add_field(name='Name', value=f'```{member.name}#{member.discriminator}```', inline=True)
        embed.add_field(name='Bot', value=f'```{("Ja" if member.bot else "Nein")}```', inline=True)
        embed.add_field(name='Nickname', value=f'```{(member.nick if member.nick else "kein Nickname")}```',inline=True)

        embed.add_field(name='Server beigetreten', value=f'```{member.joined_at}```',inline=True)
        embed.add_field(name='Account erstellt',value=f'```{member.created_at}```',inline=True)
        embed.add_field(name='Rollen',value=f'```{len(member.roles)}```',inline=True)

        embed.add_field(name='Höchste Rolle', value=f'```{member.top_role.name}```',inline=True)
        embed.add_field(name='Farbe', value=f'```{member.color}```',inline=True)
        embed.add_field(name='Boostet Server', value=f'```{("Ja" if member.premium_since else "Nein")}```', inline=True)

        embed.set_footer(text=f'Angefordert von {ctx.author.name} * {ctx.author.id}')
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Userinfo(client))