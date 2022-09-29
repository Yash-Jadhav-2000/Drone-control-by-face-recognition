#!/usr/bin/python3
import os
import cv2
import sys
import time

"""
Example usage:
    ./auto-snap-image.py <ready_time> <image_index_start> <output_folder_path> \
        <interval_snap_time> <convert_image_to_grayscale>

    what it does?
        - ready_time                : initial ready time before snap image process started
        - image_index_start         : initial snapped image number
        - output_folder_path        : where to save the snapped images
        - interval_snap_time        : time interval between snap
        - convert_image_to_grayscale: flag to convert snapped images to grayscale
"""

# Capture input from CLI.
ready_time                  = int(sys.argv[1])
image_index_start           = int(sys.argv[2])
output_folder_path          = sys.argv[3]
interval_snap_time          = float(sys.argv[4])
convert_image_to_grayscale  = int(sys.argv[5])

# Wait time to be ready.
time.sleep(ready_time)

# OpenCV video capture.
stream = cv2.VideoCapture('IMG_3821.MP4') # take input from webcam/video
last_capture_time = time.time() # keep track last snap

while True:
    # Get frame.
    grabbed, frame = stream.read()

    # Transform to grayscale.
    if convert_image_to_grayscale:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Save image.
    if grabbed:
        if (time.time() - last_capture_time) > interval_snap_time:
            # Generate filename and output path.
            fname = '%s.jpg' % str(image_index_start)
            output_path = os.path.join(output_folder_path, fname)
            # Save the image.
            cv2.imwrite(output_path, frame)
            last_capture_time = time.time()
            # Increase filename index.
            image_index_start += 1

        # Display image.
        cv2.imshow('Auto Snap!', frame)
        cv2.waitKey(1)

# Destroying all windows.
cv2.destroyAllWindows()