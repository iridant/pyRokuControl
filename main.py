import tkinter as tk 
import tkinter.font as tkfont
import requests

roku_address = "http://192.168.0.8:8060"

r = tk.Tk() 
r.title("Roku Remote")
r.configure(bg="black")
r.resizable(False, False)

def selectClick():
	requests.post("{}/keypress/select".format(roku_address))

def downClick():
	requests.post("{}/keypress/down".format(roku_address))

def upClick():
	requests.post("{}/keypress/up".format(roku_address))

def leftClick():
	requests.post("{}/keypress/left".format(roku_address))

def rightClick():
	requests.post("{}/keypress/right".format(roku_address))

def homeClick():
	requests.post("{}/keypress/home".format(roku_address))

def backClick():
	requests.post("{}/keypress/back".format(roku_address))

def fwdClick():
	requests.post("{}/keypress/fwd".format(roku_address))

def rwdClick():
	requests.post("{}/keypress/rwd".format(roku_address))

def replayClick():
	requests.post("{}/keypress/instantreplay".format(roku_address))

def infoClick():
	requests.post("{}/keypress/info".format(roku_address))

def ppClick():
	requests.post("{}/keypress/play".format(roku_address))


selectButton = tk.Button(r, height=5, width=10, text="o", command=selectClick, bg='purple', fg='white')
selectButton.grid(row=2,column=2)

upButton = tk.Button(r, height=5, width=10, text="^", command=upClick, bg='purple', fg='white')
upButton.grid(row=1,column=2)

downButton = tk.Button(r, height=5, width=10, text="v", command=downClick, bg='purple', fg='white')
downButton.grid(row=3,column=2)

leftButton = tk.Button(r, height=5, width=10, text="<", command=leftClick, bg='purple', fg='white')
leftButton.grid(row=2,column=1)

rightButton = tk.Button(r, height=5, width=10, text=">", command=rightClick, bg='purple', fg='white')
rightButton.grid(row=2,column=3)

homeButton = tk.Button(r, height=5, width=10, text="HOME", command=homeClick, bg='purple', fg='white')
homeButton.grid(row=1,column=3)

backButton = tk.Button(r, height=5, width=10, text="BACK", command=backClick, bg='purple', fg='white')
backButton.grid(row=1,column=1)

fwdButton = tk.Button(r, height=5, width=10, text=">>", command=fwdClick, bg='purple', fg='white')
fwdButton.grid(row=4,column=3)

rwdButton = tk.Button(r, height=5, width=10, text="<<", command=rwdClick, bg='purple', fg='white')
rwdButton.grid(row=4,column=1)

infoButton = tk.Button(r, height=5, width=10, text="*", command=infoClick, bg='purple', fg='white')
infoButton.grid(row=3,column=3)

replayButton = tk.Button(r, height=5, width=10, text="REPLAY", command=replayClick, bg='purple', fg='white')
replayButton.grid(row=3,column=1)

ppButton = tk.Button(r, height=5, width=10, text="PLAY", command=ppClick, bg='purple', fg='white')
ppButton.grid(row=4,column=2)

r.mainloop()
