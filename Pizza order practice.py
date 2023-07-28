print("Welcome to pizza delivery")
size=input("S OR M OR L:")
pep=input("Y OR N:")
che=input("Y or N:")
amount=0
if (size=="S"):
    amount+=15
elif(size=="M"):
    amount+=20
else:
    amount+=25
if(size=="S" and  pep=="Y"):
    amount+=2
else:
    amount+=3
if(che=="Y"):
    print("Amount:",amount+1)
else:
    print("Amount:",amount)