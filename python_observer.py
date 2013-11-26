class Mailbox:
    def __init__(self, ownersName):
        self.owner = ownersName
        self.messages = []
        self.newMessageObservers = []
    
    def deliverMessage(self, message):
        self.messages.append(message)
        for notifyNewMessage in self.newMessageObservers:
            notifyNewMessage(message,self.owner)

    def subscribe(self, observer):
        self.newMessageObservers.append(observer)

class MailboxObserver:
    def __init__(self, observerName):
        self.name = observerName
    def newMessageHandler(self, contents, owner):
        print self.name + " observed a new message in "+\
            owner+"'s mailbox'"
        print "The message said: "+ contents


alice = MailboxObserver("alice")
bob = MailboxObserver("bob");
alicesMailbox = Mailbox("alice")
alicesMailbox.subscribe(bob.newMessageHandler)
alicesMailbox.subscribe(alice.newMessageHandler)
alicesMailbox.deliverMessage("Hello, world!")
