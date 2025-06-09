from tkinter import*
import sys
import subprocess
from tkinter import filedialog
import cv2
import numpy as np
import os

#Create tkinter window
Fail = Tk()
Fail.geometry("1000x600")
canvas = Canvas(Fail, width=1000, height=600)
canvas.pack(fill="both", expand=True)
bg=PhotoImage(file='resources/importbg.png')
canvas.create_image(0,0,image=bg, anchor=NW)
Fail.title("Noten")

def back(): #Restart the program so other modules can be imported again
    p = 'Noten.exe'
    subprocess.Popen(p)
    sys.exit()

def help2(): #Opens the powerpoint which is the user guide
    file = 'User Manual.ppsm'
    os.startfile(file)

def Other(): #Import a new image with file explorer and checks for the validity (same as the one in Noten.py)
    file = filedialog.askopenfilename()
    if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg'):
        sheet_music = cv2.imread(file, cv2.IMREAD_UNCHANGED)
        
        clef = cv2.imread('template/clef.png', cv2.IMREAD_UNCHANGED)
        clef_w = clef.shape[1]
        clef_h = clef.shape[0]

        threshold = 0.2
        result_clef = cv2.matchTemplate(sheet_music, clef, cv2.TM_SQDIFF_NORMED)

        if result_clef.any():
            f = open('file.txt','w')
            f.write(file)
            f.close()
            Fail.destroy()
            import ImpSuccess

#Buttons that calls for commands
help2_img = PhotoImage(file='resources/help2.png')
help2 = Button(Fail, image=help2_img, command=help2, height=51, width=278,anchor="center", borderwidth=0)
help2_canvas = canvas.create_window(202, 480, anchor="nw",window = help2)

other_img = PhotoImage(file='resources/Other.png')
other = Button(Fail, image=other_img, command=Other, height=51, width=278,anchor="center", borderwidth=0)
other_canvas = canvas.create_window(520, 480, anchor="nw",window = other)
    
back_img = PhotoImage(file='resources/Back.png')
btn = Button(Fail, image=back_img, command=back, height=34, width=100, anchor = "center", borderwidth=0)
btn_canvas = canvas.create_window(20, 20, anchor = "nw", window = btn)

#Window loop
Fail.mainloop()
