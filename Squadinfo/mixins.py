from bs4 import BeautifulSoup as bs
import requests
from players.models import match , Squad



def match_results(url):
    team = {}
    url = url+'/squads'
    req = requests.get(url,headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT x.y; Win64; x64; rv:10.0) Gecko/20100101 Firefox/10.0',
            })
    soup = bs(req.content,'html.parser')
    link = soup.find_all('a',class_ = 'black-link d-none d-md-inline-block pl-2')
    num = 0
    for i in link:
        players = []
        
        l = i['href'].split('/')
        code = l[3].split('-')[-1]
        # mat.append(code)
        url1 = 'https://www.espncricinfo.com'+i['href']
        req1 = requests.get(url1,headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT x.y; Win64; x64; rv:10.0) Gecko/20100101 Firefox/10.0',
            })
        soup1 = bs(req1.content,'html.parser')
        name = soup1.find_all('a',class_='h3 benton-bold name black-link d-inline')
        for j in name:
            players.append(j.text)
            # print(j.text)
        team[i.text] = players
        print(num, i.text)
        num += 1
    print(team)
    return team


def value_stored(url):
    match.objects.all().delete()
    Squad.objects.all().delete()
    teams = match_results(url)
    for i in teams.keys():
        Squad.objects.create(name = "----------")
        Squad.objects.create(name = i)
        Squad.objects.create(name = "----------")
        print(i)
        for k in teams[i]:
            print(k)
            Squad.objects.create(name=k)
