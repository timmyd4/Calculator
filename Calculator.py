import ttkbootstrap as tb

#Window Properties
Window = tb.Window(themename='darkly')
Window.geometry('550x150')
Window.title('Calculator')

#Functions for Caculator
def add(x, y):
    return x + y

def subtract(x, y):
    if x > y:
        return y - x
    else:
        return x - y
    
def multiply(x, y):
    return x * y

def divide(x, y):
    if x % 2 != 0:
        return x // y
    else:
        return x / y
    
def get_Input():
    global input_x, input_y
    input_x = int(x_Entry.get())
    input_y = int(y_Entry.get())

def AddValues():
    get_Input()
    total = add(input_x, input_y)
    result.config(text=total)

def SubtractValues():
    get_Input()
    total = subtract(input_x, input_y)
    result.config(text=total)

def MultiplyValues():
    get_Input()
    total = multiply(input_x, input_y)
    result.config(text=total)

def DivideValues():
    get_Input()
    total = divide(input_x, input_y)
    result.config(text=total)

#Window Addons
information = tb.Label(Window, text='Enter 2 Numbers')
x_Entry = tb.Entry(Window)
y_Entry = tb.Entry(Window)

add_Button = tb.Button(text='Add', command=AddValues)
subtract_Button = tb.Button(text='Subtract', command=SubtractValues)
multiply_Button = tb.Button(text='Multiply', command=MultiplyValues)
divide_Button = tb.Button(text='Divide', command=DivideValues)

result = tb.Label(Window, text='')

# Center all elements
Window.grid_columnconfigure(0, weight=1)
Window.grid_columnconfigure(1, weight=1)
Window.grid_columnconfigure(2, weight=1)
Window.grid_columnconfigure(3, weight=1)
Window.grid_columnconfigure(4, weight=1)

Window.grid_rowconfigure(0, weight=1)
Window.grid_rowconfigure(1, weight=1)
Window.grid_rowconfigure(2, weight=1)
Window.grid_rowconfigure(3, weight=1)
Window.grid_rowconfigure(4, weight=1)

# Grid layout
information.grid(row=0, column=1, columnspan=3, sticky='ew')  # Span across 3 columns
x_Entry.grid(row=1, column=1, sticky='ew')
y_Entry.grid(row=1, column=2, sticky='ew')

add_Button.grid(row=2, column=1, sticky='ew')
subtract_Button.grid(row=2, column=2, sticky='ew')
multiply_Button.grid(row=3, column=1, sticky='ew')
divide_Button.grid(row=3, column=2, sticky='ew')

# Result label below the buttons
result.grid(row=4, column=1, columnspan=2, sticky='ew')

Window.mainloop()