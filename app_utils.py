import serial.tools.list_ports
import serial

def setup_serial():
    # Define the target COM port
    target_port = "COM13"
    
    # Initialize serial object
    serialInst = serial.Serial()

    # Set the baudrate and port
    serialInst.baudrate = 9600
    serialInst.port = target_port
    serialInst.open()

    # Continuously read from the serial port
    while True:
        if serialInst.in_waiting:
            packet = serialInst.readline()
            print(packet.decode('utf').rstrip('\n'))        # return bpmdata 

# Call the function to set up and start reading from the serial port
# setup_serial()
