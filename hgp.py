import cv2 as cv
import mediapipe as mp
import pyautogui


captureHand = mp.solutions.hands.Hands()
draw = mp.solutions.drawing_utils
scrwidth, scrheight = pyautogui.size()
cam = cv.VideoCapture(0)

def rescaleFrame(frame , scale = 1.5):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimentions = (width, height)

    return cv.resize(frame , dimentions, interpolation= cv.INTER_AREA)


while True:
    _,img = cam.read()

    resized_img = rescaleFrame(img)


    imgheight, imgwidth, _ = resized_img.shape
    resized_img = cv.flip(resized_img,1)
    rgbimg = cv.cvtColor(resized_img,cv.COLOR_BGR2RGB)
    capOutputhand= captureHand.process(rgbimg)
    bothHands = capOutputhand.multi_hand_landmarks
    handness = capOutputhand.multi_handedness

    if bothHands and  handness:
        for hand, handedness in zip(bothHands, handness):
            label = handedness.classification[0].label
            draw.draw_landmarks(resized_img , hand)
            handLandmark = hand.landmark
            
            for fp , lm in enumerate(handLandmark):
                x = int(lm.x * imgwidth)
                y = int(lm.y * imgheight)
                print(x,y)
                if fp == 8:
                    mousex = int(scrwidth/ imgwidth * x)
                    mousey = int(scrheight/ imgheight * y)
                    
                    if label == 'Right': 
                        cv.circle(resized_img,(x,y),10,(0,255,0),thickness = -1) 
                        pyautogui.moveTo(mousex, mousey)
                    elif label == 'Left':  
                        cv.circle(resized_img,(x,y),10,(255,255,255),thickness = -1)
                        pyautogui.click()

    cv.imshow('Movement',resized_img)

    if cv.waitKey(100) & 0xFF == ord('x'): 
        break
cam.release()
cv.destroyAllWindows()