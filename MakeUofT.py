import hackernews_module
import discord
client = discord.Client()

#commands
@client.event
async def on_ready():
    general_channel = client.get_channel(812470218106470453) #put client ID here
    await general_channel.send(hackernews_module.tophn_wrapper(0))

client.run('ODEwMjI3NDk1NTA4NzcwODg2.YCglKA.rJAJwMH1Pkr1NCrbo8JXHdBt6I0') #put discord bot token here