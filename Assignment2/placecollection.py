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
    def add_place(self):
        with open('places.csv','w') as in_file:
            for place in self.placelist:
                in_file.write(place[0].name+','+place[0].country+','+place[0].priority+'\n')


