import tkinter as tk
import os
from Config import conTheme as ctm
import time 
from tkinter import * 
from tkinter.ttk import * 
from time import strftime
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
    screenLogin()
    screenMain() # type: ignore

def screenMain():
    root = Tk()
    root.title(thisTitle)
    menubar = Menu(root)
    root.configure(bg=thDark)
    # root.eval('tk::Placeroot . center')
    #root.columnconfigure(0, minsize=250)
    #root.rowconfigure(0, minsize=100)
    x = root.winfo_screenwidth() // 8
    y = int(root.winfo_screenwidth() * 0.001)
    root.geometry(thWindowGeo + str(x) + "+" + str(y))
        
    # Creating Menubar
    
    # Adding File Menu and commands
    file = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='File', menu = file)
    file.add_command(label ='New File', command = None)
    file.add_command(label ='Open...', command = None)
    file.add_command(label ='Save', command = None)
    file.add_separator()
    file.add_command(label ='Exit', command = root.destroy)
    # Adding Edit Menu and commands
    edit = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Edit', menu = edit)
    edit.add_command(label ='Cut', command = None)
    edit.add_command(label ='Copy', command = None)
    edit.add_command(label ='Paste', command = None)
    edit.add_command(label ='Select All', command = None)
    edit.add_separator()
    edit.add_command(label ='Find...', command = None)
    edit.add_command(label ='Find again', command = None)
    # Adding Help Menu
    help_ = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Help', menu = help_)
    help_.add_command(label ='Tk Help', command = None)
    help_.add_command(label ='Demo', command = None)
    help_.add_separator()
    help_.add_command(label ='About Tk', command = None)
    root.config(menu = menubar, background='black',
                       cursor='hand2')
    
    # Frames and Labels
    frame0 = tk.Frame(master=root, name="frLeft", width=500, height=400, bg=thDark , relief="raised", borderwidth=2)
    frame0.pack(side=tk.LEFT,padx=5, pady=20, fill='y')
    label0 = tk.Label(master=frame0, name='labTop0', width=40, height=2 ,text='sup      ', relief='raised', bg=thLight, fg=thLight,borderwidth=2, padx=5)
    label0.pack(anchor='n', padx=1)
    frame1 = tk.Frame(master=root, width=500, height=1100, relief='raised',borderwidth=2, bg=thDark)
    frame1.pack(side=tk.LEFT, padx=5, pady=20, fill='both')                      
    label1 = tk.Label(master=frame1, name='labTop1',width=160, height=2, relief='raised',text='Column1', bg=thDark, fg=thLight,borderwidth=2, padx=5)
    label1.pack(padx=1,)
    frame2 = tk.Frame(master=root, width=500, height=1100, relief='raised', borderwidth=2, bg=thUltraDark)
    frame2.pack(side=tk.RIGHT, padx=5, pady=20, fill='y')
    label2 = tk.Label(master=frame2, name='labTop2',width=140, height=2, relief='raised',text='Column2', bg=thDark, fg=thLight,borderwidth=2, padx=5)
    label2.pack(padx=1,)
    root.mainloop()
        
    #Background frames and labels
    #frame2.rowconfigure(0, minsize=400)
    #frame2.columnconfigure(0, minsize=400)

    
def screenLogin():
    root = tk.Tk()
    root.title(f'UserLogion: {thisTitle}')
    '''    root.configure(bg=thDark)
    x = root.winfo_screenwidth() // 8
    y = int(root.winfo_screenwidth() * 0.001)
    root.geometry(thWindowGeo + str(x) + "+" + str(y))
    '''    # Creating Menubar
    menubar = tk.Menu(root)
    
    # Adding File Menu and commands
    file = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='File', menu = file)
    file.add_command(label ='New File', command = None)
    file.add_command(label ='Open...', command = None)
    file.add_command(label ='Save', command = None)
    file.add_separator()
    file.add_command(label ='Exit', command = root.destroy)
    
    # Adding Edit Menu and commands
    edit = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Edit', menu = edit)
    edit.add_command(label ='Cut', command = None)
    edit.add_command(label ='Copy', command = None)
    edit.add_command(label ='Paste', command = None)
    edit.add_command(label ='Select All', command = None)
    edit.add_separator()
    edit.add_command(label ='Find...', command = None)
    edit.add_command(label ='Find again', command = None)
    
    # Adding Help Menu
    help_ = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Help', menu = help_)
    help_.add_command(label ='Tk Help', command = None)
    help_.add_command(label ='Demo', command = None)
    help_.add_separator()
    help_.add_command(label ='About Tk', command = None)

    root.config(menu = menubar)
    root.mainloop()
        
'''    #Background frames and labels
    frame0 = tk.Frame(master=root, name="frLeft", width=500, height=400, bg=thDark , relief="raised", borderwidth=2)
    frame0.pack(side=tk.LEFT,padx=5, pady=20, fill='y')
    label0 = tk.Label(master=frame0, name='labTop0', width=40, height=2 ,text='sup      ', relief='raised', bg=thLight, fg=thLight,borderwidth=2, padx=5)
    label0.pack(anchor='n', padx=1)
    frame1 = tk.Frame(master=root, width=500, height=1100, relief='raised',borderwidth=2, bg=thDark)
    frame1.pack(side=tk.LEFT, padx=5, pady=20, fill='both')                      
    label1 = tk.Label(master=frame1, name='labTop1',width=160, height=2, relief='raised',text='Column1', bg=thDark, fg=thLight,borderwidth=2, padx=5)
    label1.pack(padx=1,)
    frame2 = tk.Frame(master=root, width=500, height=1100, relief='raised', borderwidth=2, bg=thUltraDark)
    frame2.pack(side=tk.RIGHT, padx=5, pady=20, fill='y')
    label2 = tk.Label(master=frame2, name='labTop2',width=140, height=2, relief='raised',text='Column2', bg=thDark, fg=thLight,borderwidth=2, padx=5)
    label2.pack(padx=1,)
    #frame2.rowconfigure(0, minsize=400)
    #frame2.columnconfigure(0, minsize=400)
'''  


        # root.frame()
def test(): 
    # creating tkinter window
    root = Tk()
    root.title('test')
    x = root.winfo_screenwidth() // 8
    y = int(root.winfo_screenwidth() * 0.001)
    root.geometry(thWindowGeo + str(x) + "+" + str(y))

    root.configure(bg=thDark)
    
    # Creating Menubar
    menubar = Menu(root)
    
    # Adding File Menu and commands
    file = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='File', menu = file)
    file.add_command(label ='New File', command = None)
    file.add_command(label ='Open...', command = None)
    file.add_command(label ='Save', command = None)
    file.add_separator()
    file.add_command(label ='Exit', command = root.destroy)
    
    # Adding Edit Menu and commands
    edit = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Edit', menu = edit)
    edit.add_command(label ='Cut', command = None)
    edit.add_command(label ='Copy', command = None)
    edit.add_command(label ='Paste', command = None)
    edit.add_command(label ='Select All', command = None)
    edit.add_separator()
    edit.add_command(label ='Find...', command = None)
    edit.add_command(label ='Find again', command = None)
    
    # Adding Help Menu
    help_ = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Help', menu = help_)
    help_.add_command(label ='Tk Help', command = None)
    help_.add_command(label ='Demo', command = None)
    help_.add_separator()
    help_.add_command(label ='About Tk', command = None)
    
    # display Menu
    root.config(menu = menubar)
    mainloop()

sceneManager()
