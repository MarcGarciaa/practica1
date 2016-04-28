from Notification import Notification

class MockObject(Notification):
    """Notify, that, via configuration file, will deliver notifiations to
    all channels the user has configured. Two implementations must be provided,
    first a Mock one, that will simply print on console the sent message, and
    a Telegram Bot one, that will using Telegram the notification"""
    def __init__(self, cfg=None, name="MockObject"):
        super(MockObject, self).__init__(cfg, name)
        self.messages = []
        with open ("messages.txt", "r") as f:
            for line in f:
                self.messages.append(line)


    def get_msg(self):
        if self.msg_avail():
            return self.messages.pop(0)

    def msg_avail(self):
        return len(self.messages) > 0


    def notify(self, user, message):
        """Send to "user", the message "message"."""
        pass

    def broadcast(self, message):
        """Send to the "broadcast" channel the message "message"."""
        pass
