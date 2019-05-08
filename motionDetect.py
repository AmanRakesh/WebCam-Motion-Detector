import cv2 as cv
import time
import pandas as pd
from datetime import datetime

statusList=[None,None]
times = []
first_frame = None
df = pd.DataFrame(columns=["Start","End"])
video = cv.VideoCapture(0)

while True:
    status = 0
    check, frame = video.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray = cv.GaussianBlur(gray, (21,21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    deltaFrame = cv.absdiff(first_frame, gray)
    threshFrame = cv.threshold(deltaFrame, 30, 255, cv.THRESH_BINARY)[1]
    thresh_frame = cv.dilate(threshFrame, None, iterations=2)

    (cntrs, _) = cv.findContours(thresh_frame.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for con in cntrs:
        if cv.contourArea(con)<10000:
            continue

        status = 1
        (x, y, w, h) = cv.boundingRect(con)
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    statusList.append(status)
    statusList = statusList[-2:]
    if statusList[-1]==1 and statusList[-2]==0:
        times.append(datetime.now())
    if statusList[-1]==0 and statusList[-2]==1:
        times.append(datetime.now())

    cv.imshow("Gray Frame", gray)
    cv.imshow("Delta Frame", deltaFrame)
    cv.imshow("Threshold", threshFrame)
    cv.imshow("Color Frame", frame)
    key = cv.waitKey(1)

    if key == ord('q'):
        if status==1:
            times.append(datetime.now())
        break

   # print(status)

#print(statusList)
print(times)

for i in range(0,len(times),2):
    df = df.append({"Start":times[i], "End":times[i+1]}, ignore_index=True)

df.to_csv("Times.csv")
video.release()
cv.destroyAllWindows()

