'''
Emotional changes associated with Delirium:

    - Anxiety, Fear
    - Possibly anger
    - Quick changes in mood
'''

import threading
import cv2
from deepface import DeepFace

# Initialize webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Set frame dimensions
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
emotion_detected = False
dominant_emotion = "Not recognized"
font = cv2.FONT_HERSHEY_SIMPLEX

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Function to check emotion using DeepFace in a separate thread
def check_emotion(frame):
    global emotion_detected, dominant_emotion
    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        if result:
            dominant_emotion = result[0]['dominant_emotion']
            emotion_detected = True
        else:
            emotion_detected = False
    except Exception as e:
        print(f"Emotion detection error: {e}")
        emotion_detected = False

while True:
    # Read frame from the webcam
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Every 30 frames, analyze the emotion in a new thread
    if counter % 30 == 0:
        try:
            threading.Thread(target=check_emotion, args=(frame.copy(),)).start()
        except Exception as e:
            print(f"Threading error: {e}")
    
    counter += 1

    # Display the detected emotion on the video frame
    if emotion_detected:
        cv2.putText(frame, f"Emotion: {dominant_emotion}", (20, 450), font, 1, (0, 255, 0), 2)
    else:
        cv2.putText(frame, "Emotion: Not recognized", (20, 450), font, 1, (0, 0, 255), 2)

    # Show the video feed
    cv2.imshow("Real-Time Face Monitoring", frame)

    # Press 'q' to quit
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
