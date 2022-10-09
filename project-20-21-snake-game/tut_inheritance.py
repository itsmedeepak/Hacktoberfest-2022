'''class Animal:
    def __init__(self):
        self.leg = 4
        self.num_eye = 2

    def breathe(self):
        print("inhale, exhale")
        print(self.leg)


class Dog(Animal):
    def __init__(self):
        super().__init__()

    def bark(self):
        super().breathe()
        print("yeah")


nemo = Dog()
print(nemo.num_eye)'''


class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")


nemo = Fish()
nemo.breathe()
