import tkinter,os
import tkinter.messagebox
screen = tkinter.Tk()
screen.title("Turning off my pc")
screen.geometry("400x300")
Label1=tkinter.Label(text="Your pc to be turned off after how many minutes",)
Label1.place(x=0,y=50)
user = tkinter.StringVar()
time = tkinter.Entry(screen,textvariable=user)
time.place(x=180,y=50)
def shut():
    global time
    time = eval(time.get())
    os.system("shutdown -s -t {}".format(int(time)*60))
button = tkinter.Button(screen,text = "Turn off",command = shut)
button.place(x=200,y=120)
def cancel():
    tkinter.messagebox.showinfo("Reminding", "Cancel the turning off")
    os.system("shutdown -a")
button2 = tkinter.Button(screen,text="Cancel",command=cancel)
button2.place(x=280,y=120)
screen.mainloop()

