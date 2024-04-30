"""
Name: Kyle Radcliffe Ong
Student ID: 010523715
Email: kong5@wgu.edu
"""
import datetime
from typing import List
import csv
from hash_table import HashTable
from package import Package
from truck import Truck

def load_package_data(csv_file: str) -> None:
    with open(csv_file) as packages:
        package_data = csv.reader(packages, delimiter=',')
        next(package_data) # skip header 

        for package in package_data:
            package_id = int(package[0])
            delivery_address = package[1]
            delivery_city = package[2]
            delivery_state = package[3]
            delivery_zip_code = int(package[4])
            delivery_deadline = package[5]
            package_weight = int(package[6])
            delivery_notes = package[7]
            delivery_status = 'at the hub'

            package = Package(package_id, 
                              delivery_address, 
                              delivery_city, 
                              delivery_state,
                              delivery_zip_code,
                              delivery_deadline,
                              package_weight,
                              delivery_notes,
                              delivery_status)
            
            hash_table.insert(package_id, package)

hash_table = HashTable()
load_package_data('package.csv')
# for i in range(len(hash_table.array)):
#     print(f"Key: {i+1}, Value: {hash_table.get(i+1)}")

with open("./address.csv") as address_csv:
    address_data = csv.reader(address_csv)
    address_list = list(address_data)

with open("./distance.csv") as distance_csv:
    distance_data = csv.reader(distance_csv)
    distance_list = list(distance_data)   

def get_distance_between(address1: int, address2: int) -> float:
    distance = distance_list[address1][address2]
    if distance == '':
        distance = distance_list[address2][address1]
    return float(distance)

def get_min_distance_from(address, truck_packages):
    min_dist = float("inf")
    for package in truck_packages:
        dist = get_distance_between(address, package.delivery_address) 
        min_dist = min(min_dist, dist)
    return min_dist 

packages1 = [1,13,14,15,16,19,20,29,30,31,34,37,40]
truck1 = Truck('4001 South 700 East', 18, 0.0, packages1, datetime.timedelta(hours=8))
packages2 = [3,6,12,17,18,21,22,23,24,26,27,33,35,36,38,39]
truck2 = Truck('4001 South 700 East', 18, 0.0, packages2, datetime.timedelta(hours=9, minutes=5))
packages3 = [2,4,5,7,8,9,10,11,25,28,32]
truck3 = Truck('4001 South 700 East', 18, 0.0, packages3, None)

# idxToAddress = {int(a[0]):a[2] for a in address_list}
addressToIdx = {a[2]:int(a[0]) for a in address_list}
def truck_deliver_packages(truck: Truck):
    to_deliver = []
    for package_id in truck.packages:
        package = hash_table.get(package_id)
        to_deliver.append(package)

    truck.packages.clear()
    while to_deliver:
        min_dist = float("inf")
        for package in to_deliver:
            dist = get_distance_between(addressToIdx[truck.current_location], addressToIdx[package.delivery_address])
            if dist < min_dist:
                min_dist = dist
                next_package = package 

        to_deliver.remove(next_package)

        truck.packages.append(next_package.package_id)
        truck.miles += min_dist
        truck.time += datetime.timedelta(hours=min_dist/18)
        truck.current_location = next_package.delivery_address
        
        next_package.depart_time = truck.depart_time
        next_package.delivery_time = truck.time

truck_deliver_packages(truck1)
truck_deliver_packages(truck2)
truck3.depart_time = truck3.time = min(truck1.time, truck2.time)
truck_deliver_packages(truck3)