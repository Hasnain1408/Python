from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("my First GUI program")
window.config(background="#5cfcff")

icon = PhotoImage(file='img/photoshop.png')
window.iconphoto(True, icon)
window.mainloop()