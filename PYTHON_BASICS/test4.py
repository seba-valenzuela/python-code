num_list = [1,2,3,4,5]

squared_list = [num*num for num in num_list]
print(squared_list)
print()

cubed_list = [num*num*num for num in num_list if num != 1]
print(cubed_list)
print()

class US_Price():
    def __init__(self, cost):
        self.cost = cost

    def showCost(self):
        print("The cost of this item in the US is ${}".format(self.cost))
        print()

class Canada_Price(US_Price):
    def __init__(self, cost, inflation):
        super(Canada_Price, self).__init__(cost)
        self.inflation = inflation

    def showCost(self):
        super(Canada_Price, self).showCost()
        new_price = self.cost * self.inflation
        print("The cost of this item in Canada is ${}".format(new_price))
        print()

US_item = US_Price(10)
US_item.showCost()

Canada_item = Canada_Price(10,2)
Canada_item.showCost()