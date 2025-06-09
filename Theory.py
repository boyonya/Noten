from tkinter import*
import webbrowser
import os
import sys
import subprocess

#Create tkinter window
theory = Tk()
theory.geometry("1000x600")
canvas = Canvas(theory, width=1000, height=600)
canvas.pack(fill="both", expand=True)
bg=PhotoImage(file='resources/theorybg.png')
canvas.create_image(0,0,image=bg, anchor=NW)
theory.title("Noten")

#Restart program so that the same module can be imported again
def back():
    p = 'Noten.exe'
    subprocess.Popen(p)
    sys.exit()

#The webpage that each button will open
def c():
    webbrowser.open_new('https://m.basicmusictheory.com/c-major-key-signature')

def g():
    webbrowser.open_new('https://m.basicmusictheory.com/g-major-key-signature')

def d():
    webbrowser.open_new('https://m.basicmusictheory.com/d-major-key-signature')

def a():
    webbrowser.open_new('https://m.basicmusictheory.com/a-major-key-signature')

def e():
    webbrowser.open_new('https://m.basicmusictheory.com/e-major-key-signature')

def b():
    webbrowser.open_new('https://m.basicmusictheory.com/b-major-key-signature')

def f():
    webbrowser.open_new('https://m.basicmusictheory.com/f-major-key-signature')

def bb():
    webbrowser.open_new('https://m.basicmusictheory.com/b-flat-major-key-signature')

def eb():
    webbrowser.open_new('https://m.basicmusictheory.com/e-flat-major-key-signature')

def ab():
    webbrowser.open_new('https://m.basicmusictheory.com/a-flat-major-key-signature')

def db():
    webbrowser.open_new('https://m.basicmusictheory.com/d-flat-major-key-signature')

def gb():
    webbrowser.open_new('https://m.basicmusictheory.com/g-flat-major-key-signature')

#Buttons that call commands which can open webpages
back_img = PhotoImage(file='resources/Back.png')
btn = Button(theory, image=back_img, command=back, height=34, width=100, anchor = "center", borderwidth=0)
btn_canvas = canvas.create_window(20, 20, anchor = "nw", window = btn)

c_img = PhotoImage(file='resources/c.png')
c_btn = Button(theory, image=c_img, command=c, height=163, width=150, anchor="center", borderwidth=0)
c_btn_canvas = canvas.create_window(20, 160, anchor="nw", window=c_btn)

g_img = PhotoImage(file='resources/g.png')
g_btn = Button(theory, image=g_img, command=g, height=163, width=150, anchor="center", borderwidth=0)
g_btn_canvas = canvas.create_window(180, 160, anchor="nw", window=g_btn)

d_img = PhotoImage(file='resources/d.png')
d_btn = Button(theory, image=d_img, command=d, height=163, width=150, anchor="center", borderwidth=0)
d_btn_canvas = canvas.create_window(340, 160, anchor="nw", window=d_btn)

a_img = PhotoImage(file='resources/a.png')
a_btn = Button(theory, image=a_img, command=a, height=163, width=150, anchor="center", borderwidth=0)
a_btn_canvas = canvas.create_window(500, 160, anchor="nw", window=a_btn)

e_img = PhotoImage(file='resources/e.png')
e_btn = Button(theory, image=e_img, command=e, height=163, width=150, anchor="center", borderwidth=0)
e_btn_canvas = canvas.create_window(660, 160, anchor="nw", window=e_btn)

b_img = PhotoImage(file='resources/b.png')
b_btn = Button(theory, image=b_img, command=b, height=163, width=150, anchor="center", borderwidth=0)
b_btn_canvas = canvas.create_window(820, 160, anchor="nw", window=b_btn)

f_img = PhotoImage(file='resources/f.png')
f_btn = Button(theory, image=f_img, command=f, height=163, width=150, anchor="center", borderwidth=0)
f_btn_canvas = canvas.create_window(20, 360, anchor="nw", window=f_btn)

bb_img = PhotoImage(file='resources/bb.png')
bb_btn = Button(theory, image=bb_img, command=bb, height=163, width=150, anchor="center", borderwidth=0)
bb_btn_canvas = canvas.create_window(180, 360, anchor="nw", window=bb_btn)

eb_img = PhotoImage(file='resources/eb.png')
eb_btn = Button(theory, image=eb_img, command=eb, height=163, width=150, anchor="center", borderwidth=0)
eb_btn_canvas = canvas.create_window(340, 360, anchor="nw", window=eb_btn)

ab_img = PhotoImage(file='resources/ab.png')
ab_btn = Button(theory, image=ab_img, command=ab, height=163, width=150, anchor="center", borderwidth=0)
ab_btn_canvas = canvas.create_window(500, 360, anchor="nw", window=ab_btn)

db_img = PhotoImage(file='resources/db.png')
db_btn = Button(theory, image=db_img, command=db, height=163, width=150, anchor="center", borderwidth=0)
db_btn_canvas = canvas.create_window(660, 360, anchor="nw", window=db_btn)

gb_img = PhotoImage(file='resources/gb.png')
gb_btn = Button(theory, image=gb_img, command=gb, height=163, width=150, anchor="center", borderwidth=0)
gb_btn_canvas = canvas.create_window(820, 360, anchor="nw", window=gb_btn)

#Window loop
theory.mainloop()
