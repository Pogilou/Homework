class HistoryDict:

    dictionary = {}

    def __init__(self, ):

        self.history = []

    def set_value(self, key, value):

        self.dictionary[key] = value
        self.history.append(key)

    def get_history(self):

        return print(self.history[-10:])

d = HistoryDict()
d.set_value("bar", 43)
d.get_history()


