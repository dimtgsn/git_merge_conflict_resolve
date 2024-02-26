class AbstractPizza:
    def description(self) ->str:
        pass
    def cost(self) ->float:
        pass

class AbstractPizzaIngredient(AbstractPizza):
    def __init__(self, origin: AbstractPizza) ->None:
        self.__origin = origin
    def ingredientDescription(self) ->str:
        pass
    def ingredientCost(self) ->float:
        pass

    def description(self) ->str:
        return self.__origin.description() + self.ingredientDescription()
    def cost(self) ->float:
        return self.__origin.cost() + self.ingredientCost()

# ========================================
class SmallPizza(AbstractPizza):
    def description(self) ->str:
        return '[small pizza]'
    def cost(self) ->float:
        return 10
class MiddlePizza(AbstractPizza):
    def description(self) ->str:
        return '[middle pizza]'
    def cost(self) ->float:
        return 13
class BigPizza(AbstractPizza):
    def description(self) ->str:
        return '[big pizza]'
    def cost(self) ->float:
        return 15
# ========================================
class Pepper(AbstractPizzaIngredient):
    def ingredientDescription(self) ->str:
        return '[pepper]'
    def ingredientCost(self) ->float:
        return 3
class Chicken(AbstractPizzaIngredient):
    def ingredientDescription(self) ->str:
        return '[chicken]'
    def ingredientCost(self) ->float:
        return 5
class Cheese(AbstractPizzaIngredient):
    def ingredientDescription(self) ->str:
        return '[cheese]'
    def ingredientCost(self) ->float:
        return 2
# ========================================
def print_pizza_to_ui(pizza: AbstractPizza) ->None:
    print(f'Name: {pizza.description()}|Cost: {pizza.cost()}')
# ========================================




if __name__ == '__main__':
    pizza = BigPizza()
    pizza = Pepper(pizza)
    pizza = Pepper(pizza)
    pizza = Pepper(pizza)
    pizza = Pepper(pizza)
    print_pizza_to_ui(pizza)
