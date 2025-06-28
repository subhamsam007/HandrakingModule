import cv2
import mediapipe as mp
import time

# print("OpenCV version:", cv2.__version__)
# print("MediaPipe version:", mp.__version__)


cap = cv2.VideoCapture(0)

mphands = mp.solutions.hands
hands = mphands.Hands()
mpDraw = mp.solutions.drawing_utils


cTime = 0
pTime = 0

#Custom drawing styles
hand_landmarks_style = mpDraw.DrawingSpec(color=(0, 255, 0), thickness=3, circle_radius=5)  # Green points
hand_connections_style = mpDraw.DrawingSpec(color=(255, 0, 150), thickness=2)  # Blue connections

while True:
    ret, frame = cap.read()
    if not ret:
        break
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks) # Print the landmarks for each detected hand that hand is detected


    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame, handLms, mphands.HAND_CONNECTIONS, hand_landmarks_style, hand_connections_style)
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                # if id == 4:
                cv2.circle(frame, (cx, cy), 5, (255,100, 255), cv2.FILLED)
#for fps calculation 
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(frame, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()