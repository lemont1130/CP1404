class Programminglanguage:
    def __init__(self,language,typing,reflection,year):
        self.language=language
        self.typing=typing
        self.reflection=reflection
        self.year=year
    def is_dynamic(self):
        return self.typing=="Dynamic"
    def __str__(self):
        return f"{self.language}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
    def running(self):
        ruby = Programminglanguage("Ruby", "Dynamic", True, 1995)
        python = Programminglanguage("Python", "Dynamic", True, 1991)
        visual_basic = Programminglanguage("Visual Basic", "Static", False, 1991)
        language_list=[ruby,python,visual_basic]
        print("The dynamically type languages are: ")
        for language in language_list:
            if language.is_dynamic():
                print(language.language)


