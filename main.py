class User:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def send_message(self, recipient, message):
        print(f"Повідомлення для {recipient.name}:")
        print(f"Текст: {message}")
        print("Статус: Надіслано успішно ✅")

def invite_to_coffee(sender, recipient, idea=None):
    if idea:
        text = f"Привіт, {recipient.name}! Я поруч у {recipient.location}. Давай вип'ємо кави та обговоримо твою ідею: '{idea}'?"
    else:
        text = f"Привіт, {recipient.name}! Я також зараз у {recipient.location}. Маєш час на каву?"
    
    sender.send_message(recipient, text)

if __name__ == "__main__":
    current_user = User("Іван", "Харків (Наукова)")
    neighbor = User("Олексій", "Харків (Наукова)")

    invite_to_coffee(current_user, neighbor, "Розробка AI-асистента для студентів")