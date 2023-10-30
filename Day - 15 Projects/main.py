MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 150,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 250,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print("Sorry We Can't Process Your Order.")
            return False
    return True


def process_coins():
    print("Please Insert cash:")
    total = int(input("How Many ₹50 Notes:"))*50
    total += int(input("How Many ₹100 Notes:"))*100
    total += int(input("How Many ₹200 Notes:"))*200
    return total


def is_transaction_successful(coffee_price,received_money):
    if received_money >= coffee_price:
        change = round(received_money-coffee_price,2)
        print(f"Your Change:{change}")
        global profit
        profit += coffee_price
        return True
    else:
        print("Not Sufficient Money. Sorry!!!!")
        return False


def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Enjoy Your {drink_name} ☕.Enjoy!!")


is_on = True
while is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino):")
    if user_input == 'off':
        is_on = False
    elif user_input == "Report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Profit: ₹{profit}")
    else:
        drink = MENU[user_input]
        if is_resources_sufficient(drink['ingredients']):
            cost=process_coins()
            if is_transaction_successful(drink['cost'], cost):
                make_coffee(user_input, drink["ingredients"])