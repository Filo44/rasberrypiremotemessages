import socket
import pyttsx3
import tkinter as tk
from tkinter import ttk
import threading

HOST = '192.168.0.13'  # IP address of the receiving PC
PORT = 5000  # Arbitrary port number

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)
print("hi")


def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=50, padx=50)
    B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.mainloop()


while True:
    conn, addr = s.accept()
    # print('Connected by', addr)
    data = conn.recv(1024)
    conn.close()

    print(f'Received data: {data.decode("utf-8")}')
    engine = pyttsx3.init()
    engine.say(data.decode("utf-8"))
    engine.runAndWait()
    popupmsg(data.decode("utf-8"))
