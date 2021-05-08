from tkinter import *
root=Tk()
root.geometry("500x500")
root.resizable(0,0)
x=StringVar()
e1=Entry(root,font=("Arial",25),textvariable=x)
e1.pack()
def show():
    s=x.get()
    print(s)
    x.set("")  #for clearing box after filling info
b1=Button(root,text="Click",font=("Arial",25),command=show)
b1.pack()
root.mainloop()






#when entry1 will submit after submission msg will display in entry2

from tkinter import *
root=Tk()
root.geometry("500x500")
root.resizable(0,0)
x=StringVar()
y=StringVar()
e1=Entry(root,font=("Arial",25),textvariable=x)
e1.pack()
def show():
    s=x.get()
    print(s)
    y.set(s)
    x.set("")  #for clearing box after filling info
b1=Button(root,text="Click",font=("Arial",25),command=show)
b1.pack()
e2=Entry(root,font=("Arial",25),textvariable=y)
e2.pack()
root.mainloop()


#content of entry 1 and entry 2 after clicking the button sum the sum will show in entry3

from tkinter import *
root=Tk()
root.geometry("500x500")
root.resizable(0,0)
x=IntVar()    #for float value ude DoubleVar()
y=IntVar()
z=IntVar()
e1=Entry(root,font=("Arial",25),textvariable=x)
e1.pack()
e2=Entry(root,font=("Arial",25),textvariable=y)
e2.pack()
def show():
    a=x.get()
    b=y.get()
    c=a+b
    z.set(c)
def show1():
    a=x.get()
    b=y.get()
    c=a-b
    z.set(c)
def show2():
    a=x.get()
    b=y.get()
    c=a*b
    z.set(c)
def show3():
    a=x.get()
    b=y.get()
    c=a/b
    z.set(c)
b1=Button(root,text="+",font=("Arial",25),command=show)
b1.pack()
b2=Button(root,text="-",font=("Arial",25),command=show1)
b2.pack()
b1=Button(root,text="*",font=("Arial",25),command=show2)
b1.pack()
b1=Button(root,text="/",font=("Arial",25),command=show3)
b1.pack()

e3=Entry(root,font=("Arial",25),textvariable=z)
e3.pack()
root.mainloop()



#simple calculation
from tkinter import *
root=Tk()
root.geometry("500x500")
root.resizable(0,0)
x=IntVar()    #for float value ude DoubleVar()
y=IntVar()
z=IntVar()
e1=Entry(root,font=("Arial",25),textvariable=x)
e1.pack()
e2=Entry(root,font=("Arial",25),textvariable=y)
e2.pack()
def show(op):
    a=x.get()
    b=y.get()
    if(op==1):
        c=a+b
        z.set(c)
    if(op==2):
        c=a-b
        z.set(c)
    if(op==3):
        c=a*b
        z.set(c)
    if(op==4):
        c=a/b
        z.set(c)

b1=Button(root,text="+",font=("Arial",25),command=lambda:show(1))
b1.pack()
b2=Button(root,text="-",font=("Arial",25),command=lambda:show(2))
b2.pack()
b1=Button(root,text="*",font=("Arial",25),command=lambda:show(3))
b1.pack()
b1=Button(root,text="/",font=("Arial",25),command=lambda:show(4))
b1.pack()

e3=Entry(root,font=("Arial",25),textvariable=z)
e3.pack()
root.mainloop()



#button click msg change



from tkinter import *
root=Tk()
root.geometry("500x500")
root.resizable(0,0)
def show(b):
    b["bg"]="black"
    b["fg"]="blue"
    b["width"]=10
    b["height"]=10
    b["text"]="Lata sharma"
      
b1=Button(root,text="click",font=("Arial",25),command=lambda:show(b1))
b1.pack()

root.mainloop()
