from pipeline_new import pipeline

def demo(path_data_point='data/VRPTW_data_sample_2.xlsx', path_data_vehicle = 'data/VRPTW_data_sample_vehicle_list.xlsx',time_waiting_max = 1236):
    vehicles,point = pipeline(path_data_point, path_data_vehicle ,time_waiting_max)
    sum_distance = 0
    xe = 0
    results = ''
    for i in vehicles:
        xe+=1
        for j in i.return_route():
            results += "xe "+str(xe) +" Thời gian khởi hành: "+str(j.return_time_first_start())+' '+str(j.return_route())
            results += "thời gian đến: "+str(j.return_time_arrival())
            results += "Tải hiện tại: "+str(j.return_list_capacity())
            results += "Thời gian đợi: "+str(j.return_sum_time_waiting())
            #print(j.return_distance_cost())
            sum_distance += j.return_distance_cost()
        
    kt = 1
    for i in point:
        if i != 1:
            kt = 0
            break
    if kt == 1:
        results += "tất cả các điểm được phục vụ"
    results += "Tổng quãng đường tất cả các xe di chuyển: " + str(sum_distance)

    return results

