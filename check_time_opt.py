# from core.core import *
# import numpy as np
# import time

# data = read_xlsx('data_anh_Son/VRPTW_data_sample_1.xlsx')
# ### constant

# capacity = 200
# speed = 1
# number_point = len(data)
# point = np.zeros(number_point)
# point[0] = 1
# depot = [data['x_coor'][0],data['y_coor'][0]]


# def remaining_point():
#     #print(point)
#     index_process = []
#     for i in range(len(point)):
#         if point[i] == 0:
#             index_process.append(i)
#     #print(index_process)
#     return index_process

# def opt_time(time_now0,point_now,remaining_point):
#     for i in remaining_point:
#         earliest_arrival_time = data['earliest_arrival_time'][i]
#         latest_arrival_time = data['latest_arrival_time'][i]

#         value = latest_arrival_time - earliest_arrival_time


# opt_time([35,35],remaining_point())