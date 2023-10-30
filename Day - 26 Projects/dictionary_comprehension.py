import random as rd
import pandas as pd
# names = ["vikas", "vanya", "mohit", "suyash", "roshan"]
# student_dict = {name: rd.randint(1, 100) for name in names}
# print(student_dict)
# dat = {i: j for (i,j) in student_dict.items()}
# print(dat)
# passed = {i: j for (i,j) in student_dict.items() if j > 40}
# print(passed)
# for (i,j) in student_dict.items():
#     print(i,j)
student_dic = {
    "names": ["vikas", "vanya", "mohit", "suyash", "roshan"],
    "marks": [75, 90, 81, 83, 89]
}
student_dataframe = pd.DataFrame(student_dic)
# print(student_dataframe)

# looping
# for (key, value) in student_dataframe.items():
#     print(value) # pura do baar aa rha h
# inbuilt loop
# for (i, j) in student_dataframe.iterrows():
#     print(j.names)  # each row wise
for (i, j) in student_dataframe.iterrows():
    print(j)  # each row wise and converted to series

