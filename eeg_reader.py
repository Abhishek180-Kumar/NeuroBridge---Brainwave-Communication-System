import serial
import time

# Replace with the correct serial port of your EEG device
ser = serial.Serial('COM3', 9600)

print("Reading EEG data...")
while True:
    data = ser.readline()
    if data:
        print("EEG Raw: ", data.decode().strip())
    time.sleep(0.1)