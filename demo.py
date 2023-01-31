from pipeline_new import pipeline

vehicles,point = pipeline(path_data_point='data/VRPTW_data_sample_1.xlsx', path_data_vehicle = 'data/VRPTW_data_sample_vehicle_list.xlsx',time_waiting_max = 1236)
sum_distance = 0
xe = 0
for i in vehicles:
    xe+=1
    for j in i.return_route():
        print("xe ",xe," Thời gian khởi hành: ",j.return_time_first_start(),' ',j.return_route())
        print("thời gian đến: ",j.return_time_arrival())
        print("Tải hiện tại: ",j.return_list_capacity())
        print("Thời gian đợi: ",j.return_sum_time_waiting())
        #print(j.return_distance_cost())
        sum_distance += j.return_distance_cost()
    
kt = 1
for i in point:
    if i != 1:
        kt = 0
        break
if kt == 1:
    print("tất cả các điểm được phục vụ")
print("Tổng quãng đường tất cả các xe di chuyển: ",sum_distance)

