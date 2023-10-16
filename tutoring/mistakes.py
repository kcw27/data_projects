# To make the manual data collection step of my tutoring data project more efficient.
# This is meant to be used in the command prompt's interactive mode. import mistakes, mistakes.new_mistakes()
# So you can initialize, re-initialize, and print dictionaries as needed.

# I should implement a function that writes the dictionary to a file so that you can visualize which mistakes were most common using R. (A heat map?)
import pandas as pd
import numpy as np
import re 

def sorted_nicely( l ): # from https://stackoverflow.com/questions/2669059/how-to-sort-alpha-numeric-set-in-python
    """ Sort the given iterable in the way that humans expect.""" 
    convert = lambda text: int(text) if text.isdigit() else text 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)


def mistake_freqs(q, d):
	"""
	Takes a comma-separated string of questions (q) and updates pre-existing dictionary d with mistake frequencies as of the entry of q.
	"""
	q_list = q.split(',')
	for question in q_list: # adds the new mistakes to the dictionary, and increments previously-encountered mistakes by 1
		d[question] = d.get(question, 0) + 1


def new_mistakes(q, d):
	"""
	Prints how many new mistakes were added, relative to the last group of mistakes entered. 
	q: all questions missed by a group of students
	d: the dictionary to compare questions against and to update with the new mistakes
	"""

	if q == "":
		#return [np.NaN, len(d), 0, np.NaN] # no mistakes made, no change to number of total mistakes, zero additional mistakes, no additional mistakes
		return [np.NaN, len(d), 0, []] # revised to return an empty list for the additional mistake IDs, so it's consistent with the output when there are mistakes but none of them are new
	else:
		orig_d = {k:d[k] for k in d} # to compare against later; need to construct a new dictionary because otherwise orig_d stays the same as d
	
		mistake_freqs(q, d)

		#q_list = q.split(',')
		#for question in q_list: # adds the new mistakes to the dictionary, and increments previously-encountered mistakes by 1
			#d[question] = d.get(question, 0) + 1
	
		old = list(orig_d.keys()) # list of questions before the new ones were added
		current = list(d.keys()) # list of questions with new ones added
		new = [k for k in current if k not in old] # questions in the current list that weren't in the old list

		#print("Total mistakes:", len(current))
		#print("Number of additional mistakes to review:", len(new))
		#print("Additional mistakes:", new)

		# should return a list with the following info: mistakes made by current student (q), number of total mistakes made, number of additional mistakes made, IDs of the additional mistakes
		return [q, len(current), len(new), new]

def check_all(mistakes_df, d_list):
	"""
	Runs new_mistakes() on all mistake lists in mistakes_table, and adds to the corresponding dictionary specified in dict_list.
	mistakes_df: Column names are dictionaries named in dict_list. Each cell in a column corresponds to one student's mistakes list. Students are ordered according to nonverbal score, best first.
	d_list: list of mistake dictionaries in which mistake frequencies are tracked. Dictionary names are given as strings.
	"""
	rd = {} # results dictionary; the output.
	rd["results"] = pd.DataFrame(columns = ["test", "group_size", "student_mistakes", "total_mistakes", "add_mistakes", "add_mistake_ids"]) 

	for dict in d_list:
		rd[dict] = {}

		for j in range(len(mistakes_df[dict])):
			if pd.isna(mistakes_df[dict][j]): # for any NaN (i.e. student didn't make a mistake), need to convert to "" so mistakes.new_mistakes() can work with it
				mistakes_df[dict][j] = ""

			#print(mistakes_df[dict][j])
			x = new_mistakes(q=mistakes_df[dict][j], d=rd[dict]) # get some stuff for x, and also write to the dictionary at rd[dict] 
			x.insert(0, j+1) # group_size column
			x.insert(0, dict) # test column
			rd["results"].loc[len(rd["results"])] = x # add a new row to the end of the results df

	return rd



def mistake_freqs_d(m):
	"""
	It's kind of a wrapper function for mistake_freqs(), but it does create, sort, and return a new dictionary for mistake_freqs to add to
	"""

	d = {} # dictionary of mistake frequencies

	# add to d
	for student in m:
		mistake_freqs(student, d)

	# should add an optional argument to specify which way you want the dictionary sorted
	#d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])} # sorts d by frequencies (which are the values)

	d = {k: d[k] for k in sorted_nicely(d.keys())} # to sort the keys in correct alphanumeric order

	return d

def common_mistakes(m, threshold):
	"""
	Given a set of students, returns the list of questions which at least threshold-many students made mistakes on.

	m is a list of strings, each string containing the list of mistakes made by an individual student.
	It's recommended to save the data for m in a .txt file separated by newlines, then read it in and split the string by \n
	like v_file = open("v.txt", "r") then v_data = v_file.read() then v_list = v_data.split("\n"), then use m=v_list
	where v_file has the list of mistakes every student made on the verbal test

	threshold is a positive int. If you set threshold == 1, it'll just return the whole list, so it's recommended to use threshold >= 2.
	"""

	d = mistake_freqs_d(m)
	common_d = {k: v for k, v in d.items() if v >= threshold} # only keeps questions with mistakes at or above the threshold

	common_d = {k: common_d[k] for k in sorted_nicely(common_d.keys())} # to sort the keys in correct alphanumeric order

	return common_d

# also consider a function to undo a new_mistakes() call (i.e. revert changes made by that call) in case you accidentally reenter it and it messes up the frequencies
# nah actually that's no longer needed because I made the mistakes_get.check_all() function so I can just put all the data in a .tsv file