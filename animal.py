class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health = self.health - 1
        return self
    def run(self):
        self.health = self.health - 5
        return self
    def displayhealth(self):
        print self.name + " "
        print self.health 
class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name, 150)
    def pet(self):
        self.health += 5
        return self
class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name, 170)
    def fly(self):
        self.health -= 10
        return self
    def displayhealth(self):
        super(Dragon, self).displayhealth()
        print "I am a Dragon"

dog1 = Dog("Boomer")
dragon1 = Dragon("Rhaegal")

dog1.pet().pet().walk().displayhealth()
dragon1.fly().fly().fly().displayhealth()