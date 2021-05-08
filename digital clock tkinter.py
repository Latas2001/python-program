from tkinter import *
import time
root=Tk()
root.title("Digital Clock")
root.geometry("1350x700+0+0")
root.config(bg="#081923")
def clock():
    h=str(time.strftime("%H"))
    m=str(time.strftime("%M"))
    s=str(time.strftime("%S"))
    #print(h,m,s)
    if int(h)>12 and int(m)>0:
        lbl_hr7.config(text="PM")
    if int (h)>12:
        h=str(int(int(h)/12))
   
    
    lbl_hr.config(text=h)
    lbl_hr3.config(text=m)
    lbl_hr5.config(text=s)

    lbl_hr.after(200,clock)

lbl_hr=Label(root,text="12",font=("time new roman",50,"bold"),bg="blue",fg="white")
lbl_hr.place(x=350,y=200,width=150,height=150)
lbl_hr2=Label(root,text="HOUR",font=("time new roman",20,"bold"),bg="black",fg="white")
lbl_hr2.place(x=350,y=360,width=150,height=50)
lbl_hr3=Label(root,text="12",font=("time new roman",50,"bold"),bg="grey",fg="white")
lbl_hr3.place(x=520,y=200,width=150,height=150)
lbl_hr4=Label(root,text="MINUTE",font=("time new roman",20,"bold"),bg="black",fg="white")
lbl_hr4.place(x=520,y=360,width=150,height=50)
lbl_hr5=Label(root,text="12",font=("time new roman",50,"bold"),bg="blue",fg="white")
lbl_hr5.place(x=690,y=200,width=150,height=150)
lbl_hr6=Label(root,text="SECOND",font=("time new roman",20,"bold"),bg="black",fg="white")
lbl_hr6.place(x=690,y=360,width=150,height=50)
lbl_hr7=Label(root,text="AM",font=("time new roman",50,"bold"),bg="grey",fg="white")
lbl_hr7.place(x=860,y=200,width=150,height=150)
lbl_hr8=Label(root,text="NOON",font=("time new roman",20,"bold"),bg="black",fg="white")
lbl_hr8.place(x=860,y=360,width=150,height=50)
clock()
root.mainloop
