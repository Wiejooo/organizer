import tkinter as tk
from tkinter import ttk

root = tk.Tk()

list_of_orders = []

list_of_no_orders = list_of_orders.copy()

list__of_own_orders = []


# ------------------------ FUNCTIONS


def show_value_left_mid():
    value = entry_orders_list.get()
    list_of_orders.append(value)
    for order in list_of_orders:
        order_number_left = ttk.Label(left_data, text=order)
        # order_number.grid(row=2, column=0, sticky='WN')
        order_number_left.pack()

    for order in list_of_orders:
        order_number_mid = ttk.Label(mid_area, text=order, width=50)
        order_number_mid.pack()


def test():
    current_left_side = left_data.cget('text')
    input_value = entry_orders_list.get()
    update_order = current_left_side + input_value
    left_data.configure(text=update_order)


def show_value_on_right():
    value = entry_order.get()
    order_number = ttk.Label(root, text=value)
    order_number.grid(row=2, column=2, sticky='WN')


def clear_left_value():
    entry_orders_list.delete(0, 'end')


def clear_right_value():
    entry_order.delete(0, 'end')


# ------------------------ STYLING
s = ttk.Style()
s.configure('label_area.TFrame', background='#839de9')
s.configure('button_area.TFrame', background='#CE18C9')
s.configure('input_area.TFrame', background='#cdced2')
s.configure('show_area.TFrame', background='#686868')
# s.configure('left_data.TFrame', background='#b1b2b5')
s.configure('Label.TLabel', background='#839de9', font=('Helventica', 14))
s.configure('left_data.TLabel',
            # background="#4A4A48",
            # font=('Helvetica', 12),
            # foreground="white",
            # wraplength=170,
            # anchor="nw",
            # padding=(3, 3, 3, 3)
            )

# ------------------------ GRID CONFIGURATIONS
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)
#
# root.columnconfigure(1, weight=1)
# root.rowconfigure(1, weight=1)

# ------------------------ WIDGET
# --- title
# label
title_area = ttk.Frame(root, width=900, height=40, style='label_area.TFrame')
title_area.grid(row=0, column=0, columnspan=3, sticky='NSEW')

title = ttk.Label(title_area, text='Welcome User', style='Label.TLabel')
title.pack(padx=10, pady=10)

# --- left side
left_side_area = ttk.Frame(root, width=300, height=100, style='input_area.TFrame')
left_side_area.grid(row=1, column=0, rowspan=2, sticky='NS')

# label
title_left_side = ttk.Label(left_side_area, text='Entry the list', background='#cdced2')
title_left_side.grid(row=0, column=0, columnspan=2, pady=5)

# entry
entry_orders_list = ttk.Entry(left_side_area, width=31)
entry_orders_list.grid(row=1, column=0, rowspan=1, padx=10, pady=10, sticky='NS')

# buttons
submit_button_left = ttk.Button(left_side_area, text='Submit', command=test)
submit_button_left.grid(row=1, column=1, padx=5)

clear_button_left = ttk.Button(left_side_area, text='Clear')
clear_button_left['command'] = clear_left_value
clear_button_left.grid(row=2, column=1, padx=5)

# left side
left_data = ttk.Label(left_side_area, text='QWERTY')
left_data.grid(row=3, column=0, columnspan=2, sticky='NSEW')

# testtt = ttk.Label(left_side_area, text='100000')
# testtt.grid(row=3, column=0,)


# --- show mid area
mid_area = ttk.Frame(root, width=300, height=400, style='show_area.TFrame')
mid_area.grid(row=1, column=1, rowspan=2, sticky='NSEW')

# --- right area
right_side_area = ttk.Frame(root, width=300, height=70, style='input_area.TFrame')
right_side_area.grid(row=1, column=2, sticky='NS')

# label
title_right_side = ttk.Label(right_side_area, text='Entry number', background='#cdced2')
title_right_side.grid(row=0, column=0, columnspan=2, pady=5)

# entry
entry_order = ttk.Entry(right_side_area, width=31)
entry_order.grid(row=1, column=0, rowspan=1, padx=10, pady=10, sticky='NS')

# buttons
submit_button_right = ttk.Button(right_side_area, text='Submit')
submit_button_right['command'] = show_value_on_right
submit_button_right.grid(row=1, column=1, padx=5)

clear_button_right = ttk.Button(right_side_area, text='Clear')
clear_button_right['command'] = clear_button_right
clear_button_right.grid(row=2, column=1, padx=5)

# right side
right_data = ttk.Frame(root, width=300, height=300, style='show_data_list.TFrame')
right_data.grid(row=2, column=2, sticky='NS')

root.mainloop()
