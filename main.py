"""
Name: Kyle Radcliffe Ong
Student ID: 010523715
Email: kong5@wgu.edu
"""
from hash_table import HashTable
from package import Package
import csv

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
            delivery_time = None

            package = Package(package_id, 
                              delivery_address, 
                              delivery_city, 
                              delivery_state,
                              delivery_zip_code,
                              delivery_deadline,
                              package_weight,
                              delivery_notes,
                              delivery_status,
                              delivery_time)
            
            hash_table.insert(package_id, package)

def load_distance_data(csv_file):
    pass

def load_address_data(csv_file):
    pass

hash_table = HashTable()
load_package_data('package.csv')
# for i in range(len(hash_table.array) + 1):
#     print(f"Key: {i+1}, Value: {hash_table.get(i+1)}")