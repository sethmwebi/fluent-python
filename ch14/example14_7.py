import tkinter
def print_mro(cls):
    print(', '.join(c.__name__ for c in cls.__mro__))
print_mro(tkinter.Text)
