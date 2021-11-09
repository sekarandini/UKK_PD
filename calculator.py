from tkinter import *
from math import *

root = Tk()

root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)



def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)


def button_equal():
    global f_num
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + float(second_number))
    if math == "subtraction":
        e.insert(0, f_num - float(second_number))
    if math == "multiplication":
        e.insert(0, f_num * float(second_number))
    if math == "division":
        e.insert(0, f_num / float(second_number))
    if math == "comma":
        e.insert(0,f_num +  + float(second_number))
    if math == "squere":
        e.insert(0, f_num ** int(2))
    if math == "sroot":
        e.insert(0, sqrt(f_num) )



def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)



def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)

def button_comma():
    global f_num
    first_number = e.get()
    f_num=str(first_number)
    s_num = e.get()
    e.insert(0, str(f_num) +  str(".")  + str(s_num))

def Button_num(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+ str(number))

def Button_squeree():
    global math
    global f_num
    first_number = e.get()
    f_num = int(first_number)
    math="squere"
    current=e.get()
    e.delete(0, END)
    e.insert(0,int(current) ^ int(first_number))

def Button_sroott():
    first_number = e.get()
    global f_num
    global math
    math = "sroot"
    f_num = float(first_number)
    e.delete(0, END)




'''   
def button_comma():
    current = e.get()
    e.insert(0, str(current) + str(","))



Button_comma = Button(root, text="," ,padx=40,pady=20,command=lambda: button_comma())
Button_comma.grid(row = 7 , column = 0 )
'''



Button1 = Button(root, text="1", padx=30, pady=20, command=lambda: button_click(1))
Button2 = Button(root, text="2", padx=30, pady=20, command=lambda: button_click(2))
Button3 = Button(root, text="3", padx=30, pady=20, command=lambda: button_click(3))

Button4 = Button(root, text="4", padx=30, pady=20, command=lambda: button_click(4))
Button5 = Button(root, text="5", padx=30, pady=20, command=lambda: button_click(5))
Button6 = Button(root, text="6", padx=30, pady=20, command=lambda: button_click(6))

Button7 = Button(root, text="7", padx=30, pady=20, command=lambda: button_click(7))
Button8 = Button(root, text="8", padx=30, pady=20, command=lambda: button_click(8))
Button9 = Button(root, text="9", padx=30, pady=20, command=lambda: button_click(9))

Button0 = Button(root, text="0", padx=30, pady=20, command=lambda: button_click(0))
Button_add = Button(root, text="+", padx=30,bg="#3d3d3d",fg="#fff",pady=20, command=button_add)
Button_equal = Button(root, text="=", padx=30,bg="#3d3d3d",fg="#fff", pady=20, command=button_equal)

Button_clear = Button(root, text="AC", padx=30,bg="#3d3d3d",fg="#fff", pady=20, command=button_clear)
Button_subtract = Button(root, text="-", padx=30,bg="#3d3d3d",fg="#fff", pady=20, command=button_subtract)
Button_multiply = Button(root, text="*", padx=30,bg="#3d3d3d",fg="#fff", pady=20, command=button_multiply)

Button_divide = Button(root, text="/", padx=30,bg="#3d3d3d",fg="#fff", pady=20, command=button_divide)
btn_decimal = Button(root, text=u'\u002E', padx=30,bg="#3d3d3d",fg="#fff", pady=20, command=lambda:Button_num("."))
Button_squere = Button(root,text="x2",padx=30,bg="#3d3d3d",fg="#fff", pady=20,command=Button_squeree)

Button_sroot =  Button(root, text="r",padx=30,bg="#3d3d3d",fg="#fff", pady=20, command=Button_sroott)



Button1.grid(row=3, column=0)
Button2.grid(row=3, column=1)
Button3.grid(row=3, column=2)

Button4.grid(row=2, column=0)
Button5.grid(row=2, column=1)
Button6.grid(row=2, column=2)

Button7.grid(row=1, column=0)
Button8.grid(row=1, column=1)
Button9.grid(row=1, column=2)

Button0.grid(row=4, column=0)
Button_add.grid(row=5, column=0)
Button_equal.grid(row=5, column=1)

Button_clear.grid(row=4, column=1)
Button_subtract.grid(row=6, column=0)
Button_multiply.grid(row=6, column=1)

Button_divide.grid(row=6, column=2)
btn_decimal.grid(row=7,column=0)
Button_squere.grid(row=7,column=1)


Button_sroot.grid(row=7 , column=2)








root.mainloop()