from tkinter import*
import sys
from tkinter import filedialog
import cv2
import numpy as np
import PIL.Image,  PIL.ImageTk
from io import BytesIO
import win32clipboard
from PIL import Image
import os
import subprocess

#Create tkinter window
Convert = Tk()
Convert.geometry("1000x600")
canvas = Canvas(Convert, width=1000, height=600)
canvas.pack(fill="both", expand=True)
bg=PhotoImage(file='resources/convertbg.png')
canvas.create_image(0,0,image=bg, anchor=NW)
Convert.title("Noten")

#read file for directory of image
f = open('file.txt')
directory = f.read()

#read file for key signature of sheet music
f2 = open('KS.txt')
KeySignature = f2.read()

#read image
sheet_music = cv2.imread(directory, cv2.IMREAD_UNCHANGED)

#import attributes of the templates
quarter = cv2.imread('template/quarter.png', cv2.IMREAD_UNCHANGED)
quarter_w = quarter.shape[1]
quarter_h = quarter.shape[0]

semi = cv2.imread('template/semi.png', cv2.IMREAD_UNCHANGED)
semi_w = semi.shape[1]
semi_h = semi.shape[0]

whole = cv2.imread('template/whole.png', cv2.IMREAD_UNCHANGED)
whole_w = whole.shape[1]
whole_h = whole.shape[0]

clef = cv2.imread('template/clef.png', cv2.IMREAD_UNCHANGED)
clef_w = clef.shape[1]
clef_h = clef.shape[0]

threshold_q = 0.2
threshold_s = 0.2
threshold_w = 0.2
threshold_c = 0.1

#matching template with image
result_quarter = cv2.matchTemplate(sheet_music, quarter, cv2.TM_SQDIFF_NORMED)
result_semi = cv2.matchTemplate(sheet_music, semi, cv2.TM_SQDIFF_NORMED)
result_whole = cv2.matchTemplate(sheet_music, whole, cv2.TM_SQDIFF_NORMED)
result_clef = cv2.matchTemplate(sheet_music, clef, cv2.TM_SQDIFF_NORMED)

#record locations where they are certainly matched
location_quarter = np.where(result_quarter <= threshold_q)
location_semi = np.where(result_semi <= threshold_s)
location_whole = np.where(result_whole <= threshold_w)
location_clef = np.where(result_clef <= threshold_c)

#unpack locations and change to array
location_quarter = list(zip(*location_quarter[::-1]))
location_semi = list(zip(*location_semi[::-1]))
location_whole = list(zip(*location_whole[::-1]))
location_clef = list(zip(*location_clef[::-1]))

rectangles_quarter = []
rectangles_semi = []
rectangles_whole = []
rectangles_clef = []

#draw rectangles for each match
for loc_q in location_quarter:
    rect_q = [int(loc_q[0]), int(loc_q[1]), quarter_w, quarter_h]
    rectangles_quarter.append(rect_q)
for loc_s in location_semi:
    rect_s = [int(loc_s[0]), int(loc_s[1]), semi_w, semi_h]
    rectangles_semi.append(rect_s)
for loc_w in location_whole:
    rect_w = [int(loc_w[0]), int(loc_w[1]), whole_w, whole_h]
    rectangles_whole.append(rect_w)
for loc_c in location_clef:
    rect_c = [int(loc_c[0]), int(loc_c[1]), clef_w, clef_h]
    rectangles_clef.append(rect_c)

#merge rectangles so that each note have only one rectangle
rectangles_quarter, weights = cv2.groupRectangles(rectangles_quarter, 1,  0.5)
rectangles_semi, weights = cv2.groupRectangles(rectangles_semi, 1,  0.5)
rectangles_whole, weights = cv2.groupRectangles(rectangles_whole, 1,  0.5)
rectangles_clef, weights = cv2.groupRectangles(rectangles_clef, 1,  0.5)

#conversion table for position value to notes for each key signature
KSList = {
    'C' : ['B', 'A', 'G', 'F', 'E', 'D', 'C', 'B', 'A', 'G', 'F', 'E', 'D', 'C'],
    'F' : ['Bb', 'A', 'G', 'F', 'E', 'D', 'C', 'Bb', 'A', 'G', 'F', 'E', 'D', 'C'],
    'Bb' : ['Bb', 'A', 'G', 'F', 'Eb', 'D', 'C', 'Bb', 'A', 'G', 'F', 'Eb', 'D', 'C', ],
    'Eb' : ['Bb', 'Ab', 'G', 'F', 'Eb', 'D', 'C', 'Bb', 'Ab', 'G', 'F', 'Eb', 'D', 'C'],
    'Ab' : ['Bb', 'Ab', 'G', 'F', 'Eb', 'Db', 'C', 'Bb', 'Ab', 'G', 'F', 'Eb', 'Db', 'C'],
    'Db' : ['Bb', 'Ab', 'Gb', 'F', 'Eb', 'Db', 'C', 'Bb', 'Ab', 'Gb', 'F', 'Eb', 'Db', 'C'],
    'Gb' : ['Bb', 'Ab', 'Gb', 'F', 'Eb', 'Db', 'B', 'Bb', 'Ab', 'Gb', 'F', 'Eb', 'Db', 'B'],
    'G' : ['B', 'A', 'G', 'F#', 'E', 'D', 'C', 'B', 'A', 'G', 'F#', 'E', 'D', 'C'],
    'D' : ['B', 'A', 'G', 'F#', 'E', 'D', 'C#', 'B', 'A', 'G', 'F#', 'E', 'D', 'C#'],
    'A' : ['B', 'A', 'G#', 'F#', 'E', 'D', 'C#', 'B', 'A', 'G#', 'F#', 'E', 'D', 'C#'],
    'E' : ['B', 'A', 'G#', 'F#', 'E', 'D#', 'C#', 'B', 'A', 'G#', 'F#', 'E', 'D#', 'C#'],
    'B' : ['B', 'A#', 'G#', 'F#', 'E', 'D#', 'C#', 'B', 'A#', 'G#', 'F#', 'E', 'D#', 'C#']
}

#annotation font
font = cv2.FONT_HERSHEY_DUPLEX
fontScale = 4
color = (0, 0, 0)
thickness = 10

y_location_q = []
y_location_s = []
y_location_w = []
y_location_c = []

#locate the clef and where the staff lines are
if len(rectangles_clef):
    for (x, y, w, h) in rectangles_clef:
        top_left = (x, y)
        y_location_c = int(top_left[1])

#find note position and convert to letter notation
if len(rectangles_quarter):
    for (x, y, w, h) in rectangles_quarter:
        top_left = (x, y)
        bottom_right = (x + w, y + h)
        y_pos_q = int(top_left[1]) + int(quarter_h/2) #this is the middle point of the note
        y_location_q.append(y_pos_q)
        PositionValue = round(((y_pos_q) - (y_location_c) + 3 * (clef_h/8))/(clef_h/8)) #how many notes is it away from the highest note that can be detected
        a = KSList[KeySignature]
        NoteValue = a[PositionValue] #conversion between position value and note value
        y = int(sheet_music.shape[0] - clef_h/16)
        pos = (x, y)
        cv2.putText(sheet_music, NoteValue, pos, font, fontScale, color, thickness, cv2.LINE_AA) #text overlay on image

if len(rectangles_semi):
    for (x, y, w, h) in rectangles_semi:
        top_left = (x, y)
        bottom_right = (x + w, y + h)
        y_pos_s = int(top_left[1]) + int(semi_h/2)
        y_location_s.append(y_pos_s)
        PositionValue = round(((y_pos_s) - (y_location_c) + 3 * (clef_h/8))/(clef_h/8))
        a = KSList[KeySignature]
        NoteValue = a[PositionValue]
        y = int(sheet_music.shape[0] - clef_h/16)
        pos = (x, y)
        cv2.putText(sheet_music, NoteValue, pos, font, fontScale, color, thickness, cv2.LINE_AA)
        
if len(rectangles_whole):
    for (x, y, w, h) in rectangles_whole:
        top_left = (x, y)
        bottom_right = (x + w, y + h)
        y_pos_w = int(top_left[1]) + int(whole_h/2)
        y_location_w.append(y_pos_w)
        PositionValue = round(((y_pos_w) - (y_location_c) + 3 * (clef_h/8))/(clef_h/8))
        a = KSList[KeySignature]
        NoteValue = a[PositionValue]
        y = int(sheet_music.shape[0] - clef_h/16)
        pos = (x, y)
        cv2.putText(sheet_music, NoteValue, pos, font, fontScale, color, thickness, cv2.LINE_AA)

#go back to menu
def back():
    p = 'Noten.exe'
    subprocess.Popen(p)
    sys.exit()

#output the image by opening file explorer to select directory
def Output():
    directory = filedialog.askdirectory()
    os.chdir(directory)
    cv2.imwrite('noten.png', sheet_music)

#copy the image to the computer's clipboard
def Copy():
    def send_to_clipboard(clip_type, data):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(clip_type, data)
        win32clipboard.CloseClipboard()

    image = Image.fromarray(sheet_music)
    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()

    send_to_clipboard(win32clipboard.CF_DIB, data)

#resize image for better display
music_w = sheet_music.shape[1]
music_h = sheet_music.shape[0]
y = int((1000*music_h)/music_w)
resize = cv2.resize(sheet_music, (1000, y))

#buttons that call the commands
export_img = PhotoImage(file='resources/export.png')
export = Button(Convert, image=export_img, command=Output, height=51,width=278,anchor="center", borderwidth=0)
export_canvas = canvas.create_window (520, 360, anchor="nw",window = export)

copy_img = PhotoImage(file='resources/copy.png')
copy = Button(Convert, image=copy_img, command=Copy, height=51,width=278,anchor="center", borderwidth=0)
copy_canvas = canvas.create_window (202, 360, anchor="nw",window = copy)

back_img = PhotoImage(file='resources/Back.png')
btn = Button(Convert, image=back_img, command=back, height=34, width=100, anchor = "center", borderwidth=0)
btn_canvas = canvas.create_window(20, 20, anchor = "nw", window = btn)

#provides a preview of the annotated image
cv2.imshow('Preview', resize)

#Window loop
Convert.mainloop()
