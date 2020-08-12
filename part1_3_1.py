import pandas as pd

# example part 1-16

exam_data = {'name':['Seojoon','Woohyun','Ina'], 'math':[90,80,70], 'eng':[98,89,95], ' music':[85,95,100], 'gym':[100,90,90]}
df = pd.DataFrame(exam_data)
print(df)
print()

ndf = df.set_index(['name'])
print(df)
print()
ndf2 = df.set_index(['music'])
print(df)
prin()
ndf3 = df.sex_index(['math','music'])
print(df)
print()
