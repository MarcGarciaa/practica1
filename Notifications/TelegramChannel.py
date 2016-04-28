from Notification import Notification
import telepot

class BeerBot(telepot.Bot):
    """BeerBot is my telegram bot"""
    def __init__(self, token, usuaris):
        super(BeerBot, self).__init__(token)
        self.clist = None
        self.chat_id = None
        self.users = usuaris

    def set_list(self, clist):
        self.clist = clist

    def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            command = msg['text']
            if self.clist is not None:
                self.clist.append(command)
                self.chat_id = chat_id
            else:
                self.sendMessage(chat_id, "No estas autoritzat!")

    def respond(self, message):
        if self.chat_id is not None:
            self.sendMessage(self.chat_id, message)


class TelegramChannel(Notification):
    """Notify, that, via notification file, will deliver notifiations to
    all channels the user has configured. Two implementations must be provided,
    first a Mock one, that will simply print on console the sent message, and
    a Telegram Bot one, that will using Telegram the notification"""
    def __init__(self, cfg=None, name="TelegramChannel"):
        super(TelegramChannel, self).__init__(cfg, name)
        token = self.cfg["telegram"]["token"]
        self.bot = BeerBot(token, self.cfg["telegram"]["usuaris"])
        self.messages = []
        self.bot.set_list(self.messages)
        self.bot.notifyOnMessage()

    def get_msg(self):
        if self.msg_avail():
            return self.messages.pop(0)

    def msg_avail(self):
        return len(self.messages) > 0

    def broadcast(self, message):
        if message is None:
            message = "Command not understood"
        self.bot.broadcast(message)



    def notify(self, user, message):
        """Send to "user", the message "message"."""
        pass
