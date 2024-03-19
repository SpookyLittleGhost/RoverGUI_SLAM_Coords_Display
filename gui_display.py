import tkinter as tk

global window
global canvas

global window_height
global window_width

global points


def start():
    global window
    global canvas

    global window_height
    global window_width

    print("!--- GUI DISPLAY THREAD STARTED ---!")

    window = tk.Tk()

    size = window_width.__str__() + "x" + window_height.__str__()
    window.geometry(size)

    canvas = tk.Canvas(window, width=window_width, height=window_height)

    canvas.create_rectangle(10, 10, window_width-10, window_height-10, outline='black', fill='gray')
    canvas['bg'] = 'red'

    canvas.pack()

    window.mainloop()


def prepare_window_size():
    print("!--- WINDOW SITE PREPARED ---!")

    global window_height
    global window_width

    window_height = -1
    window_width = -1

    while window_width < 0:
        print("Please enter the desired width of your display window:")
        window_width = int(input())

    while window_height < 0:
        print("Please enter the desired height of your display window:")
        window_height = int(input())


def add_coordinate(x, y, color):
    print("!--- COORDINATE ADDED ---!")

    global canvas
    global window_height
    global window_width

    oval_x_coord = x + (window_width/2)
    oval_y_coord = y + (window_height/2)
    radius = 2

    point = canvas.create_oval(oval_x_coord-radius, oval_y_coord-radius, oval_x_coord+radius, oval_y_coord+radius, fill=color)
