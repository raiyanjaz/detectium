import serial.tools.list_ports
import serial
import time
from threading import Lock

def setup_serial(serial_data, port="COM3", baudrate=9600):
    serial_lock = Lock()
    
    try:
        serialInst = serial.Serial(port=port, baudrate=baudrate, timeout=1)
        print(f"Successfully connected to {port}")
        
        while True:
            try:
                if serialInst.in_waiting:
                    packet = serialInst.readline().decode('utf-8', errors='ignore').strip()
                    
                    # Extract values
                    parts = packet.replace("No finger?", "").split(", ")
                    bpm = avg_bpm = "N/A"
                    finger_detected = 1
                    
                    for part in parts:
                        if "BPM=" in part and "Avg" not in part:
                            try:
                                bpm = float(part.split("=")[1])
                            except ValueError:
                                bpm = "N/A"
                        elif "Avg BPM=" in part:
                            try:
                                avg_bpm = float(part.split("=")[1])
                            except ValueError:
                                avg_bpm = "N/A"
                    
                    if "No finger?" in packet:
                        finger_detected = 0
                    
                    # Update the shared dictionary thread-safely
                    with serial_lock:
                        serial_data['bpm'] = bpm
                        serial_data['avg_bpm'] = avg_bpm
                        serial_data['finger_detected'] = finger_detected
                
                # Add a small sleep to prevent busy-waiting
                time.sleep(0.01)
                
            except serial.SerialException as e:
                print(f"Serial communication error: {e}")
                time.sleep(1)  # Wait before retrying
                continue
                
    except serial.SerialException as e:
        print(f"Failed to connect to {port}: {e}")
        raise