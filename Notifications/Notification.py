class Notification(object):
    """Notify, that, via configuration file, will deliver notifiations to
    all channels the user has configured. Two implementations must be provided,
    first a Mock one, that will simply print on console the sent message, and
    a Telegram Bot one, that will using Telegram the notification"""
    def __init__(self, cfg, name):
        super(Notification, self).__init__()
        self.name = name
        self.cfg = cfg

    def notify(self, user, message):
        """Send to "user", the message "message"."""
        print "OK!", message, user

    def broadcast(self, message):
        """Send to the "broadcast" channel the message "message"."""
        print "OK Broadcast!", message
