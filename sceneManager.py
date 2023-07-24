import tkinter as tk
import os
from Config import conTheme as ctm
import time 
sTime = time.asctime() # type: ignore
theme = ctm.defaultTheme
user = os.environ.get('USERNAME',)

thisTheme = theme
thisTitle = f'User: {user} Login@: {sTime}'
thUltraDark = ctm.getTheme(theme, 'DK_MODE', 'ultraDark')
thDark = ctm.getTheme(theme, 'DK_MODE', 'dark')
thMedium = ctm.getTheme(theme, 'DK_MODE', 'medium')
thLight = ctm.getTheme(theme, 'DK_MODE', 'light')
thUltraLight = ctm.getTheme(theme, 'DK_MODE', 'ultraLight')
thWindowGeo = ctm.getTheme(theme, 'WIND', 'geometry')

def sceneManager():
    screenMain() # type: ignore

def screenMain():
    window = tk.Tk()
    window.title(thisTitle)
    window.configure(bg=thDark)
    # window.eval('tk::PlaceWindow . center')
    #window.columnconfigure(0, minsize=250)
    #window.rowconfigure(0, minsize=100)
    x = window.winfo_screenwidth() // 8
    y = int(window.winfo_screenwidth() * 0.001)
    window.geometry(thWindowGeo + str(x) + "+" + str(y))
    frame0 = tk.Frame(master=window, name="frLeft", width=500, height=400, bg=thDark , relief="raised", borderwidth=2)
    frame0.pack(side=tk.LEFT,padx=5, pady=20, fill='y')
    label0 = tk.Label(master=frame0, name='labTop0', width=40, height=2 ,text='sup      ', relief='raised', bg=thLight, fg=thLight,borderwidth=2, padx=5)
    label0.pack(anchor='n', padx=1)
    frame1 = tk.Frame(master=window, width=500, height=1100, relief='raised',borderwidth=2, bg=thDark)
    frame1.pack(side=tk.LEFT, padx=5, pady=20, fill='both')                      
    label1 = tk.Label(master=frame1, name='labTop1',width=160, height=2, relief='raised',text='Column1', bg=thDark, fg=thLight,borderwidth=2, padx=5)
    label1.pack(padx=1,)
    frame2 = tk.Frame(master=window, width=500, height=1100, relief='raised', borderwidth=2, bg=thUltraDark)
    frame2.pack(side=tk.RIGHT, padx=5, pady=20, fill='y')
    label2 = tk.Label(master=frame2, name='labTop2',width=140, height=2, relief='raised',text='Column2', bg=thDark, fg=thLight,borderwidth=2, padx=5)
    label2.pack(padx=1,)
    #frame2.rowconfigure(0, minsize=400)
    #frame2.columnconfigure(0, minsize=400)
    window.mainloop()
def screenLogin():
    window = tk.Tk()
    window.title(f'UserLogion: {thisTitle}')
    window.configure(bg=thDark)
    x = window.winfo_screenwidth() // 8
    y = int(window.winfo_screenwidth() * 0.001)
    window.geometry(thWindowGeo + str(x) + "+" + str(y))

    window.mainloop()
        # window.frame()

    '''for i in range(3):
        for j in range(3):
            frame = tk.Frame(
                master=window,
                relief=tk.RAISED,
                borderwidth=1
            )
            frame.grid(row=i, column=j, padx=5, pady=5)
            label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
            label.pack()'''
sceneManager()
