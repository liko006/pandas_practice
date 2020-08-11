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
print()

# example part 1-5

# creating dataframe with indexing the raws and naming the columns
df = pd.DataFrame([[15, 'male', 'Dukyoung'], [17, 'female', 'Soori']], index=['Junseo', 'Yeeun'], columns=['age', 'sex', 'school'])

# check index raw and column name
print(df)     # dataframe
print()
print(df.index)   # index raw
print()
print(df.columns)   # column name
print()

# changing index of rows and names of columns
df.index = ['student1', 'student2']
df.columns = ['age', 'male_female', 'belong']

print(df)     # DataFrame
print()
print(df.index)   # index raw
print()
print(df.column)   # column name
print()

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
print()

# example part 1-7

# converting data type by using DataFrame() function and save as 'df'
exam_data = {'math':[90,80,70], 'eng':[98,89,95], 'music':[85,95,100], 'gym':[100,90,90]}

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
print()

# example part 1-8

# converting data type by using DataFrmae() function and save as 'df'
exam_data = {'math':[90,80,70], 'eng':[98,89,95], 'music':[85,95,100], 'gym':[100,90,90]}

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

# example part 1-9

exam_data = {'math':[90,80,70], 'eng':[98,89,95], 'music':[85,95,100], 'gym':[100,90,90]}

df = pd.DataFrame(exam_data, index=['Seojoon', 'Woohyun', 'Ina'])
print(df)
print()

label1 = df.loc['Seojoon']
position1 = df.iloc[0]
print(label1)
print()
print(position1)
print()

label2 = df.loc[['Seojoon', 'Woohyun']]
position2 = df.iloc[[0,1]]
print(label2)
print()
print(position2)
print()

label3 = df.loc[['Seojoon':'Woohyun']]
position3 = df.iloc[[0:1]]
print(label3)
print()
print(position3)
print()

# example part 1-10 

exam_data = {'name': ['Seojoon', 'Woohyun', 'Ina'], 'math':[90,80,70], 'eng':[98,89,95], 'music':[85,95,100], 'gym':[100,90,90]}
df = pd.DataFrame(exam_data)
print(df)
print(type(df))
print()

math1 = df['math']
print(math1)
print(type(math1))
print()
print()

english = df.english
print(english)
print(type(english))

music_gym = df[['music', 'gym']]
print(music_gym)
print(type(music_gym))
print()

math2 = df[['math']]
print(math2)
print(type(math2))
print()

# example part 1-11

exam_data = {'name': ['Seojoon', 'Woohyun', 'Ina'], 'math':[90,80,70], 'eng':[98,89,95], 'music':[85,95,100], 'gym':[100,90,90]}
df = pd.DataFrame(exam_data)

df.set_index('name', inplace=True)
print(df)
print()

a = df.loc['Seojoon', 'music']
print(a)
b = df.iloc[0, 2]
print(b)
print()

c = df.loc['Seojoon', ['music', 'gym']]
print(c)
d = df.iloc[0, [2,3]]
print(d)
e = df.loc['Seojoon', 'music':'gym']
print(e)
f = df.iloc[0, 2:]
print(f)
print()

g = df.loc[['Seojoon', 'Woohyun'], ['music', 'gym']]
print(g)
h = df.iloc[[0, 1], [2, 3]]
print(h)
i = df.loc['Seojoon':'Woohyun', 'music':'gym']
print(i)
j = df.iloc[0:2, 2:]
print(j)

# example part 1-12

exam_data = {'name': ['Seojoon', 'Woohyun', 'Ina'], 'math':[90,80,70], 'eng':[98,89,95], 'music':[85,95,100], 'gym':[100,90,90]}
df = pd.DataFrame(exam_data)
print(df)
print()

df['kor'] = 80
print(df)
print()

# example part 1-13

exam_data = {'name': ['Seojoon', 'Woohyun', 'Ina'], 'math':[90,80,70], 'eng':[98,89,95], 'music':[85,95,100], 'gym':[100,90,90]}
df = pd.DataFrame(exam_data)
print(df)
print()

df.loc[3] = 0
print(df)
print()

df.loc[4] = ['Dongkyu',90,80,70,60]
print(df)
print()

df.loc['raw5'] = df.loc[3]
print(df)
print()

# example part 1-14

exam_data = {'name': ['Seojoon', 'Woohyun', 'Ina'], 'math':[90,80,70], 'eng':[98,89,95], 'music':[85,95,100], 'gym':[100,90,90]}
df = pd.DataFrame(exam_data)
print(df)
print()

df.set_index('name', inplace=True)
print(df)
print()

df.iloc[0][3] = 80
print(df)
print()

df.loc['Seojoon','gym'] = 90
print(df)
print()

df.loc['Seojoon','gym'] = 100
print(df)
print()

df.loc['Seojoon', ['music','gym']] = 50
print(df)
print()

df.loc['Seojoon', ['music','gym']] = 100, 50
print(df)
print()

# example 1-15

exam_data = {'name': ['Seojoon', 'Woohyun', 'Ina'], 'math':[90,80,70], 'eng':[98,89,95], 'music':[85,95,100], 'gym':[100,90,90]}
df = pd.DataFrame(exam_data)
print(df)
print()

df = df.transpose()
print(df)
print()

df = df.T
print(df)
print()

