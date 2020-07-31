import pandas as pd

# example part 1-4

# define the dictionary which names the columns as key and the lists as values (2 dimension)
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

# convert dictionary data type to Dataframe data type as df using DataFrame function in pandas
df = pd.DataFrame(dict_data)

# print data type of df
print(type(df))
print()
# print the object which is saved in variable, 'df'
print(df)

# example part 1-5

# creating dataframe with indexing the raws and naming the columns
df = pd.DataFrame([[15, 'male', 'Dukyoung'], [17, 'female', 'Soori']], index=['Junseo', 'Yeeun'], columns=['age', 'sex', 'school'])

# check index raw and column name
print(df)     # dataframe
print()
print(df.index)   # index raw
print()
print(df.columns)   # column name

# changing index of rows and names of columns
df.index = ['student1', 'student2']
df.columns = ['age', 'male_female', 'belong']

print(df)     # DataFrame
print()
print(df.index)   # index raw
print()
print(df.column)   # column name

# example part 1-6

# creating dataframe with indexing the raws and naming the columns
df = pd.DataFrame([[15, 'male', 'Dukyoung'], [17, 'female', 'Soori']], index=['Junseo', 'Yeeun'], columns=['age', 'sex', 'school'])

# priint DataFrame 'df'
print(df)
print()

# renaming name of columns using rename() method
df.rename(columns={'age':'age', 'sex':'male_female', 'school':'belong'}, inplace=True)

# renaming index of rows using rename() method
df.rename(index={'Junseo':'student1', 'Yeeun':'student2'}, inplace=True)

# print 'df' after change
print(df)

# example part 1-7

# converting data type by using DataFrame() function and save as 'df'
exam_data = {'math':[90,80,70], 'eng':[98,89,95], 'music':[85,95,100], 'phys_ed':[100,90,90]}

df = pd.DataFrame(exam_data, index=['Seojoon', 'Woohyun', 'Ina'])
print(df)
print()

# copy df and save as df2, remove one row of df2
df2 = df[:]
df2.drop('Woohyun', inplace=True)
print(df2)
print()

# copy df and save as df3, remove two row of df3
df3 = df[:]
df3.drop(['Woohyun', 'Ina'], axis=0, inplace=True)
print(df3)

# example part 1-8

# converting data type by using DataFrmae() function and save as 'df'
exam_data = {'math':[90,80,70], 'eng':[98,89,95], 'music':[85,95,100], 'phys_ed':[100,90,90]}

df = pd.DataFrame(exam_data, index=['Seojoon', 'Woohyun', 'Ina'])
print(df)
print()

# copy df and save as df4, remove one column of df4
df4 = df[:]
df4.drop('math', axis=1, inplace=True)
print(df4)
print()

# copy df and save as df5, remove two columns of df5
df5 = df[:]
df5.drop(['eng', 'music'], axis=1, inplace=True)
print(df5)
print()


