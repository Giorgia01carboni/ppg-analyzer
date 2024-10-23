# Heart Rate Extraction from Video Using Python

## Overview

This project is a proof-of-concept implementation of photoplethysmography (PPG) using a smartphone camera. The goal is to estimate a person's heart rate by analyzing the color variations in a video recording of their finger placed over the camera and flashlight. These color variations are caused by the changes in light absorption due to the varying oxygenation levels in the blood during the cardiac cycle.

The primary tool used for this analysis is the **Discrete Fourier Transform (DFT)**, which helps in identifying the dominant frequency in the captured video that corresponds to the heart rate.

## Data Acquisition Protocol

1. Use a smartphone to record a 1-minute video of a finger placed gently over the phone's camera and flashlight. The video should show slight color variations due to blood flow.  
2. The video can also be captured by placing a small portion of skin, like the forehead, in view of the camera.
3. Ensure the video is recorded at a frame rate of **30 FPS** (frames per second).

An example video file (`IMG_6062.MOV`) was provided for testing purposes, but you can record your own videos using the steps above.

## How It Works

1. **Video Input**: The video is loaded and processed frame by frame using OpenCV.
2. **Red Channel Extraction**: The average intensity from the red color channel is computed for each frame.
3. **Signal Analysis**: The resulting intensity values are analyzed using the **Discrete Fourier Transform (DFT)** to extract the dominant frequency, which corresponds to the heart rate.
4. **Heart Rate Calculation**: The dominant frequency (in Hz) is multiplied by 60 to convert it into beats per minute (BPM).

## Implementation Steps

1. **Loading the Video**:
   - The video is loaded into a matrix of size HxWx3xT, where H and W are the height and width of the video in pixels, 3 represents the RGB channels, and T is the number of frames in the video.
   
2. **Processing the Red Channel**:
   - For each frame, the average pixel intensity in the red channel is computed. This yields a vector of average red intensities over time.

3. **Time Vector Setup**:
   - A corresponding time vector is created to represent the time in seconds for each frame, based on the frame rate (30 FPS).

4. **Applying the DFT**:
   - The Discrete Fourier Transform (DFT) is applied to the red intensity signal to identify the dominant frequency.
   
5. **Heart Rate Calculation**:
   - The frequency corresponding to the highest magnitude in the DFT result is identified. This frequency is then converted to BPM.

## Requirements

To run this project, you will need:

- Python 3.x
- OpenCV
- NumPy
- Matplotlib (for plotting)
- (Optional) Git Large File Storage (LFS) for handling large video files on GitHub

You can install the required libraries using:

```bash
pip install opencv-python numpy matplotlib
