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
    bot = commands.Bot(command_prefix="!",intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f"User:{bot.user}(ID:{bot.user.id})")
        for cog_file in settings.COGS_DIR.glob("*.py"):
            if cog_file!="__init.py__":
                await bot.load_extension(f"cogs.{cog_file.name[:-3]}")

    @bot.command()
    async def load (ctx,cog:str):
        await bot.load_extension(f"cogs.{cog.lower()}")
    @bot.command()
    async def unload (ctx,cog:str):
        await bot.unload_extension(f"cogs.{cog.lower()}")
    @bot.command()
    async def reload(ctx,cog:str):
        await bot.reload_extension(f"cogs.{cog.lower()}")
        

    

    @bot.command()
    @commands.check(is_owner)
    async def ping(ctx):
        await ctx.send("wann is my pooku wooku")

    @ping.error
    async def say_error(ctx,error):
        if isinstance(error,commands.CommandError):
            await ctx.send("Permission Denied")

    @bot.command()
    async def say(ctx,*what):
        await ctx.send(" ".join(what))
    

    @bot.command()
    async def choose(ctx,*options):
        await ctx.send(random.choice(options))











    bot.run(settings.DISCORD_API_SECRET,root_logger=True)


    


if __name__=="__main__":
    run()