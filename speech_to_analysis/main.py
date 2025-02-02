from speech_to_analysis.speech_emotion_analysis import record_audio, detect_emotions

def main():
    """
    Runs the audio recording and emotion detection for testing.
    """
    print("Recording...")
    audio_data = record_audio()
    emotions = detect_emotions(audio_data)
    
    print("Detected Emotions:", emotions)

if __name__ == "__main__":
    main()