#importing libraries
import cv2
import mediapipe as mp

#
mp_drawings=mp.solutions.drawing_utils
mp_drawings_styles=mp.solutions.drawing_styles

#tracking hands irl
mphands=mp.solutions.hands

#opening camera
cap=cv2.VideoCapture(0)
hands=mphands.Hands()
while True:
    data,image=cap.read()
        
    #flips the image
    image=cv2.cvtColor(cv2.flip(image,1),cv2.COLOR_BGR2RGB)
    
    #storing the results
    results=hands.process(image)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawings.draw_landmarks (
                image,
                hand_landmarks,mphands.HAND_CONNECTIONS)
    
    cv2.imshow('Handtraker',image)
    cv2.waitKey(1)