from google_ngram_downloader import readline_google_store
import json

def read_ngrams_file(filename):
	ngrams = {}
	lines = [line.strip().lower() for line in open(filename)]
	for year in range(1800, 2009):
		if year not in ngrams:
			ngrams[year] = {}
			for word in lines:
				letter = word[0]
				if letter not in ngrams[year]:
					ngrams[year][letter] = {}
				ngrams[year][letter][word] = 0

	return ngrams

ngrams = read_ngrams_file("ngrams.txt")



for letter in ngrams[1800]:
	for a in range(1,3):
		try:
			fname, url, records = next(readline_google_store(ngram_len=a,indices=letter))
			for rec in records:
				letter2 = rec[0][0]
				word = rec[0]
				year = rec[1]
				count = rec[2]
				if year >= 1800:
					if letter2.lower() in ngrams[year]:
						if word.lower() in ngrams[year][letter2.lower()]:
							ngrams[year][letter2.lower()][word.lower()] += count
		except Exception, e:
			print "Error: "+str(e)
			print "Letter: "+letter
			print "Len: "+str(a)

j = json.dumps(ngrams, indent=4)
f = open('results.json', 'w')
print >> f, j
# print ngrams
# for x in range(0,20005):
#     rec = next(records)
#     print rec