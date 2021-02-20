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
            if points > 900:
                hn.append({'Title': title, 'Link': href, 'Votes': points})  # Creating a list of the title + link + votes 
    return ranker(hn)

import discord
client = discord.Client()

#commands
@client.event
async def on_ready():
    general_channel = client.get_channel(123456789) #put client ID here
    await general_channel.send(tophn(links, subtext))

client.run('token') #put discord bot token here