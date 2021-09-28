class Bird:

    def __init__(self, name):
        self.name = name

    def walk(self):
        return "Bird {name} is walking".format(name = self.name)

    def fly(self):
        return "{name} is flying".format(name = self.name)

    def __str__(self):
        return "{name} bird can walk and fly".format(name = self.name)

class FlyingBird(Bird):

    def __init__(self, name, ration="corn"):
        super().__init__(Bird)
        self.name = name
        self.ration = ration

    def eat(self):
        return "{name} the bird is eating {ration}".format(name = self.name, ration = self.ration)

    def __str__(self):
        return "{name} bird can walk, fly and eat {ration} ".format(name = self.name, ration = self.ration)

class NonFlyingBird(FlyingBird):

    def __init__(self, name, ration="fish"):
        super().__init__(FlyingBird)
        self.name = name
        self.ration = ration

    def eat(self):
        return "{name} can eat {ration}".format(name=self.name, ration=self.ration)

    def swim(self):
        return "{name} bird can swim".format(name=self.name)

    def fly(self):
        raise AttributeError(" {name} object has no attribute 'fly'".format(name=self.name)

    def __str__(self):
        return "{name} bird can walk, swim and eat {ration} ".format(name = self.name, ration = self.ration)

class SuperBird(NonFlyingBird):
    def __init__(self, name, ration = "all"):
        super().__init__(NonFlyingBird)
        self.name = name
        self.ration = ration

    def fly(self):
        return FlyingBird.fly(self)

    def __str__(self):
        return "{name} bird can all, even write and can calculate the 3rd integral ".format(name = self.name)



