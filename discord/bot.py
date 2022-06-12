import discord
from discord.ext import commands

client = commands.Bot( command_prefix= "=") 
client.run('')



@client.event
class MyClient(discord.Client):
    async def on_ready(self):
        print('Залогинился как {0}!'.format(self.user))
@client.command( pass_context = True)

async def help( ctx ):
    await ctx.send("Im only log bot, im dont have activities")


#Made by MarselHapa5|Сделано MarselHapa5