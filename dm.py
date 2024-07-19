import settings
import discord
import random
from discord.ext import commands
from cogs.greetings import Greetings
logger=settings.logging.getLogger("bot")

async def is_owner(ctx):
    return ctx.author.id == ctx.guild.owner_id 

def run():
    intents=discord.Intents.default()
    intents.message_content=True
    intents.members=True
    bot = commands.Bot(command_prefix="!",intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f"User:{bot.user}(ID:{bot.user.id})")

    @bot.command()
    async def ping2(ctx):
        user=ctx.author
        try:
            await user.send("Hello bro")  # Send a DM to the user
        except discord.Forbidden:
            await ctx.send(f"Sorry, {user.name}, I can't send you a DM. Please check your privacy settings.")











    bot.run(settings.DISCORD_API_SECRET,root_logger=True)


    


if __name__=="__main__":
    run() 