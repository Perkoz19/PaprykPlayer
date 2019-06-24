from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
from player import Player

plr = Player()
pathtofile = ''
selected = 0


def browseFile():
    # index = 0
    global pathtofile
    pathtofile = filedialog.askopenfilename()
    plr.musicAdd(pathtofile)
    fname = os.path.basename(pathtofile)
    playlistbox.insert(END, fname)
    # index += 1


def playFile(*args):
    selected = playlistbox.curselection()
    if len(selected) != 0:
        selected = int(selected[0])
    else:
        selected = 0
    plr.musicPlay(selected)


def nextFile(selected):
    plr.musicNext(selected)


def playRandom():
    plr.musicPlayRandom()


root = Tk()
root.title("Papryk Player")

root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)

playlistframe = ttk.Frame(root)
secondframe = ttk.Frame(root)

playlistframe.grid(row=1, column=0, sticky=(N, S, W, E))
secondframe.grid(row=0, column=0)

playlistframe.rowconfigure(0, weight=1)
playlistframe.columnconfigure(0, weight=1)

playlistbox = Listbox(playlistframe)
playlistbox.grid(row=0, column=0, sticky=(N, S, W, E))

add = ttk.Button(secondframe, text="Add file...", command=browseFile)
add.grid(column=0, row=0)
play = ttk.Button(secondframe, text="Play!", command=playFile)
play.grid(column=1, row=0)
pause = ttk.Button(secondframe, text="Pause!", command=lambda: plr.musicPause())
pause.grid(column=2, row=0)
next = ttk.Button(secondframe, text="Random!", command=playRandom)
next.grid(column=3, row=0)

playlistbox.bind('<Double-Button-1>', playFile)

root.mainloop()
