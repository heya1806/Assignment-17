import socket
from tkinter import *

def send(listbox, entry):
    message = entry.get()
    listbox.insert('end', "Server: "+message)
    entry.delete(0, END)
    client.send(bytes(message, "utf-8"))

def receive(listbox):
    message_from_client = client.recv(50)
    listbox.insert('end', "Client: "+message_from_client.decode('utf-8'))

root = Tk()

root.title("Server")

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

s.bind((HOST_NAME, PORT))

s.listen(4)
client, address = s.accept()


root.mainloop()