from prac08.unreliable_car import Unreliablecar
def main():
    car1=Unreliablecar("Car1",100,99)
    car2=Unreliablecar("Car2",100,11)
    car1.drive(10)
    car2.drive(10)
    print(car1)
    print(car2)
main()
