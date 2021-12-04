from tkinter import *
import tkinter
import WebCam_Threading
import GestureDetector
import cv2
from PIL import Image
from PIL import ImageTk



class cameraStream():    
    def __init__(self):
        self.gestureDectector = GestureDetector.GestureDetector()
        
        self.window = tkinter.Tk()
        self.window.title('Computer Vision')
        self.window.geometry('900x400')

        self.panel = tkinter.Label()
        self.panel.grid(column=0, row=0)
        
        self.camera = cv2.VideoCapture(0)
        self.Camera()
        self.window.mainloop()
        self.window.after(500,self.Camera)
        
    def Camera(self):
        
        message, frame = self.gestureDectector.gestureDetection()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = Image.fromarray(frame)
        frame = ImageTk.PhotoImage(frame)

        self.panel.configure(image=frame)
        self.panel.image = frame
        self.panel.after(1,self.Camera)

        frame2 = Frame(self.window,width=100, highlightbackground='blue', highlightthickness=3)
        frame2.grid(row=0,column=1, padx=100, pady=10, ipadx=60, ipady=145)

        frame3 = Frame(self.window,width=100, highlightbackground='blue', highlightthickness=2)
        frame3.grid(row=0,column=1, padx=10, pady=10, ipadx=40, ipady=100,)
        
        label2= Label(frame3, text=message,fg='red', font=(18))
        label2.place(x=85, y=6, anchor="center")
        
        frame4 = Frame(self.window,width=100, highlightbackground='blue', highlightthickness=2)
        frame4.grid(row=0,column=1, padx=10, pady=10, ipadx=40, ipady=50,)

        
        
if __name__ == "__main__":
    cameraStream()