import random
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers=["0","1","2","3","4","5","6","7","8","9"]
symbols=["~","!","@","$","#","%","^","&","*","(",")","_","-","+"]
print("Welcome to password generator")
letters_length=int(input("How many letters you want?"))
numbers_length=int(input("How many numbers you want?"))
symbols_length=int(input("How many symbols you want?"))
password=[]
for letter in range(1,letters_length+1):
    password += random.choice(letters)
for symbol in range(1,letters_length+1):
    password += random.choice(symbols)
for number in range(1,letters_length+1):
    password += random.choice(numbers)
random.shuffle(password)
new_password=""
for char in password:
    new_password += char
print(new_password)    
