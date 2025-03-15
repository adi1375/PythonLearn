import pandas

data = pandas.read_csv("Python_100_days/Day25_Country_State_Guessing_Game/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colors = data["Primary Fur Color"].to_list()
color_dict = {}
for color in colors:
    if str(color) != "nan":
        color_dict[color] = colors.count(color)

color_data = pandas.DataFrame([color_dict])
color_data.to_csv("Python_100_days/Day25_Country_State_Guessing_Game/squirrel_colors.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict ={
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[gray_squirrels_count,cinnamon_squirrels_count,black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Python_100_days/Day25_Country_State_Guessing_Game/squirrel_count.csv")