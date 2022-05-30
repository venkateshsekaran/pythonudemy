from random import randint
answer = randint(0,100)


print("Welcome to the number guessing game")
print("I'm thinking of number between 1 to 100")
turn=int(input("How many attempts you want? "))
flag=True
while flag:
   print(f"You have {turn} attempts remaining")
   guess = int(input("Guess a number! :"))
   if guess>answer:
      print("Too high")
      turn -= 1
   elif guess<answer:
      print("Too low")
      turn -= 1
   elif guess==answer:
      print("You won")
      flag=False
   if turn==0:
      flag=False
print("Game over....")      