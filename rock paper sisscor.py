import random
rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''
game=[rock,paper,scissors]
print("Rock,Paper,Scissors:")
print("Welcome")
print("0-Rock\n1-Papers\n2-Scissors\n")
ch=int(input("Enter your choice:"))
ra=random.randint(0,2)
#using multiple if ele:
if(ch>2):
    print("Invalid Input.YOU LOSE..!")
else:
    print(game[ch], "\n")
    print(game[ra], "\n")
    if(ch==ra):
        print("DRAW...!")
    elif(ch==0):
        if(ra==1):
            print("Computer Won.")
        else:
            print("You Won.")
    elif(ch==1):
        if(ra==2):

            print("Computer Won.")
        else:
            print("You Won")
    elif(ch==2):
        if(ra==0):
            print("Computer Won")
        else:
            print("You Won.")


#Another way

if(ch>2):
    print("Invalid input..You lose..!")
else:
    print(game[ch], "\n")
    print(game[ra], "\n")
    if(ch==ra):
        print("Draw")
    elif (ch==0 and ra==2):
        print("YOU WiN")
    elif(ch==1 and ra==0):
        print("You win")
    elif(ch==2 and ra==1):
        print("You Win")
    else:
        print("Computer Won")
