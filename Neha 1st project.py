from tkinter import*
import time

root=Tk()
root.geometry('500x400')
root.resizable(0,0)
root.config(bg='pink')
root.title('Count down timer')
Label(root,text=' Count down timer',font='arial 20 bold',bg='blue').pack()



##starting timer
sec = StringVar()
Entry(root, textvariable = sec, width = 2, font = 'arial 12').place(x=250, y=155)
sec.set('00')

mins= StringVar()
Entry(root, textvariable = mins, width =2, font = 'arial 12').place(x=225, y=155)
mins.set('00')

hrs= StringVar()
Entry(root, textvariable = hrs, width =2, font = 'arial 12').place(x=200, y=155)
hrs.set('00')


def countdown():
    times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get())
    while times > -1:
        minute,second = (times // 60 , times % 60)

        hour = 0
        if minute > 60:
            hour , minute = (minute // 60 , minute % 60)

        sec.set(second)
        mins.set(minute)
        hrs.set(hour)

        root.update()
        time.sleep(1)

        if(times == 0):
            sec.set('00')
            mins.set('00')
            hrs.set('00')
        times -= 1
Label(root, font ='arial 15 bold', text = 'set the time',   bg ='brown').place(x = 40 ,y = 150)

Button(root, text='START', bd ='5', command = countdown, bg = 'white', font = 'arial 10 bold').place(x=150, y=210)

root.mainloop()

