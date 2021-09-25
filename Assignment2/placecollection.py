import csv

from Assignment2.place import Place
class PlaceCollection:
    def __init__(self):
        self.placelist=[]
    def append_place(self,name,country,priority):
        self.placelist.append(Place(name,country,priority,'n'))
    def load_place(self):
        filereader= open('places.csv','r')
        for place in filereader:
            place_string=place.split(',')
            self.placelist.append([Place(place_string[0],place_string[1],int(place_string[2]),place_string[3].strip())])
        filereader.close()

    def add_place(self):
        filewriter=open('places.csv','w')
        writer=csv.writer(filewriter)
        writer.writerows(self.placelist)
        filewriter.close()
    def count_invite_place(self):
        place_to_invite=0
        for place in self.placelist:
            if place[0].status=='n':
                place_to_invite+=1
        return place_to_invite
    def get_place(self,name):
        for place in self.placelist:
            if place[0].name==name:
                return place[0]




