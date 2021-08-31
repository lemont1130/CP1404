from prac06.guitar import guitar
def main():
    guitar_list=[]
    print("My Guitars!")
    name=input("Name: ")
    while name!="":
        year=input("Year: ")
        cost=int(input("Cost: $"))
        Guitars=guitar(name,year,cost)
        guitar_list.append(Guitars)
        print(Guitars,  "added")
        name=input("Name: ")
    guitar_list.append(guitar("Gibson L-5 CES", 1922, 16035.40))
    guitar_list.append(guitar("Line 6 JTV-59", 2010, 1512.9))
    print("There are my guitars: ")
    for i,Guitar in enumerate(guitar_list):
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f}".format(i + 1, Guitar.name, Guitar.year, Guitar.cost))
main()

