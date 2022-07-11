# In Python you can indicate default values for parameters in a function
# Normally, for example, if a function has 3 parameters,
# your call to that function should have 3 arguments

# with KEYWORD PARAMETERS, you specify a default value for a parameter,
# so the user doesn't have to explicitly include it in their call

class BurgerKing():

    def orderBurgers(self, nBurgers, ketchup=True, mustard=True, pickle=True):
        if nBurgers < 1:
            self.nBurgers = 0
            return print('You must order at least 1 burger.')
        self.nBurgers = nBurgers #can't order 0 burgers *fix*
        self.ketchup = ketchup
        self.mustard = mustard
        self.pickle = pickle
    
    def printOrder(self):
        if self.nBurgers == 0:
            return

        # check for toppings, save to list
        toppingsList = []
        toppingsStr = ''
        if self.ketchup == True:
            toppingsList.append('ketchup')
        if self.mustard == True:
            toppingsList.append('mustard')
        if self.pickle == True:
            toppingsList.append('pickles')
        print(toppingsList)
        
        # create the toppings string
        # none
        if len(toppingsList) == 0:
            toppingsStr = 'no toppings.'
        
        # singular
        elif len(toppingsList) == 1:
            toppingsStr = '{}.'.format(toppingsList[0])
        
        # plural
        elif len(toppingsList) > 1:
            # add the 1st list item
            toppingsStr += toppingsList[0]
            
            if len(toppingsList) == 2:
                toppingsStr += ' and {}.'.format(toppingsList[1])
                # toppingsStr + ' and ' + toppingsList[1] + '.'
            if len(toppingsList) == 3:
                toppingsStr += ', {}, and {}.'.format(toppingsList[1], toppingsList[2])
                # toppingsStr + ', ' + toppingsList[2] + ', and ' + toppingsList[2] + '.'
        
        if self.nBurgers == 1:
            order = 'You ordered 1 burger with ' + toppingsStr
        elif self.nBurgers > 1:
            order = 'You ordered {} burgers with '.format(self.nBurgers) + toppingsStr

        return print(order)

order1 = BurgerKing()
order2 = BurgerKing()

print()
order1.orderBurgers(1)
order1.printOrder()
print()

order1.orderBurgers(2, False)
order1.printOrder()
print()

order1.orderBurgers(3, True, False)
order1.printOrder()
print()

order1.orderBurgers(4, False, False)
order1.printOrder()
print()

order1.orderBurgers(10, False, False, False)
order1.printOrder()
print()

order1.orderBurgers(0, False, False, False)
order1.printOrder()
print()

order2.orderBurgers(2, pickle=False, ketchup=False)
order2.printOrder()
print()