from tkinter import *


window= Tk()
window.title('Computer Vision')
window.geometry('900x400')



frame1 = Frame(window, width=100,highlightbackground='blue',highlightthickness= 3)
frame1.grid(row=0, column=0, padx=30,pady= 40, ipadx= 195,ipady=140)

label1= Label(frame1, text="Camera",fg='red', font=(18))
label1.place(x=215, y=3, anchor="center")


frame2 = Frame(window,width=100, highlightbackground='blue', highlightthickness=3)
frame2.grid(row=0,column=1, padx=100, pady=10, ipadx=60, ipady=145)

frame3 = Frame(window,width=100, highlightbackground='blue', highlightthickness=2)
frame3.grid(row=0,column=1, padx=10, pady=10, ipadx=40, ipady=100,)
label2= Label(frame3, text="Result List",fg='red', font=(18))
label2.place(x=85, y=6, anchor="center")


frame4 = Frame(window,width=100, highlightbackground='blue', highlightthickness=2)
frame4.grid(row=0,column=1, padx=10, pady=10, ipadx=40, ipady=50,)




window.mainloop()