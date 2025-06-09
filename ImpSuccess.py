from tkinter import*
import sys
import subprocess
from tkinter import filedialog
import cv2
import numpy as np
import PIL.Image,  PIL.ImageTk

#Create tkinter window
Success = Tk()
Success.geometry("1000x600")
canvas = Canvas(Success, width=1000, height=600)
canvas.pack(fill="both", expand=True)
bg=PhotoImage(file='resources/importbg2.png')
canvas.create_image(0,0,image=bg, anchor=NW)
Success.title("Noten")

#Get the directory from the image imported into the Noten.py module and validated
f = open('file.txt')
directory = f.read()

sheet_music = cv2.imread(directory, cv2.IMREAD_UNCHANGED) #Read the image with the directory in the file

music_w = sheet_music.shape[1]
music_h = sheet_music.shape[0]
y = int((900*music_h)/music_w) #Resize image to display it inside tkinter window
resize = cv2.resize(sheet_music, (900, y))

img = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(resize))
canvas.create_image(500, 250, image=img, anchor="center")

flat = cv2.imread('template/flat.png', cv2.IMREAD_UNCHANGED) #Getting template attributes
flat_w = flat.shape[1]
flat_h = flat.shape[0]

sharp = cv2.imread('template/sharp.png', cv2.IMREAD_UNCHANGED)
sharp_w = sharp.shape[1]
sharp_h = sharp.shape[0]

threshold = 0.2

result_flat = cv2.matchTemplate(sheet_music, flat, cv2.TM_SQDIFF_NORMED) #Match image with templates
result_sharp = cv2.matchTemplate(sheet_music, sharp, cv2.TM_SQDIFF_NORMED)

location_flat = np.where(result_flat <= threshold) #Get the location of those matches
location_sharp = np.where(result_sharp <= threshold)

location_flat = list(zip(*location_flat[::-1])) #Repack the location returned form the cv2 matching
location_sharp = list(zip(*location_sharp[::-1]))

rectangles_flat = []
rectangles_sharp = []

for loc_f in location_flat: #draw rectangles at places where the flats and sharps are matched
    rect_f = [int(loc_f[0]), int(loc_f[1]), flat_w, flat_h]
    rectangles_flat.append(rect_f)
for loc_s in location_sharp:
    rect_s = [int(loc_s[0]), int(loc_s[1]), sharp_w, sharp_h]
    rectangles_sharp.append(rect_s)

rectangles_flat, weights = cv2.groupRectangles(rectangles_flat, 1,  0.5) #merge rectangles as they overlaps
rectangles_sharp, weights = cv2.groupRectangles(rectangles_sharp, 1,  0.5)

AmountofFlats = len(rectangles_flat) 
AmountofSharps = len(rectangles_sharp)

FlatScales = ['C', 'F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb'] #convert the amount of sharps and flats to its corresponding key signature
SharpScales = ['C', 'G', 'D', 'A', 'E', 'B']
if AmountofFlats == 0 and AmountofSharps < 6:
    KeySignature = SharpScales[AmountofSharps]
elif AmountofSharps == 0 and AmountofFlats <7:
    KeySignature  = FlatScales[AmountofFlats]

f2 = open("keysignature.txt", "w") #write the detected key signature into a file so other modules can access it
f2.write(KeySignature)
f2.close()

def back(): #Go back to main menu
    p = 'Noten.exe'
    subprocess.Popen(p)
    sys.exit()

def Confirm(): #Key signature correct, write the KeySignature into a different file which will be accessed by the conversion module
    f3 = open("KS.txt", "w")
    f3.write(KeySignature)
    f3.close()
    Success.destroy() #close window and run convert
    import Convert

def KSChange(): #change key signature (opens a new window)
    Success.destroy()
    import KSChange

#determines which button to display based of the detected/changed signature (for better appearance)
if KeySignature == 'C': 
    C_img = PhotoImage(file='resources/C2.png')
    C = Button(Success, image=C_img, command=KSChange, height=51,width=278,anchor="center", borderwidth=0)
    C_canvas = canvas.create_window (202, 460, anchor="nw",window = C)
elif KeySignature == 'G': 
    G_img = PhotoImage(file='resources/G2.png')
    G = Button(Success, image=G_img, command=KSChange, height=51,width=278,anchor="center", borderwidth=0)
    G_canvas = canvas.create_window (202, 460, anchor="nw",window = G)
elif KeySignature == 'D': 
    D_img = PhotoImage(file='resources/D2.png')
    D = Button(Success, image=D_img, command=KSChange, height=51,width=278,anchor="center", borderwidth=0)
    D_canvas = canvas.create_window (202, 460, anchor="nw",window = D)
elif KeySignature == 'A': 
    A_img = PhotoImage(file='resources/A2.png')
    A = Button(Success, image=A_img, command=KSChange, height=51,width=278,anchor="center", borderwidth=0)
    A_canvas = canvas.create_window (202, 460, anchor="nw",window = A)
elif KeySignature == 'E': 
    E_img = PhotoImage(file='resources/E2.png')
    E = Button(Success, image=E_img, command=KSChange, height=51,width=278,anchor="center", borderwidth=0)
    E_canvas = canvas.create_window (202, 460, anchor="nw",window = E)
elif KeySignature == 'B': 
    B_img = PhotoImage(file='resources/B2.png')
    B = Button(Success, image=B_img, command=KSChange, height=51,width=278,anchor="center", borderwidth=0)
    B_canvas = canvas.create_window (202, 460, anchor="nw",window = B)
elif KeySignature == 'F': 
    F_img = PhotoImage(file='resources/F2.png')
    F = Button(Success, image=F_img, command=KSChange, height=51,width=278,anchor="center", borderwidth=0)
    F_canvas = canvas.create_window (202, 460, anchor="nw",window = F)
elif KeySignature == 'Bb': 
    Bb_img = PhotoImage(file='resources/Bb2.png')
    Bb = Button(Success, image=Bb_img, command=KSChange, height=51,width=278,anchor="center", borderwidth=0)
    Bb_canvas = canvas.create_window (202, 460, anchor="nw",window = Bb)
elif KeySignature == 'Eb': 
    Eb_img = PhotoImage(file='resources/Eb2.png')
    Eb = Button(Success, image=Eb_img, command=KSChange, height=51,width=278,anchor="center", borderwidth=0)
    Eb_canvas = canvas.create_window (202, 460, anchor="nw",window = Eb)
elif KeySignature == 'Ab': 
    Ab_img = PhotoImage(file='resources/Ab2.png')
    Ab = Button(Success, image=Ab_img, command=KSChange, height=51,width=278,anchor="center", borderwidth=0)
    Ab_canvas = canvas.create_window (202, 460, anchor="nw",window = Ab)
elif KeySignature == 'Db': 
    Db_img = PhotoImage(file='resources/Db2.png')
    Db = Button(Success, image=Db_img, command=KSChange, height=51,width=278,anchor="center", borderwidth=0)
    Db_canvas = canvas.create_window (202, 460, anchor="nw",window = Db)
elif KeySignature == 'Gb': 
    Gb_img = PhotoImage(file='resources/Gb2.png')
    Gb = Button(Success, image=Gb_img, command=KSChange, height=51,width=278,anchor="center", borderwidth=0)
    Gb_canvas = canvas.create_window (202, 460, anchor="nw",window = Gb)


#other buttons
confirm_img = PhotoImage(file='resources/Confirm.png')
confirm = Button(Success, image=confirm_img, command=Confirm, height=51, width=278,anchor="center", borderwidth=0)
confirm_canvas = canvas.create_window(520, 460, anchor="nw",window = confirm)
    
back_img = PhotoImage(file='resources/Back.png')
btn = Button(Success, image=back_img, command=back, height=34, width=100, anchor = "center", borderwidth=0)
btn_canvas = canvas.create_window(20, 20, anchor = "nw", window = btn)

#Window loop
Success.mainloop()
