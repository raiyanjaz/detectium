'''
Emotional changes associated with Delirium:

    - Anxiety, Fear
    - Possibly anger
    - Quick changes in mood
'''

import threading
import cv2
import mediapipe as mp
from deepface import DeepFace

# Initialize Mediapipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Initialize webcam and frame dimension
cap = cv2.VideoCapture(2, cv2.CAP_DSHOW)
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

# Function to calculate head orientation based on face landmarks
def is_face_front_facing(landmarks, width, height):
    # Get key landmarks (e.g., nose tip, eyes)
    nose_tip = landmarks[1]
    left_eye_outer = landmarks[33]
    right_eye_outer = landmarks[263]

    # Calculate horizontal distances to check if head is turned
    left_distance = abs(nose_tip.x - left_eye_outer.x) * width
    right_distance = abs(nose_tip.x - right_eye_outer.x) * width

    # If the distances are relatively similar, the face is front-facing
    return abs(left_distance - right_distance) < 50  # Threshold for detecting frontal face

while True:
    # Read frame from the webcam
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = mp_face_mesh.process(frame_rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            width, height = frame.shape[1], frame.shape[0]

            # Check if face is front-facing
            if is_face_front_facing(face_landmarks.landmark, width, height):
                # Every 30 frames, check emotion
                if counter % 30 == 0:
                    threading.Thread(target=check_emotion, args=(frame.copy(),)).start()
                
                # Display emotion on the screen
                if emotion_detected:
                    cv2.putText(frame, f"Emotion: {dominant_emotion}", (20, 450), font, 1, (0, 255, 0), 2)
                else:
                    cv2.putText(frame, "Analyzing...", (20, 450), font, 1, (0, 255, 0), 2)
            else:
                cv2.putText(frame, "Face not front-facing", (20, 450), font, 1, (0, 0, 255), 2)
    else:
        cv2.putText(frame, "No face detected", (20, 450), font, 1, (0, 0, 255), 2)
    
    counter += 1

    # Show video feed
    cv2.imshow("Real-Time Face Monitoring", frame)

    # Press 'q' to quit
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
