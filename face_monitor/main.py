import threading
import cv2
from face_pos import is_face_front_facing, detect_face_landmarks
from emotion_analyzer import analyze_emotion

cap = cv2.VideoCapture(2, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
dominant_emotion = "Not recognized"
font = cv2.FONT_HERSHEY_SIMPLEX
emotion_detected = False

def check_emotion(frame):
    global dominant_emotion, emotion_detected
    dominant_emotion = analyze_emotion(frame)
    emotion_detected = True if dominant_emotion else False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    landmarks, width, height = detect_face_landmarks(frame)

    if landmarks:
        if is_face_front_facing(landmarks, width, height):
            if counter % 30 == 0:
                threading.Thread(target=check_emotion, args=(frame.copy(),)).start()
            
            if emotion_detected:
                cv2.putText(frame, f"Emotion: {dominant_emotion}", (20, 450), font, 1, (0, 255, 0), 2)
            else:
                cv2.putText(frame, "Analyzing...", (20, 450), font, 1, (0, 255, 0), 2)
        else:
            cv2.putText(frame, "Face not front-facing", (20, 450), font, 1, (0, 0, 255), 2)
    else:
        cv2.putText(frame, "No face detected", (20, 450), font, 1, (0, 0, 255), 2)

    counter += 1
    cv2.imshow("Real-Time Face Monitoring", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
