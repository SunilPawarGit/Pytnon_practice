from cProfile import label
from cgitb import text
from time import strftime
from tkinter import *
from tkinter import font
from  playsound import playsound
clk = Tk()
clk.title("Clock")
clk.geometry("1350x700")
clk.config(bg ="#0C1E28")
def time():
    hr = strftime('%H')
    lb_hr.config(text=hr)
    lb_hr.after(1000000 ,time)

    mn =strftime('%M')
    lb_mn.config(text=mn)
    lb_mn.after(1000000,time)

    sec =strftime('%S')
    lb_sec.config(text=sec)
    lb_sec.after(1,time)

    if(hr == "16" and mn=="39" and sec == "00"):
        playsound('out.wav')
lb_head= Label(clk,text="Digital Clock",font=("Times 20 bold",50,"bold"),bg="white")
lb_head.place(x=350,y=20,width=490,height=150)

lb_hr = Label(clk,text="12",font=("Times 20 bold",75,"bold"),bg="white")
lb_hr.place(x=350,y=200,width=150,height=150)

lb_cr = Label(clk,text=":",font=("Times 20 bold",75,"bold"),bg="white")
lb_cr.place(x=500,y=200,width=20,height=150)

lb_mn = Label(clk,text="00",font=("Times 20 bold",75,"bold"),bg="white")
lb_mn.place(x=520,y=200,width=150,height=150)

lb_cr1 = Label(clk,text=":",font=("Times 20 bold",75,"bold"),bg="white")
lb_cr1.place(x=670,y=200,width=20,height=150)

lb_sec = Label(clk,text="00",font=("Times 20 bold",75,"bold"),bg="white")
lb_sec.place(x=690,y=200,width=150,height=150)

time()

clk.mainloop()