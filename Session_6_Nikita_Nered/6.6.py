class Sun:

    instance = None

    def __new__(self,):
        if not isinstance(self.instance, self):
            self.instance = super().__new__(self)

    @staticmethod
    def inst():
        return Sun()


x = Sun.inst()
y = Sun.inst()

print(x is y)
