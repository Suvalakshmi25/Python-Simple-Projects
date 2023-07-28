import random
logo=""" _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       """
hangman = [ """ 
____
|/   |
|   
|    
|    
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|    
|    
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|    |
|    |    
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   \|
|    |
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   \|/
|    |
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   \|/
|    |
|   / 
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   \|/
|    |
|   / \
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   /|\
|    |
|   | |
|
|_____
"""]
print(logo)
lst=["executioner","headsman","murderer","executor","assassin"]
word=random.choice(lst)
g="_"*len(word)
gword=list(g)
print("GUESS THE WORD...!!")
print(g)
chance=7
i=0
count=len(word)
while(chance>0):
    if(count!=0):
        letter=input("Guess the letter:")
        if letter.lower() in word:
            gword[word.find(letter)]=letter.lower()
            count-=1
            print("GUESSED CORRECTLY.....!!HURRAY...!")
            for j in gword:
                print(j,end="")
            print()
        else:
            print("<<<<OOPS.....WRONG GUESS...!!>>>>>>>")
            chance-=1
            print(hangman[i])
            i+=1
            for j in gword:
                print(j,end="")
            print()
    else:
        print("<<<<<<<<<<<<HURRAYYYY....YOU WON THE GAME>>>>>>>>>>>>")
        break
else:
    print("<<<<<<<TRY AGAIN....!!...YOU LOST THE GAME...!!")
