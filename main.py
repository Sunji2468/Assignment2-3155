import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

resources = data.resources
recipes = data.recipes

sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

def main():

    choice = input("What size sandwich would you like? (small/medium/large): ").lower()

    if choice not in recipes:
        print("Invalid sandwich size.")
        return

    order_ingredients = recipes[choice]["ingredients"]
    cost = recipes[choice]["cost"]

    if sandwich_maker_instance.check_resources(order_ingredients):

        coins = cashier_instance.process_coins()

        if cashier_instance.transaction_result(coins, cost):
            sandwich_maker_instance.make_sandwich(choice, order_ingredients)

if __name__ == "__main__":
    main()