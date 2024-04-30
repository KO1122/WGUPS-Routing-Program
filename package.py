import datetime

class Package:
    def __init__(self, package_id: int, 
                       delivery_address: str, 
                       delivery_city: str, 
                       delivery_state: str, 
                       delivery_zip_code: int, 
                       delivery_deadline: str,
                       package_weight: int, 
                       delivery_notes: str,
                       delivery_status: str):

        self.package_id = package_id
        self.delivery_address = delivery_address
        self.delivery_city = delivery_city
        self.delivery_state = delivery_state
        self.delivery_zip_code = delivery_zip_code
        self.delivery_deadline = delivery_deadline
        self.package_weight = package_weight
        self.delivery_notes = delivery_notes
        self.delivery_status = delivery_status
        self.depart_time = None
        self.delivery_time = None

    def __str__(self) -> str:
        return (
            f"{self.package_id} {self.delivery_address} " +
            f"{self.delivery_city} {self.delivery_state} " +
            f"{self.delivery_zip_code} {self.delivery_deadline} " + 
            f"{self.package_weight} {self.delivery_notes} " + 
            f"{self.delivery_status} {self.depart_time} " + 
            f"{self.delivery_time}" 
        )
    
    def update_status(self, time: datetime):
        if self.delivery_time < time:
            self.delivery_status = "delivered"
        elif self.depart_time > time:
            self.delivery_status = "en route"
        else:
            self.status = "at the hub" 