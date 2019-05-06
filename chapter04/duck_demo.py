class Cat(object):
    def run(self, name):
        print("Cat", name, "run")


class Dog(object):
    def run(self, action):
        print("Dog", action)
        print("Dog", "run")


class Animal(object):
    def run(self, kind):
        print("I'm a", kind)
        print("Animal", "run")


animal_list = [Cat, Dog, Animal]
for animal in animal_list:
    animal().run("123")
