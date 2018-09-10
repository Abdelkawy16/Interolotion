from tkinter import *
from decimal import *
import numpy as np
import math
from newtonPoly import *
## key press function:
def clear():
    display.delete(0, END)
    display2.delete(0,END)
    display3.delete(0,END)
    display4.delete(0,END)
    display5.delete(0,END)

def solve():
    display4.delete(0,END)
    try:
        x = display.get()
        xx =x.split()
        count = 0
        for i in xx:
            xx[count]= eval(i)
            count+=1
        xData = np.array(xx)

        y = display2.get()
        yy =y.split()
        count2 = 0
        for k in yy:
            yy[count2]= eval(k)
            count2 +=1
        yData = np.array(yy)
        a = coeffts(xData,yData)
        c= eval(display5.get())
        cc= evalPoly(a,xData,c)
        try:
            yExact = eval(display3.get())
            display4.insert(0," x    yInterpolation    yExact------>>")
            display4.insert(END,'{:3.3f} {:9.5f} {:9.5f}'.format(c,cc,yExact))
        except:
            display4.insert(0," x    yInterpolation------>>")
            display4.insert(END,'{:3.3f} {:9.5f} '.format(c,cc))
    except:
        display4.insert(0, " --> Error!")
###################
##    def click(key):
##        if key == operator_pad_list[0]:
##            display3.insert(END,c)


##### main:
window = Tk()
window.title("Interpolation")
window.geometry("650x700+100+0")
## labels
label1 = Label(text="Enter xDATA",bg="yellow").place(x=10,y=10)
label2 = Label(text="Enter yDATA",bg="yellow").place(x=10,y=60)
label3 = Label(text="Enter Function (Optional)",bg="yellow").place(x=10,y=200)
label4 = Label(text="Enter X",bg="yellow").place(x=10,y=130)
# create top_row frame
top_row = Frame(window)
top_row.place(x=10,y=40)
# use Entry widget for an editable display
display = Entry(top_row, width=100, bg="light green")
display.grid()
# create scond_row frame
sec_row = Frame(window)
sec_row.place(x=10,y=100)
# use Entry widget for an editable display2
display2 = Entry(sec_row, width=100, bg="light green")
display2.grid()
# create thrd_row frame
thrd_row = Frame(window)
thrd_row.place(x=100,y=250)
# use Entry widget for an editable display3
display3 = Entry(thrd_row, width=45, bg="light green")
display3.grid()
# create forth_row frame
forth_row = Frame(window)
forth_row.place(x=70,y=350)
# use Entry widget for an editable display4
display4 = Entry(forth_row, width=70, bg="light green")
display4.grid()
# create fifth_row frame
fifth_row = Frame(window)
fifth_row.place(x=100,y=170)
# use Entry widget for an editable display5
display5 = Entry(fifth_row, width=45, bg="light green")
display5.grid()

### create operaters_frame
##operator_pad = Frame(window)
##operator_pad.place(x=100,y=300)
### provide a list of keys for the number pad:
##operator_pad_list = [
##'X', 'pi', 'sin(',
##'cos(', 'tan(', '*',
##'^', '/',
##'+', '-',
##'(', ')']
### create num_pad buttons with a loop
##r = 0 # row counter
##c = 0 # column counter
##for btn_text in operator_pad_list:
##    def cmd(x=btn_text):
##        click(x)
##    Button(operator_pad, text=btn_text, width=5, command=cmd).grid(row=r, column=c)
##    c = c+1
##    if c > 2:
##        c = 0
##        r = r+1

##Buttons
button1 = Button(text="Solve",command= solve).place(x=30,y=300)
button2 = Button(text="Clear",command= clear).place(x=550,y=300)
##### Run mainloop
window.mainloop()
