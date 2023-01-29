import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.webhook_url_label = QLabel("Webhook URL:", self)
        self.webhook_url_label.move(20, 20)

        self.webhook_url_input = QLineEdit(self)
        self.webhook_url_input.move(20, 50)
        self.webhook_url_input.resize(280, 30)

        self.message_label = QLabel("Message:", self)
        self.message_label.move(20, 90)

        self.message_input = QLineEdit(self)
        self.message_input.move(20, 120)
        self.message_input.resize(280, 30)

        self.send_button = QPushButton("Send", self)
        self.send_button.move(20, 160)
        self.send_button.clicked.connect(self.send_message)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle("Streaming Movie App")
        self.show()

    def send_message(self):
        webhook_url = self.webhook_url_input.text()
        message = self.message_input.text()
        # use requests library to send the message to the webhook URL
        requests.post(webhook_url, json={"content": message})

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
