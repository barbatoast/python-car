#!/usr/bin/env python3

class Car:
    def __init__(self, owner, mpwh, distance):
        self.owner = owner
        self.mpwh = mpwh
        self.distance = distance

    def get_owner(self):
        return self.owner

    def get_mpwh(self):
        return self.mpwh

    def get_distance(self):
        return self.distance

    def set_mpwh(self, mpwh):
        self.mpwh = mpwh
    
    def compute_distance_km(self):
        distance_miles = self.get_distance()
        distance_km = distance_miles * 1.6
        return distance_km

    def compute_kwh(self):
        miles = self.get_distance()
        mpwh = self.get_mpwh()
        wh = miles / mpwh
        kwh = wh / 1000
        return kwh

    def compute_kmpkwh(self):
        km = self.compute_distance_km()
        kwh = self.compute_kwh()
        kmpkwh = km / kwh
        return kmpkwh


if __name__ == '__main__':
    car = Car('Elon', 0.003, 400)
    print('The car owner is %s' %   \
        (car.get_owner()))
    print('The car gets %f miles per watt-hour' %   \
        (car.get_mpwh()))
    print('%s has driven the car %d miles' %    \
        (car.get_owner(), car.get_distance()))
    print('%s has driven the car %d kilometers' %   \
        (car.get_owner(), car.compute_distance_km()))
    print('The car has consumed %d kilowatt-hours' %    \
        (car.compute_kwh()))
    print('The car gets %d kilometers per kilwatt-hour' %   \
        (car.compute_kmpkwh()))