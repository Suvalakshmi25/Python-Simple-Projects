MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit=0
value={"quarters" :0.25,"dimes" : 0.10,"nickles" : 0.05,"pennies":0.01,}
def update_resource(c):
    if c=="espresso":
        resources['water']-=MENU[c]["ingredients"]['water']
        resources['coffee'] -= MENU[c]["ingredients"]['coffee']
    else:
        resources['milk'] -= MENU[c]["ingredients"]['milk']
        resources['water'] -= MENU[c]["ingredients"]['water']
        resources['coffee'] -= MENU[c]["ingredients"]['coffee']
def calculate_bill():
    print("Insert Coins...!")
    quarters = float(input("Quarters:"))*0.25
    dimes = float(input("Dimes:"))*0.10
    nickles = float(input("Nickles:"))*0.05
    pennies = float(input("pennies:"))*0.01
    total_paid=quarters+dimes+nickles+pennies
    bill = total_paid - coffee_price
    if total_paid>=coffee_price:
        update_resource(coffee)
        return f"Here is the change {round(bill,2)})
    else:
        return "Sorry that's not enough money. Money refunded."
game=True
while game==True:
    coffee=input("What would you like? (espresso/latte/cappuccino):")
    if coffee=="latte" or coffee=="cappuccino":
        if (resources['milk'] >=MENU[coffee]["ingredients"]['milk']) and (resources['water'] >= MENU[coffee]["ingredients"]['water']) and (resources['coffee'] >= MENU[coffee]["ingredients"]['coffee']):
            coffee_price = MENU[coffee]['cost']
            if coffee == "latte":
                price = calculate_bill()
                print(price)
            else:
                price = calculate_bill()
                print(price)
            print(f"Here is your {coffee}. Enjoy!”")
            profit += coffee_price
        else :
            if resources['water'] <=MENU[coffee]["ingredients"]['milk']:
                print("Sorry there is not enough water.")
            elif resources['milk'] <= MENU[coffee]["ingredients"]['water']:
                print("Sorry there is not enough milk.")
            else:
                print("Sorry there is not enough coffee.")
    elif coffee=="espresso":
        coffee_price = MENU[coffee]['cost']
        if (resources['water'] >= MENU[coffee]["ingredients"]['water']) and (resources['coffee'] >= MENU[coffee]["ingredients"]['coffee']):
            price = calculate_bill()
            print(price)
            print(f"Here is your {coffee}. Enjoy!”")
            profit += coffee_price
        else:
            if resources['water'] <=MENU[coffee]["ingredients"]['water']:
                print("Sorry there is not enough water.")
            else:
                print("Sorry there is not enough coffee.")

    elif coffee=="report":
        for keys in resources:
            print(keys.title(), ":", resources[keys])
        print("Profit: $", profit)
    else:
        game=False





