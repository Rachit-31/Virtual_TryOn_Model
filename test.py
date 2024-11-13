import os

import cvzone
import cv2
from cvzone.PoseModule import PoseDetector

cap = cv2.VideoCapture(0)
detector = PoseDetector()

shirtFolderPath = "Resources/Shirts"
listShirts = os.listdir(shirtFolderPath)
print(listShirts)

fixedRatio = 262/190
shirtHeightRatio = 581 / 440

while True:
    success, img = cap.read()
    img = detector.findPose(img)
    img = cv2.flip(img, 1)
    lmlist, bboxInfo = detector.findPosition(img, bboxWithHands=False, draw=False)
    if lmlist:
        # center = bboxInfo["center"]
        # cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)
        lm11 = lmlist[24][1:3]
        lm12 = lmlist[12][1:3]
        imgShirt = cv2.imread(os.path.join(shirtFolderPath, listShirts[0]), cv2.IMREAD_UNCHANGED)

        widthOfShirt = int((lm12[0]-lm11[0]) * fixedRatio)
        print(widthOfShirt)
        imgShirt = cv2.resize(imgShirt, (0, 0), None, 0.5, 0.5)
        # imgShirt = cv2.resize(imgShirt, (int(widthOfShirt), int(widthOfShirt * shirtHeightRatio)))
        try:
            img = cvzone.overlayPNG(img, imgShirt, lm11)
        except:
            pass


    cv2.imshow("Image", img)
    cv2.waitKey(1)