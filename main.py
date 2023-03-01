# platform for Juniper to test password, snmp, and telnet requirements.
# main.py contains gui menu for platform using tkinter:
# (Source: tutorialsteacher.com/python/create-gui-using-tkinter-python)

# import tinkter and create widgets
from tkinter import *
mainmenu = Tk()

# button widgets
button1 = Button(mainmenu, text="Telnet Scan", fg='red')
button1.place(x=80, y=100)
button2 = Button(mainmenu, text="SNMP string scan", fg='blue')
button2.place(x=80, y=135)
button3 = Button(mainmenu, text="password scan", fg='green')
button3.place(x=80, y=170)

# title widget
title = Label(mainmenu, text="Platform: Juniper", fg='black', font=("Helvetica", 16))
title.place(x=60, y=50)
subtitle = Label(mainmenu, text="Please select an option.", fg='black', font=("Helvetica", 8))
subtitle.place(x=60, y=75)

# window title and size
mainmenu.title('Platform: Juniper')
mainmenu.geometry("300x300+10+20")
mainmenu.mainloop()
