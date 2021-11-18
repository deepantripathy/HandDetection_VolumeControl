import cv2
import mediapipe as mp
import numpy as np 
from math import hypot
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

cap = cv2.VideoCapture(0)
mpHand = mp.solutions.hands
hand = mpHand.Hands()
mpDraw = mp.solutions.drawing_utils

device = AudioUtilities.GetSpeakers()
interface = device.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

vol = cast(interface, POINTER(IAudioEndpointVolume))
volMin, volMax = vol.GetVolumeRange()[:2]

while True:
    success, image = cap.read()
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result = hand.process(imageRGB)

    imglist = []

    if result.multi_hand_landmarks:
        for handmark in result.multi_hand_landmarks:
            for id, lm in enumerate(handmark.landmark):
                h, w, _ = image.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                imglist.append([id, cx, cy])
            mpDraw.draw_landmarks(image, handmark, mpHand.HAND_CONNECTIONS)
    
    if imglist:
        x1, y1 = imglist[4][1], imglist[4][2]
        x2, y2 = imglist[8][1], imglist[8][2]
        cv2.circle(image, (x1,y1), 4, (255,0,0), cv2.FILLED)
        cv2.circle(image, (x2,y2), 4, (255,0,0), cv2.FILLED)
        cv2.line(image, (x1,y1), (x2,y2), (255,0,0), 3)
        
        length = hypot(x2-x1, y2-y1)

        volBar = np.interp(length, [15,220], [volMin, volMax])
        print(volBar, length)
        vol.SetMasterVolumeLevel(volBar, None)

    cv2.imshow('Image', image)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
