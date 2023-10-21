import mistakes
import pandas as pd
import numpy as np

# reading the files in
week3_sat = pd.read_csv('data\week3_sat.txt', sep='\t')
week3_sat = week3_sat.astype(str)

week3_sun = pd.read_csv('data\week3_sun.txt', sep='\t')
week3_sun = week3_sun.astype(str)

week4_sat = pd.read_csv('data\week4_sat.txt', sep='\t')
week4_sat = week4_sat.astype(str)

week4_sun = pd.read_csv('data\week4_sun.txt', sep='\t')
week4_sun = week4_sun.astype(str)

week5_sat = pd.read_csv('data\week5_sat.txt', sep='\t')
week5_sat = week5_sat.astype(str)

week5_sun = pd.read_csv('data\week5_sun.txt', sep='\t')
week5_sun = week5_sun.astype(str)

week6_sat = pd.read_csv('data\week6_sat.txt', sep='\t')
week6_sat = week6_sat.astype(str)

week6_sun = pd.read_csv('data\week6_sun.txt', sep='\t')
week6_sun = week6_sun.astype(str)

week7_sat = pd.read_csv('data\week7_sat.txt', sep='\t')
week7_sat = week7_sat.astype(str)

week7_sun = pd.read_csv('data\week7_sun.txt', sep='\t')
week7_sun = week7_sun.astype(str)

# converting all values to str 
# (floats from students who made only one mistake didn't seem to be an issue in mistakes_get.py, but they cause problems here)
# it seems like this code doesn't work (probably something to do with local vs global) so I will have to convert the types manually

#file_list = [week3_sat, week3_sun, week4_sat, week4_sun, week5_sat, week5_sun, week6_sat, week6_sun, week7_sat, week7_sun]
#for file in file_list:
	#file = file.astype(str)

# testing the grouping metrics
d_3sat=["v_3sat", "n_3sat", "q_3sat"]
grouped_3sat = mistakes.compare_all_groups(week3_sat, d_3sat)

d_3sun=["v_3sun", "n_3sun", "q_3sun"]
grouped_3sun = mistakes.compare_all_groups(week3_sun, d_3sun)

d_4sat=["v_4sat", "n_4sat", "q_4sat"]
grouped_4sat = mistakes.compare_all_groups(week4_sat, d_4sat)

d_4sun=["v_4sun", "n_4sun", "q_4sun"]
grouped_4sun = mistakes.compare_all_groups(week4_sun, d_4sun)

d_5sat=["v_5sat", "n_5sat", "q_5sat"]
grouped_5sat = mistakes.compare_all_groups(week5_sat, d_5sat)

d_5sun=["v_5sun", "n_5sun", "q_5sun"]
grouped_5sun = mistakes.compare_all_groups(week5_sun, d_5sun)

d_6sat=["e_6sat", "m_6sat", "n_6sat", "q_6sat"]
grouped_6sat = mistakes.compare_all_groups(week6_sat, d_6sat)

d_6sun=["e_6sun", "m_6sun", "n_6sun", "q_6sun"]
grouped_6sun = mistakes.compare_all_groups(week6_sun, d_6sun)

d_7sat=["eic_7sat", "mic_7sat", "ehw_7sat", "mhw_7sat"]
grouped_7sat = mistakes.compare_all_groups(week7_sat, d_7sat)

d_7sun=["eic_7sun", "mic_7sun", "ehw_7sun", "mhw_7sun"]
grouped_7sun = mistakes.compare_all_groups(week7_sun, d_7sun)

# print the grouping metric dictionaries, ideally one at a time
def print_d(d):
	"""
	Prints grouping metric dictionaries nicely
	"""
	for d in d.items():
		print(d[0]) # a string that says the metric used
		dict = d[1] # a dictionary containing all "solutions" (pairs of groups that minimize the metric)
		for i in dict.items():
			print(i)
		print()


#print_d(grouped_3sat)
#print_d(grouped_3sun)
#print_d(grouped_4sat)
#print_d(grouped_4sun)
#print_d(grouped_5sat)
#print_d(grouped_5sun)
#print_d(grouped_6sat)
#print_d(grouped_6sun)
#print_d(grouped_7sat)
print_d(grouped_7sun)