from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk()
GUI.title('ตารางสอบ')       #ชื่อโปรแกรม
GUI.geometry('600x500')     #ขนาดโปรแกรม


L1 = Label(GUI,text='ตารางสอบ',font=('Sukhumvit Set',26),fg='green') #ตัวหนังสือ
L1.place(x=200,y=20)

#ตัวเลือกที่ 1
L2 = Label(GUI,text='วันอังคารที่ 7 มีนาคม พ.ศ. 2566',font=('Sukhumvit Set',12),fg='green') #ตัวหนังสือ
L2.place(x=70,y=120)

def Button1():
    text = 'FLUID POWER CONTROL เวลา 09:30-12:30 ตึกเครื่องกล ME-402:B4'
    messagebox.showinfo('วันอังคารที่ 7 มีนาคม พ.ศ. 2566',text)
    
FB1 = Frame(GUI)        #คล้ายกระดาน
FB1.place(x=350,y=100)   #ตำแหน่ง
B1 = ttk.Button(FB1,text='คลิก!',command=Button1)
B1.pack(ipadx=30,ipady=20)

#ตัวเลือกที่ 2
L3 = Label(GUI,text='วันพฤหัสบดีที่ 9 มีนาคม พ.ศ. 2566',font=('Sukhumvit Set',12),fg='green') #ตัวหนังสือ
L3.place(x=70,y=200)

def Button2():
    text = 'INDUSTRIAL ROBOTICS เวลา 13:30-16:30 ตึกโหล:E12-903:A4'
    messagebox.showinfo('วันพฤหัสบดีที่ 9 มีนาคม พ.ศ. 2566',text)
    
FB2 = Frame(GUI)        #คล้ายกระดาน
FB2.place(x=350,y=180)   #ตำแหน่ง
B2 = ttk.Button(FB2,text='คลิก!',command=Button2)
B2.pack(ipadx=30,ipady=20)

#ตัวเลือกที่ 3
L4 = Label(GUI,text='วันศุกร์ที่ 10 มีนาคม พ.ศ. 2566',font=('Sukhumvit Set',12),fg='green') #ตัวหนังสือ
L4.place(x=70,y=280)

def Button3():
    text = 'ELECTRICAL SAFETY เวลา 13:30-16:30 ตึกเครื่องกล ME-402:B4'
    messagebox.showinfo('วันศุกร์ที่ 10 มีนาคม พ.ศ. 2566',text)
    
FB3 = Frame(GUI)        #คล้ายกระดาน
FB3.place(x=350,y=260)   #ตำแหน่ง
B3 = ttk.Button(FB3,text='คลิก!',command=Button3)
B3.pack(ipadx=30,ipady=20)

GUI.mainloop()
