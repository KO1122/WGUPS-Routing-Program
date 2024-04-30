from typing import List
from package import Package
import datetime
class Truck:
    def __init__(self, current_location: str, speed: int, miles: float, packages: List[Package], depart_time: datetime):
        self.current_location = current_location 
        self.speed = speed
        self.miles = miles 
        self.packages = packages 
        self.depart_time = depart_time
        self.time = depart_time
    
    def __str__(self) -> str:
        return (
            f"{self.current_location} {self.speed} " +
            f"{self.miles} {self.packages} " +
            f"{self.depart_time} {self.time}"
        )