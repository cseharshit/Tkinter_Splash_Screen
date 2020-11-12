from tkinter import *
from PIL import ImageTk, Image
from quotes import sherlocked


splash= Tk()
splash.overrideredirect(True)
# splash.geometry("1920x1080")
# splash_label= Label(splash, text="Splash Screen !!!", font=("Comic Sans MS", 20))
# splash_label.pack(pady=20)
# C = Canvas(splash, bg="blue", height=1920, width=1080)

filename = ImageTk.PhotoImage(Image.open("./Sher.jpg"))
background_label = Label(splash, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.pack()
#Splash Screen Timer
def main_window():
    splash.destroy()
    root= Tk()
    root.title('Sherlocked')
    root.geometry("500x300")
    # main_image=ImageTk.PhotoImage(Image.open("./main.jpg"))
    mainLabelText=StringVar()
    mainLabelText.set(sherlocked+"\n\n\n-Sherlock Holmes")
    main_label = Label(root, textvariable=mainLabelText, font=('Comic Sans MS', 20), wraplength=500, justify=CENTER )
    main_label.place(x=0,y=0,relwidth=1,relheight=1)
    main_label.pack(pady=20)

splash.after(5000, main_window)

mainloop()