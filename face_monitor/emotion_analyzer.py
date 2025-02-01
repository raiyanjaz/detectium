from deepface import DeepFace

def analyze_emotion(frame):
    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        if result:
            return result[0]['dominant_emotion']
    except Exception as e:
        print(f"Emotion detection error: {e}")
    return None
