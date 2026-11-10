import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands.Hands(max_num_hands=4)
draw_unit = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)
#finger_counter = 0


while True:

    success , frame = cap.read()
    finger_counter = 0
    finger_tips = [8, 12, 16, 20]
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = mp_hands.process(frameRGB)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            landmark = hand.landmark
           #draw_unit.draw_landmarks(frame, hand, mp.solutions.hands.HAND_CONNECTIONS)
        for tip in finger_tips:
            if landmark[tip].y < landmark[tip - 2].y:
                finger_counter += 1
        if landmark[4].x > landmark[3].x:
            finger_counter += 1

    cv2.putText(frame, str(finger_counter), (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 2)


    if not success:
            break        
    

    cv2.imshow('Webcam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()