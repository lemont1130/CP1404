from kivy.app import App
from kivy.lang import Builder
class DynamicweidgetApp(App):
    def build(self):
        self.title = "Dynamic labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root
    def create_widgets(self):
        temp_button=Label(text=name)
        self.root.ids.for_test.add_widget(temp_button)
        temp_button.bind(on_release=self.press_entry)
    def press_entry(self):
        pass
