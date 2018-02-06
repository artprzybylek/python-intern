# Python intern tasks - Artur Przybyłek

Repository created and tested in Python 3.5.4

## Task 1
Used modules: re, collections.  
Typical usage for calculating hack power:
```
from hack_power import hack_calcutator
hack_calculator('babacaba')
```
Unit tests for some hacks are written in file hack_tests.py. Running tests:
```
py.test hack_tests.py
```
### How to change algorithm so it could calculate hack power for dynamically provided letters and phrases?

For the case of dynamically provided letters and phrases in hack_calculator() function, calculating power from letteres would be the same (but with the use of provided letters dictionary). The only thing that changes is calculating power from phrases. Main idea in this algorithm is to check all possibilities of taking different combinations of phrases in case when they overlap. It could be done as follows:
1. Set **total power** = 0.
2. For all phrases find all indices of **start** and **end** of **phrase** in hack, save them to list of tuples: **(phrase, start, end)**.
3. Sort list by **start** in ascending order.
4. Iterate through sorted list and find all non-overlapping phrases and groups of overlapping phrases (next phrase overlapps the previous one when its start is lower than the previous end).
5. Add powers of all non-overlapping phrases to total_power.
6. For each group of overlapping phrases, create all possible lists of non-overlapping phrases, such that:
  * first element of list is either first phrase in group or one of the following phrases that overlaps the first phrase,
  * given **last phrase** in list, new phrase in list is either **first of the following phrases** that doesn't overlap the **last phrase** or one of the following phrases that overlaps that **first of the following phrases**,
  * if phrase overlaps the last element in group of overlapping phrases, it is the last element in list.
7. For each group of overlapping phrases, add to **total power** maximum power of phrases from created lists.
8. At the end of algorithm **total power** is power from phrases.


For example, when hack='advantage', phrases={'ad': 10, 'ant': 13, 'age': 24, 'van': 13, 'tag': 5}: 

list of instances: [('ad', 0, 2), ('ant', 3, 6), ('age', 6, 9), ('van', 2, 5), ('tag', 5, 8)]  
sorted list of instances: [('ad', 0, 2), ('van', 2, 5), ('ant', 3, 6), ('tag', 5, 8), ('age', 6, 9)]  
non-overlapping phrases: [('ad', 0, 2)], power of non-overlapping phrases: 10  
There is one group of overlapping phrases: [('van', 2, 5), ('ant', 3, 6), ('tag', 5, 8), ('age', 6, 9)]  
Possible lists of non-overlapping phrases for group of overlapping phrases and power of them:  
['van', 'tag']: 18, ['van', 'age']: 37, ['ant', 'age']: 37  
Finally, total power from phrases: 10 + 37 = 47

## Task 2
Used modules: sys, re, csv, django - for validation of URL, datetime - for validation of datetime string.  
Functions in file validate.py check input validation. File page_report.py is for generating report.  
Typical usage for generating traffic report:
```
python page_report.py today.log > report.csv
```
