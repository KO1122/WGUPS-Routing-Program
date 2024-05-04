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

# Function to load package data 
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

# Instantiate hash table object and load it with packages 
hash_table = HashTable()
load_package_data('package.csv')

with open("./address.csv") as address_csv:
    address_data = csv.reader(address_csv)
    address_list = list(address_data)

with open("./distance.csv") as distance_csv:
    distance_data = csv.reader(distance_csv)
    distance_list = list(distance_data)   

# Function to get the distance between 2 addresses 
def get_distance_between(address1: int, address2: int) -> float:
    distance = distance_list[address1][address2]
    if distance == '':
        distance = distance_list[address2][address1]
    return float(distance)

# Instantiate truck objects 
packages1 = [1,13,14,15,16,19,20,29,30,31,34,37,40]
truck1 = Truck(1, '4001 South 700 East', 18, 0.0, packages1, datetime.timedelta(hours=8))
packages2 = [3,6,12,17,18,21,22,23,24,26,27,33,35,36,38,39]
truck2 = Truck(2, '4001 South 700 East', 18, 0.0, packages2, datetime.timedelta(hours=9, minutes=5))
packages3 = [2,4,5,7,8,9,10,11,25,28,32]
truck3 = Truck(3, '4001 South 700 East', 18, 0.0, packages3, None)

# Dictionary that maps addresses to their corresponding index number 
addressToIdx = {a[2]:int(a[0]) for a in address_list}

def truck_deliver_packages(truck: Truck):
    # Append package objects to to_deliver array 
    to_deliver = []
    for package_id in truck.packages:
        # Find the package in the hash table 
        package = hash_table.lookup(package_id)
        to_deliver.append(package)

    truck.packages.clear()

    # Get the address with the minimum distance from the current location 
    while to_deliver:
        min_dist = float("inf")
        for package in to_deliver:
            # Package 9 can only be handled after 10:20
            if package.package_id == 9 and truck.total_time < datetime.timedelta(hours=10, minutes=20):
                continue 
            dist = get_distance_between(addressToIdx[truck.current_location], addressToIdx[package.delivery_address])
            if dist < min_dist:
                min_dist = dist
                next_package = package 

        to_deliver.remove(next_package)

        # Update truck attributes once package has been delivered 
        truck.packages.append(next_package.package_id)
        truck.miles += min_dist
        truck.total_time += datetime.timedelta(hours=min_dist/18)
        truck.current_location = next_package.delivery_address
        
        # Update package attributes once package has been delivered 
        next_package.truck = truck.id
        next_package.depart_time = truck.depart_time
        next_package.delivery_time = truck.total_time

truck_deliver_packages(truck1)
truck_deliver_packages(truck2)
truck3.depart_time = truck3.total_time = min(truck1.total_time, truck2.total_time)
truck_deliver_packages(truck3)

def update_package_9(package: Package, time: datetime):
    if package.package_id == 9:
        if time < datetime.timedelta(hours=10, minutes=20):
            package.delivery_address = '300 State St'
            package.delivery_zip_code = 84103
        else:
            package.delivery_address = '410 S State St'
            package.delivery_zip_code = 84111

def main():
    # User Interface 
    while True:
        print()
        print("Welcome to Western Governors University Parcel Service!")
        print("""
Options: 
    1. Print All Package Final Status and Total Mileage
    2. Get a Single Package Status with a Time
    3. Get All Package Status with a Time 
    4. Exit the Program
"""
        )

        num = int(input("Input a number: "))
        if num == 1:
            for i in range(1, 41):
                package = hash_table.lookup(i)
                package.delivery_status = 'delivered'
                update_package_9(package, datetime.timedelta(hours=17))
                print(package)
            mileage = truck1.miles + truck2.miles + truck3.miles
            print(f"The total mileage is {mileage}")
        elif num == 2:
            user_package_id = int(input("Please enter a valid package ID: "))
            user_time = input("Please enter a valid time in the form (HH:MM:SS): ")
            h, m, s = user_time.split(":")
            time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            package = hash_table.lookup(user_package_id)
            package.update_status(time)
            update_package_9(package, time)
            print(package)
        elif num == 3:
            user_time = input("Please enter a valid time in the form (HH:MM:SS): ")
            h, m, s = user_time.split(":")
            time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            for i in range(1, 41):
                package = hash_table.lookup(i)
                package.update_status(time)
                update_package_9(package, time)
                print(package)
        elif num == 4:
            exit()
        else:
            print("Enter a valid number!!!")
            
main()