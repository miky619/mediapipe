import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands.Hands(max_num_hands=4)
draw_unit = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)
finger_counter = 0
x = ''

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
        
        if finger_counter == 0:
            x = "mosht"
            y = '0'
        elif finger_counter == 1:
            x = "one"
            y = '1'
        elif finger_counter == 2:
            x = "two"
            y = '2'
        elif finger_counter == 3:
            x = "three"
            y = '3'
        elif finger_counter == 4:
            x = "four"
            y = '4'
        elif finger_counter == 5:
            x = "baz"
            y = '5'
        y += y
    
    cv2.putText(frame, x, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 2)


    if not success:
            break        
    

    cv2.imshow('Webcam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print(int(y))
cap.release()
cv2.destroyAllWindows()
