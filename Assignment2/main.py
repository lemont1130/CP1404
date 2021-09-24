from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from Assignment2.placecollection import PlaceCollection
State={'Visited':"V",'Priority':"P",'Country':"C",'Name':"N"}
class TravelTrackerApp(App):
    state_codes = ListProperty()
    current_state = StringProperty()

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.place_list=PlaceCollection()

    def build(self):
        self.title='TravelTracker'
        self.root=Builder.load_file('app.kv')
        self.place_list.load_place()
        self.state_codes=sorted(State.keys())
        self.current_state=self.state_codes[0]

        return self.root

if __name__ == '__main__':
    TravelTrackerApp().run()



