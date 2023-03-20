# # CSV files
#
# # with open('weather_data.csv', mode = 'r') as whether:
# #     data = whether.readlines()
# #
# # print(data)
#
# # import csv
# #
# # with open('weather_data.csv', newline = '') as data_file:
# #     data = csv.reader(data_file)
# #     next(data)  # skip first iteration
# #     temperatures = []
# #     for row in data:
# #         temp = int(row[1])
# #         temperatures.append(temp)
# # print(temperatures)
#
import pandas

#
# data = pandas.read_csv('weather_data.csv')
# # print(data)
# # print(type(data['temp']))
# data_dict = data.to_dict()
# # print(data_dict)
# temp_list = data["temp"].to_list()
# # print(temp_list)
#
# # avg_temp = 0
# # for temp in temp_list:
# #     avg_temp += temp / 2
# # avg_temp = sum(temp_list) / len(temp_list)
# avg_temp = data["temp"].mean()
# # print('avgtemp:', avg_temp)
#
# max_val = data["temp"].max()
#
# # TEt data in colums
# print(data["condition"])
# print(data.condition)

# get data in rows
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_fh = (int(monday.temp) * 1.8) + 32
# # print(monday_fh)
#
# data_dic = {
#     "students": ["jon", 'onj', "noj"]
#     , "scores": [30, 40, 50]
# }
# datas = pandas.DataFrame(data_dic)
# datas.to_csv('new_datas.csv')
# print(datas)

# TODO: count all squirrel based on primary fur color
# TODO: colors are Gray , Cinnamon, Black

# data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
#
# sq_primary = data["Primary Fur Color"]
# sq_gray = 0
# sq_black = 0
# sq_cinnamon = 0
# for color in sq_primary:
#     if color == "Gray":
#         sq_gray += 1
#     if color == "Black":
#         sq_black += 1
#     if color == "Cinnamon":
#         sq_cinnamon += 1
#
# fur = {
#     "Fur color": ['gray', 'red', 'black'],
#     "count": [sq_gray, sq_cinnamon, sq_black]
# }
#
# fur_color = pandas.DataFrame(fur)
# fur_color.to_csv('squirrel_count.csv')

# another solution
# n_data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# g_sq = len(n_data[n_data["Primary Fur Color"] == "Gray"])
# r_sq = len(n_data[n_data["Primary Fur Color"] == "Cinnamon"])
# b_sq = len(n_data[n_data["Primary Fur Color"] == "Black"])
#
# n_data_dic = {
#     "Fur color": ["Gray", "Cinnamon", "Black"],
#     "Count": [g_sq, r_sq, b_sq]
# }
#
# n_dic = pandas.DataFrame(n_data_dic)
# n_dic.to_csv('new_Squirrel_count.csv')
