import tkinter as tk
from Config import conTheme as ctm


def sceneManager(theme,titleName):
    
    thUltraDark = ctm.getTheme(theme,'DKMODE','ultradark')
    thDark = ctm.getTheme(theme,'DKMODE','dark')
    thMedium = ctm.getTheme(theme,'DKMODE','medium')
    thLight = ctm.getTheme(theme,'DKMODE','light')
    thUltraLight = ctm.getTheme(theme,'DKMODE','ultraLight')
    thWindowGeo = ctm.getTheme(theme,'WIND','geometry')
    
    
    
    window = tk.Tk()
    window.title(titleName)
    window.configure(bg=thDark)
    # window.eval('tk::PlaceWindow . center')
    # window.columnconfigure(0, minsize=250)
    # window.rowconfigure(0, minsize=100)
    x = window.winfo_screenwidth() // 8
    y = int(window.winfo_screenwidth() * 0.001)
    window.geometry(thWindowGeo + str(x) + "+" + str(y))

    frame = tk.Frame(master=window, name="frame", width=500, height=400, bg=thDark # type: ignore
                     , relief="raised", padx=5, borderwidth=2)
    frame.pack(side=tk.LEFT, fill='y', padx=5, pady=20)
    label = tk.Label(master=frame, text='sup        ', relief='raised',
                     bg=thDark, fg=thLight, borderwidth=2, padx=5)
    label.pack(anchor='n')

    frame1 = tk.Frame(master=window, width=1100, height=1100, relief='raised',
                      borderwidth=2, bg=thMedium)
    frame1.pack(side=tk.LEFT, padx=5, pady=20, fill='both')
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

    window.mainloop()
