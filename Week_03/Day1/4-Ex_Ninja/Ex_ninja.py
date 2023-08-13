class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, other_phone):
        print(f"{self.phone_number} called {other_phone.phone_number}")
        self.call_history.append(
            f"{self.phone_number} called {other_phone.phone_number}"
        )

    def show_call_history(self):
        print(self.call_history)

    def send_message(self, other_phone, content):
        self.messages.append(
            {
                "to": other_phone.phone_number,
                "from": self.phone_number,
                "content": content,
            }
        )

    def show_outgoing_messages(self):
        for message in self.messages:
            if message["from"] == self.phone_number:
                print(message)

    def show_incoming_messages(self):
        for message in self.messages:
            if message["to"] == self.phone_number:
                print(message)

    def show_messages_from(self, phone_number):
        for message in self.messages:
            if message["from"] == phone_number:
                print(message)
