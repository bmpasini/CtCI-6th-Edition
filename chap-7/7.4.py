# Design a parking lot using object-oriented principles.

from datetime import datetime

class ParkingLot(object):

    def __init__(self):
        self.floors = dict()
        self.receipts = dict()

    def set_vehicle_capacity(self, floor_number, _type, capacity):
        floor = self.floors[floor_number]
        floor.set_vehicle_capacity(_type, capacity)

    def set_vehicle_count(self, floor_number, _type, count):
        floor = self.floors[floor_number]
        floor.set_vehicle_count(_type, count)

    def new_recipt(self, vehicle_type, vehicle_plate=None, vehicle_make=None, vehicle_model=None):
        _id = len(receipts)+1
        self.receipts[_id] = Receipt(_id, vehicle_type, vehicle_plate, vehicle_make, vehicle_model)

    def close_recipt(self, _id):
        self.receipts[_id].end_hour = datetime.now()

    def park_vehicle(self, _type, floor_number):
        self.floors[floor_number].park_vehicle(_type)

    def unpark_vehicle(self, _type):
        self.floors[floor_number].unpark_vehicle(_type)


class Floor(object):

    def __init__(self):
        self.vehicle_capacity = {
                                    "Car" : 0,
                                    "Motorcycle" : 0,
                                    "Bike" : 0,
                                }
        self.vehicle_count    = {
                                    "Car" : 0,
                                    "Motorcycle" : 0,
                                    "Bike" : 0,
                                }

    def set_vehicle_capacity(self, _type, capacity):
        self.vehicle_capacity[_type] = capacity

    def set_vehicle_count(self, _type, count):
        self.vehicle_count[_type] = count

    def park_vehicle(self, _type):
        self.vehicle_count[_type] += 1

    def unpark_vehicle(self, _type):
        self.vehicle_count[_type] -= 1


class Vehicle(object):

    def __init__(self, _id, _type):
        self.id = _id
        self.costs = {
                          "Car" : Cost(),
                          "Motorcycle" : Cost(),
                          "Bike" : Cost(),
                     }

    def change_costs(self, _type,
                           first_hour=20,
                           first_two_hours=35,
                           additional_hour=10,
                           twelve_hours=60,
                           day=100,
                           week=400,
                           month=800,
                           year=5000):
        self.costs[_type].first_hour = first_hour
        self.costs[_type].first_two_hours = first_two_hours
        self.costs[_type].additional_hour = additional_hour
        self.costs[_type].twelve_hours = twelve_hours
        self.costs[_type].day = day
        self.costs[_type].week = week
        self.costs[_type].month = month
        self.costs[_type].year = year

    def apply_discount(self, _type, percentage):
        pass


class Cost(object):

    def __init__(self):
        self.first_hour = 20
        self.first_two_hours = 35
        self.additional_hour = 10
        self.twelve_hours = 60
        self.day = 100
        self.week = 400
        self.month = 800
        self.year = 5000

    def apply_discount(self, percentage):
        pass


class Receipt(object):

    def __init__(self, vehicle_type, vehicle_plate=None, vehicle_make=None, vehicle_model=None):
        self._id = _id
        self.vehicle_type = vehicle_type
        self.vehicle_plate = vehicle_plate
        self.vehicle_make = vehicle_make
        self.vehicle_model = vehicle_model
        self.start_hour = datetime.now()
        self.end_hour = None

    def get_cost(self):
        pass





