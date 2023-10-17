import mistakes

my_file = open("data\class_oct12.txt", "r") 
data = my_file.read()
my_file.close()

data_list = data.split("\n") # first split by student

all_tests = {"ehw":[], "mhw":[], "eic":[],"mic":[]} # English and math; homework and in-class tests

for student in data_list: # order in a dictionary is somewhat arbitrary, so I specify what list in the dict to append to, rather than using a loop
	student_lists = student.split("\t")
	all_tests["ehw"].append(student_lists[0])
	all_tests["mhw"].append(student_lists[1])
	all_tests["eic"].append(student_lists[2])
	all_tests["mic"].append(student_lists[3])

for test in all_tests:
	whole = mistakes.mistake_freqs_d(all_tests[test])
	filtered = mistakes.common_mistakes(all_tests[test], 2) # filter to only mistakes made by 2+ people
	print(test, "mistakes without filtering: length of", len(whole), "\n", whole)
	print(test, "mistakes with threshold of 2: length of", len(filtered), "\n", filtered)

	# also, to test out the parameter that specifies whether to sort alphabetically or by frequency:
	whole_byfreq = mistakes.mistake_freqs_d(all_tests[test], alphabetical = False)
	filtered_byfreq = mistakes.common_mistakes(all_tests[test], 2, alphabetical = False) # filter to only mistakes made by 2+ people
	print(test, "mistakes without filtering, by frequency: length of", len(whole_byfreq), "\n", whole_byfreq)
	print(test, "mistakes with threshold of 2, by frequency: length of", len(filtered_byfreq), "\n", filtered_byfreq)

	if len(whole) <= 20: # assuming that a list of over 20 mistakes is too many to review
		print("Human-readable complete list:")
		[print(i) for i in whole]

	else: # if the whole list is too long, go with the filtered list
		print("Human-readable filtered list:")
		[print(i) for i in filtered]
	print()
