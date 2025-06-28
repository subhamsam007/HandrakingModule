import cv2
import mediapipe as mp 
import time 




def count_fingers(e):
    count = 0
    limit = (e.landmark[0].y-e.landmark[9].y)/2
    if (e.landmark[5].y - e.landmark[8].y) < limit:
        count += 1   
    if (e.landmark[9].y - e.landmark[12].y) < limit:
        count += 1       
    if (e.landmark[13].y - e.landmark[16].y) < limit:
        count += 1  
    if (e.landmark[17].y - e.landmark[20].y) < limit:
        count += 1      

        return count 


cap = cv2.VideoCapture(0)


mphands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils
hands = mphands.Hands(max_num_hands =1, min_detection_confidence=0.7, min_tracking_confidence=0.5)
hand_connections_style = mpDraw.DrawingSpec(color=(255, 0, 150), thickness=2)  # Blue connections

while True :
    Success , frame = cap.read()
    frame =cv2.flip(frame,1) #flip the frame horizontally
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:

        hand_keyPoints = results.multi_hand_landmarks[0]

        count = count_fingers(hand_keyPoints)
        print(count )

        mpDraw.draw_landmarks(frame,hand_keyPoints , mphands.HAND_CONNECTIONS , hand_connections_style)

    cv2.imshow("video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()