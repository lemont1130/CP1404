from kivy.app import App
from kivy.lang import Builder
class ConvertmilestokmApp(App):
    def build(self):
        self.title = "Convert miles to km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root
    def handle_calculate(self,value):
        result=value/1000
        self.root.ids.output_label.text=str(result)
    def handle_increment(self,change):
        num=float(self.root.ids.input_number.text)+float(change)
        self.root.ids.input_number.text=str(num)
    def check_input(self,text):
        if text>0 or text!=" ":
            return float(text)
        else:
            return 0.0


ConvertmilestokmApp().run()





