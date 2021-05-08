Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t=turtle.Turtle()
>>> t.forward(100)
>>> t.left
<bound method TNavigator.left of <turtle.Turtle object at 0x037CC550>>
>>> 

9
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> forward(100)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    forward(100)
NameError: name 'forward' is not defined
>>> t.forward(100)
>>> 