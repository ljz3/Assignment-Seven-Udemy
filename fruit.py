from food import Food

class Fruit(Food):
    def clean(self):
        print("Cleaning " + self.kind + " " + self.name)


banana = Fruit("Banana", "Columbian")
banana.clean()