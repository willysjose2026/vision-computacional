import cv2
import time
import os
import handDetector as hd


class GestureDetector():
    def __init__(self):
        self.wCam, self.hCam = 640, 480
        self.cap = cv2.VideoCapture(0)
        self.pTime = 0
        self.detector = hd.handDetector(detectionCon=0.75)
        self.tipIds = [4, 8, 12, 16, 20]
        self.message = ''


    def gestureDetection(self):
        
        while True:
            success, self.img = self.cap.read()
            self.img = cv2.flip(self.img,1)
            self.img = self.detector.findHands(self.img)
            lmList = self.detector.findPosition(self.img, draw=False)
            # print(lmList)

            if len(lmList) != 0:
                self.fingers = []

                # Thumb
                if lmList[self.tipIds[0]][1] > lmList[self.tipIds[0] - 1][1]:
                    self.fingers.append(1)
                else:
                    self.fingers.append(0)

                # 4 Fingers
                for id in range(1, 5):
                    if lmList[self.tipIds[id]][2] < lmList[self.tipIds[id] - 2][2]:
                        self.fingers.append(1)
                    else:
                        self.fingers.append(0)

                
                totalFingers = self.fingers.count(1)
                #print(totalFingers)

                if self.fingers == [0,1,0,0,1] or self.fingers == [1,1,0,0,0] or self.fingers == [0,1,1,0,0] or self.fingers == [1,1,0,0,1] or self.fingers == [0,0,0,0,1]:
                    self.message = 'HELP!!!'
                else:
                    self.message == "IT'S OK!!" 
        
                #h, w, c = overlayList[totalFingers - 1].shape
                #img[0:h, 0:w] = overlayList[totalFingers - 1]

                #cv2.rectangle(self.img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
                #cv2.putText(self.img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN,
                #            10, (255, 0, 0), 25)

            cTime = time.time()
            fps = 1 / (cTime - self.pTime)
            pTime = cTime

            
            #cv2.imshow('Image', self.img)
            cv2.waitKey(1)
            return self.message, self.img

    def gestureMessage(self):
        pass
        
        
        