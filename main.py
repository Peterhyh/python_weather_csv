import pandas

data = pandas.read_csv("weather_data.csv")

data_dict = data.to_dict()

temp_list = data["Temperature"].to_list()


average_temp = data["Temperature"].mean()

print(average_temp)
