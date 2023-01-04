from abc import ABCMeta, abstractmethod

class Subscriber(metaclass=ABCMeta):

    @abstractmethod
    def update(self):
        pass

class Subscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())

class SMSSubscriber(Subscriber):
    def __init__(self, publisher):
        super().__init__(publisher)

class EmailSubscriber(Subscriber):
    def __init__(self, publisher):
        super().__init__(publisher)

class AnyOtherSubscriber(Subscriber):
    def __init__(self, publisher):
        super().__init__(publisher)

# class SMSSubscriber(Subscriber):
#     def __init__(self, publisher):
#         self.publisher = publisher
#         self.publisher.attach(self)

#     def update(self):
#         print(type(self).__name__, self.publisher.getNews())

# class EmailSubscriber:
#     def __init__(self, publisher):
#         self.publisher = publisher
#         self.publisher.attach(self)

#     def update(self):
#         print(type(self).__name__, self.publisher.getNews())

# class AnyOtherSubscriber:
#     def __init__(self, publisher):
#         self.publisher = publisher
#         self.publisher.attach(self)

#     def update(self):
#         print(type(self).__name__, self.publisher.getNews())