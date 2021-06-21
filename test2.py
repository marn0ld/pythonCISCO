import math
from tkinter import *

root = Tk()
root.title("Arno's calculator")

# interface
box = Entry(root, width=70, borderwidth=15, bg="Yellow")
box.grid(row=0, column=0, columnspan=7, padx=10, pady=10)


# buttons functions(numbers)
def knopka_func(number):
    global calc
    current = box.get()
    box.delete(0, END)
    box.insert(0, str(current) + str(number))

def knopka_add():
    global add
    global index
    index = "add"
    add = int(box.get())
    box.delete(0, END)

def knopka_sub():
    global sub
    global index
    index = "sub"
    sub = int(box.get())
    box.delete(0, END)

def knopka_div():
    global div
    global index
    index = "div"
    div = int(box.get())
    box.delete(0, END)

def knopka_mul():
    global mul
    global index
    index = "mul"
    mul = int(box.get())
    box.delete(0, END)

# buttons functions(math functions)
def knopka_cos():
    global cos
    global index
    index = "cos"
    cos = int(box.get())
    box.delete(0, END)

def knopka_sin():
    global sin
    global index
    index = "sin"
    sin = float(box.get())
    box.delete(0, END)

def knopka_tg():
    global tg
    global index
    index = "tan"
    tg = int(box.get())
    box.delete(0, END)

def knopka_ctg():
    global ctg
    global index
    index = "ctg"
    ctg = int(box.get())
    box.delete(0, END)

def knopka_log():
    global log
    global index
    index = "log"
    log = int(box.get())
    box.delete(0, END)

def knopka_ln():
    global ln
    global index
    index = "ln"
    ln = int(box.get())
    box.delete(0, END)

def knopka_percent():
    global perc
    global index
    index = "%"
    perc = int(box.get())
    box.delete(0, END)

def knopka_bin():
    global binnum
    global index
    index = "bin"
    binnum = int(box.get())
    box.delete(0, END)

def knopka_clear():
    box.delete(0, END)

def knopka_equal():
    num = box.get()
    box.delete(0, END)

    if index == "add":
        box.insert(0, add + int(num))
    elif index == "sub":
        box.insert(0, sub - int(num))
    elif index == "div":
        box.insert(0, div / int(num))
    elif index == "mul":
        box.insert(0, mul * int(num))
    elif index == "sin":
        box.insert(0, math.sin(float(sin)))
    elif index == "cos":
        box.insert(0, math.cos(float(cos)))
    elif index == "tan":
        box.insert(0, math.tan(float(tg)))
    elif index == "ctg":
        box.insert(0, math.cos(float(ctg)) / math.sin(float(ctg)))
    elif index == "log":
        box.insert(0, math.log10(float(log)))
    elif index == "ln":
        box.insert(0, math.log(float(ln)))
    elif index == "%":
        box.insert(0, (int(num)*perc)/100)
    elif index == "bin":
        def decimalToBinary(n):
            return bin(n).replace("0b", "")
        box.insert(0, decimalToBinary(binnum))

knopka_1 = Button(root, text="1", padx=25, pady=1, command=lambda: knopka_func(1), bg="Black", foreground="Yellow")
knopka_2 = Button(root, text="2", padx=25, pady=1, command=lambda: knopka_func(2),  bg="Black", foreground="Yellow")
knopka_3 = Button(root, text="3", padx=25, pady=1, command=lambda: knopka_func(3),  bg="Black", foreground="Yellow")
knopka_4 = Button(root, text="4", padx=25, pady=1, command=lambda: knopka_func(4),  bg="Black", foreground="Yellow")
knopka_5 = Button(root, text="5", padx=25, pady=1, command=lambda: knopka_func(5),  bg="Black", foreground="Yellow")
knopka_6 = Button(root, text="6", padx=25, pady=1, command=lambda: knopka_func(6),  bg="Black", foreground="Yellow")
knopka_7 = Button(root, text="7", padx=25, pady=1, command=lambda: knopka_func(7),  bg="Black", foreground="Yellow")
knopka_8 = Button(root, text="8", padx=25, pady=1, command=lambda: knopka_func(8),  bg="Black", foreground="Yellow")
knopka_9 = Button(root, text="9", padx=25, pady=1, command=lambda: knopka_func(9),  bg="Black", foreground="Yellow")
knopka_0 = Button(root, text="0", padx=25, pady=1, command=lambda: knopka_func(0),  bg="Black", foreground="Yellow")

# buttons(operations)
add = Button(root, text="+", padx=40, pady=1, command=knopka_add, bg="Yellow")
sub = Button(root, text="-", padx=40, pady=1, command=knopka_sub, bg="Yellow")
div = Button(root, text="/", padx=40, pady=1, command=knopka_div, bg="Yellow")
mul = Button(root, text="*", padx=40, pady=1, command=knopka_mul, bg="Yellow")
equal = Button(root, text="=", padx=40, pady=1, command=knopka_equal, bg="Yellow")
clear = Button(root, text="Clear", padx=39, pady=1, command=knopka_clear, bg="Yellow")

# buttons(operations)
cos = Button(root, text="cos", padx=28, pady=1, command=knopka_cos, bg="Yellow")
sin = Button(root, text="sin", padx=29, pady=1, command=knopka_sin, bg="Yellow")
tg = Button(root, text="tan", padx=29, pady=1, command=knopka_tg, bg="Yellow")
ctg = Button(root, text="ctg", padx=29, pady=1, command=knopka_ctg, bg="Yellow")
log = Button(root, text="log", padx=29, pady=1, command=knopka_log, bg="Yellow")
ln = Button(root, text="ln", padx=33, pady=1, command=knopka_ln, bg="Yellow")
percent = Button(root, text="%", padx=33, pady=1, command=knopka_percent, bg="Yellow")
binconvert = Button(root, text="bin", padx=33, pady=1, command=knopka_bin, bg="Yellow")

# placing buttons(numbers)
knopka_1.grid(row=3, column=3)
knopka_2.grid(row=3, column=4)
knopka_3.grid(row=3, column=5)
knopka_4.grid(row=2, column=3)
knopka_5.grid(row=2, column=4)

knopka_6.grid(row=2, column=5)
knopka_7.grid(row=1, column=3)
knopka_8.grid(row=1, column=4)
knopka_9.grid(row=1, column=5)
knopka_0.grid(row=4, column=3)

# placing buttons(functions)
sin.grid(row=1, column=0)
cos.grid(row=2, column=0)
tg.grid(row=3, column=0)
ctg.grid(row=4, column=0)
log.grid(row=5, column=0)
ln.grid(row=6, column=0)
percent.grid(row=7, column=0)
binconvert.grid(row=8,column=0)

# placing buttons(sings)
add.grid(row=1, column=6)
sub.grid(row=2, column=6)
div.grid(row=3, column=6)
mul.grid(row=4, column=6)
equal.grid(row=5, column=6)
clear.grid(row=6, column=6)

root.mainloop()