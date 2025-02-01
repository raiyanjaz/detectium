import sounddevice as sd
import numpy as np
from transformers import pipeline

# Load pre-trained emotion recognition pipeline
emotion_pipeline = pipeline('audio-classification', model='superb/wav2vec2-base-superb-er')

# Audio recording parameters
RATE = 16000
DURATION = 2  # Record every 2 seconds
RMS_THRESHOLD = 0.002  # Threshold for detecting silence based on RMS

print("\nRecording started. Press Ctrl+C to stop.\n")

try:
    with sd.InputStream(samplerate=RATE, channels=1, dtype='float32') as stream:
        while True:
            # Read audio from the stream
            print("Recording...")
            audio_data, _ = stream.read(int(DURATION * RATE))

            # Reshape and flatten the audio data, make 1D
            audio_data = np.squeeze(audio_data)

            # Calculate RMS (Root Mean Square) to detect coherent audio
            rms_value = np.sqrt(np.mean(np.square(audio_data)))

            # # Check if RMS indicates significant audio presence
            # if rms_value < RMS_THRESHOLD:
            #     print("No coherent audio detected.")
            #     continue

            # Run emotion detection directly on NumPy array
            results = emotion_pipeline(audio_data, sampling_rate=RATE)

            # Print detected emotions
            print(f"Detected Emotions: {results}")

except KeyboardInterrupt:
    print("\nRecording stopped.")
