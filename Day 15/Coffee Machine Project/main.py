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
QUARTER=0.25
DIME=0.10
NICKLE=0.05
PENNY=0.01

def display_report(r,m):
    print(f'Water: {r['water']}ml')
    print(f'Milk: {r['milk']}ml')
    print(f'Coffee: {r['coffee']}g')
    print(f'Money: ${m}')

def making_coffee_function(choice,r,m):
    is_enough = resource_tracker(MENU[choice]['ingredients'], r)
    if is_enough:
        taken = coin_tracking(MENU[choice]['cost'])
        if taken:
            #take money
            m += taken

            #make coffee
            for item in MENU[choice]['ingredients']:
                left = r[item] - MENU[choice]['ingredients'][item]
                r[item] = left
            print(f'Here is your {choice}☕ Enjoy!')
            return m, r
    return m, r

def coin_tracking(cost):
    print('Please insert coins.')
    quarters=int(input('How many quarters? '))
    dimes=int(input('How many dimes? '))
    nickles=int(input('How many nickles? '))
    pennies=int(input('How many pennies? '))
    total_taken=quarters*QUARTER+dimes*DIME+nickles*NICKLE+pennies*PENNY

    if total_taken>=cost:
        print(f'Here is ${round(total_taken-cost,2)} in change.')
        return cost
    else:
        print("Sorry that's not enough money. Money refunded")

def resource_tracker(ingredients,r):
    for item in ingredients:
        if r[item]<ingredients[item]:
            print(f'Sorry, there is not enough {item}')
            return False
        else:
            return True

def machine():
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    money=0
    working=True
    while working:
        choice=input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice=='report':
            display_report(resources,money)
        elif choice in ['espresso', 'latte', 'cappuccino']:
            money,resources=making_coffee_function(choice,resources,money)
        elif choice=='off':
            working=False
        else:
            print('invalid choice')

machine()