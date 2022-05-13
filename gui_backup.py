import tkinter as tk
import tkinter
from tkinter import ttk
import main

root = tk.Tk()
root.title("Tab Widget")
tabControl = ttk.Notebook(root)

Circle = ttk.Frame(tabControl)
Rectangle = ttk.Frame(tabControl)
Square = ttk.Frame(tabControl)
Triangle = ttk.Frame(tabControl)

tabControl.add(Circle, text='Circle')
tabControl.add(Rectangle, text='Rectangle')
tabControl.add(Square, text='Square')
tabControl.add(Triangle, text='Triangle')
tabControl.pack(expand=1, fill="both")


# Circle

def circle_click():
    radius_math = radius.get()
    float(radius_math)
    answer = main.circle_area(radius_math)
    area = ttk.Label(Circle, text="{}".format(answer))
    area.grid(column=1, row=1, padx=30, pady=30)


ttk.Label(Circle, text="Circle Area:").grid(column=0, row=1, padx=30, pady=30)
ttk.Label(Circle, text="Enter Radius:").grid(column=0, row=0, padx=30, pady=30)

radius = ttk.Entry(Circle)
radius.grid(column=1, row=0, padx=30, pady=30)

ttk.Button(Circle, text="Find the Area", command=circle_click).grid(row=2, padx=30, pady=30)


# Rectangle
def rectangle_click():
    length_math = rect_length.get()
    float(length_math)
    width_math = rect_width.get()
    float(width_math)
    answer1 = main.rectangle_area(length_math, width_math)
    area = ttk.Label(Rectangle, text="{}".format(answer1))
    area.grid(column=1, row=2, padx=30, pady=30)


ttk.Label(Rectangle, text="Enter Length:").grid(column=0, row=0, padx=30, pady=30)
ttk.Label(Rectangle, text="Enter Width:").grid(column=0, row=1, padx=30, pady=30)
ttk.Label(Rectangle, text="Rectangle Area:").grid(column=0, row=2, padx=30, pady=30)

rect_length = ttk.Entry(Rectangle)
rect_length.grid(column=1, row=0, padx=30, pady=30)

rect_width = ttk.Entry(Rectangle)
rect_width.grid(column=1, row=1, padx=30, pady=30)

ttk.Button(Rectangle, text="Find the Area", command=rectangle_click).grid(row=3, padx=30, pady=30)


# Square
def square_click():
    sq_math = square_length.get()
    float(sq_math)
    answer2 = main.square_area(sq_math)
    area = ttk.Label(Square, text="{}".format(answer2))
    area.grid(column=1, row=1, padx=30, pady=30)


ttk.Label(Square, text="Square Area:").grid(column=0, row=1, padx=30, pady=30)
ttk.Label(Square, text="Enter Length:").grid(column=0, row=0, padx=30, pady=30)

square_length = ttk.Entry(Square)
square_length.grid(column=1, row=0, padx=30, pady=30)

ttk.Button(Square, text="Find the Area", command=square_click).grid(row=2, padx=30, pady=30)


# Triangle
def triangle_click():
    length_math = tri_length.get()
    float(length_math)
    width_math = tri_length.get()
    float(width_math)
    answer1 = main.triangle_area(length_math, width_math)
    area = ttk.Label(Triangle, text="{}".format(answer1))
    area.grid(column=1, row=2, padx=30, pady=30)


ttk.Label(Triangle, text="Enter Length:").grid(column=0, row=0, padx=30, pady=30)
ttk.Label(Triangle, text="Enter Width:").grid(column=0, row=1, padx=30, pady=30)
ttk.Label(Triangle, text="Triangle Area:").grid(column=0, row=2, padx=30, pady=30)

tri_length = ttk.Entry(Triangle)
tri_length.grid(column=1, row=0, padx=30, pady=30)

tri_width = ttk.Entry(Triangle)
tri_width.grid(column=1, row=1, padx=30, pady=30)

ttk.Button(Triangle, text="Find the Area", command=triangle_click).grid(row=3, padx=30, pady=30)

root.mainloop()
