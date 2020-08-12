import pandas as pd

# example part 1-16

exam_data = {'name':['Seojoon','Woohyun','Ina'], 'math':[90,80,70], 'eng':[98,89,95], ' music':[85,95,100], 'gym':[100,90,90]}
df = pd.DataFrame(exam_data)
print(df)
print()

ndf = df.set_index(['name'])
print(ndf)
print()
ndf2 = df.set_index(['music'])
print(ndf2)
prin()
ndf3 = df.sex_index(['math','music'])
print(ndf3)
print()

# example 1-17

dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

df = pd.DataFrame(dict_data, index=['r0','r1','r2'])
print(df)
print()

new_index = ['r0','r1','r2','r3','r4']
ndf = df.set_index(new_index)
print(ndf)
print()

new_index = ['r0','r1','r2','r3','r4']
ndf2 = df.sex_index(new_index, fill_value=0)
print(ndf2)
print()

# example part 1-18

dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

df = pd.DataFrame(dict_data, index=['r0','r1','r2'])
print(df)
print()

ndf = df.reset_index()
print(ndf)
print()

# example part 1-19

dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

df = pd.DataFrame(dict_data, index=['r0','r1','r2'])
print(df)
print()

ndf = df.sort_index(ascending=False)
print(ndf)
print()

# exam
