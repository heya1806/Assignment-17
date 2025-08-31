import socket
from tkinter import *

def send(listbox, entry):
    message = entry.get()
    listbox.insert('end', "Client: "+message)
    entry.delete(0, END)
    s.send(bytes(message, "utf-8"))
    receive(listbox)

def receive(listbox):
    message = s.recv(50)
    listbox.insert('end', "Server: "+message.decode('utf-8'))

root = Tk()

root.title("Client")

entry = Entry(root, font=("Arial", 14))
entry.pack(side = "bottom", fill="x", ipady=8, padx=10, pady=5)

listbox = Listbox(root, font=("Arial", 14))
listbox.pack(fill = "both", expand = True, padx=10, pady=10 )

button = Button(root, text = "Send", command=lambda: send(listbox, entry), font=("Arial", 12))
button.pack(side = "bottom", pady=5)

rbutton = Button(root, text = "Receive", command=lambda: receive(listbox), font=("Arial", 12))
rbutton.pack(side = "bottom", pady = 5)



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST_NAME = socket.gethostname()
PORT = 12345

s.connect((HOST_NAME, PORT))

root.mainloop()



