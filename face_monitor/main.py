import cv2
from face_monitor.face_pos import detect_face_landmarks, is_face_front_facing
from face_monitor.emotion_analyzer import analyze_emotion

counter = 0
dominant_emotion = "Not recognized"

def process_frame(frame):
    global counter, dominant_emotion
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Detect face landmarks
    landmarks, width, height = detect_face_landmarks(frame)

    if landmarks:
        if is_face_front_facing(landmarks, width, height):
            # Every 15 frames, run emotion detection
            if counter % 15 == 0:
                emotion = analyze_emotion(frame)
                if emotion:
                    dominant_emotion = emotion

            # Display the latest detected emotion
            cv2.putText(frame, f"Emotion: {dominant_emotion}", (20, 450), font, 1, (0, 255, 0), 2)
        else:
            cv2.putText(frame, "Face not front-facing", (20, 450), font, 1, (0, 0, 255), 2)
    else:
        cv2.putText(frame, "No face detected", (20, 450), font, 1, (0, 0, 255), 2)

    counter += 1  # Increment frame counter
    return frame