
class Food:
# Instance way
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

        
    def __repr__(self):
        return("Joe Rogan likes {}, {} {}".format(self.name,self.kind,self.name))


    def describe(self):
        print("The food is {}, {} {}".format(self.name,self.kind,self.name))



# food = Food("Meat", "Elk")
# food.describe()
#-----------------------------------------------------------------------------------

# Class method way
#     name ="name"
#     kind = "kind"

#     @classmethod
#     def describe(cls):
#         print("Joe Rogan likes {}, {} {}".format(cls.name,cls.kind,cls.name))

# Food.name = "Meat"
# Food.kind ="Elk"
# Food.describe()

#-----------------------------------------------------------------------------------

# Static method way

#     @staticmethod
#     def describe(name,kind):
#         print("Joe Rogan likes {}, {} {}".format(name,kind,name))

# Food.describe("Meat", "Elk")