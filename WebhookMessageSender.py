import requests
from tkinter import *
from tkinter import ttk

def send_message():
    message = message_input.get()
    webhook_url = webhook_url_input.get()
    requests.post(webhook_url, json={"content": message})

root = Tk()
root.title("Discord Webhook Sender")
root.geometry("400x200")

# Title label
title = Label(root, text="Made By Nova,#1437", font=("Arial", 14), bg="white", fg="black")
title.pack(pady = (10,0))

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
style = ttk.Style()
style.configure("TButton", background="blue", font=("Arial", 14), relief=FLAT)
send_button = ttk.Button(root, text="Send", command=send_message)
send_button.pack()

# Get the width and height of the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates to center the GUI on the screen
x_coord = (screen_width/2) - (400/2)
y_coord = (screen_height/2) - (200/2)
root.geometry("+%d+%d" % (x_coord, y_coord))

root.mainloop()
