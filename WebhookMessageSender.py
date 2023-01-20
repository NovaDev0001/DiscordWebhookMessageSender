import requests
from tkinter import *

def send_message():
    message = message_input.get()
    webhook_url = webhook_url_input.get()
    requests.post(webhook_url, json={"content": message})
    message_input.delete(0, END)
    webhook_url_input.delete(0, END)

root = Tk()
root.title("Discord Webhook Sender")
root.geometry("400x200")

#Change the font and font size for the labels
webhook_url_label = Label(root, text="Webhook URL:", font=("Arial", 14), bg="white", fg="black")
webhook_url_label.pack()

message_label = Label(root, text="Message:", font=("Arial", 14), bg="white", fg="black")
message_label.pack()

#Change the font and font size for the input fields
webhook_url_input = Entry(root, font=("Arial", 14))
webhook_url_input.pack()

message_input = Entry(root, font=("Arial", 14))
message_input.pack()

#Change the background and foreground color for the button
send_button = Button(root, text="Send", command=send_message, bg = "blue", fg = "white")
send_button.pack()

root.mainloop()
