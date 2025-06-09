from tkinter import*
import webbrowser
import os
import sys
import subprocess

#Create tkinter window
change = Tk()
change.geometry("1000x600")
canvas = Canvas(change, width=690, height=600)
canvas.pack(fill="both", expand=True)
bg=PhotoImage(file='resources/changebg.png')
canvas.create_image(0,0,image=bg, anchor=NW)
change.title("Noten")

#confirm the choice and run the conversion module
def Confirm():
    change.destroy()
    import Convert

#The commands that overwrite the file which provides the key signature in the conversion module
def c():
    f = open("KS.txt", "w")
    f.write("C")
    f.close()

def g():
    f = open("KS.txt", "w")
    f.write("G")
    f.close()

def d():
    f = open("KS.txt", "w")
    f.write("D")
    f.close()

def a():
    f = open("KS.txt", "w")
    f.write("A")
    f.close()

def e():
    f = open("KS.txt", "w")
    f.write("E")
    f.close()

def b():
    f = open("KS.txt", "w")
    f.write("B")
    f.close()

def f():
    f = open("KS.txt", "w")
    f.write("F")
    f.close()

def bb():
    f = open("KS.txt", "w")
    f.write("Bb")
    f.close()

def eb():
    f = open("KS.txt", "w")
    f.write("Eb")
    f.close()

def ab():
    f = open("KS.txt", "w")
    f.write("Ab")
    f.close()

def db():
    f = open("KS.txt", "w")
    f.write("Db")
    f.close()

def gb():
    f = open("KS.txt", "w")
    f.write("Gb")
    f.close()

#Buttons that change the signature when pressed
c_img = PhotoImage(file='resources/c.png')
c_btn = Button(change, image=c_img, command=c, height=163, width=150, anchor="center", borderwidth=0)
c_btn_canvas = canvas.create_window(20, 69, anchor="nw", window=c_btn)

g_img = PhotoImage(file='resources/g.png')
g_btn = Button(change, image=g_img, command=g, height=163, width=150, anchor="center", borderwidth=0)
g_btn_canvas = canvas.create_window(180, 69, anchor="nw", window=g_btn)

d_img = PhotoImage(file='resources/d.png')
d_btn = Button(change, image=d_img, command=d, height=163, width=150, anchor="center", borderwidth=0)
d_btn_canvas = canvas.create_window(340, 69, anchor="nw", window=d_btn)

a_img = PhotoImage(file='resources/a.png')
a_btn = Button(change, image=a_img, command=a, height=163, width=150, anchor="center", borderwidth=0)
a_btn_canvas = canvas.create_window(500, 69, anchor="nw", window=a_btn)

e_img = PhotoImage(file='resources/e.png')
e_btn = Button(change, image=e_img, command=e, height=163, width=150, anchor="center", borderwidth=0)
e_btn_canvas = canvas.create_window(660, 69, anchor="nw", window=e_btn)

b_img = PhotoImage(file='resources/b.png')
b_btn = Button(change, image=b_img, command=b, height=163, width=150, anchor="center", borderwidth=0)
b_btn_canvas = canvas.create_window(820, 69, anchor="nw", window=b_btn)

f_img = PhotoImage(file='resources/f.png')
f_btn = Button(change, image=f_img, command=f, height=163, width=150, anchor="center", borderwidth=0)
f_btn_canvas = canvas.create_window(20, 250, anchor="nw", window=f_btn)

bb_img = PhotoImage(file='resources/bb.png')
bb_btn = Button(change, image=bb_img, command=bb, height=163, width=150, anchor="center", borderwidth=0)
bb_btn_canvas = canvas.create_window(180, 250, anchor="nw", window=bb_btn)

eb_img = PhotoImage(file='resources/eb.png')
eb_btn = Button(change, image=eb_img, command=eb, height=163, width=150, anchor="center", borderwidth=0)
eb_btn_canvas = canvas.create_window(340, 250, anchor="nw", window=eb_btn)

ab_img = PhotoImage(file='resources/ab.png')
ab_btn = Button(change, image=ab_img, command=ab, height=163, width=150, anchor="center", borderwidth=0)
ab_btn_canvas = canvas.create_window(500, 250, anchor="nw", window=ab_btn)

db_img = PhotoImage(file='resources/db.png')
db_btn = Button(change, image=db_img, command=db, height=163, width=150, anchor="center", borderwidth=0)
db_btn_canvas = canvas.create_window(660, 250, anchor="nw", window=db_btn)

gb_img = PhotoImage(file='resources/gb.png')
gb_btn = Button(change, image=gb_img, command=gb, height=163, width=150, anchor="center", borderwidth=0)
gb_btn_canvas = canvas.create_window(820, 250, anchor="nw", window=gb_btn)

confirm_img = PhotoImage(file='resources/Confirm.png')
confirm = Button(change, image=confirm_img, command=Confirm, height=51, width=278,anchor="center", borderwidth=0)
confirm_canvas = canvas.create_window(520, 480, anchor="nw",window = confirm)

#window loop
change.mainloop()
