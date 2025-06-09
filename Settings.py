from tkinter import*
import sys
import subprocess

#Create tkinter window
settings = Tk()
settings.geometry("1000x600")
canvas = Canvas(settings, width=1000, height=600)
canvas.pack(fill="both", expand=True)
bg=PhotoImage(file='resources/settingsbg.png')
canvas.create_image(0,0,image=bg, anchor=NW)
settings.title("Noten")

#Restart program so that same module can be opened again with import
def back():
    p = 'Noten.exe'
    subprocess.Popen(p)
    sys.exit()

#Button that go back
back_img = PhotoImage(file='resources/Back.png')
btn = Button(settings, image=back_img, command=back, height=34, width=100, anchor = "center", borderwidth=0)
btn_canvas = canvas.create_window(20, 20, anchor = "nw", window = btn)

#Window loop
settings.mainloop()
