import RPi.GPIO as GPIO
import time
import socket

GPIO.setmode(GPIO.BOARD)

GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)


def sendMessage(message):
    HOST = '192.168.0.13'  # IP address of the receiving PC
    PORT = 5000  # Arbitrary port number
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    message = message
    s.sendall(bytes(message, "utf-8"))
    s.close()


# Switch on
GPIO.output(3, GPIO.HIGH)
GPIO.output(5, GPIO.HIGH)

# To read the state
wasOn = False
wasOn2 = False
while True:
    state = GPIO.input(3)
    state2 = GPIO.input(5)
    if state == False and wasOn == False:
        print('on')
        sendMessage("Pronto!")
        wasOn = True
    elif state == True and wasOn == True:
        print("kinda off")
        wasOn = False
    if state2 == False and wasOn2 == False:
        print('on')
        sendMessage("Doccia!")
        wasOn2 = True
    elif state2 == True and wasOn2 == True:
        print("kinda off")
        wasOn2 = False
    time.sleep(0.1)
