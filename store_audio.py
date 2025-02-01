import pyaudio
import wave
import keyboard  
import threading

FORMAT = pyaudio.paInt16
CHANNELS = 1 
RATE = 16000  
CHUNK = 1024  
OUTPUT_FILENAME = "delerium.wav"  


audio = pyaudio.PyAudio()
stream = None
frames = []
recording = False  

def record_audio():
    """Continuously records audio until Enter is pressed again."""
    global recording, stream, frames
    print("\nRecording started... Press Enter to stop.")

    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    frames = []

    while recording:
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()

    with wave.open(OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    print(f"\nRecording finished. Audio saved as {OUTPUT_FILENAME}")

print("Press Enter to start recording...")

while True:
    keyboard.wait("enter")  
    if not recording:
        recording = True
        threading.Thread(target=record_audio).start()  
    else:
        recording = False  
        break 
