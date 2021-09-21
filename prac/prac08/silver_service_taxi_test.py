from prac.prac08.silver_service_taxi import Silverservicetaxi
def main():
    car1=Silverservicetaxi("Car1",100,35)
    car1.drive(15)
    print(car1)
    print(car1.get_fare())
    car2=Silverservicetaxi("Car2",100,11)
    car2.drive(18)
    print(car2)
    print(car2.get_fare())
main()
