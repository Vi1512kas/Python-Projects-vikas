# with open("weather_data.csv") as file:
# #     student_dict = file.readlines()
# # print(student_dict)
# import csv
# with open("weather_data.csv") as data_file:
#     student_dict = csv.reader(data_file)
#     temperatures = []
#     for d in student_dict:
#         if d[1] != "temp":
#             temperatures.append(int(d[1]))
# print(temperatures)
import pandas
# student_dict = pandas.read_csv("weather_data.csv")
# data_list = student_dict["temp"].to_list()
# avg = sum(data_list)/len(data_list)
# print(avg)
# data_dict = student_dict.to_dict()
# print(data_dict)
# print(f"mean: {student_dict['temp'].mean()}")
# print(f"max: {student_dict['temp'].max()}")
# print(f"min: {student_dict['temp'].min()}")

# Extracting columns.
# print(student_dict.condition)
# print(student_dict["condition"])

# #  Extracting from row.
# print(student_dict[student_dict.day == "Monday"])

# Extracting row having max temperature.
# print(student_dict[student_dict.temp == student_dict["temp"].max()])

# converting temp 0f monday from Celsius to Fahrenheit.
# temp_of_monday = student_dict[student_dict.day == "Monday"].temp
# temp_of_monday = temp_of_monday.to_list()
# print(temp_of_monday)
# print(type(temp_of_monday))
# print(9*int(temp_of_monday[0])/5+32)

#  Creating DataFrame
# student_dict = {
#     'name': ['vikas', 'vanya', 'mohit', 'suyash'],
#     'branch': ['ai', 'cs', 'cs', 'ai']
# }
# dataframe = pandas.DataFrame(student_dict)
# print(dataframe)
# dataframe.to_csv("student.csv")
# count of squirrels based on fur colours
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data_2 = data["Primary Fur Color"].to_list()
i = 0
j = 0
k = 0
for p in data_2:
    if p == 'Gray':
        i += 1
    elif p == 'Cinnamon':
        j += 1
    elif p == 'Black':
        k += 1
    else:
        continue
data_3 = {
    'Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [i, j, k]
}
dt = pandas.DataFrame(data_3)
dt.to_csv("final_squirrel.csv")

