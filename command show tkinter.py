from tkinter import *
root=Tk()
root.geometry("500x500")
root.resizable(0,0)
def show():
    print("Lata sharma")
    root.configure(background="blue")
b1=Button(root,text="submit",font=("Arial",25),command=show)   #command show used for displaying message in shell after the click
b1.pack()
root.mainloop()
