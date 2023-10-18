# Motivation
I currently work as a tutor at a test prep service. I collected data on how students performed on our practice tests so that I could explore some patterns that I observed. These findings will inform us of ways to increase the efficiency of our workflow. I also developed some time-saving tools that quickly identify the test problems that students need additional help with. These tools will allow tutors to optimize how they allocate time toward explaining tricky problems and concepts.

# Contents
## Data
The data analyzed in this project were collected from first grade classes. Two classes are featured: a Saturday class and a Sunday class. The majority of students are from the same school district. All data are anonymized.
<ul>Files titled in the format "weekX_day.txt" are raw data. They contain lists of mistakes that the twelve best-performing students made on each test. Each row corresponds to a student.</ul>
<ul>class_oct12.txt is the data used with class_oct12.py. Each row in this tab-separated file contains a single student's test scores. Order of students is arbitrary. This file only includes students that were in my review group.</ul>
<ul>In the subdirectory /output, files titled in the format "checked_Xday.csv" were processed using the mistakes module.</ul>

## Code
Ideally, we'd be able to review every single problem that each student made mistakes on. However, in reality, class time is limited. Tutors are assigned a group of students to review with, and they must pace their explanations such that they best serve the needs of the group within the time allotted.
<ul>mistakes.py: the mistakes module contains several functions that construct and work with dictionaries of mistake frequencies. </ul>
<ul>class_oct12.py: a script that demonstrates how to use functions in the mistakes module to get an optimized list of questions to review, complete with mistake frequencies.</ul>
<ul>find_common.py: a generic fill-in-the-blank version of class_oct12.py.</ul>
<ul><b>TO DO: create a user manual explaining the format in which to collect data from one's group of students. This user manual should be accessible even to people who have never used Python or the command prompt.</b></ul>

Another issue we face is that the student-to-tutor ratio is often higher than we'd like it to be. If a tutor cancels on short notice, this ratio becomes even higher. I'd like to predict how the pool of unique mistakes among a group of students increases as students are added to the group.  
<ul>mistakes.py: as explained above.</ul>
<ul>mistakes_get.py: uses the mistakes module to produce output data. The output data tracks, for each group size (1-12 students in increasing order of mistake count), the number of total unique mistakes to review, the number of additional mistakes attributed to the newly-added student, and the IDs of the additional mistakes.</ul>

Finally, there are some miscellaneous questions that I'd like to answer using this data.
<ul><b>TO DO: upload tutoring.Rmd</b></ul>
