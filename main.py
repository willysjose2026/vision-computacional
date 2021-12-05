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
        
        label2= Label(frame3, text='Informacion', fg='red', font=(18))
        label2.place(x=85, y=6, anchor="center")
        
        frame4 = Frame(self.window,width=100, highlightbackground='blue', highlightthickness=2)
        frame4.grid(row=0,column=1, padx=10, pady=10, ipadx=40, ipady=50,)

        label4= Label(frame4, text=message,fg='red', font=(18))
        label4.place(x=85, y=6, anchor="center")
        
        
        
if __name__ == "__main__":
    cameraStream()


"""
import cv2 as cv
from PIL import Image, ImageTk
import mediapipe as mp

from facerecognition import FaceRecognition

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils


window = Tk()
cap = cv.VideoCapture(0)
window.title('Computer Vision')
window.geometry('900x400')


frame1 = Frame(window, width=100, height=100, highlightbackground='blue',
               highlightthickness=3)
frame1.grid(row=0, column=0, padx=30, pady=40, ipadx=195, ipady=110)

label1 = Label(frame1, text="Camera", fg='red', font=(18))
label1.place(x=250, y=80, anchor="center")


def show_frames():
    success, image = cap.read()
    cv2image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    label1.imgtk = imgtk
    label1.configure(image=imgtk)
    label1.after(20, show_frames)

def detect_face():
    # return FaceRecognition()
    FaceRecognition(cap)
    # window.destroy()


frame2 = Frame(window, width=100, highlightbackground='blue',
               highlightthickness=3)
frame2.grid(row=0, column=1, padx=100, pady=10, ipadx=60, ipady=145)

frame3 = Frame(window, width=100, highlightbackground='blue',
               highlightthickness=2)
frame3.grid(row=0, column=1, padx=10, pady=10, ipadx=40, ipady=100,)
label2 = Label(frame3, text="Result List", fg='red', font=(18))
label2.place(x=85, y=6, anchor="center")


frame4 = Frame(window, width=100, highlightbackground='blue',
               highlightthickness=2)
frame4.grid(row=0, column=1, padx=10, pady=10, ipadx=40, ipady=50,)

btn = Button(frame1, text="Start face recognition", height=2,
                command=detect_face )
btn.place(x=180, y=260)

show_frames()
window.mainloop()


"""