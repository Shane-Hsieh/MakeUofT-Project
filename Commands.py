import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')  # Converts requests.text into HTML
links = soup.select('.storylink')
subtext = soup.select('.subtext')

def ranker(hnlist):
    return sorted(hnlist, key = lambda k:k['Votes'], reverse= True)


def tophn(links, subtext) -> object:
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        votes = subtext[idx].select('.score')
        if len(votes):
            points = int(votes[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'Title': title, 'Link': href, 'Votes': points})  # Creating a list of the title + link + votes 
    return ranker(hn)
    
def tophn_wrapper(articles):
    for day in range (1,5):
        return "Title: " + tophn(links, subtext)[day]['Title'] + "\nLink: " + tophn(links, subtext)[day]['Link'] + "\nVotes: "\
           + str(tophn(links, subtext)[day]['Votes'])

import discord

from discord.ext import commands

client = commands.Bot(command_prefix = "!")

@client.command()
async def ping(ctx):
	await ctx.send(f'{round(client.latency * 1000)} ms')

@client.command()
async def jerome(ctx):
	await ctx.send('my bad OG 😩')

@client.command()
async def hackerNews(ctx):
	await ctx.send(f'Articles over 100 votes will be presented.')
	await ctx.send(tophn_wrapper(0))

client.run('ODEwMjI3NDk1NTA4NzcwODg2.YCglKA.rJAJwMH1Pkr1NCrbo8JXHdBt6I0')