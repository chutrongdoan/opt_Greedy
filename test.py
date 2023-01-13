from pipeline import pipeline

vehicles,point = pipeline(path_data_point='data_anh_Son/VRPTW_data_sample_1.xlsx', path_data_vehicle = 'data_anh_Son/VRPTW_data_sample_vehicle_list.xlsx')

xe = 0
for i in vehicles:
    xe+=1
    for j in i.return_route():
        print("xe ",xe," Thời gian khởi hành: ",j.return_time_first_start(),' ',j.return_route())
kt = 1
for i in point:
    if i != 1:
        kt = 0
        break
if kt == 1:
    print("tất cả các điểm được phục vụ")

