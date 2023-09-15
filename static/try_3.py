import random
import tkinter as tk
from tkinter import ttk


root = tk.Tk()

# ------------------------ STYLING
s = ttk.Style()
s.configure('Frame.TFrame', background='#417D7A')
s.configure('Label.TLabel',
            background='#F7FF93',
            font=('Helventica', 14),
            foreground='blue',
            padding=(15, 6, 15, 6)
            )

# ------------------------ WIDGET
mainFrame = ttk.Frame(root, width=250, height=250, style='Frame.TFrame')
mainFrame.grid(row=0, column=0, sticky='NSEW')

greetingLabel = ttk.Label(mainFrame, text='Welcome User', style='Label.TLabel')
greetingLabel.grid(row=0, column=0, padx=10, pady=10, sticky='WE')

# ------------------------ GRID CONFIGURATIONS
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainFrame.columnconfigure(0, weight=1)

# ------------------------ LOOP
root.mainloop()


