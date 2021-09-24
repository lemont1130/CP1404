import csv

from Assignment2.place import Place
class PlaceCollection:
    def __init__(self):
        self.placelist=[]
    def append_place(self,name,country,priority):
        self.placelist.append(Place(name,country,priority,'n'))
    def load_place(self):
        with open('places.csv','r')as in_file:
            placesreader=csv.reader(in_file)
            for place in placesreader:
                place_str=place.split(',')
                self.placelist.append([Place(place_str[0],place_str[1],place_str[2],place_str[3].strip())])


