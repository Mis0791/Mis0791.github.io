class Product(object):
    def __init__(self, price, item, weight, brand, status):
        self.price = price
        self.item = item 
        self.weight = weight
        self.brand = brand
        self.status = status 
    def Sell(self):
        self.status = "sold"
        return self
 
    def Tax(self):
        tax = .09 * self.price
        total = self.price + tax
        return total
    
    def Return(self):
        if (self.status == "defective"):
            self.price = 0
        elif (self.status == "for sale"):
            self.price = self.price
        elif (self.status == "used"):
            self.price *= .20

    def displayInfo(self):
        print "Price is" + " " + str(self.price) + " " + "dollars"
        print "Item: " + str(self.item)
        print str(self.weight) + "lbs"
        print "Brand: " + self.brand
        print self.status + ""
        return self

product1 = Product(15, "chicken", 2, "Foster Farms", "for sale")

product1.displayInfo()