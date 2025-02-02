from flask import Flask, render_template, Response, jsonify, stream_with_context
import cv2
from face_monitor.main import process_frame
import threading
from heart_monitor.app_utils import setup_serial
from speech_to_analysis.speech_emotion_analysis import record_audio, detect_emotions
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

# Initialize webcam
camera = cv2.VideoCapture(0)
if not camera.isOpened():
    raise RuntimeError("Could not start camera")

# Shared data store for serial data
serial_data = {'bpm': 'N/A', 'avg_bpm': 'N/A', 'finger_detected': 1}

# Add a lock for thread-safe updates
serial_data_lock = threading.Lock()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_serial_data')
def get_serial_data():
    with serial_data_lock:
        return jsonify(serial_data.copy())  # Return a copy to prevent race conditions

def generate_frames():
    while camera.isOpened():
        success, frame = camera.read()
        if not success:
            print("Failed to grab frame")
            break
            
        try:
            # Process the frame
            processed_frame = process_frame(frame)
            
            # Encode the frame
            ret, buffer = cv2.imencode('.jpg', processed_frame)
            if not ret:
                print("Failed to encode frame")
                continue
                
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
        except Exception as e:
            print(f"Error processing frame: {str(e)}")
            continue

@app.route('/video_feed')
def video_feed():
    return Response(
        generate_frames(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )

@app.route('/stream_emotions')
def stream_emotions():
    """
    Continuously streams detected emotions to the frontend.
    """
    def generate_emotions():
        while True:
            audio_data = record_audio()
            emotions = detect_emotions(audio_data)

            # Prepare the data to be sent as an event stream
            yield f"data: {jsonify(emotions).get_data(as_text=True)}\n\n"
            
            time.sleep(2)  # Adjust sleep time as needed for smoother updates

    return Response(stream_with_context(generate_emotions()), mimetype='text/event-stream')


# Start the serial communication in a separate thread
def start_serial_communication():
    global serial_data
    try:
        setup_serial(serial_data)
    except Exception as e:
        print(f"Serial communication error: {str(e)}")

def cleanup():
    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    # Start serial communication thread
    serial_thread = threading.Thread(target=start_serial_communication)
    serial_thread.daemon = True
    serial_thread.start()
    
    try:
        app.run(debug=False, threaded=True)  # Changed debug to False
    finally:
        cleanup()