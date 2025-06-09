from tkinter import*
import os
from tkinter import filedialog
import cv2
import numpy as np

#Create tkinter window
root = Tk()
root.geometry("1000x600")
canvas = Canvas(root, width=1000, height=600)
canvas.pack(fill="both", expand=True)
root.title("Noten")
title=PhotoImage(file='resources/title.png')
canvas.create_image(0,0,image=title, anchor=NW)

#When called will close current window and run Theory.py
def theory():
    root.destroy()
    import Theory

def Imp():
    root.destroy #Close window
    file = filedialog.askopenfilename() #Get user to select file for import
    if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg'): #Check for file formatting
        sheet_music = cv2.imread(file, cv2.IMREAD_UNCHANGED)
        
        clef = cv2.imread('template/clef.png', cv2.IMREAD_UNCHANGED) #Import clef template and attributes
        clef_w = clef.shape[1]
        clef_h = clef.shape[0]

        threshold = 0.2 #Template matching threshold
        try: 
            result_clef = cv2.matchTemplate(sheet_music, clef, cv2.TM_SQDIFF_NORMED) #Test to see if a clef can be located
            if len(result_clef):
                f = open('file.txt','w') #If yes: write image directory into a text file, and run ImpSuccess
                f.write(file)
                f.close()
                root.destroy()
                import ImpSuccess
        except cv2.error as e: #If not: run ImpFail
            root.destroy()
            import ImpFail

def help(): #Opens a powerpoint show file which is the user guide
    file = 'User Manual.ppsm'
    os.startfile(file)

def settings(): #Opens settings
    root.destroy()
    import Settings

#Buttons that can call commands
convert_img = PhotoImage(file='resources/convert.png')
btn = Button(root, image=convert_img, command=Imp, height=213, width=200, anchor = "center", borderwidth=0)
btn_canvas = canvas.create_window(60, 300, anchor = "nw", window = btn)

theory_img = PhotoImage(file='resources/theory.png')
btn = Button(root, image=theory_img, command=theory, height=213, width=200, anchor = "center", borderwidth=0)
btn_canvas = canvas.create_window(275, 300, anchor = "nw", window = btn)

help_img = PhotoImage(file='resources/help.png')
btn = Button(root, image=help_img, command=help, height=213, width=200, anchor = "center", borderwidth=0)
btn_canvas = canvas.create_window(490, 300, anchor = "nw", window = btn)

settings_img = PhotoImage(file='resources/settings.png')
btn = Button(root, image=settings_img, command=settings, height=213, width=200, anchor = "center", borderwidth=0)
btn_canvas = canvas.create_window(705, 300, anchor = "nw", window = btn)

#Window loop
root.mainloop()
