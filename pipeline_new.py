from core.core import *
import numpy as np
import time
def pipeline(path_data_point='data/VRPTW_data_sample_1.xlsx', path_data_vehicle = 'data/VRPTW_data_sample_vehicle_list.xlsx',time_waiting_max = 0):
    data = read_xlsx(path_data_point)
    vehicle_data = read_xlsx(path_data_vehicle)
    ### constant
    capacity = 200
    speed = 1
    number_point = len(data)
    point = np.zeros(number_point)
    point[0] = 1
    depot = [data['x_coor'][0],data['y_coor'][0]]

    def list_distance(point_1, points):
        distances = []
        for i in points:
            distances.append(distance(point_1[0],point_1[1],i[0],i[1]))

        return sorted(range(len(distances)), key=lambda k: distances[k])

    # route1 = Route(start_point = depot, start_time = 0, depot_start_time = 0, depot_end_time = 230, capacity = 200, capacity_now = 0)
    # print(route1.return_route())

    def remaining_point():
        #print(point)
        index_process = []
        for i in range(len(point)):
            if point[i] == 0:
                index_process.append(i)
        #print(index_process)
        return index_process

    def check_remaining_point():
        for i in range(len(point)):
            if point[i] == 0:
                return True
        return False
    #print(depot[0])
    def Run(): 
        st_time = time.time()
        start_time = 0

        start_point = depot
        while check_remaining_point():
            route = Route(start_point = depot, start_time = start_time, depot_start_time = 0, depot_end_time = 230, capacity = 200,speed = speed,time_waiting_max = time_waiting_max)
            add_first = 1
            kt_ap = False
            while check_remaining_point():
                points = []
                list_distance_now = []
                vt = remaining_point()
                for i in vt:
                    points.append([data['x_coor'][i],data['y_coor'][i]])
                list_distance_now_tmp = list_distance(start_point,points)
                for _ in list_distance_now_tmp:
                    list_distance_now.append(vt[_])
                #print(list_distance_now)
                #new_point = [data['x_coor'][list_distance_now[0]],data['y_coor'][list_distance_now[0]]]
                #print((depot[0] - new_point[0])**2 + (depot[1]- new_point[1])**2)
            
                kt_all = False
                for stt_ut in range(len(list_distance_now)):
                    if route.excute(new_point = [data['x_coor'][list_distance_now[stt_ut]],data['y_coor'][list_distance_now[stt_ut]]] , capacity_add = data['demand'][list_distance_now[stt_ut]]\
                    , earliest_arrival_time = data['earliest_arrival_time'][list_distance_now[stt_ut]],latest_arrival_time = data['latest_arrival_time'][list_distance_now[stt_ut]]\
                    ,serving_time = data['serving_time'][list_distance_now[stt_ut]]):
                        #print([data['x_coor'][list_distance_now[stt_ut]+1],data['y_coor'][list_distance_now[stt_ut]+1]])
                        #print(point[list_distance_now[stt_ut]+1])
                        if route.return_time_waiting_max() > 0:
                            route.append_sum_time_waiting()
                        point[list_distance_now[stt_ut]] = 1
                        kt_ap = True
                        start_point = [data['x_coor'][list_distance_now[stt_ut]],data['y_coor'][list_distance_now[stt_ut]]]
                        route.reset_time_waiting()
                        add_first = 1
                        break
                        
                if stt_ut == len(list_distance_now)-1 and not(route.check_time_waiting()):
                    kt_all = True
                    break
                        #print('11111')
                
                
                if stt_ut == len(list_distance_now)-1 and route.check_time_waiting():
                    if add_first == 1:
                        time_old = route.return_time_now()
                        add_first = 0
                    route.add_time_waiting()
            if (kt_ap and kt_all) or (kt_ap and not route.check_time_waiting) :
                start_time = route.return_time_now()
                if route.return_time_waiting_max() > 0:
                    route.set_time_now(time_old)
                route.excute_depot(new_point = [data['x_coor'][0],data['y_coor'][0]] , capacity_add = data['demand'][0]\
                    , earliest_arrival_time = data['earliest_arrival_time'][0],latest_arrival_time = data['latest_arrival_time'][0]\
                    ,serving_time = data['serving_time'][0])
                start_time = route.return_time_now()
                return route
                #routes.append(route)
            else:
                start_time += 1
            #print('aaaaaaaaaaaaa',max(data['latest_arrival_time']))
            if start_time>max(data['latest_arrival_time']):
                #print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
                # route.excute_depot(new_point = [data['x_coor'][0],data['y_coor'][0]] , capacity_add = data['demand'][0]\
                #     , earliest_arrival_time = data['earliest_arrival_time'][0],latest_arrival_time = data['latest_arrival_time'][0]\
                #     ,serving_time = data['serving_time'][0])
                return route

        if not check_remaining_point():
            route.excute_depot(new_point = [data['x_coor'][0],data['y_coor'][0]] , capacity_add = data['demand'][0]\
                    , earliest_arrival_time = data['earliest_arrival_time'][0],latest_arrival_time = data['latest_arrival_time'][0]\
                    ,serving_time = data['serving_time'][0])
        
        return route



    ##################################################### vehicle
    vehicles = []
    for i in range(len(vehicle_data)):
        vehicle_now = Vihicle(vehicle_data['vehicle_id'][i], vehicle_data['capacity'][i], vehicle_data['start_point_id'][i])
        vehicles.append(vehicle_now)

    while check_remaining_point():
        st_time = time.time()
        route = Run()
        kt = 0
        for vehicle in vehicles:
            if vehicle.check_time_busy([route.return_start_time(),route.return_time_now()]):
                vehicle.add_route(route)
                kt = 1
                break
        if kt == 0:
            print('all vehicle busy')
        if time.time() - st_time > 10:
            break
    return vehicles,point