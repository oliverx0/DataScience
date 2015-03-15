
import urllib
import re

corpora={'eng_us_2012':17, 'eng_us_2009':5, 'eng_gb_2012':18, 'eng_gb_2009':6, 
	'chi_sim_2012':23, 'chi_sim_2009':11,'eng_2012':15, 'eng_2009':0,
	'eng_fiction_2012':16, 'eng_fiction_2009':4, 'eng_1m_2009':1, 'fre_2012':19, 'fre_2009':7, 
	'ger_2012':20, 'ger_2009':8, 'heb_2012':24, 'heb_2009':9, 
	'spa_2012':21, 'spa_2009':10, 'rus_2012':25, 'rus_2009':12, 'ita_2012':22}

def getNgrams(query, corpus, startYear, endYear, smoothing):
	urlquery = urllib.quote_plus(query, safe='"')
	corpusNumber=corpora[corpus]
	url = 'http://books.google.com/ngrams/graph?content=%s&year_start=%d&year_end=%d&corpus=%d&smoothing=%d&share='%(urlquery,startYear,endYear,corpusNumber,smoothing)
	response = urllib.urlopen( url ).read()
	
	res=re.findall("data.addColumn(.*?);", response)
	# terms=[r[:-1].split(',')[1].replace("'","").strip() for r in res]
		
	# res = re.findall("data.addRows(.*?);", response.replace('\n',''))
	# data = [[float(c) for c in r[1:-1].split(',')] for r in re.findall("\[.*?\]", res[0][1:].strip()[1:-1:])]
	return res
	# return url, urlquery, [terms]+data

print getNgrams("hello",'eng_us_2012', 1800, 1802, 3)