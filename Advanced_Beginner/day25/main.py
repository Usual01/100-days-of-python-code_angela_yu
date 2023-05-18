# with open ("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open ("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temparature = []
#     for row in data:
#         if row[1] != "temp":
#             temparature.append(int(row[1]))
#     print(temparature)
# 
import pandas

data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
average = sum(temp_list) / len(temp_list)
print(f"The average temperature in the week was: {average}")
print(data[data.temp == data.temp.max()])
