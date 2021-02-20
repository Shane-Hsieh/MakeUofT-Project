import hackernews_module
import discord
client = discord.Client()

#commands
@client.event
async def on_ready():
    general_channel = client.get_channel(812458238133534820) #put client ID here
    await general_channel.send(hackernews_module.tophn_wrapper())

client.run('ODEwMjI3NDk1NTA4NzcwODg2.YCglKA.dRa9jEQ3zUWVUOTvwBzuxafxpKE') #put discord bot token here