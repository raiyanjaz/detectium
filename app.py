from flask import Flask, render_template, Response, jsonify
import cv2
from face_monitor.main import process_frame
from speech_to_analysis.speech_emotion_analysis import record_audio, detect_emotions

app = Flask(__name__)

# Initialize webcam
camera = cv2.VideoCapture(2)

@app.route('/')
def index():
    # Main page
    return render_template('index.html')

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            # Process the frame (e.g., run face detection)
            processed_frame = process_frame(frame)

            # Encode the frame for streaming
            _, buffer = cv2.imencode('.jpg', processed_frame)
            frame_bytes = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/video_feed')
def video_feed():
    # Video streaming route
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/detect_emotion', methods=['GET'])
def detect_emotion_route():
    """
    Flask route to record audio and detect emotions.
    Returns emotions with confidence above 60%.
    """
    audio_data = record_audio()
    emotions = detect_emotions(audio_data)
    return jsonify(emotions)
