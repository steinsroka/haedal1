
#import bs4
#import requests

#headers = {
#    'User-Agent': 'Not_Crawling X)'
#}

#response = requests.get('https://trends.google.co.kr/trends/trendingsearches/daily?geo=KR', headers=headers).text
#soup = bs4.BeautifulSoup(response, 'html.parser')

#datas = soup.select('div.feed-list-wrapper > div.feed-item')
#date = soup.select_one('div.feed-list-wrapper > div.content-header > div.content-header-title')
#with open('google_rank.csv', 'w') as f:

#    f.write(f'')
#    for data in datas:
#        rank = data.select_one('div.feed-item-header > div.index.large-font').text
#        kword = data.select_one('div.feed-item-header > div.details > div.title.title-break > s.titlePart.in.titleArray > s').text
#        f.write(f'{rank},{kword}\n')

import bs4
import requests
import csv

headers ={
    'User-Agent': 'Not_Crawling X'
}

response = requests.get('https://kin.naver.com/',headers=headers).text
soup = bs4.BeautifulSoup(response, 'html.parser')
ranks = soup.select('#rankingChart > ul > li')

ranking = lambda rank: int(rank.select_one('span.no').text)
content = lambda rank: rank.select_one('a.ranking_title').text

with open('kin_rank.csv','w') as ff:
    writer = csv.writer(ff)
    for rank in sorted(ranks, key=ranking):
       ranks = ranking(rank)
       contents = content(rank)
       writer.writerow([f'{ranks}위', contents])
