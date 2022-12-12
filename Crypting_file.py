import os
import subprocess
import sys
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd

root = Tk()
root.title("Crypting file")

# center window
# set window size
WIN_WIDTH = 500
WIN_HEIGHT = 300
# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# find the center point
center_x = int(screen_width / 2 - WIN_WIDTH / 2)
center_y = int(screen_height / 2 - WIN_HEIGHT / 2)
# set the position of the window to the center of the screen
root.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}+{center_x}+{center_y}")

FILE_NAME = 'Set file to crypt'
LEN_PASS = 64

# Creates top frame
frame1 = LabelFrame(root, width=500, height=280, bd=5)
frame1.grid(sticky="WE")

# Creates bottom frame
frame2 = LabelFrame(root, width=500, height=20, bd=0)
frame2.grid(sticky="WE")

root.grid_columnconfigure(0, weight=1)
frame1.grid_columnconfigure(0, weight=1)
frame2.grid_columnconfigure(0, weight=1)


def enable(children):
    for child in children:
        child.configure(state='enable')


def load_encryption():
    global FILE_NAME
    FILE_NAME = fd.askopenfilename(title='Choose a file',
                                   filetypes=[('all', '*.*')
                                              ])

    if len(FILE_NAME) > 0:
        file_entry = ttk.Entry(frame1)
        file_entry.insert(END, FILE_NAME)
        file_entry.grid(row=3, column=0, sticky="WE", pady=2)
        but_Crypt.grid(row=4, column=0, sticky="WE", pady=2)
        but_Create_Pass.grid(row=5, column=0, sticky="WE", pady=2)


def load_decryption():
    global FILE_NAME
    FILE_NAME = fd.askopenfilename(title='Choose a enc file',
                                   filetypes=[('encrypted', '*.enc')
                                              ])
    if len(FILE_NAME) > 0:
        file_entry = ttk.Entry(frame1)
        file_entry.insert(END, FILE_NAME)
        file_entry.grid(row=3, column=0, sticky="WE", pady=2)
        but_Decrypts.grid(row=4, column=0, sticky="WE", pady=2)


def encrypt():
    try:
        pname = os.path.dirname(os.path.abspath(FILE_NAME))+"\\pass.txt"
        fname, fextension = os.path.splitext(FILE_NAME)
        value = 'encryption.bat '+fname+' '+fextension+' '+pname
        print(fname)
        print(fextension)
        print(value)
        subprocess.call(value)
        for child in frame1.winfo_children():
            child.configure(state='disable')
        but_done.grid(row=5, column=0, sticky="WE", pady=2)
    except ValueError:
        pass


def decrypts():
    try:
        pname = os.path.dirname(os.path.abspath(FILE_NAME))+"\\pass.txt"
        fname, fextension = os.path.splitext(FILE_NAME)
        value = 'decryption.bat '+fname+' '+fextension+' '+pname
        print(fname)
        print(fextension)
        print(value)
        subprocess.call(value)
        for child in frame1.winfo_children():
            child.configure(state='disable')
        but_done.grid(row=5, column=0, sticky="WE", pady=2)
    except ValueError:
        pass


def set_len_newpass():
    pass_entry = Entry(frame1)
    pass_entry.insert(END, LEN_PASS)
    but_set_len = Button(
        frame1, text="Ok", command=lambda: create_newpass(pass_entry.get()))
    pass_entry.grid(row=6, column=0, sticky="W", pady=2)
    but_set_len.grid(row=6, column=0, sticky="E", pady=2)


def create_newpass(LEN_PASS):
    try:
        pname = os.path.dirname(os.path.abspath(FILE_NAME))+"\\pass.txt"
        value = 'create_pass.bat ' + pname+' ' + str(LEN_PASS)
        subprocess.call(value)
        for child in frame1.winfo_children():
            child.configure(state='disable')
        but_done.grid(row=7, column=0, sticky="WE", pady=2)
    except ValueError:
        pass


def reload_script():
    os.execl(sys.executable, sys.executable, *sys.argv)


but_File_to_Crypt = ttk.Button(
    frame1, text="File to Crypt",  command=load_encryption)
but_File_to_Decrypts = ttk.Button(
    frame1, text="File to Decrypts", command=load_decryption)
but_Create_Pass = Button(
    frame1, text="Create new pass", command=set_len_newpass)

but_File_to_Crypt.grid(row=0, column=0, sticky="WE", pady=2)
but_File_to_Decrypts.grid(row=1, column=0, sticky="WE", pady=2)


but_Crypt = ttk.Button(frame1, text="Crypt", command=encrypt)
but_Decrypts = ttk.Button(frame1, text="Decrypts", command=decrypts)

but_done = Button(frame2, text="Done!", bg="#449B32",
                  fg="#fff", command=reload_script)

root.mainloop()