# the main disadvantage of interpreted languages like Python was the lack of speed when dealing with large volumes of data and complex mathematical operations. The Python NumPy (Numerical Python) library loads its data efficiently into memory and integrates C code, which compiles at run time.
import numpy as np

import scipy
import matplotlib
import pandas as pd

# numerical python
# print numpy.array([1, 2, 3]) + numpy.array([1, 2, 3])
print
print "------"
print np.array([1, 2, 3])[2] * np.array([1, 2, 3])


# ===============================================================

# pandas
print "-------------------"
# series objects
series = pd.Series([1, 2, 3])
print series


print "-------------------"
s = pd.Series([7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'])
print s
print

# create your own indexes
s2 = pd.Series([7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'],
              index=['A', 'Z', 'C', 'Y', 'E'])
print s2
print

# convert a dictionary into a Series
d = {'Chicago': 1000, 'New York': 1300, 'Portland': 900, 'San Francisco': 1100,
     'Austin': 450, 'Boston': None}
cities = pd.Series(d)
print cities
print

# use keys to only display the cities you want
print cities[['Chicago', 'Portland', 'San Francisco']]
print
# use booleans to only display the cities you want
print cities[cities < 1000]
print

# 
less_than_1000 = cities < 1000
print less_than_1000
print '\n'
print cities[less_than_1000]
print

# check whether a city is in a series (returns true or false)
print 'Seattle' in cities
print 'San Francisco' in cities
print




# ============================================

# data frames: data like a spreadsheet

data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
        'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions', 'Lions', 'Lions'],
        'wins': [11, 8, 10, 15, 11, 6, 10, 4],
        'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
football = pd.DataFrame(data, columns=['year', 'team', 'wins', 'losses'])
print football
print 


# import csv file data with headers:
from_csv = pd.read_csv('mariano-rivera.csv')
print from_csv.head()
print

# without headers:
cols = ['num', 'game', 'date', 'team', 'home_away', 'opponent',
        'result', 'quarter', 'distance', 'receiver', 'score_before',
        'score_after']
no_headers = pd.read_csv('peyton-passing-TDs-2012.csv', sep=',', header=None, names=cols)
print no_headers.head()
print

# export our table to a csv file
no_headers.head().to_csv('peyton_file.csv')





# ======================================================

# reading from excel, then write back to excel (use Python, not VBA!)
# get rid of the meaningless index
# import xlwt
# import xlrd

# peyton = no_headers.head()
# peyton.to_excel('peyton.xlsx', index=False)

# # delete the dataframe
# del peyton

# # read back from the excel file we created
# # peyton = pd.read_excel('peyton.xlsx', 'sheet1')
# # print peyton

# workbook = xlrd.open_workbook('peyton.xlsx')
# print workbook
















































