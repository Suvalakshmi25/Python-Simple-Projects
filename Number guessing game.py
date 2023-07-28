import random
logo="""

  _   _                 _                      _____                      
 | \ | |               | |                   / ____|                     
 |  \| |_   _ _ __ ___ | |__   ___ _ __     |  __ _   _  ___  ___ ___  
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|    | | |_ | | | |/ _ \/ __/ __| 
 | |\  | |_| | | | | | | |_) |  __/ |       | |__| | |_| |  __/\__ \__ \ 
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|        \_____|\__,_|\___||___/___/ 
                                                                      
                                                                      

"""
print(logo)
print("Welcome to 'GUESS NUMBER...!\nI'am thinking of a number between 1 and 100..!")
level=input("Choose Difficulty:Type 'easy' or 'hard':")
if level=="easy":
    no_of_attempts = 10
else:
    no_of_attempts = 5
computer_guess=random.randint(1,100)
def guess_number():
    guess_no= int(input("Make a guess:"))
    return guess_no
while(no_of_attempts>0):
    print(f'You have {no_of_attempts} remaining attempts..!')
    guess_user=guess_number()
    if guess_user==computer_guess:
        print("YOU WIN...!")
        print(f"GOT ROGHT...!Number was {computer_guess}")
        break
    elif guess_user>computer_guess:
        print("Too High..!\nGuess again..!")
    else:
        print("Too Low...!\nGuess again...!")
    no_of_attempts-=1
else:
    print("Attempts Over...!")



