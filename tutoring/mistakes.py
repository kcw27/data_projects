# So far there's no function that writes the mistake frequency dictionaries to a file, but they are printed by mistakes_get.py.
import pandas as pd
import numpy as np
import re
import itertools
import operator

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
	Runs new_mistakes() on all mistake lists in mistakes_df, and adds to the corresponding dictionary specified in d_list.
	mistakes_df: Column names are dictionaries named in dict_list. Each cell in a column corresponds to one student's mistakes list. Students are ordered according to score, best first.
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



def mistake_freqs_d(m, alphabetical = True):
	"""
	It's kind of a wrapper function for mistake_freqs(), but it does create, sort, and return a new dictionary for mistake_freqs to add to.
	alphabetical specifies the type of sorting for the dictionary. By default, it's True, so it sorts questions alphabetically.
	If alphabetical == False, then it sorts questions by frequencies instead.
	"""

	d = {} # dictionary of mistake frequencies

	# add to d
	for student in m:
		mistake_freqs(student, d)

	if alphabetical:
		d = {k: d[k] for k in sorted_nicely(d.keys())} # to sort the keys in correct alphanumeric order
	else:
		d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse = True)} # sorts d by frequencies (which are the values) in descending order

	return d

def common_mistakes(m, threshold, alphabetical = True):
	"""
	Given a set of students, returns the list of questions which at least threshold-many students made mistakes on.

	m is a list of strings, each string containing the list of mistakes made by an individual student.
	It's recommended to save the data for m in a .txt file separated by newlines, then read it in and split the string by \n
	like v_file = open("v.txt", "r") then v_data = v_file.read() then v_list = v_data.split("\n"), then use m=v_list
	where v_file has the list of mistakes every student made on the verbal test

	threshold is a positive int. If you set threshold == 1, it'll just return the whole list, so it's recommended to use threshold >= 2.

	alphabetical specifies the type of sorting for the dictionary. By default, it's True, so it sorts questions alphabetically.
	If alphabetical == False, then it sorts questions by frequencies instead.
	"""

	d = mistake_freqs_d(m) # alphabetical parameter left unspecified; by default it's sorted alphabetically
	common_d = {k: v for k, v in d.items() if v >= threshold} # only keeps questions with mistakes at or above the threshold

	if alphabetical:
		common_d = {k: common_d[k] for k in sorted_nicely(common_d.keys())} # to sort the keys in correct alphanumeric order
	else:
		common_d = {k: v for k, v in sorted(common_d.items(), key=lambda item: item[1], reverse = True)} # sorts d by frequencies (which are the values) in descending order

	return common_d

def get_groupings():
	"""
	Gets all unique combinations of students (indexed 0-11), where they're split into two groups of six.
	"""
	students = list(range(12)) # so far, this code only supports even numbers
	all_combos = list(itertools.combinations(students, 6)) # the ordering makes it very convenient to find which groups are pairs (as seen below)

	# pair groups of students together such that all students appear once within the pair of groups
	reversed_all_combos = list(reversed(all_combos)) # it just so happens that for all i from 0 to 461, groups at indices 0+i and 924-1-i pair together
	zipped = list(zip(all_combos, reversed_all_combos))
	halfway = len(all_combos)//2 # floor-divided to get an int; evaluates to 924/2=462
	zipped = zipped[:halfway] # goes up to halfway - 1, so pairings are made for all i from 0 to 461

	return zipped


def compare_all_groups(mistakes_df, d_list):
	"""
	For all possible groupings among the twelve students (indices 0-11, split into two groups of six), find the groups that minimize two metrics:
	Minimization: find the pair of groups which minimizes the sum of all test mistakes across these two groups for that day's tests
	Parity: find the pair of groups which minimizes (the sum of) the differences in test mistakes for each test for that day

	For each metric, displays the total number of mistakes, as well as how many mistakes there are for group 1 and group 2 separately.
	"""
	all_student_groups = get_groupings()

	minimize_d = {}
	parity_d1 = {} # approach 1 to parity: minimize differences in mistakes for each test
	parity_d2 = {} # approach 2 to parity: minimize differences in total mistakes

	general_d = {} # to make calculations from
	#comparisons_d = {} # a version of general_d that's easier to read

	results_d = {} # to populate with results later

	for pair in all_student_groups:
		general_d[pair] = []
		#comparisons_d[pair] = {} # each pair of groups is a key in the index; the value will be a dictionary containing test names and the groups' scores

		for d in d_list:
			group1_mistakes = [mistakes_df[d][x] for x in pair[0]]
			group2_mistakes = [mistakes_df[d][x] for x in pair[1]]

			grp1 = mistake_freqs_d(group1_mistakes)
			grp2 = mistake_freqs_d(group2_mistakes)

			group1_count = len(grp1)
			group2_count = len(grp2)

			general_d[pair] = general_d[pair] + [group1_count, group2_count] # for each test, add the mistake counts for group 1 and group 2 to the end of the list
			#comparisons_d[pair][d] = [group1_count, group2_count] # comparisons specifies which test the results came from

	for pair in general_d: # now calculate the metrics for minimization and parity
		minimize_d[pair] = sum(general_d[pair])

		list_odd = general_d[pair][1::2] # in general_d, odd indices are group 2's mistakes
		list_even = general_d[pair][0::2] # in general_d, even indices are group 1's mistakes

		# my first approach to parity: minimize the difference in mistakes for each individual test
		diffs = map(operator.sub, list_odd, list_even) # find the difference in the number of mistakes between groups 1 and 2
		parity_d1[pair] = sum([abs(k) for k in diffs]) # then sum the absolute values of the differences across all tests for that pair of groups

		# my second approach to parity: minimize the difference in total mistakes (across all tests)
		diff = sum(list_odd) - sum(list_even)
		parity_d2[pair] = abs(diff)


	min_pair = {k:v for k,v in minimize_d.items() if v == min(minimize_d.values())}
	results_d["min"] = {k:{} for k in min_pair.keys()}
	for key in min_pair:
		results_d["min"][key]["total_mistakes"] = sum(general_d[key]) # could use min_pair[key], but for consistency's sake I'm using sum(general_d[key])

		list_odd = general_d[key][1::2] # in general_d, odd indices are group 2's mistakes
		list_even = general_d[key][0::2] # in general_d, even indices are group 1's mistakes
		results_d["min"][key]["grp1_mistakes"] = sum(list_odd)
		results_d["min"][key]["grp2_mistakes"] = sum(list_even)
		

	par1_pair = {k:v for k,v in parity_d1.items() if v == min(parity_d1.values())} # first select the pair(s) that minimize the differences in mistakes for each test
	# then select the pair(s) that minimize the total mistakes to review
	par1_totalmistakes = {k:sum(general_d[k]) for k in par1_pair.keys()}
	par1_pair_filtered = {k:v for k,v in par1_pair.items() if sum(general_d[k]) == min(par1_totalmistakes.values())}

	results_d["par1"] = {k:{} for k in par1_pair_filtered.keys()}
	for key in par1_pair_filtered:
		results_d["par1"][key]["total_mistakes"] = sum(general_d[key])

		list_odd = general_d[key][1::2] # in general_d, odd indices are group 2's mistakes
		list_even = general_d[key][0::2] # in general_d, even indices are group 1's mistakes
		results_d["par1"][key]["grp1_mistakes"] = sum(list_odd)
		results_d["par1"][key]["grp2_mistakes"] = sum(list_even)

	# for debug
	#results_d["par1_debug"] = {}
	#for key in par1_pair:
		#results_d["par1_debug"][key] = sum(general_d[key])
	
	par2_pair = {k:v for k,v in parity_d2.items() if v == min(parity_d2.values())} # first select the pair(s) that minimize the difference in total mistakes
	# then select the pair(s) that minimize the total mistakes to review
	par2_totalmistakes = {k:sum(general_d[k]) for k in par2_pair.keys()}
	par2_pair_filtered = {k:v for k,v in par2_pair.items() if sum(general_d[k]) == min(par2_totalmistakes.values())}

	results_d["par2"] = {k:{} for k in par2_pair_filtered.keys()}
	for key in par2_pair_filtered:
		results_d["par2"][key]["total_mistakes"] = sum(general_d[key]) 

		list_odd = general_d[key][1::2] # in general_d, odd indices are group 2's mistakes
		list_even = general_d[key][0::2] # in general_d, even indices are group 1's mistakes
		results_d["par2"][key]["grp1_mistakes"] = sum(list_odd)
		results_d["par2"][key]["grp2_mistakes"] = sum(list_even)

	# for debug
	#results_d["par2_debug"] = {}
	#for key in par2_pair:
		#results_d["par2_debug"][key] = sum(general_d[key])


	# also want to get a sense of how the minimization and parity approach mistake counts compare to the default grouping of (0, 1, 2, 3, 4, 5) and (6, 7, 8, 9, 10, 11)
	default_key = all_student_groups[0]
	results_d["default"] = {default_key:{}}
	results_d["default"][default_key]["total_mistakes"] = sum(general_d[default_key])

	# here, list_odd and list_even aren't local to a loop, so exercise caution
	list_odd = general_d[default_key][1::2] # in general_d, odd indices are group 2's mistakes
	list_even = general_d[default_key][0::2] # in general_d, even indices are group 1's mistakes
	results_d["default"][default_key]["grp1_mistakes"] = sum(list_odd)
	results_d["default"][default_key]["grp2_mistakes"] = sum(list_even)


	return results_d