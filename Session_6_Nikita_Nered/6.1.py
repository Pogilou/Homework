class Counter:
    def __init__(self, start = 0, stop = None):
        self.start = start
        self.stop = stop

    def increment(self):
        if self.stop != None and self.start >= self.stop:
            return print ("Maximum value reached")
        self.start += 1

    def get(self):
        return self.start

c = Counter(start=42, stop=43)

c.increment()
c.increment()


