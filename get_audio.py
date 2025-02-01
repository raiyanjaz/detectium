import pyaudio
import wave

# Define required audio properties for Groq's Whisper
FORMAT = pyaudio.paInt16  # 16-bit PCM
CHANNELS = 1  # Mono audio
RATE = 16000  # 16 kHz sample rate (Whisper requirement)
CHUNK = 1024  # Buffer size
RECORD_SECONDS = 5  # Change this for longer recordings
OUTPUT_FILENAME = "delerium.wav"  # File saved in Whisper-compatible format

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open microphone stream
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("\nRecording... Speak now.")

frames = []

# Capture audio from the microphone
for _ in range(int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Recording complete.")

# Stop and close the stream
stream.stop_stream()
stream.close()
audio.terminate()

# Save audio in the correct Whisper-compatible format (16kHz, mono, 16-bit PCM)
with wave.open(OUTPUT_FILENAME, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))

print(f"Audio saved as {OUTPUT_FILENAME} (Groq/Whisper-compatible format)")
