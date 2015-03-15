import csv
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

import numpy as np
from numpy.random import randn



def count_attacks(filename):
	keys = {}
	attacks_list = {}
	current_attack = None
	skipped = 0

	with open(filename, "rb") as f_obj:
		data = [row for row in csv.reader(f_obj.read().splitlines())]

		flag = False
		for row in data:
			if flag == True:
				try:
					attack_year = int(row[keys['iyear']])
					if int(row[keys['doubtterr']]) == 0:
						if attack_year not in attacks_list:
							attacks_list[attack_year] = 0

						else:
							attacks_list[attack_year] += 1
				except Exception, e:
					print e
					skipped += 1
			else:
				counter = 0
				for element in row:
					# print element
					keys[element] = counter
					counter += 1
				flag = True
	print "skipped: "+str(skipped)
	return attacks_list

def count_major_attacks(filename):
	keys = {}
	attacks_list = {}
	current_attack = None
	skipped = 0
	attacks_description = {}
	with open(filename, "rb") as f_obj:
		data = [row for row in csv.reader(f_obj.read().splitlines())]

		flag = False
		for row in data:
			if flag == True:

				try:
					attack_year = int(row[keys['iyear']])
					if int(row[keys['doubtterr']]) == 0:
						if attack_year not in attacks_list:
							attacks_list[attack_year] = {}
							kills = 0
							wounds = 0
							try:
								kills = float(row[keys['nkill']])
							except:
								pass
							try:
								wounds = float(row[keys['nwound']])
							except:
								pass

							attacks_list[attack_year]['impact'] = kills + wounds
							attacks_list[attack_year]['summary'] = row[keys['summary']]
							attacks_list[attack_year]['country'] = row[keys['country_txt']]


						else:
							kills = 0
							wounds = 0
							try:
								kills = float(row[keys['nkill']])
							except:
								pass
							try:
								wounds = float(row[keys['nwound']])
							except:
								pass
							if attacks_list[attack_year]['impact'] < (kills + wounds):
								attacks_list[attack_year]['impact'] = kills + wounds
								attacks_list[attack_year]['summary'] = row[keys['summary']]
								attacks_list[attack_year]['country'] = row[keys['country_txt']]
				
				except Exception, e:
					# print e
					print row[keys['nkill']] +" "+row[keys['nwound']]
					skipped += 1
			else:
				counter = 0
				for element in row:
					keys[element] = counter
					counter += 1
				flag = True

	print "skipped: "+str(skipped)
	return attacks_list

def draw_distribution(dictionary, title, x_label, y_label):
	sns.set_palette("deep", desat=.6)
	sns.set_context(rc={"figure.figsize": (8, 4)})

	x = [d for d in dictionary]
	x.sort()
	y = []
	for d in x:
		if dictionary[d]['impact'] > 600:
			y.append(dictionary[d]['impact'])
		else:
			y.append(0)
	# y = [dictionary[d]['impact'] if for d in x]

	plt.title(title)
	plt.ylabel(x_label)
	plt.xlabel(y_label)
	plt.xticks(x,  rotation='vertical')
	plt.bar(x,y, width = 1, align = 'center')
	plt.show()
	plt.legend()
    # plt.savefig(FIGURES+filename)

	return None

if __name__ == '__main__':

	# dictionary = count_attacks("terrorist_attacks.csv")
	# draw_distribution(dictionary,"Distribution of Terrorist Attacks per Year", 'Number of Terrorist Attacks', 'Year')
	dictionary = count_major_attacks("terrorist_attacks.csv")
	draw_distribution(dictionary,"Distribution of Major Terrorist Attacks per Year", 'Impact of Attack (Killed + Wounded)', 'Year')
	print dictionary




