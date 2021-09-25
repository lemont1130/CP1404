from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from Assignment2.placecollection import PlaceCollection
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
State={'Visited':"V",'Priority':"P",'Country':"C",'Name':"N"}
class TravelTrackerApp(App):
    state_codes = ListProperty()
    current_state = StringProperty()

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.place_list=PlaceCollection()
        self.name_text_input=TextInput(write_tab=False,multiline=False)
        self.country_text_input = TextInput(write_tab=False, multiline=False)
        self.priority_text_input = TextInput(write_tab=False, multiline=False)


    def build(self):
        self.title='TravelTracker'
        self.root=Builder.load_file('app.kv')
        self.place_list.load_place()
        self.state_codes=sorted(State.keys())
        self.current_state=self.state_codes[0]

        return self.root
    def add_place_button(self):
        if str(self.name_text_input.text).strip()=='' or str(self.country_text_input.text).strip()=='' or str(self.priority_text_input.text).strip()=='':
            self.root.ids.output_label2.text='All fields must be completed'
        else:
            try:

                if int(self.priority_text_input.text)<0:
                    self.root.ids.output_label2.text='Priority must be > 0 '
                else:
                    self.place_list.append_place(self.name_text_input.text, self.country_text_input.text, int(self.priority_text_input.text))
            except ValueError:
                self.root.ids.output_label2.text='Please enter a valid number'
    def visit_place(self,button):
        if self.place_list.get_place(button.id).status=='n':
            self.place_list.get_place(button.id).status='v'
            self.root.ids.output_label2.text='You need to visit '+str(self.place_list.get_place(button.id).name)
        else:
            self.place_list.get_place(button.id).status='n'
            self.root.ids.output_label2.text='You visit '+str(self.place_list.get_place(button.id).name)
        self.root.ids.buttonlayout.clear_button()
        self.click_for_visited()

    def click_for_visited(self):
        self.root.ids.output_label1.text='Place to visit:' + str(self.place_list.count_invite_place())
        for place in self.place_list.placelist:
            if place[0].status=='n':
                place_button=Button(text=place[0].name+'in'+place[0].country+','+str(place[0].priority))
                place_button.background_color=[88,89,0,0.3]
            else:
                place_button=Button(text=place[0].name+'in'+place[0].country+','+str(place[0].priority)+'visited')
            place_button.bind(on_release=self.visit_place)
            self.root.ids.buttonlayout.add_widget(place_button)






    def clear_button(self):
        self.root.ids.input_name.text=''
        self.root.ids.input_country.text = ''
        self.root.ids.input_priority.text = ''



if __name__ == '__main__':
    TravelTrackerApp().run()



