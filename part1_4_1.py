import pandas as pd

# example part 1-21

student1 = pd.Series({'kor':100, 'eng':80, 'math':90})
print(student1)
print()

percentage = student1/200

print(percentage)
print()
print(tpye(percentage))
print()

# example part 1-22

student1 = pd.Series({'kor':100, 'eng':80, 'math':90})
student2 = pd.Series({'math':80, 'kor':90, 'eng':80})
print(student1)
print()
print(student2)
print()

addition = student1 + student2
subtraction = student1 - student2
multipliaction = student1 * student2
division = student1 / student2
print(type(division))
print()

result = pd.DataFrame([addition, subtraction, multiplication, division], index=['add','sub','mul','div'])
print(result)
print()

