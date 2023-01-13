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

# def list_distance(point_1, points):
#     distances = []
#     for i in points:
#         distances.append(distance(point_1[0],point_1[1],i[0],i[1]))

#     return sorted(range(len(distances)), key=lambda k: distances[k])

# # route1 = Route(start_point = depot, start_time = 0, depot_start_time = 0, depot_end_time = 230, capacity = 200, capacity_now = 0)
# # print(route1.return_route())

# def remaining_point():
#     #print(point)
#     index_process = []
#     for i in range(len(point)):
#         if point[i] == 0:
#             index_process.append(i)
#     #print(index_process)
#     return index_process

# def check_remaining_point():
#     for i in range(len(point)):
#         if point[i] == 0:
#            return True
#     return False
# #print(depot[0])
# def Greedy(): 
#     routes = []
#     st_time = time.time()
#     start_time = 0
#     #start_time = min(data['earliest_arrival_time']) -

#     start_point = depot
#     while check_remaining_point():
#         route = Route(start_point = depot, start_time = start_time, depot_start_time = 0, depot_end_time = 230, capacity = 200,speed = speed)
#         #kt_all = False
#         kt_ap = False
#         while check_remaining_point():
#             points = []
#             list_distance_now = []
#             vt = remaining_point()
#             for i in vt:
#                 points.append([data['x_coor'][i],data['y_coor'][i]])
#             list_distance_now_tmp = list_distance(start_point,points)
#             for _ in list_distance_now_tmp:
#                 list_distance_now.append(vt[_])
#             #print(list_distance_now)
#             #new_point = [data['x_coor'][list_distance_now[0]],data['y_coor'][list_distance_now[0]]]
#             #print((depot[0] - new_point[0])**2 + (depot[1]- new_point[1])**2)
        
#             kt_all = False
#             for stt_ut in range(len(list_distance_now)):
#                 if route.excute(new_point = [data['x_coor'][list_distance_now[stt_ut]],data['y_coor'][list_distance_now[stt_ut]]] , capacity_add = data['demand'][list_distance_now[stt_ut]]\
#                 , earliest_arrival_time = data['earliest_arrival_time'][list_distance_now[stt_ut]],latest_arrival_time = data['latest_arrival_time'][list_distance_now[stt_ut]]\
#                 ,serving_time = data['serving_time'][list_distance_now[stt_ut]]):
#                     #print([data['x_coor'][list_distance_now[stt_ut]+1],data['y_coor'][list_distance_now[stt_ut]+1]])
#                     #print(point[list_distance_now[stt_ut]+1])
#                     point[list_distance_now[stt_ut]] = 1
#                     kt_ap = True
#                     start_point = [data['x_coor'][list_distance_now[stt_ut]],data['y_coor'][list_distance_now[stt_ut]]]
#                     break
#             if stt_ut == len(list_distance_now)-1:
#                 kt_all = True
#                 break
#                     #print('11111')
#         if kt_ap and kt_all:
#             start_time = route.return_time_now()
#             route.excute(new_point = [data['x_coor'][0],data['y_coor'][0]] , capacity_add = data['demand'][0]\
#                 , earliest_arrival_time = data['earliest_arrival_time'][0],latest_arrival_time = data['latest_arrival_time'][0]\
#                 ,serving_time = data['serving_time'][0])
#             start_time = route.return_time_now()
#             routes.append(route)
#         else:
#             start_time += 1
#         if start_time>max(data['latest_arrival_time']):
#             return routes
#             #break
        
#         #break
#     # for r in routes:
#     #     #pass
#     #     print(r.return_route())
#     return routes

# a = Greedy()
# for i in a:
#     print(i.return_route())

