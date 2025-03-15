# with open ("Python_100_days/Day25_Country_State_Guessing_Game/weather_data.csv") as file:
#     weather_data = file.readlines()
#     print(weather_data)

# import csv

# with open("Python_100_days/Day25_Country_State_Guessing_Game/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures =[]
#     for row in data:
#         if row[1]!="temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("Python_100_days/Day25_Country_State_Guessing_Game/weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict=data.to_dict()
# print(data_dict)

# temp_list=data["temp"].to_list()
# print(temp_list)
# avg = sum(temp_list)/len(temp_list)
# print(round(avg,2))

# print(data["temp"].mean())
# print(data["temp"].max())

# pandas column
# print(data.condition)

# pandas row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp
# print(monday_temp*9/5 +32)

# create dataframe
# data_dict ={
#     "students" : ["Amy","James", "Angela"],
#     "scores": [76,56,65],
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")