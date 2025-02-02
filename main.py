import threading
import store_audio
import text_to_speech
import summarize

def run_store_audio():
    store_audio.record_audio()

def run_text_to_speech(audio_file, result_container):
    result_container["text"] = text_to_speech.transcribe_audio(audio_file)

def run_summarize(text):
    summary = summarize.summarize_text(text)
    print("Final Summary:", summary)

def main():
    audio_thread = threading.Thread(target=run_store_audio)
    audio_thread.start()
    audio_thread.join()  

    transcription_result = {}
    tts_thread = threading.Thread(target=run_text_to_speech, args=("delerium.wav", transcription_result))
    tts_thread.start()
    tts_thread.join()  

    print("Starting summarization thread...")
    summarize_thread = threading.Thread(target=run_summarize, args=(transcription_result["text"],))
    summarize_thread.start()
    summarize_thread.join()  

    print("Process complete!")

if __name__ == "__main__":
    main()

