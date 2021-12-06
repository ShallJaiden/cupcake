from discord.ext import commands
import discord
import wikipedia
import asyncio


class Wiki(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("bot is on")

    @commands.command()
    async def wiki(self, ctx, *, value=None):
        global search, msg
        first_run = True
        if value is None:
            await ctx.reply("what do you want to look up?")
        else:
            while True:
                if first_run:
                    embed = discord.Embed(title="Wikipedia", url="https://wikipedia.org/",
                                          description="Here's the result you are looking for. Choose the desired one "
                                                      "by "
                                                      "reacting the number",
                                          color=discord.colour.Colour.blue())
                    first_run = False
                    search = wikipedia.search(value[1:], results=5)
                    print(search)
                    embed.add_field(name="1️⃣", value=search[0], inline=False)
                    embed.add_field(name="️2️⃣", value=search[1], inline=False)
                    embed.add_field(name="3️⃣", value=search[2], inline=False)
                    embed.add_field(name="4️⃣", value=search[3], inline=False)
                    embed.add_field(name="5️⃣", value=search[4], inline=False)
                    msg = await ctx.send(embed=embed)
                    await msg.add_reaction("1️⃣")
                    await msg.add_reaction("2️⃣")
                    await msg.add_reaction("3️⃣")
                    await msg.add_reaction("4️⃣")
                    await msg.add_reaction("5️⃣")

                def check_react(reaction, user_, react_emoji=None):
                    if react_emoji is None:
                        react_emoji = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"]
                    if reaction.message.id != msg.id:
                        return False
                    if user_ != ctx.message.author:
                        return False
                    if str(reaction.emoji) not in react_emoji:
                        return False
                    return True

                try:
                    res, user = await self.client.wait_for('reaction_add', check=check_react)
                except asyncio.TimeoutError:
                    return await msg.clear_reactions()

                if user != ctx.message.author:
                    pass
                elif '1️⃣' in str(res.emoji):
                    await msg.remove_reaction("1️⃣", user)
                    result = await ctx.send(wikipedia.page(search[0]).url)
                elif '2️⃣' in str(res.emoji):
                    await msg.remove_reaction("2️⃣", user)
                    await result.edit(content=wikipedia.page(search[1]).url)
                elif '3️⃣' in str(res.emoji):
                    await msg.remove_reaction("3️⃣", user)
                    await result.edit(content=wikipedia.page(search[2]).url)
                elif '4️⃣' in str(res.emoji):
                    await msg.remove_reaction("4️⃣", user)
                    await result.edit(content=wikipedia.page(search[3]).url)
                elif '5️⃣' in str(res.emoji):
                    await msg.remove_reaction("5️⃣", user)
                    await result.edit(content=wikipedia.page(search[4]).url)


def setup(client):
    client.add_cog(Wiki(client))
