import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_sum,computer_sum):
    if user_sum==computer_sum:
        return "Draw😑"
    elif computer_sum==0:
        return "Lose,oppenent has Blackjack."
    elif user_sum==0:
        return "Win with a Blackjack."
    elif user_sum>21:
        return "You went over.You lose."
    elif computer_sum>21:
        return "Oppenent went over.You win."
    elif user_sum>computer_sum:
        return "You Win."
    else:
        return "You lose."
def game():

    user_card=[]
    computer_card=[]
    end_of_game=False
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())



    while not end_of_game:
        user_sum=calculate_score(user_card)
        computer_sum=calculate_score(computer_card)
        print(f"Your cards:{user_card},current score:{user_sum}")
        print(f"Computers first card:{computer_card[0]}")

        if user_sum==0 or computer_sum==0 or user_sum>21:
            end_of_game=True
        else:
            user_should_deal=input("Type 'y' to get another card,type 'n' to pass:")
            if user_should_deal=="y":
                user_card.append(deal_card())
            else:
                end_of_game=True

    while computer_sum!=0 and computer_sum<17:
        computer_card.append(deal_card())
        computer_sum=calculate_score(computer_card)
    print(f"YOUR FINAL HAND:{user_card}, FINAL SCORE :{user_sum}")
    print(f"COMPUTER;S FINAL HAND:{computer_card},FINAL SCORE:{computer_sum}")
    print(compare(user_sum,computer_sum))
while input("DO YOU WANNA PLAY......?TYPE(Y/N):")=="y":
    game()


