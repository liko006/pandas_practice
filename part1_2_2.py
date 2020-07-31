import pandas as pd

# example 1-4

# define the dictionary which names the columns as key and the lists as values (2 dimension)
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

# convert dictionary data type to Dataframe data type as df using DataFrame function in pandas
df = pd.DataFrame(dict_data)

# print data type of df
print(type(df))
print()
# print the object which is saved in variable, 'df'
print(df)

# creating dataframe with indexing the raws and naming the columns
df = pd.DataFrame([[15, 'male', 'Dukyoung'], [17, 'female', 'Soori']], index=['Junseo', 'Yeeun'], columns=['age', 'sex', 'school'])

# check index raw and column name
print(df)     # dataframe
print()
print(df.index)   # index raw
print()
print(df.columns)   # column name


