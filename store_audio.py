import pyaudio
import wave
import time

# Audio Configuration
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1024
OUTPUT_FILENAME = "delerium.wav"
RECORD_SECONDS = 5  # Fixed recording duration

def record_audio():
    """Records microphone input for a fixed duration (5 seconds)."""
    print("\nRecording started... Recording for 5 seconds.")

    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    
    frames = []
    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()  # Ensure PyAudio is properly closed

    with wave.open(OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    print(f"\nRecording finished. Audio saved as {OUTPUT_FILENAME}")

# Ensure script only runs when executed directly, not when imported
if __name__ == "__main__":
    record_audio()
