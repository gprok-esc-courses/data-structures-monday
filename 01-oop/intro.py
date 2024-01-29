
class Car:
    def __init__(self, plate: str, km: float) -> None:
        self.plate = plate
        self.km = km

    def __str__(self) -> str:
        return self.plate + ", km:" + str(self.km)
    
class Bus(Car):
    def __init__(self, plate: str, km: float, passengers: int) -> None:
        super().__init__(plate, km)
        self.passengers = passengers
    
    def __str__(self) -> str:
        return super().__str__() + " seats: " + str(self.passengers)


a = Car("ABX5612", 2009)
b = Car("ZXB9012", 21091)
c = Bus("TAA7609", 1098, 45)

print(a)
print(b)
print(c)
