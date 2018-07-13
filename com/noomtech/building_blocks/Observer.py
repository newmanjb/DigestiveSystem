"""Holds objects associated with the implementation of the observer pattern"""

class Observable :

    """For objects that can be 'observed'.  A listener can be registered under an event type. """

    def __init__(self):
        self.observers = {}


    def addObserver(self, eventType, fn):

        """Add an event listener for the give type of event"""

        if eventType not in self.observers:
            self.observers[eventType] = []

        self.observers[eventType].append(fn)

    def removeObserver(self, eventType, observer):
        if eventType in self.observers and observer in self.observers[eventType]:
            self.observers[eventType].remove(observer)
        else :
            raise ValueError("Observer (" + str(observer) + ") not found")

    def fireObservers(self, eventType, **args):
        if eventType in self.observers:
            event = Event()
            [setattr(event,k,v) for k,v in args.items()]
            obsList = self.observers[eventType]
            for fn in obsList:
                fn(event)

class Event:
    """"The class used to hold event data"""
    pass