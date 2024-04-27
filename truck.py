class Truck:
    def __init__(self, current_location, speed, miles, packages, depart_time):
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