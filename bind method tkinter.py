from tkinter import *
root=Tk()
root.geometry("500x500")
root.resizable(0,0)
def show(e):
    root.configure(background="blue")  #or  ''' show=lambad e:root.configure(background="red")
def show2(e):
    root.configure(background="pink")
def show3 (e):
    root.configure(background="green")
b1=Button(root,text="submit",font=("Arial",25))   #command show used for displaying message in shell after the click
b1.bind("<Button-1>",show)#Left click on mouse        if you want to perform the action with double clivck :-  ("<Double-1">,show)
b1.bind("<Button-2>",show2) #Wheel
b1.bind("<Button-3>",show3) #right
b1.pack()
root.mainloop()


#color change of background without clicking the button

from tkinter import *
root=Tk()
root.geometry("500x500")
root.resizable(0,0)
show=lambda e:root.configure(background="black")
show2=lambda e:root.configure(background="pink")
b1=Button(root,text="submit",font=("Arial",25))
b1.bind("<Enter>",show)                          #enter works without click,,,,,,,show functyion can be paste here
b1.bind("<Leave>",show2)     #when leave the button color will change
b1.pack()
root.mainloop()






#when enter in window color will change


from tkinter import *
root=Tk()
root.geometry("500x500")
root.resizable(0,0)

root.bind("<Enter>",lambda e:root.configure(background="pink"))
root.bind("<Leave>",lambda e:root.configure(background="cyan"))
root.mainloop()





#changing background using keyboard keys

from tkinter import *
root=Tk()
root.geometry("500x500")
root.resizable(0,0)

root.bind("<Key-a>",lambda e:root.configure(background="pink"))
root.bind("<Key-b>",lambda e:root.configure(background="purple"))
root.bind("<Key-c>",lambda e:root.configure(background="blue"))
root.mainloop()



#using numbers


from tkinter import *
root=Tk()
root.geometry("500x500")
root.resizable(0,0)

root.bind("2",lambda e:root.configure(background="pink"))
root.bind("3",lambda e:root.configure(background="purple"))
root.bind("4",lambda e:root.configure(background="blue"))
root.mainloop()


#using shift+up,doewn,right,left   also use alt and control key


from tkinter import *
root=Tk()
root.geometry("500x500")
root.resizable(0,0)

root.bind("<Shift-Up>",lambda e:root.configure(background="pink"))
root.bind("<Shift-Down>",lambda e:root.configure(background="purple"))
root.bind("<Shift-Right>",lambda e:root.configure(background="blue"))
root.bind("<Shift-Left>",lambda e:root.configure(background="yellow"))

root.mainloop()


#background change  after click and leave

from tkinter import *
root=Tk()
root.geometry("500x500")
root.resizable(0,0)
b1=Button(root,text="Click",font=("Arial",25))
b1.bind("<Button>",lambda e:root.configure(background="red"))
b1.bind("<ButtonRelease>",lambda e:root.configure(background="black"))
b1.pack()
root.mainloop()



#entry focusIn focusout


from tkinter import *
root=Tk()
root.geometry("500x500")
root.resizable(0,0)
e1=Entry(root,font=("Arial",25))
e1.bind("<FocusIn>",lambda e:root.configure(background="blue"))
e1.bind("<FocusOut>",lambda e:root.configure(background="black"))
e1.pack()
e2=Entry(root,font=("Arial",25))
e2.pack()
root.mainloop()
