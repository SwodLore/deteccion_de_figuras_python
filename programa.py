import mediapipe as mp
import cv2
import math
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
cap = cv2.VideoCapture(1)

with mp_hands.Hands(
    static_image_mode= False,
    max_num_hands=2,
    min_detection_confidence=0.5) as hands:
    
    while True:
        ret, frame = cap.read()
        if ret ==False:
            break
        
        height, width, _ = frame.shape
        frame = cv2.flip(frame,1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        results = hands.process(frame_rgb)
        
        if results.multi_hand_landmarks is not None:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
                )
                
                x1 = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].x*width)
                y1 = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y*height)
                
                x2 = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x*width)
                y2 = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y*height)
                
                x3 = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x*width)
                y3 = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y*height)
                
                d1 = math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
                d2 = math.sqrt(math.pow(x1-x3,2)+math.pow(y1-y3,2))
                d3 = math.sqrt(math.pow(x2-x3,2)+math.pow(y2-y3,2))
                
                cos_angulo=(math.pow(d1,2)+math.pow(d2,2)-math.pow(d3,2))/(2*d1*d2)
                angulo_radianes=math.acos(cos_angulo)
                angulo_grados=math.degrees(angulo_radianes)
                #print(angulo_grados)
                
                if angulo_grados < 53:
                    xc= (x2+x3)//2
                    yc= (y2+y3)//2
                    rc= int(d3/2)
                    cv2.circle(frame, (xc, yc), rc, (0, 255, 0), 2)
                    cv2.putText(frame,'Circulo',(300,80),5,1,(0,255,0),2,cv2.LINE_AA)
                    #print("Circulo")
                    
                elif 53 < angulo_grados < 68:
                    puntos = [(x1,y1),(x3,y3),(x1,y1)]
                    cv2.polylines(frame,[np.array(puntos)],isClosed=True,color=(0, 255, 0),thickness=2)
                    cv2.putText(frame,'Triangulo',(300,80),5,1,(0,255,0),2,cv2.LINE_AA)
                    #print("Triangulo")
                    
                elif angulo_grados > 68:
                    cv2.rectangle(frame,(x2,y2),(x3,y3),(0, 255, 0),2)
                    cv2.putText(frame,'Rectangulo',(300,80),5,1,(0,255,0),2,cv2.LINE_AA)
                    #print("Rectangulo")
                    
                
                   
        cv2.imshow("Frame",frame)
        
        if cv2.waitKey(1) & 0xFF ==27:
            break

cv2.release()
cv2.destroyAllWindows()    
