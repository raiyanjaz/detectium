import sounddevice as sd
import numpy as np
from transformers import pipeline

# Load pre-trained wav2vec2 model for emotion recognition
emotion_pipeline = pipeline('audio-classification', model='superb/wav2vec2-base-superb-er')

# Audio recording parameters
RATE = 16000
DURATION = 2  # Duration for each recording (in s)

def record_audio():
    """
    Records audio for a specified duration and returns normalized audio data.
    """
    with sd.InputStream(samplerate=RATE, channels=1, dtype='float32') as stream:
        audio_data, _ = stream.read(int(DURATION * RATE))
        audio_data = np.squeeze(audio_data)

        if np.max(np.abs(audio_data)) != 0:
            audio_data = audio_data / np.max(np.abs(audio_data))

        return audio_data

def detect_emotions(audio_data):
    """
    Detects emotions from the recorded audio data.
    Returns emotions with confidence above 60%.
    """
    results = emotion_pipeline(audio_data, sampling_rate=RATE)

    filtered_emotions = [
        {"emotion": result['label'], "confidence": round(result['score'], 2)}
        for result in results if result['score'] > 0.6
    ]

    # Potentially change to neutral emotion then
    return filtered_emotions if filtered_emotions else {"message": "No emotions detected with confidence above 60%."}
