import cv2 as cv
import mediapipe as mp
import time

def FaceRecognition(cap):
    mp_face_detection = mp.solutions.face_detection
    mp_drawing = mp.solutions.drawing_utils

    ptime = 0
    with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
        
        success, image = cap.read()
            
        if not success:
            print("Failed to capture image")
            
            
        image.flags.writeable = False
        image = cv.flip(image,1)
        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        results = face_detection.process(image)

        image.flags.writeable = True
        image = cv.cvtColor(image, cv.COLOR_RGB2BGR)

        if results.detections:
            for detection in results.detections:
                #mp_drawing.draw_detection(image, detection)
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, ic = image.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
                final_img = cv.rectangle(image, bbox, (0, 200, 0), 2)
                cv.putText(final_img, 'Willys',  (int(bboxC.xmin * iw), int(bboxC.ymin * ih)), cv.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
                
                
                #cv.imshow("Face Detection", image)

            #cv.waitKey(1)
        
        return image
            #if cv.waitKey(1) & 0xFF == ord('q'):
                #cv.destroyAllWindows()
                #break                
    
    #cap.release()

