# This is a generic fill-in-the-blank document for generating the list of mistakes you need to review with your group
# It's especially useful if the website shows you a long list of mistakes for a test, as this will allow you to filter it to just the common mistakes
# Capitalized text indicates parts that should be replaced according to your own needs 

import mistakes

my_file = open("data\MYFILE.txt", "r") # see manual for instructions on formatting the data table file
data = my_file.read()
my_file.close()

data_list = data.split("\n") # first split by student

all_tests = {"ehw":[], "mhw":[], "eic":[],"mic":[]} # REPLACE WITH YOUR TESTS. In this case I had English and math, both as homework and in-class tests

for student in data_list: # order in a dictionary is somewhat arbitrary, so I specify what list in the dict to append to, rather than using a loop
	student_lists = student.split("\t")

	# MAKE SURE THAT EACH INDEX OF student_lists (number in the square brackets next to student_lists) CORRESPOND TO THE TEST SPECIFIED FOR all_tests
	all_tests["ehw"].append(student_lists[0]) # Python is 0-indexed, so the first column is called column 0. I collected English HW results in the first column of my data table.
	all_tests["mhw"].append(student_lists[1])
	all_tests["eic"].append(student_lists[2])
	all_tests["mic"].append(student_lists[3])
	# CHANGE THE NUMBER OF THE ABOVE STATEMENTS AS NECESSARY

for test in all_tests:
	whole = mistakes.mistake_freqs_d(all_tests[test])
	filtered = mistakes.common_mistakes(all_tests[test], threshold=2) # filter to only mistakes made by 2+ people. IF THIS STILL PROVIDES A LONG LIST, YOU CAN CHANGE threshold TO 3 OR HIGHER

	# these mistake frequency dictionaries are printed alphabetically
	print(test, "mistakes without filtering: length of", len(whole), "\n", whole)
	print(test, "mistakes with threshold of 2: length of", len(filtered), "\n", filtered)

	# also, to test out the parameter that specifies whether to sort alphabetically or by frequency:
	whole_byfreq = mistakes.mistake_freqs_d(all_tests[test], alphabetical = False)
	filtered_byfreq = mistakes.common_mistakes(all_tests[test], 2, alphabetical = False) # filter to only mistakes made by 2+ people. ONCE AGAIN, MODIFY THRESHOLD AS NEEDED.
	print(test, "mistakes without filtering, by frequency: length of", len(whole_byfreq), "\n", whole_byfreq)
	print(test, "mistakes with threshold of 2, by frequency: length of", len(filtered_byfreq), "\n", filtered_byfreq)

	if len(whole) <= 20: # assuming that a list of over 20 mistakes is too many to review; CHANGE THE NUMBER AS NEEDED
		print("Human-readable complete list:")
		[print(i) for i in whole] # alphabetical order

	else: # if the whole list is too long, go with the filtered list
		print("Human-readable filtered list:")
		[print(i) for i in filtered] # alphabetical order
	print()
