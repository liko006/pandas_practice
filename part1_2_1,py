# example part 1-1

# import pandas
import pandas as pd

# creating dictionary data type as 'dict_data' and store key:value
dict_data = {'a':1, 'b':2, 'c':3}

# use Series() function in pandas to convert this dictionary data type to Series data type and save as 'sr'
sr = pd.Series(dict_data)

# print the data type of 'sr'
print(type(sr))
print()

# print the objects saved in 'sr'
print(sr)

# example part 1-2

# convert a list into Series and save in 'sr'
list_data = ['2019-01-02', 3.14, 'ABC', 100, True]
sr = pd.Series(list_data)
print(sr)

# save index array in 'idx' and values array in 'val'
idx = sr.index
val = sr.values
print(idx)
print()
print(val)

# example part 1-3

# convert tuple to Series (with index option)
tup_data = ('youngin', '2010-05-01', 'female', True)
sr = pd.Series(tup_data, index = ['name', 'date_of_birth', 'sex', 'student'])
print(sr)

# selecting one element
print(sr[0])
print(sr['name'])

# selecting multiple element
print(sr[[1,2]])
print()
print(sr[['date_of_birth', 'sex']])

# selecting multiple element (with index range)
print(sr[1:2])
print()
print(sr['date_of_birth', 'sex'])
