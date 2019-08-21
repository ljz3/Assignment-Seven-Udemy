from food import Food

class Meat(Food):
    def cook(self):
        print("Cooking " + self.kind + " " + self.name)


elk_meat = Meat("Meat", "Elk")
elk_meat.cook()
print(elk_meat)