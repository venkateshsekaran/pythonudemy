menu = {
    "coffee": {"milk": 100, "water": 200, "powder": 50}, "cost": 10
}
resources = {
    "milk": 1000,
    "water": 1000,
    "powder": 1000
}

print("Welcome to coffee machine")



def resource_sufficient(ingrediants):
   resources_quantity =True
   while resources_quantity:
     order = input("Do you want coffee,type 'yes' or 'no': ")
     if order =="yes":
       quantity = int(input("How many quantity you want : "))
       print("Resources:")
       for item in resources:
          resources[item] -= quantity * ingrediants[item]
          if resources[item] >ingrediants[item]:
              print(f"{item} is {resources[item]}ml present")
          else :
             print(f"Not enough quantity of {item}")
             resources_quantity =False
       if resources_quantity == True :
              print("Coffee is getting ready,Wait a minute")
     elif order=="no" : print("Thank you,Welcome again")
     else : print("invalid,check once again what you typed")
resource_sufficient(menu["coffee"])
print(" Sorry we can't make the coffee because of not enough quantity of ingredients")
