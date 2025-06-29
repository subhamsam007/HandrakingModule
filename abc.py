import cv2
import mediapipe as mp 
import time 
import pyautogui as pay



def count_fingers(e):
    count = 0
    # Thumb
    if e.landmark[4].x < e.landmark[3].x:
        count += 1
    # Fingers: Index, Middle, Ring, Pinky
    finger_tips = [8, 12, 16, 20]
    finger_dips = [6, 10, 14, 18]
    for tip, dip in zip(finger_tips, finger_dips):
        if e.landmark[tip].y < e.landmark[dip].y:  #If the tip y is higher than the joint y, it means the finger is open (raised).
            count += 1

    return count


cap = cv2.VideoCapture(0)


mphands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils
hands = mphands.Hands(max_num_hands = 1, min_detection_confidence=0.7, min_tracking_confidence=0.5)
hand_connections_style = mpDraw.DrawingSpec(color=(0, 255, 0), thickness=5)  # Green connections
previous = -1
is_muted = False
while True:
    Success, frame = cap.read()
    frame = cv2.flip(frame, 1)  # flip the frame horizontally
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:

        hand_keyPoints = results.multi_hand_landmarks[0]

        count = count_fingers(hand_keyPoints)
        print(count)
        if previous != count:
            if count == 5:
                pay.press("space")
            elif count == 2:
                pay.press("right")
            elif count == 3:
                pay.press("left")
            elif count == 1 :
                pay.press("up")
            elif count == 4:
                pay.press("down")
                if count == 0:
                    if not is_muted:
                        pay.press('m')  # Toggle mute
                        is_muted = True  # Mark as muted
            else:
                is_muted = False
            previous = count
        for hand_keyPoints in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame, hand_keyPoints, mphands.HAND_CONNECTIONS, hand_connections_style)

    cv2.imshow("video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()