from prac.prac06.guitar import guitar
def test():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40
    Guitar=guitar(name,year,cost)
    anotherguitar=guitar("Another Guitar",2013,12345)
    print(f"{Guitar.name} get_age() - Expected {99}. Got {Guitar.get_age()}")
    print(f"{anotherguitar.name} get_age() - Expected {8}. Got {anotherguitar.get_age()}")
    print(f"{Guitar.name} is_vintage() - Expected {True}. Got {Guitar.is_vintage()}")
    print(f"{anotherguitar.name} is_vintage() - Expected {False}. Got {anotherguitar.is_vintage()}")
