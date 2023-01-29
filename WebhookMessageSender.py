import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QFileDialog, QPushButton, QLabel
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create the layout
        layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        # Create the widgets
        webhook_label = QLabel("Enter Webhook Url:")
        self.webhook_input = QLineEdit()
        message_label = QLabel("Enter Message:")
        self.message_input = QTextEdit()
        send_button = QPushButton("Send")
        send_button.clicked.connect(self.send_webhook)
        self.image_label = QLabel()
        self.image_label.setPixmap(QPixmap('discord_icon.png'))
        self.image_button = QPushButton("Add Image")
        self.image_button.clicked.connect(self.open_file_dialog)

        # Add the widgets to the layout
        layout.addWidget(webhook_label)
        layout.addWidget(self.webhook_input)
        layout.addWidget(message_label)
        layout.addWidget(self.message_input)
        h_layout.addWidget(self.image_label)
        h_layout.addWidget(self.image_button)
        layout.addLayout(h_layout)
        layout.addWidget(send_button)

        # Create the central widget and set its layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Set the window title
        self.setWindowTitle("Webhook Sender")

    def send_webhook(self):
        webhook_url = self.webhook_input.text()
        message = self.message_input.toPlainText()
        



        












        # Send the webhook request with the message and image (if specified)
        files = {}
        if hasattr(self, 'image_path'):
            files = {'image': open(self.image_path, 'rb')}
        requests.post(webhook_url, data={'content': message}, files=files)

    def open_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "Images (*.png *.xpm *.jpg *.bmp *.gif);;All Files (*)", options=options)
        if file_name:
            self.image_path = file_name
            self.image_label.setPixmap(QPixmap(file_name))

app = QApplication(sys.argv)
window =MainWindow()
window.show()
sys.exit(app.exec_())
