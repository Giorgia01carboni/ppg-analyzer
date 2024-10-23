import cv2
import numpy as np
import matplotlib.pyplot as plt

# Open the video file
hr_video = cv2.VideoCapture("IMG_6062.MOV")

if not hr_video.isOpened():
    print("Error opening video file")

# Store average red intensities for each frame
red_intensities = []
total_frames = int(hr_video.get(cv2.CAP_PROP_FRAME_COUNT))
print(f"Total frames in video: {total_frames}")

# Time vector
time_vector = []
# Loop from 0 to T-1. 30 is number of frames per second
for i in range(total_frames):
    time_vector.append(i/30)

# Read frames until the end of the video
while True:
    ret, frame = hr_video.read()
    if not ret:  # Break if no frame is returned
        break
    # Split the frame into color channels and compute the mean intensity of the red channel
    (b_channel, g_channel, r_channel) = cv2.split(frame)
    red_intensities.append(np.mean(r_channel))

# Release the video capture object
hr_video.release()

# Print the total number of red intensities recorded
print(f"Total red intensities recorded: {len(red_intensities)}")

plt.plot(time_vector, red_intensities)
plt.show()

heart_rate_dft = np.fft.fft(red_intensities)
f_axis = np.fft.fftfreq(total_frames, d=1/30)
magnitude_axis = np.abs(heart_rate_dft)
omega_axis = np.angle(heart_rate_dft)

plt.plot(f_axis, magnitude_axis)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Magnitude Spectrum of Red Intensity Signal')
plt.show()

plt.plot(omega_axis, magnitude_axis)
plt.xlabel('Angular Frequency (rad/s)')
plt.ylabel('Magnitude')
plt.title('Phase Spectrum of Red Intensity Signal')
plt.show()


