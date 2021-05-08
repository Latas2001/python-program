from tkinter import *
root=Tk()
root.geometry("500x500")
root.resizable(0,0)
un=Label(root,text="Enter name:",font=("Arial",20))
un.grid(row=0,column=0,pady=25,sticky=W)   #pady use for gap from top,sticky for side equality
e1=Entry(root,font=("Arial",20),bg="pink", fg="black")
e1.grid(row=0,column=1,pady=25)
up=Label(root,text="Enter Password:",font=("Arial",25))
up.grid(row=1,column=0,pady=25)
e2=Entry(root,show="*",font=("Arial",25),bg="pink", fg="black")
e2.grid(row=1,column=1,pady=25)
b1=Button(root,text="Login",font=("Arial",25),bg="pink", fg="black")
b1.grid(row=2,column=0,columnspan=2)  #columnspan use for setting the button position
root.mainloop()
