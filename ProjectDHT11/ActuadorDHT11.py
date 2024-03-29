from time import sleep as sleepy

import serial

arduino = serial.Serial("com5", 9600, timeout=5)
sleepy(5)


def get_temperature():
    arduino.write(b'0')
    sleepy(5)
    temp = arduino.readline()
    temp = temp.decode("utf-8")
    print(temp.strip(), "°")


def get_humidity():
    arduino.write(b'1')
    sleepy(5)
    hum = arduino.readline()
    hum = hum.decode("utf-8")
    print(hum.strip(), "%")


def menu():
    option = ""
    while option is not "2":
        print("Select an option:")
        print("[0] Temperature")
        print("[1] Humidity")
        print("[2] Exit")
        option = input("Option: ")
        if option is "0":
            get_temperature()
        else:
            if option is "1":
                get_humidity()


menu()
