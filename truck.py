from typing import List
from package import Package
import datetime
class Truck:
    def __init__(self, id: int, current_location: str, speed: int, miles: float, packages: List[Package], time: datetime):
        self.id = id
        self.current_location = current_location 
        self.speed = speed
        self.miles = miles 
        self.packages = packages 
        self.depart_time = time
        self.total_time = time
    
    def __str__(self) -> str:
        return (
            f"{self.id} {self.current_location} {self.speed} " +
            f"{self.miles} {self.packages} {self.depart_time} " +
            f"{self.total_time}"
        )