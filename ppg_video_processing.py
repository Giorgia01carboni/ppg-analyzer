import cv2
import numpy as np

# heart rate from smartphone
hr_video = cv2.VideoCapture("IMG_6062.MOV")

if (hr_video.isOpened() == False):
  print("Error opening video file")

# store average red intensities for each frame
red_intensities = []

while (hr_video.isOpened()):
  ret, frame = hr_video.read()
  if ret == True:
    (b_channel, g_channel, r_channel) = cv2.split(frame)
    red_intensities.append(np.mean(r_channel))
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  else:
    break

hr_video.release()
