from flask import Flask, render_template, Response
import cv2
from face_monitor.main import process_frame
import threading
from app_utils import setup_serial

app = Flask(__name__)



# Initialize webcam
camera = cv2.VideoCapture(0)

@app.route('/')
def index():
    # Main page
    return render_template('index.html')

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            print('test')
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

# Start the serial communication in a separate thread
def start_serial_communication():
    setup_serial()
    # print(bpminfo)

serial_thread = threading.Thread(target=start_serial_communication)
serial_thread.daemon = True
serial_thread.start()

if __name__ == '__main__':
    app.run(debug=True)
