import settings
import discord
import random
from discord.ext import commands
from cogs.greetings import Greetings
logger=settings.logging.getLogger("bot")



def run():
    intents=discord.Intents.default()
    intents.message_content=True
    bot = commands.Bot(command_prefix="!",intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f"User:{bot.user}(ID:{bot.user.id})")

        await bot.tree.sync()



    @bot.hybrid_command()
    async def ping(ctx):
        await ctx.send("wann is my pooku wooku")
    
    @bot.tree.command()
    async def ciao(interaction:discord.Interaction):
        await interaction.response.send_message(f"wann is {interaction.user.mention}'s pooku wooku",ephemeral=False)


    






    bot.run(settings.DISCORD_API_SECRET,root_logger=True)


    


if __name__=="__main__":
    run()