import json
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

import numpy as np
from numpy.random import randn


def change_scale(current_val, current_min, current_max, final_min, final_max):
    return (((final_max-final_min)*(current_val-current_min))/(current_max-current_min))+final_min;

def byteify(input):
    if isinstance(input, dict):
        return {byteify(key):byteify(value) for key,value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input


json1_file = open('results.json')
json1_str = json1_file.read()
json1_data = json.loads(json1_str)
json1_data = byteify(json1_data)

init_year = 1800
final_year = 2009

years = []
years_total = {}
year_min = []
year_max = []
words = {}
for i in range(init_year, final_year):
	letters = json1_data[str(i)]
	years.append(i)
	min_val = 99999999999
	max_val = 0
	for letter in letters:
		for word in letters[letter]:
			count = letters[letter][word]
			if word not in words:
				words[word] = []
			if word not in years_total:
				years_total[word] = count
			else:
				years_total[word] += count
			
			words[word].append(count)
			
			if count > max_val:
				max_val = count
			if count < min_val:
				min_val = count
	year_max.append(max_val)
	year_min.append(min_val)

# Change to show distribution
print years_total

counter = 0
for i in range(init_year, final_year):
	for word in words:
		if years_total[word] > 0:
			words[word][counter] = float(words[word][counter])/float(years_total[word])
		else:
			words[word][counter] = float(words[word][counter])
	print words[word]
	counter+= 1

#Change to normalize from 0 to 1

# counter = 0
# for i in range(init_year, final_year):
# 	for word in words:
# 		words[word][counter] = change_scale(float(words[word][counter]), float(year_min[counter]), float(year_max[counter]), 0.0, 1.0)
# 	counter+= 1

sns.set_palette("deep", desat=.6)
sns.set_context(rc={"figure.figsize": (8, 4)})

years = np.array(years)
letters = json1_data[str(1800)]
counter = 0
for letter in letters:
	for word in words:
		if word[0] == letter:
			word_count = np.array(words[word])
			plt.plot(years,word_count, label=word)
			

			counter += 1
			if counter > 6:
				plt.ticklabel_format(axis='x', useOffset=False)
				plt.xlim(init_year, final_year)
				lgd = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
				# plt.show()
				plt.savefig("figures/distribution"+word,bbox_extra_artists=(lgd,), bbox_inches='tight')
				counter = 0
				plt.clf()
				# for j in range(1,count):
				# 	data[i].append(word)



# print data[2000]
			


