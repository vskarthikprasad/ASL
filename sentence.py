import numpy as np
#import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import operator
import cv2,keyboard
import sys, os
from gtts import gTTS
from playsound import playsound

classifier = load_model("asl_model1.h5")





def predictor(test_image):
    result = classifier.predict(test_image.reshape(1, 200, 200, 3))
    if result[0][0] == 1:
        return 'A'
    elif result[0][1] == 1:
        return 'B'
    elif result[0][2] == 1:
        return 'C'
    elif result[0][3] == 1:
        return 'D'
    elif result[0][4] == 1:
        return 'E'
    elif result[0][5] == 1:
        return 'F'
    elif result[0][6] == 1:
        return 'G'
    elif result[0][7] == 1:
        return 'H'
    elif result[0][8] == 1:
        return 'I'
    elif result[0][9] == 1:
        return 'J'
    elif result[0][10] == 1:
        return 'K'
    elif result[0][11] == 1:
        return 'L'
    elif result[0][12] == 1:
        return 'M'
    elif result[0][13] == 1:
        return 'N'
    elif result[0][14] == 1:
        return 'O'
    elif result[0][15] == 1:
        return 'P'
    elif result[0][16] == 1:
        return 'Q'
    elif result[0][17] == 1:
        return 'R'
    elif result[0][18] == 1:
        return 'S'
    elif result[0][19] == 1:
        return 'T'
    elif result[0][20] == 1:
        return 'U'
    elif result[0][21] == 1:
        return 'V'
    elif result[0][22] == 1:
        return 'W'
    elif result[0][23] == 1:
        return 'X'
    elif result[0][24] == 1:
        return 'Y'
    elif result[0][25] == 1:
        return 'Z'
    elif result[0][26] == 1:
        return 'del'
    elif result[0][27] == 1:
        return 'nothing'
    elif result[0][28] == 1:
        return 'space'

cam = cv2.VideoCapture(0)
res = ''
sequence = ''
mem = ''
consecutive = 0
i=0
voice=''

while True:
    ret, frame = cam.read()
    x1 = 10
    y1 = 10
    x2 = int(0.5*frame.shape[1])
    y2 = int(0.5*frame.shape[1])
    cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,thickness=2, lineType=8, shift=0)
    roi = frame[y1:y2, x1:x2]
    roi = cv2.resize(roi, (200, 200))
    test_image = roi

    if i == 12:
        res_temp = predictor(test_image)
        res=res_temp
        i=0
        if mem == res:
            consecutive+=1
        else:
            consecutive = 0
        if consecutive == 2 and res!='nothing':
            if res == 'space':
                sequence+= ' '
            elif res == 'del':
                sequence = sequence[:-1]
            else:
                sequence+=res
            consecutive =0
    i+=1

    cv2.putText(frame, res, (30, 400), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (255,255,255))
    mem = res
    img_sequence = np.zeros((200,1200,3), np.uint8)
    cv2.putText(img_sequence, '%s' % (sequence.upper()), (30,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
    cv2.imshow("Original Frame",frame)
    cv2.imshow('sequence', img_sequence)
    cv2.imshow("ROI",roi)
    interrupt = cv2.waitKey(10)
    if keyboard.is_pressed("s"):
        voice+=sequence
        print("Recognised text: "+sequence)
        break
    if interrupt & 0xFF == 27: # esc key
        break







language = 'en'


myobj = gTTS(text=voice, lang=language, slow=False)

myobj.save("welcome.mp3")

playsound(os.path.join(os.getcwd() , 'welcome.mp3'))


cam.release()
cv2.destroyAllWindows()
