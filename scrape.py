from bs4 import BeautifulSoup
import urllib2
import pandas as pd
from tqdm import tqdm


pos = ['10','20','30','40','80','99']
for p in tqdm(pos):
	data =[]
	for w in range(1,18):
		x = 0
		while (x<=1):
			soup = BeautifulSoup(urllib2.urlopen('http://fftoday.com/stats/playerstats.php?Season=2015&GameWeek=' + str(w) + '&PosID=' + p + '&LeagueID=26955&order_by=FFPts&sort_order=DESC&cur_page=' + str(x)).read(),'html.parser')
			tableStats = soup.find('table', attrs={'cellpadding':'2'})
			for row in tableStats.findAll('tr')[2:]:
				col = row.findAll('td')
				row_data=[str(w)]
				for i in range(len(col)):
					if i == 0:
						row_data.append(col[i].a.string.strip())
					else:
						row_data.append(col[i].string.strip())
				data.append(row_data)
			x += 1
	if p == '10':
		df = pd.DataFrame(data,columns =['Week','Name','Team','Games','Pass Comp','Pass Att','Pass Yards','Pass TD','Pass INT','Rush Att','Rush Yards','Rush TD','Fantasy PTS','FanPPG'])
		df.to_csv('Fantasy Football/QB Data.csv',sep=",")
	elif p == '20':
		df = pd.DataFrame(data,columns =['Week','Name','Team','Games','Rush Att','Rush Yards','Rush TD','Rec Targets','Rec Comp','Rec Yards','Rec TD','Fantasy PTS','FanPPG'])
		df.to_csv('Fantasy Football/RB Data.csv',sep=",")
	elif p == '30':
		df = pd.DataFrame(data,columns =['Week','Name','Team','Games','Rec Targets','Rec Comp','Rec Yards','Rec TD','Rush Att','Rush Yards','Rush TD','Fantasy PTS','FanPPG'])
		df.to_csv('Fantasy Football/WR Data.csv',sep=",")
	elif p == '40':
		df = pd.DataFrame(data,columns =['Week','Name','Team','Games','Rec Targets','Rec Comp','Rec Yards','Rec TD','Fantasy PTS','FanPPG'])
		df.to_csv('Fantasy Football/TE Data.csv',sep=",")
	elif p == '80':
		df = pd.DataFrame(data,columns =['Week','Name','Team','Games','FGM','FGA','FG%','EPM','EPA','FanPPG','FanPPG'])
		df.to_csv('Fantasy Football/K Data.csv',sep=",")
	elif p == '99':
		df = pd.DataFrame(data,columns =['Week','Name','Games','Sack','FR','INT','DefTD','PA','PaYd/G','RuYd/G','Safety','KickTD','FanPPG','FanPPG'])
		df.to_csv('Fantasy Football/DEF Data.csv',sep=",")
	

			


