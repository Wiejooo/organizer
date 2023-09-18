import tkinter as tk
from tkinter import ttk

root = tk.Tk()

for_now = '''
    13/12/WW/0 13/12/WW/1 13/12/WW/2
'''

list_of_orders = []

list_of_no_orders = []

list__of_own_orders = []


# ------------------------ FUNCTIONS


def show_value_left_mid():
    # Changing input in to the list
    value = entry_orders_list.get()
    value = value.split(' ')

    for order in value:
        list_of_orders.append(order)

    # Showing data on the left
    one_sentence = ''
    for part in list_of_orders:
        one_sentence = one_sentence + part + '\n'
    left_data.configure(text=one_sentence)

    # Updating description on the left
    number_of_orders = len(list_of_orders)
    description_text_left.configure(text=f'Number of orders: {number_of_orders}')

    # Showing data on the mid
    for order in value:
        list_of_no_orders.append(order)

    one_mid_sentence = ''
    for part in list_of_no_orders:
        one_mid_sentence = one_mid_sentence + part + '\n'
    mid_label_area.configure(text=one_mid_sentence)


def show_value_on_right():
    current_right_side = right_data.cget('text')
    input_value = entry_order.get()
    if input_value in list_of_no_orders:
        new_text = current_right_side + input_value + ' - JEST'
        # Updating mid area
        list_of_no_orders.remove(input_value)
        one_mid_sentence = ''
        for part in list_of_no_orders:
            one_mid_sentence = one_mid_sentence + part + '\n'
        mid_label_area.configure(text=one_mid_sentence)

    else:
        new_text = current_right_side + input_value + ' - NIE MA'
    right_data.configure(text=f'{new_text}\n')



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
s.configure('Label.TLabel', background='#839de9', font=('Helventica', 14))
s.configure('test.TFrame', highlightbackground="blue", highlightthickness=2)

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
submit_button_left = ttk.Button(left_side_area, text='Submit', command=show_value_left_mid)
submit_button_left.grid(row=1, column=1, padx=5)

clear_button_left = ttk.Button(left_side_area, text='Clear')
clear_button_left['command'] = clear_left_value
clear_button_left.grid(row=2, column=1, padx=5)

# left side
left_data = ttk.Label(left_side_area, anchor='center')
left_data.grid(row=3, column=0, columnspan=2, sticky='NSEW')

# description
description_left = ttk.Frame(root, width=10, height=10)
description_left.grid(row=3, columnspan=1, sticky='NS')

description_text_left = ttk.Label(description_left, text="Number of orders: 0")
description_text_left.pack()


# --- show mid area
mid_area = ttk.Frame(root, width=300, height=400, style='show_area.TFrame')
mid_area.grid(row=1, column=1, rowspan=2, sticky='NSEW')

mid_label_area = ttk.Label(mid_area, width=45, anchor='center')
mid_label_area.pack()

# description
description_mid = ttk.Frame(root, width=10, height=10)
description_mid.grid(row=3, columnspan=3, sticky='NS')

description_text_mid = ttk.Label(description_mid, text="You don't have these")
description_text_mid.pack()


# --- right area
right_side_area = ttk.Frame(root, width=300, height=100, style='input_area.TFrame')
right_side_area.grid(row=1, column=2, rowspan=2, sticky='NS')

# label
title_right_side = ttk.Label(right_side_area, text='Entry number', background='#cdced2')
title_right_side.grid(row=0, column=0, columnspan=2, pady=5)

# entry
entry_order = ttk.Entry(right_side_area, width=31)
entry_order.grid(row=1, column=0, rowspan=1, padx=10, pady=10, sticky='NS')

# buttons
submit_button_right = ttk.Button(right_side_area, text='Submit', command=show_value_on_right)
submit_button_right.grid(row=1, column=1, padx=5)

clear_button_right = ttk.Button(right_side_area, text='Clear', command=clear_right_value)
clear_button_right.grid(row=2, column=1, padx=5)

# right side
right_data = ttk.Label(right_side_area, anchor='center')
right_data.grid(row=3, column=0, columnspan=2, sticky='NSEW')

root.mainloop()
