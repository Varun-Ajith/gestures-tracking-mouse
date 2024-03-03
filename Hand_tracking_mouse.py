import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)

hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

screen_width, screen_height = pyautogui.size()

thumb_x, thumb_y = 0, 0
index_x, index_y = 0, 0

while True:
    _, frame = cap.read()

    frame = cv2.flip(frame, 1)

    frame_height, frame_width, _ = frame.shape

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)

            landmarks = hand.landmark

            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)

                if id == 8:
                    index_x = screen_width / frame_width * x
                    index_y = screen_height / frame_height * y

                if id == 4:
                    thumb_x = screen_width / frame_width * x
                    thumb_y = screen_height / frame_height * y

                    thumb_index_distance = abs(index_y - thumb_y)

                    click_threshold = 20
                    move_threshold = 100

                    if thumb_index_distance < click_threshold:
                        pyautogui.click()
                        pyautogui.sleep(1)
                    elif thumb_index_distance < move_threshold:
                        pyautogui.moveTo(index_x, index_y)

    cv2.imshow('Virtual Mouse', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
