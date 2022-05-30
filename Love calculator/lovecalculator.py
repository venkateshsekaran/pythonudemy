print("Welcome to love calculator")
Name1=input("Enter your name: ")
Name2=input("Enter your  partner name: ")
Name=Name1 + Name2
Name_lower=Name.lower()
t=Name_lower.count("t")
r=Name_lower.count("r")
u=Name_lower.count("u")
e=Name_lower.count("e")
true= t+r+u+e
l=Name_lower.count("l")
o=Name_lower.count("o")
v=Name_lower.count("v")
e=Name_lower.count("e")
love= l+o+v+e
true_love=int(str(true)+str(love))
if true_love<=10 or true_love>=90:
    print(f"Your love score is {true_love}%,You go together like coke and mentos")
elif true_love<=20 or true_love>=80:
     print(f"Your love score is {true_love}%,You go alright together")
elif true_love<=30 or true_love>=70:
     print(f"Your love score is {true_love}%,You and your partner looks like cat and dogs ")
elif true_love<=40 or true_love>=60:
     print(f"Your love score is {true_love}%,Perfect couple ")
else:
     print(f"Your love score is {true_love}%,Romantic couple ")

