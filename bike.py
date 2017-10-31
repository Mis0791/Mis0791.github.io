class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print "Price is: $" + str(self.price)
        print "Max speed:" + str(self.max_speed) + "mph"
        print "Miles:" + str(self.miles) + "miles"
    def ride(self):
        self.miles += 10
        print "Riding"
    def reverse(self):
        if self.miles >= 5:
            self.miles -= 5
        print "Reversing"

bike1 = Bike(99.99, 12)
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()