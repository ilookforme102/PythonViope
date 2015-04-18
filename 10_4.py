'''
The program tries out inheritance. In this exercise,
your task is to define a new class
which will be inherited from the class Customer.

Define a new class called ManageCustomer which has the following abilities: 
1) A method "addbill", which increases the attribute total by 50, and 
2) a method "payment" which decreases the attribute total by 100.
'''

# -*- coding: cp1252 -*-
# -*- coding: cp1252 -*-

class Customer:
    name = "John Johnsson"
    total = 1000
    paymenttype = "Masterexpress"
    number = "1234-5678-9012345"

    def printout(self):
        print("Name: ", self.name)
        print("Total: ", self.total)
        print("Payment type: ", self.paymenttype)
        print("Card/Bill number: ", self.number)

class ManageCustomer(Customer):

    def addbill(self):
        self.total += 50

    def payment(self):
        self.total -= 100
  
def main():
    person = ManageCustomer()
    person.name = "Homer Griffin"
    person.addbill()
    person.payment()
    person.payment()
    person.printout()
    
if __name__ == "__main__":
    main()
