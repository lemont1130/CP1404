import random
import csv
place=[]
def main():
    file_input=open("places.csv","r")
    read_place=file_input.readlines()
    for p in read_place:
        Place=p.strip().split(',')
        place.append(Place)
    file_input.close()
    print(f"Travel Tracker 1.0 - by Yizhen Chen  {len(place)} places loaded from places.csv")
    choose=Menu()
    while choose!="Q":
        if choose=="L":
            List_place(place)
            choose=Menu()
        elif choose=="R":
            recommend_random_place(place)
            choose=Menu()
        elif choose=="A":
            place.append(Add_new_place())
            choose=Menu()
        elif choose=="M":
            count_v=0
            for i in range (len(place)):
                if "v" in place[i][3]:
                    count_v+=1
            if count_v== len(place):
                print("No places left to visit!")
            else:
                Mark_place_as_visited(place)
            choose=Menu()
        else:
            print("Invalid menu choice")
            choose=Menu()
    Quit(place)



def List_place(place):
    i=0
    not_visited=0
    while i < len(place):
        if place[i][3]=="n":
            print(f"*{i+1}.  {place[i][0]:10} in {place[i][1]:10} {place[i][2]}" )
            not_visited+=1
        else:
            print(f" {i+1}.  {place[i][0]:10} in {place[i][1]:10} {place[i][2]}")
        i+=1
    print(f"{len(place)} places. You still want to visit {not_visited} places")
def recommend_random_place(place):
    print("Not sure where to visit next?")
    randonnumber=random.randint(0,len(place)-1)
    print(f"How about... {place[randonnumber][0]} in {place[randonnumber][1]}")
def Add_new_place():
    new_place=[]
    name=input("Name:")
    while name=="":
        print("Input can not be blank.")
        name=input("Name:")
    new_place.append(name)
    country=input("Country:")
    while country=="":
        print("Input can not be blank.")
        country=input("Country:")
    new_place.append(country)
    priority=int(input("Priority:"))
    new_place.append(priority)
    new_place.append('n')
    print(f"{name} in {country} (priority {priority}) add to Travel Tracker")
    return new_place
def Mark_place_as_visited(place):
    while True:
        print(List_place(place))
        visited=int(input("Enter the number of a place to mark as visited\n>>>"))-1
        if 'v' in place[visited]:
            print(f"You have already visited {place[visited][0]}")
            continue
        elif visited<0:
            print("Number must be > 0")
            continue
        elif visited>len(place):
            print("Invalid place number")
            continue
        break
    place[visited][3]='v'
    print(f"{place[visited][0]} in {place[visited][1]} visited ")
    return place
def Quit(place):
    print(f"{len(place)} places saved to travel tracker\n Have a nice day :)")
    out_file=open("places.csv",'w',newline='')
    writer=csv.writer(out_file)
    writer.writerows(place)
    out_file.close()
def Menu():
    menu='''Menu
            L- List place
            R - Recommend random place
            A - Add new place
            M - Mark a place as visited
            Q - Quit'''
    print(menu)
    choose=input(">>> ").upper()
    return choose


main()

