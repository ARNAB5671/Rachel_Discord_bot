import discord
from discord.ext import commands

class Greetings(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.command()
    async def hello(self,ctx):
        await ctx.send(f"Hello my pooku wooku {ctx.author.name}")
    @commands.Cog.listener()
    async def on_message(self,message:discord.Message):
        await message.add_reaction("🤤")
        
async def setup(bot):
    await bot.add_cog(Greetings(bot))
    
    # @commands.Cog.listener()
    # async def on_message(self, message: discord.Message):
    #     await message.add_reaction("✅")
    
    