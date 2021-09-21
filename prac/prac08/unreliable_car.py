from prac.prac08.car import Car
import random
class Unreliablecar(Car):
    def __init__(self,name,fuel,reliability):
        super().__init__(name,fuel)
        self.reliability=int(reliability)
    def __str__(self):
        return f"{super().__str__()}"

    def drive(self, distance):
        number=random.randint(0,100)
        if number > self.reliability:
            distance=0
        distance_driven = super().drive(distance)
        return distance_driven

