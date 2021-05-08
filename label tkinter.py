from tkinter import *
root=Tk()
root.minsize(400,400)    #size fixing of window also use ,maxsize
root.geometry("400x400")  #second method of fixing window but it can be minimize or maximize according to  ur wish
root.resizable(0,0)  # for fix in size niether inc nor dcr
un=Label(root,text="Lata sharma",font=("Algerian",25),bg="red",fg="purple",width="20",height="1")   # for displaying msg use label funt
un.pack()      #without this the msg will not display on window
root.mainloop()
