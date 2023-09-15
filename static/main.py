import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('My Awesome App')
        self.geometry('300x500')

        # label
        self.label = ttk.Label(self, text='Hello, User!')
        self.label.grid(row=0, column=0)
        self.label.pack()

        # entry
        self.entry = ttk.Entry(self, width=26)
        # self.entry.grid(row=2, column=2)
        self.entry.place(x=5, y=22)
        # self.entry.pack()

        # button show
        self.button = ttk.Button(self, text='Click Me')
        self.button['command'] = self.show_value
        self.button.place(x=195, y=20)

        # button add
        self.button_add = ttk.Button(self, text='Add')
        self.button_add['command'] = self.add
        self.button_add.place(x=195, y=45)

        self.list_of_smt = ['1', '2']

    def show_value(self):
        self.value = self.entry.get()
        self.label = ttk.Label(self, text=self.value)
        self.label.pack()

    def show_test(self):
        for x in self.list_of_smt:
            self.label = ttk.Label(self, text=x)
            self.label.pack(side='left')

    def add(self):
        self.list_of_smt.append('TEST')


if __name__ == "__main__":
    app = App()
    # app.mainloop()


def test():
    return ['test', 'tset']

print(test()[0])