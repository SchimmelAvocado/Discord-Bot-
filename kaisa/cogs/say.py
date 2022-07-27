from http import client
import discord
from discord.ext import commands

class Say(commands.Cog):


    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print('.say command loaded')


    @commands.command()
    async def say (self, ctx, *args):
        await ctx.send(f'{" ".join(args)}')


def setup(client):
    client.add_cog(Say(client))