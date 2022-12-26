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

def is_resources_sufficent(order_ingr):
  for i in order_ingr:
    if order_ingr[i]>=resources[i]:
      print(f"Sorry there is not enough {i}.")
      return False
  return True

def process_coins():
  print("please input coins:")
  total=int(input("how many quaters:"))*0.25
  total+=int(input("how many dimes:"))*0.1
  total+=int(input("how many nickels:"))*0.05
  total+=int(input("how many pennies:"))*0.01
  return total
  
def is_transaction_completed(money_received,drink_cost):
  if money_received>=drink_cost:
    change=round(money_received-drink_cost,2)
    print(f"Here is your chang:{change}")
    global profit
    profit +=drink_cost
    return True
  else:
    print("Sorry not enough money.Money refunded")
    return False

def Make_drink(drink_name,order_ingr):
  for i in order_ingr:
    resources[i]-=order_ingr[i]
  print(f"Here is your Drink :{drink_name}")


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit=0
is_on=True
while is_on:
  choice = input("What would you like to drink?(espresso/latte/cappuccino) or (off/report) : ")
  if choice=="off":
    is_on=False
  elif choice=="report":
    print(f"water={resources['water']}")
    print(f"milk={resources['milk']}")
    print(f"coffee={resources['coffee']}")
    print(f"profit={profit}")
  else:
    drink=MENU[choice]
    if is_resources_sufficent(drink['ingredients']):
      payment=process_coins()
      if is_transaction_completed(payment,drink["cost"]):
        Make_drink(choice,drink["ingredients"])