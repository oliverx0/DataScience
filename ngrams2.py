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

# print ngrams
#Open file relating to that letter
for letter in ngrams[1800]:
	print letter
	with open(letter, 'r') as outfile:
		for line in outfile:
			try:
				line = line.split("\t")
				year = int(line[1])
				letter = line[0][0]
				word = line[0]
				count = int(line[2])
				if year >= 1800:
					if letter in ngrams[year]:
						if word in ngrams[year][letter]:
							ngrams[year][letter][word] += count
			except Exception, e:
				print "Error: "+str(e)


j = json.dumps(ngrams, indent=4)
f = open('results.json', 'w')
print >> f, j
# lines = [line.strip().lower() for line in open(letter)]
# for line in lines:
# 	print line