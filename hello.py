import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cv2.namedWindow('frame', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    ret, frame = cap.read()
    height, width = frame.shape[:2]  # Get height and width directly from the frame

    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    flipped_horizental = cv2.flip(smaller_frame, 1)
    flipped_vertical = cv2.flip(smaller_frame, 0)

    image[0:height//2, 0:width//2] = flipped_vertical  # Top-left
    image[height//2:, 0:width//2] = smaller_frame   # Bottom-left
    image[0:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)  # Top-right
    image[height//2:, width//2:] = flipped_horizental  # Bottom-right

    cv2.imshow('frame', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



# Using OpenCV and NumPy to capture and process live video from your webcam.

# Reading frames using cap.read() and checking if the capture was successful.

# Setting camera resolution using cap.set() and properly retrieving height and width from the frame itself.

# Creating blank images with np.zeros_like() to use as a canvas.

# Resizing frames with cv2.resize() using scale factors fx and fy.

# Displaying video in different screen quadrants using array slicing (image[y1:y2, x1:x2]).

# Rotating and flipping images:

# cv2.rotate(..., cv2.ROTATE_180) for rotation.

# cv2.flip(..., 1) for horizontal flip.

# Using full-screen display mode with cv2.namedWindow() and cv2.setWindowProperty().

# Interactive control with cv2.waitKey() to exit the loop by pressing 'q'.

# Proper cleanup with cap.release() and cv2.destroyAllWindows().




 
