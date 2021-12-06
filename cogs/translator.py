from googletrans import Translator
import discord
from discord.ext import commands

translator = Translator()


class Translator(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("bot is on")

    @commands.command()
    async def trans(self, ctx, dest_lang=None):
        message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        if dest_lang is None:
            await ctx.reply(translator.translate(message.content).text)

        await ctx.reply(translator.translate(message.content, dest=dest_lang[1:]).text)


def setup(client):
    client.add_cog(Translator(client))
