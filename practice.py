class Store:
    def __init__(self,name):
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
        self.name=name
        self.items=[]
    
    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        self.items.append({"name":name,"price":price})

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        return sum(self.items[0]["price"])
        
obj=Store("raja")
obj.add_item("raja",[25.0,45.0,65.6])
print(obj.stock_price())


class Box:
    val=0
    def fun1(self):
        self.val=1
        print("callld a instance method!!")

    @classmethod
    def fun2(cls):
        print(cls.val)
        print("called a class method!!")

    @staticmethod
    def fun3():
        #print(val)   #this is not accessible
        print("called a satic method!!")

test=Box()
test.fun1()
Box.fun2()
test.fun3()