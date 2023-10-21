import mistakes
import pandas as pd
import numpy as np

def print_mistake_d(output, d_list):
	"""
	Prints mistake frequency dictionaries stored in output 
	output: the dictionary output from mistakes.check_all()
	d_list: a list of dictionary names (as strings), which are the keys in output corresponding to values which are dictionaries.
	"""
	print("Printing the following dictionaries:", d_list)

	for d in d_list:
		print(d, "mistake frequency dictionary:")
		print(output[d], "\n")
	print("\n\n")

# might be good to make a version that writes these mistake dictionaries to a .csv, but for now I just copy and paste them from the terminal into Google Sheets


# reading the files in
#week3_sat = pd.read_csv('data\week3_sat.txt', sep='\t')
#week3_sun = pd.read_csv('data\week3_sun.txt', sep='\t')
#week4_sat = pd.read_csv('data\week4_sat.txt', sep='\t')
#week4_sun = pd.read_csv('data\week4_sun.txt', sep='\t')
week5_sat = pd.read_csv('data\week5_sat.txt', sep='\t')
#week5_sun = pd.read_csv('data\week5_sun.txt', sep='\t')
#week6_sat = pd.read_csv('data\week6_sat.txt', sep='\t')
#week6_sun = pd.read_csv('data\week6_sun.txt', sep='\t')
#week7_sat = pd.read_csv('data\week7_sat.txt', sep='\t')
#week7_sun = pd.read_csv('data\week7_sun.txt', sep='\t')

# calculating additional mistakes and getting mistake frequency dictionaries
#d_3sat=["v_3sat", "n_3sat", "q_3sat"]
#checked_3sat = mistakes.check_all(week3_sat, d_3sat)

#d_3sun=["v_3sun", "n_3sun", "q_3sun"]
#checked_3sun = mistakes.check_all(week3_sun, d_3sun)

#d_4sat=["v_4sat", "n_4sat", "q_4sat"]
#checked_4sat = mistakes.check_all(week4_sat, d_4sat)

#d_4sun=["v_4sun", "n_4sun", "q_4sun"]
#checked_4sun = mistakes.check_all(week4_sun, d_4sun)

d_5sat=["v_5sat", "n_5sat", "q_5sat"]
checked_5sat = mistakes.check_all(week5_sat, d_5sat)

#d_5sun=["v_5sun", "n_5sun", "q_5sun"]
#checked_5sun = mistakes.check_all(week5_sun, d_5sun)

#d_6sat=["e_6sat", "m_6sat", "n_6sat", "q_6sat"]
#checked_6sat = mistakes.check_all(week6_sat, d_6sat)
# in week6_sat.txt, there was an A15 with no quotes around it in the first row there's an A15 with no quotes around it. It didn't seem to cause issues.

#d_6sun=["e_6sun", "m_6sun", "n_6sun", "q_6sun"]
#checked_6sun = mistakes.check_all(week6_sun, d_6sun)

#d_7sat=["eic_7sat", "mic_7sat", "ehw_7sat", "mhw_7sat"]
#checked_7sat = mistakes.check_all(week7_sat, d_7sat)

#d_7sun=["eic_7sun", "mic_7sun", "ehw_7sun", "mhw_7sun"]
#checked_7sun = mistakes.check_all(week7_sun, d_7sun)


# writing results to .csv
#checked_3sat["results"].to_csv("data\output\checked_3sat.csv")
#checked_3sun["results"].to_csv("data\output\checked_3sun.csv")
#checked_4sat["results"].to_csv("data\output\checked_4sat.csv")
#checked_4sun["results"].to_csv("data\output\checked_4sun.csv")
#checked_5sat["results"].to_csv("data\output\checked_5sat.csv")
#checked_5sun["results"].to_csv("data\output\checked_5sun.csv")
#checked_6sat["results"].to_csv("data\output\checked_6sat.csv")
#checked_6sun["results"].to_csv("data\output\checked_6sun.csv")
#checked_7sat["results"].to_csv("data\output\checked_7sat.csv")
#checked_7sun["results"].to_csv("data\output\checked_7sun.csv")

# print the mistake frequency dictionaries
#print_mistake_d(checked_3sat, d_3sat)
#print_mistake_d(checked_3sun, d_3sun)
#print_mistake_d(checked_4sat, d_4sat)
#print_mistake_d(checked_4sun, d_4sun)
print_mistake_d(checked_5sat, d_5sat)
#print_mistake_d(checked_5sun, d_5sun)
#print_mistake_d(checked_6sat, d_6sat)
#print_mistake_d(checked_6sun, d_6sun)
#print_mistake_d(checked_7sat, d_7sat)
#print_mistake_d(checked_7sun, d_7sun)
