'''
Uses mediapipe to estimate face position and determine if emotion can be recognized
'''

import mediapipe as mp
import cv2

mp_face_mesh = mp.solutions.face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

def detect_face_landmarks(frame):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = mp_face_mesh.process(frame_rgb)

    if results.multi_face_landmarks:
        face_landmarks = results.multi_face_landmarks[0]
        height, width = frame.shape[:2]
        return face_landmarks.landmark, width, height
    return None, None, None

def is_face_front_facing(landmarks, width, height):
    nose_tip = landmarks[1]
    left_eye_outer = landmarks[33]
    right_eye_outer = landmarks[263]

    left_distance = abs(nose_tip.x - left_eye_outer.x) * width
    right_distance = abs(nose_tip.x - right_eye_outer.x) * width

    return abs(left_distance - right_distance) < 50