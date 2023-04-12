from tkinter import *
import datetime 
from threading import *
import time
import pygame 
import tkinter.messagebox as tkm

root = Tk()
root.geometry("600x250")
root.title("暴躁狂的番茄钟")

def Threading():
    global result
    result = "no" 
    t1 = Thread(target=alarm_clock_function)
    t1.start()


a = StringVar()
b = IntVar()
h = IntVar()
m = IntVar()
s = IntVar()


#get the time of system and show out
def showtime():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    a.set(now)
    root.after(500,showtime)
def show_Remaining_time():
    global remaining_time
    if remaining_time>datetime.timedelta(seconds=0):
        remaining_time -=datetime.timedelta(seconds=1)
        b.set(remaining_time)
        time.sleep(0.1)
            


Label(root,text="北京时间",font=("Helvetica 20 bold",20)).pack()
Label(root,textvariable=a,font=("Helvetica 20 bold",20)).pack()


showtime()

result ="no"
event = Event()

def message():
    global result
    result = tkm.askquestion(title="提醒",message="一个番茄钟结束了，是否暂停闹铃？")
    event.set()

def sound():
    pygame.mixer.init()
    pygame.mixer.music.load("/home/funkyflyinggoat/python-beginner-projects/projects/Alarm_Clock_Eusoff/col.mp3")
    pygame.mixer.music.play(-1)
    while True:
        if result == "yes":
            pygame.mixer.music.stop()
            break
        time.sleep(0.1)
    event.clear()

#make the function of alarm clock:get the time what u want to  be reminded of
#compare it with time now
def alarm_clock_function():
    global remaining_time
    target_time = datetime.datetime.now()+datetime.timedelta(hours=h.get(),minutes=m.get(),seconds=s.get())
    remaining_time=datetime.timedelta(hours=h.get(),minutes=m.get(),seconds=s.get()+1)

    while True:
  
        now = datetime.datetime.now().strftime("%H:%M:%S")
        target = target_time.strftime("%H:%M:%S")
        print(target,now)
        show_Remaining_time()
        time.sleep(0.9)
        if target == now:
            Thread(target=message).start()
            Thread(target=sound,daemon=True).start()
            event.wait()
            break
frame = Frame(root)
frame.pack()
Label(frame, text="剩余时间:", font=("Helvetica 20 bold", 20)).pack(side=LEFT)
Label(frame, textvariable=b, font=("Helvetica 20 bold", 20)).pack(side=LEFT)
#GUI stuff
Label(root,text="闹钟:",font=("Helvetica 20 bold",20)).pack(side=LEFT)
hour = Entry(root,bd=5,textvariable=h,justify=RIGHT,width=5)
hour.pack(side=LEFT)
Label(root,text="小时",font=("Helvetica 20 bold",20)).pack(side=LEFT)
minute = Entry(root,bd=5,textvariable=m,justify=RIGHT,width=5)
minute.pack(side=LEFT)
Label(root,text="分钟",font=("Helvetica 20 bold",20)).pack(side=LEFT)
second = Entry(root,bd=5,textvariable=s,justify=RIGHT,width=5)
second.pack(side=LEFT)
Label(root,text="秒后提醒",font=("Helvetica 20 bold",20)).pack(side=LEFT)
Button(root,text="设定闹钟",font=("Helvetica 20 bold",20),command=Threading).pack(side=LEFT)


root.mainloop()
