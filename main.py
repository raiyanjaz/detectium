import subprocess

# Step 1: Run store_audio.py (Records Audio)
print("\nStarting audio recording...")
subprocess.run(["python", "store_audio.py"])

# Step 2: After recording is finished, run text_to_speech.py (Transcribes Audio)
print("\nRecording complete. Now transcribing the audio...")
subprocess.run(["python", "text_to_speech.py"])
