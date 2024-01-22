import serial
ser1 = serial.Serial('COM3', 115200)
ser2 = serial.Serial('COM6', 115200)
#ser3 = serial.Serial('COM3', 115200)
while True:
    if ser1.in_waiting > 0:
        data = ser1.readline().decode('utf-8').strip()
        print("sensor1", data)
    if ser2.in_waiting > 0:
        data = ser2.readline().decode('utf-8').strip()
        print("sensor2", data)
    # if ser3.in_waiting > 0:
    #     data = ser3.readline().decode('utf-8').strip()
    #     print("sensor3", data)



