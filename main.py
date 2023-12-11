import pandas

data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()

# temp_list = data["Temperature"].to_list()


# average_temp = data["Temperature"].mean


# print(data[data.Temperature == data.Temperature.max()])

row = "Monday"
selected_row = data[data.Day == f"{row}"]
selected_temp = selected_row.Temperature[0]

print(selected_temp*(9/5)+32)
