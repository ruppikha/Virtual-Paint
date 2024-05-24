import cv2
import numpy as np

frameWidth = 640
frameHeight = 480

# Try different camera indices if 1 doesn't work
cap = cv2.VideoCapture(1)
if not cap.isOpened():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise Exception("Could not open video device")

cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

myColors = [
    [90, 48, 0, 118, 255, 255]    # Blue
]

myColorValues = [
    [255, 0, 0]       # BGR for Blue
]

myPoints = []  # [x, y, colorId]

def findColor(img, myColors, myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    newPoints = []
    for count, color in enumerate(myColors):
        lower = np.array(color[:3])
        upper = np.array(color[3:])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        if x != 0 and y != 0:
            cv2.circle(imgResult, (x, y), 15, myColorValues[count % len(myColorValues)], cv2.FILLED)
            newPoints.append([x, y, count % len(myColorValues)])
        # Display the mask for debugging
        cv2.imshow(f"Mask {count}", mask)

    if colorDetected[0]:
        cv2.putText(imgResult, "Blue detected", (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
    return newPoints

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x + w // 2, y

def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture image")
        continue
    imgResult = img.copy()
    newPoints = findColor(img, myColors, myColorValues)
    if newPoints:
        myPoints.extend(newPoints)
    if myPoints:
        drawOnCanvas(myPoints, myColorValues)

    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
