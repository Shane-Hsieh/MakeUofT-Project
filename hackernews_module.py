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
        print ("Title: " + tophn(links, subtext)[day]['Title'] + "\nLink: " + tophn(links, subtext)[day]['Link'] + "\nVotes: "\
           + str(tophn(links, subtext)[day]['Votes']))

print(tophn_wrapper(0))
