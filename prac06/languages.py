from prac06.programming_language import Programminglanguage
def main():
    ruby = Programminglanguage("Ruby", "Dynamic", True, 1995)
    python = Programminglanguage("Python", "Dynamic", True, 1991)
    visual_basic = Programminglanguage("Visual Basic", "Static", False, 1991)
    language_list = [ruby, python, visual_basic]
    print("The dynamically type languages are: ")
    for language in language_list:
        if language.is_dynamic():
            print(language.language)
main()

