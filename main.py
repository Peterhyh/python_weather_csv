import pandas

data = pandas.read_csv("weather_data.csv")

data_dict = data.to_dict()

temp_list = data["Temperature"].to_list()


total = 0

for temp in temp_list:
    total += temp

average_temp = total//len(temp_list)

print(average_temp)
