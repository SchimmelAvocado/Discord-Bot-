from http import client
import discord
from discord.ext import commands

class Joe(commands.Cog):


    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print('.joe command loaded')


    @commands.command()
    async def joe (self, ctx):
        await ctx.send(f'mama')


def setup(client):
    client.add_cog(Joe(client))