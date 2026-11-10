import cv2
import mediapipe as mp
from pycaw.pycaw import AudioUtilities

mp_hand = mp.solutions.hands.Hands(max_num_hands=1)
draw_util = mp.solutions.drawing_utils

speakers = AudioUtilities.GetSpeakers()
volume = speakers.EndpointVolume

cap = cv2.VideoCapture(0)
finger_counter = 0
status_text = ''
finger_tips = [8, 12, 16, 20]

while True:

    finger_counter = 0
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = mp_hand.process(frameRGB)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:

            landmark = hand.landmark
            #draw_util.draw_landmarks(frame, hand, mp.solutions.hands.HAND_CONNECTIONS)

            # four fingers: tip higher than the joint means open
            for tip in finger_tips:
                if landmark[tip].y < landmark[tip - 2].y:
                    finger_counter += 1

            # thumb: tip farther from the pinky base than its joint means open
            thumb_tip = abs(landmark[4].x - landmark[17].x)
            thumb_joint = abs(landmark[3].x - landmark[17].x)
            if thumb_tip > thumb_joint * 1.1:
                finger_counter += 1

            if finger_counter == 0:
                volume.SetMute(1, None)
                status_text = 'MUTE'
            else:
                volume.SetMute(0, None)

                if finger_counter == 1:
                    volume.SetMasterVolumeLevelScalar(0.20, None)
                    status_text = '20%'
                elif finger_counter == 2:
                    volume.SetMasterVolumeLevelScalar(0.40, None)
                    status_text = '40%'
                elif finger_counter == 3:
                    volume.SetMasterVolumeLevelScalar(0.60, None)
                    status_text = '60%'
                elif finger_counter == 4:
                    volume.SetMasterVoluضmeLevelScalar(0.80, None)
                    status_text = '80%'
                elif finger_counter == 5:
                    volume.SetMasterVolumeLevelScalar(1.0, None)
                    status_text = '100%'

    cv2.putText(frame, f'Fingers: {finger_counter}', (50, 60),
                cv2.FONT_HERSHEY_COMPLEX, 1.5, (0, 255, 255), 3)
    cv2.putText(frame, status_text, (50, 130),
                cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 3)

    cv2.imshow('WebCam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()