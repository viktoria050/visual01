class Car:
    def __init__(self, make, model, year):
        self.make = make  
        self.model = model  
        self.year = year  

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"  


my_car = Car("BMW", "X5", 2023 )
print(my_car.get_info())  