class Animal():

    def __init__(self, food):
        self.food = 'Raw Food'

    def display_food(self):
        print(self.food)




class Dog(Animal):

    def __init__(self, food):
        self.food = food


ob = Dog(food='Dog Food')
ob.display_food()