from bs4 import BeautifulSoup as bs
import requests
from players.models import match , Squad

def squad_name():
    sq = []
    lin = []
    url = 'https://www.espncricinfo.com/series/big-bash-league-2021-22-1269637/squads'
    req = requests.get(url,headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
            })
    soup = bs(req.content,'html.parser')
    title = soup.find_all('div',class_ = 'squad-row d-flex justify-content-md-between py-2 align-content-center flex-wrap')
    for i in title:
        squad = i.find('a',class_='black-link d-none d-md-inline-block pl-2')
        # lin.append(squad['href'])
        sq.append(squad.text)
        a = squad.text.split(' ')
        st = a[0][0] + a[1][0]
        lin.append(st)
        print("squad name : ",squad.text)   
    return sq

def match_results():
    team = {}
    url = 'https://www.espncricinfo.com/series/big-bash-league-2021-22-1269637/squads'
    req = requests.get(url,headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
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
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
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


def value_stored():
    match.objects.all().delete()
    Squad.objects.all().delete()
    # print('deleted')
    teams = match_results()
    
        # m = 2*i 
        # n = i+1
        # match.objects.create(match_id = l[0][i],team1 = l[1][m] , team2 = l[1][n])
        # print('object created!!')
    # k=0
    # for i in squad_name():
    #     Squad.objects.create(name = i)
    #     for j in l[1]:
    #         Squad.objects.create(name = j)
    #         k=j
    #     # print('squad created!!')

    
    for i in teams.keys():
        Squad.objects.create(name = "----------")
        Squad.objects.create(name = i)
        Squad.objects.create(name = "----------")
        print(i)
        for k in teams[i]:
            print(k)
            Squad.objects.create(name=k)
            # print('match created!!')
