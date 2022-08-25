# The Tkinter module in Python allows us to build GUI applications
import webbrowser
from tkinter import *
from tkinter import StringVar, Entry, Button
from math import sin, cos, tan, log, log10, ceil, degrees, radians, exp, floor, e, pi, sqrt, factorial, pow, gcd

# calculator is the Calculator window into which all other widgets go.
calculator = Tk()
calculator.title("Porsche Scientific Calculator")
calculator.configure(background="lightslategray")
display = Text(calculator, width=30, height=2, borderwidth=4, fg="black", font=('Arial 18'))
display.grid(row=0, column=0, columnspan=12, padx=5, pady=5)
display.configure(background="white")
display.focus()
calculator.attributes('-alpha', 0.94)
calculator.attributes('-topmost', 1)
calculator.resizable(width="False", height="False")
calculator.geometry("467x662+700+50")
calculator.iconbitmap('C:\porsche (1).ico')


# display the menu
def open_web_p():
    webbrowser.open_new("https://www.porsche.com/")


def open_web_tk():
    webbrowser.open_new("https://docs.python.org/3/library/tk.html")


my_menu = Menu(calculator)
m1 = Menu(my_menu, tearoff=0, fg='blue')
m1.add_command(label='Tkinter Documentation', command=open_web_tk)
m1.add_command(label='Porsche', command=open_web_p)
calculator.config(menu=my_menu)
my_menu.add_cascade(label=' About ', menu=m1)
my_menu.add_command(label='Exit', command=quit)
############

# Functions:
display_txt = ""


def math_calculations(math):
    global display_txt
    display_txt = display_txt + str(math)
    display.delete("1.0", "end")
    display.insert("1.0", display_txt)


def equal():
    global display_txt
    result = str(eval(display_txt))
    display.delete("1.0", "end")
    display.insert("1.0", result)


def clear():
    global display_txt
    display_txt = ""
    display.delete("1.0", "end")


# all Buttons:0to9,-,+,*,/,.,=,(,),!,sin,cos,tan,asin,acos,AC,e,log,log10,%,min,max,degree,radian,pi,floor
# sorted by Row:
# row=1
btn_7 = Button(calculator, padx=10, pady=10, text="7", font=('arial', 14, 'bold'), width=4, height=2,
               bg="lightsteelblue2", command=lambda: math_calculations(7))
btn_8 = Button(calculator, padx=10, pady=10, text="8", font=('arial', 14, 'bold'), width=4, height=2,
               bg="lightsteelblue2", command=lambda: math_calculations(8))
btn_9 = Button(calculator, padx=10, pady=10, text="9", font=('arial', 14, 'bold'), width=4, height=2,
               bg="lightsteelblue2", command=lambda: math_calculations(9))
btn_sin = Button(calculator, padx=10, pady=10, text="sin", font=('arial', 14, 'bold'), width=4, height=2,
                 bg="lightsteelblue2", command=lambda: math_calculations("sin("))
btn_cos = Button(calculator, padx=10, pady=10, text="cos", font=('arial', 14, 'bold'), width=4, height=2,
                 bg="lightsteelblue2", command=lambda: math_calculations("cos("))
btn_tan = Button(calculator, padx=10, pady=10, text="tan", font=('arial', 14, 'bold'), width=4, height=2,
                 bg="lightsteelblue2", command=lambda: math_calculations("tan("))
# row=2
btn_4 = Button(calculator, padx=10, pady=10, text="4", font=('arial', 14, 'bold'), width=4, height=2,
               bg="lightsteelblue2", command=lambda: math_calculations(4))
btn_5 = Button(calculator, padx=10, pady=10, text="5", font=('arial', 14, 'bold'), width=4, height=2,
               bg="lightsteelblue2", command=lambda: math_calculations(5))
btn_6 = Button(calculator, padx=10, pady=10, text="6", font=('arial', 14, 'bold'), width=4, height=2,
               bg="lightsteelblue2", command=lambda: math_calculations(6))
btn_exp = Button(calculator, padx=10, pady=10, text="exp", font=('arial', 14, 'bold'),
                 width=4, height=2, bg="lightsteelblue2", command=lambda: math_calculations("exp("))
btn_factorial = Button(calculator, padx=10, pady=10, text="x!", font=('arial', 14, 'bold'), width=4, height=2,
                       bg="lightsteelblue2", command=lambda: math_calculations("factorial("))
btn_abs = Button(calculator, padx=10, pady=10, text="abs", font=('arial', 14, 'bold'), width=4, height=2,
                 bg="lightsteelblue2", command=lambda: math_calculations("abs("))
# row=3
btn_1 = Button(calculator, padx=10, pady=10, text="1", font=('arial', 14, 'bold'), width=4, height=2,
               bg="lightsteelblue2", command=lambda: math_calculations(1))
btn_2 = Button(calculator, padx=10, pady=10, text="2", font=('arial', 14, 'bold'), width=4, height=2,
               bg="lightsteelblue2", command=lambda: math_calculations(2))
btn_3 = Button(calculator, padx=10, pady=10, text="3", font=('arial', 14, 'bold'), width=4, height=2,
               bg="lightsteelblue2", command=lambda: math_calculations(3))
btn_log = Button(calculator, padx=10, pady=10, text="log", font=('arial', 14, 'bold'), width=4, height=2,
                 bg="lightsteelblue2", command=lambda: math_calculations("log("))
btn_log10 = Button(calculator, padx=10, pady=10, text="log10", font=('arial', 14, 'bold'), width=4, height=2,
                   bg="lightsteelblue2", command=lambda: math_calculations("log10("))
btn_e = Button(calculator, padx=10, pady=10, text="e", font=('arial', 14, 'bold'), width=4, height=2,
               bg="lightsteelblue2", command=lambda: math_calculations("e"))
# row=4
btn_divide = Button(calculator, padx=10, pady=10, text="/", font=('arial', 14, 'bold'), width=4, height=2,
                    bg="lightsteelblue2", command=lambda: math_calculations("/"))
btn_0 = Button(calculator, padx=10, pady=10, text="0", font=('arial', 14, 'bold'), width=4, height=2,
               bg="lightsteelblue2", command=lambda: math_calculations(0))
btn_multiply = Button(calculator, padx=10, pady=10, text="*", font=('arial', 14, 'bold'), width=4, height=2,
                      bg="lightsteelblue2", command=lambda: math_calculations("*"))
btn_add = Button(calculator, padx=10, pady=10, text="+", font=('arial', 14, 'bold'), width=4, height=2,
                 bg="lightsteelblue2", command=lambda: math_calculations("+"))
btn_sub = Button(calculator, padx=10, pady=10, text="-", font=('arial', 14, 'bold'), width=4, height=2,
                 bg="lightsteelblue2", command=lambda: math_calculations("-"))
btn_mdl = Button(calculator, padx=10, pady=10, text="%", font=('arial', 14, 'bold'), width=4, height=2,
                 bg="lightsteelblue2", command=lambda: math_calculations("%"))
# row=5
btn_brakt_open = Button(calculator, padx=10, pady=10, text="(", font=('arial', 14, 'bold'), width=4, height=2,
                        bg="lightsteelblue2", command=lambda: math_calculations("("))
btn_brakt_close = Button(calculator, padx=10, pady=10, text=")", font=('arial', 14, 'bold'), width=4, height=2,
                         bg="lightsteelblue2", command=lambda: math_calculations(")"))
btn_dot = Button(calculator, padx=10, pady=10, text=".", font=('arial', 14, 'bold'), width=4, height=2,
                 bg="lightsteelblue2", command=lambda: math_calculations("."))
btn_comma = Button(calculator, padx=10, pady=10, text=",", font=('arial', 14, 'bold'), width=4, height=2,
                   bg="lightsteelblue2", command=lambda: math_calculations(","))
btn_sqrt = Button(calculator, padx=10, pady=10, text="√", font=('arial', 14, 'bold'), width=4, height=2,
                  bg="lightsteelblue2", command=lambda: math_calculations("sqrt("))
btn_pow = Button(calculator, padx=10, pady=10, text="x^y", font=('arial', 14, 'bold'),
                 width=4, height=2, bg="lightsteelblue2", command=lambda: math_calculations("pow("))
# row=6
btn_sqr = Button(calculator, padx=10, pady=10, text="**", font=('arial', 14, 'bold'), width=4, height=2,
                 bg="lightsteelblue2", command=lambda: math_calculations("**"))
btn_ceil = Button(calculator, padx=10, pady=10, text="ceil", font=('arial', 14, 'bold'), width=4, height=2,
                  bg="lightsteelblue2", command=lambda: math_calculations("ceil("))
btn_degrees = Button(calculator, padx=10, pady=10, text="degree", font=('arial', 14, 'bold'), width=4, height=2,
                     bg="lightsteelblue2", command=lambda: math_calculations("degrees("))
btn_radian = Button(calculator, padx=10, pady=10, text="radian", font=('arial', 14, 'bold'), width=4, height=2,
                    bg="lightsteelblue2", command=lambda: math_calculations("radians("))
btn_pi = Button(calculator, padx=10, pady=10, text="π", font=('arial', 14, 'bold'), width=4, height=2,
                bg="lightsteelblue2", command=lambda: math_calculations(pi))
btn_floor = Button(calculator, padx=10, pady=10, text="floor", font=('arial', 14, 'bold'), width=4, height=2,
                   bg="lightsteelblue2", command=lambda: math_calculations("floor("))
# row=7
btn_gcd = Button(calculator, padx=10, pady=10, text="gcd", font=('arial', 14, 'bold'),
                 width=4, height=2, bg="lightsteelblue2", command=lambda: math_calculations("gcd("))
btn_clear = Button(calculator, padx=10, pady=10, text="AC", font=('arial', 14, 'bold'),
                   width=10, height=2, bg="whitesmoke", command=lambda: clear())
btn_equal = Button(calculator, padx=10, pady=10, text="=", font=('arial', 14, 'bold'), width=17, height=2,
                   bg="turquoise3", command=lambda: equal())
# bring the Buttons on the calculator window,sorted by row:
# row=1
btn_7.grid(row=1, column=0, padx=1, pady=1)
btn_8.grid(row=1, column=1, padx=1, pady=1)
btn_9.grid(row=1, column=2, padx=1, pady=1)
btn_sin.grid(row=1, column=3, padx=1, pady=1)
btn_cos.grid(row=1, column=4, padx=1, pady=1)
btn_tan.grid(row=1, column=5, padx=1, pady=1)
# row=2
btn_4.grid(row=2, column=0, padx=1, pady=1)
btn_5.grid(row=2, column=1, padx=1, pady=1)
btn_6.grid(row=2, column=2, padx=1, pady=1)
btn_exp.grid(row=2, column=3, padx=1, pady=1)
btn_factorial.grid(row=2, column=4, padx=1, pady=1)
btn_abs.grid(row=2, column=5, padx=1, pady=1)
# row=3
btn_1.grid(row=3, column=0, padx=1, pady=1)
btn_2.grid(row=3, column=1, padx=1, pady=1)
btn_3.grid(row=3, column=2, padx=1, pady=1)
btn_log.grid(row=3, column=3, padx=1, pady=1)
btn_log10.grid(row=3, column=4, padx=1, pady=1)
btn_e.grid(row=3, column=5, padx=1, pady=1)
# row=4
btn_divide.grid(row=4, column=0, padx=1, pady=1)
btn_0.grid(row=4, column=1, padx=1, pady=1)
btn_multiply.grid(row=4, column=2, padx=1, pady=1)
btn_add.grid(row=4, column=3, padx=1, pady=1)
btn_sub.grid(row=4, column=4, padx=1, pady=1)
btn_mdl.grid(row=4, column=5, padx=1, pady=1)
# row=5
btn_brakt_open.grid(row=5, column=0, padx=1, pady=1)
btn_brakt_close.grid(row=5, column=1, padx=1, pady=1)
btn_dot.grid(row=5, column=2, padx=1, pady=1)
btn_comma.grid(row=5, column=3, padx=1, pady=1)
btn_sqrt.grid(row=5, column=4, padx=1, pady=1)
btn_pow.grid(row=5, column=5, padx=1, pady=1)
# row=6
btn_sqr.grid(row=6, column=0, padx=1, pady=1)
btn_ceil.grid(row=6, column=1, padx=1, pady=1)
btn_degrees.grid(row=6, column=2, padx=1, pady=1)
btn_radian.grid(row=6, column=3, padx=1, pady=1)
btn_pi.grid(row=6, column=4, padx=1, pady=1)
btn_floor.grid(row=6, column=5, padx=1, pady=1)
# row=7
btn_gcd.grid(row=7, column=0, padx=1, pady=1)
btn_clear.grid(row=7, column=1, padx=1, pady=1, columnspan=2, sticky='nsew')
btn_equal.grid(row=7, column=2, padx=1, pady=1, columnspan=12, sticky='nse')
# calculator. mainloop() is a method on the main window which we execute when we want to run our application
# This method will loop forever, waiting for events from the user, until the user exits the program
calculator.mainloop()