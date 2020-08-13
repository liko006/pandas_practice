
# example part 1-21
import pandas as pd

student1 = pd.Series({'kor':100, 'eng':80, 'math':90})
print(student1)
print()

percentage = student1/200

print(percentage)
print()
print(tpye(percentage))
print()

# example part 1-22
import pandas as pd

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

# example part 1-23
import pandas as pd
import numpy as np

student1 = pd.Series({'kor':np.nan, 'eng':80, 'math':90})
student2 - pd.Series({'math':80, 'kor':90})
print(student1)
print()
print(student2)
print()

# example part 1-24
import pandas as pd
import numpy as np

student1 = pd.Series({'kor':np.nan, 'eng':80, 'math':90})
student2 - pd.Series({'math':80, 'kor':90})
print(student1)
print()
print(student2)
print()

sr_add = student1.add(student2, fill_value=0)
sr_sub = student1.sub(student2, fill_value=0)
sr_mul = student1.mul(student2, fill_value=0)
sr_div = student1.div(student2, fill_value=0)

result = pd.DataFrame([sr_add, sr_sub, sr_mul, sr_div], index=['add','sub','mul','div'])
print(result)
print()
