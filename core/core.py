import pandas as pd
from math import sqrt

def read_xlsx(path):
    data =pd.read_excel(path)
    return data

def distance(x1,y1,x2,y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

class Route:
    def __init__(self, start_point, start_time, depot_start_time, depot_end_time, capacity, capacity_now = 0, speed=1):
        self.start_point = start_point
        self.start_time = start_time
        self.depot_start_time = depot_start_time
        self.depot_end_time = depot_end_time
        self.time_now = start_time
        self.point_now = start_point
        self.list_point = []
        self.list_point.append(start_point)
        self.capacity = capacity
        self.capacity_now = capacity_now
        self.speed = speed 
        self.time_first_start = -1

    def distance_point(self,point1,point2):
        return sqrt((point1[0] - point2[0])**2 + (point1[1]- point2[1])**2)

    def check_capacity(self, capacity_add):
        if self.capacity_now + capacity_add > self.capacity:
            return False
        else:
            return True

    def check_time(self, new_point, earliest_arrival_time,latest_arrival_time):
        trip_time = self.distance_point(self.point_now,new_point)/self.speed
        if self.time_now + trip_time > latest_arrival_time or self.time_now + trip_time < earliest_arrival_time:
            return False
        else:
            return True

    def excute(self, new_point, capacity_add, earliest_arrival_time,latest_arrival_time,serving_time):
        trip_time = self.distance_point(self.point_now,new_point)/self.speed
        if self.check_capacity(capacity_add) and self.check_time(new_point, earliest_arrival_time,latest_arrival_time):
            self.list_point.append(new_point)
            self.point_now = new_point
            #print(trip_time)
            self.time_now = self.time_now + trip_time + serving_time
            self.capacity_now = self.capacity_now + capacity_add
            if self.time_first_start == -1 :
                self.time_first_start = self.time_now - serving_time
            return True
        else:
            #print(new_point)
            return False
    def return_time_now(self):
        return self.time_now
        
    def return_route(self):
        return self.list_point 
    def return_start_time(self):
        return self.start_time 
    def return_time_now(self):
        return self.time_now 
    def return_time_first_start(self):
        return self.time_first_start


class Vihicle:
    def __init__(self, vehicle_id, capacity, start_point_id):
        self.vehicle_id = vehicle_id
        self.capacity = capacity
        self.start_point_id = start_point_id
        self.route = []
        self.time_busy = []
        self.new = 1
    def check_time_busy(self,new_time):
        if self.new ==1 :
            return True
        for time in self.time_busy:
            #print(time[1])
            #print(new_time[0])
            if time[1]>=new_time[0] and time[1]<=new_time[1] or new_time[1]>=time[0] and new_time[1]<=time[1]:
                return False
            if time[0]>=new_time[0] and time[1]<=new_time[1] or new_time[0]>=time[0] and new_time[1]<=time[1]:
                return False
            
        return True

    def add_route(self,route):
        new_time = [route.return_start_time(),route.return_time_now()]
        if self.check_time_busy(new_time):
            self.time_busy.append(new_time)
            self.new = 0
            self.route.append(route)
            return True
        else:
            return False
    def return_route(self):
        return self.route


        
