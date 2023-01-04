class NewsPublisher:
    def __init__(self):
        self.__subscribers = []
        self.__lastestNews = None
    
    def attach(self, subscriber):
        self.__subscribers.append(subscriber)
    
    def detach(self):
        return self.__subscribers.pop()
    
    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]
    
    def notifySubscribers(self):
        for sub in self.__subscribers:
            sub.update()

    def addNews(self, news):
        self.__lastestNews = news

    def getNews(self):
        return "Got news:", self.__lastestNews