import torch
import librosa
from transformers import Speech2TextProcessor, Speech2TextForConditionalGeneration

# Load the Hugging Face Speech2Text model and processor
model = Speech2TextForConditionalGeneration.from_pretrained("facebook/s2t-small-librispeech-asr")
processor = Speech2TextProcessor.from_pretrained("facebook/s2t-small-librispeech-asr")

def transcribe_audio(file_path):

    audio_array, sampling_rate = librosa.load(file_path, sr=16000)
    inputs = processor(audio_array, sampling_rate=sampling_rate, return_tensors="pt")

    with torch.no_grad():
        generated_ids = model.generate(inputs["input_features"], attention_mask=inputs["attention_mask"])

    transcription = processor.batch_decode(generated_ids, skip_special_tokens=True)
    
    return transcription[0]

file_path = "delerium.wav"
transcription = transcribe_audio(file_path)
print("\nTranscription:\n", transcription)
