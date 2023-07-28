import random
#easy level
print("PASSWORD GENERATOR..!")
alpha=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
       'N', 'O', 'P', 'Q', 'R', 'S','T', 'U', 'V', 'W', 'X', 'Y', 'Z',
       'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
       'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num=["0","1","2","3","4","5","6","7","8","9"]
sym=["!","@","#","$","%","^","&","*","(",")"]
p=int(input("Length of the password:"))
b=int(input("Number of digits:"))
c=int(input("Number of symbols:"))
a= p-b-c
pwd=""
#EASY LEVEL
for i in range(0,a):
    pwd+=random.choice(alpha)
for i in range(0,b):
    pwd += random.choice(num)
for i in range(0,c):
    pwd+=random.choice(sym)
print(f"You're Password:{pwd}")
#HARD LEVEL
pwd2=[]
for i in range(0,a):
    pwd2.append(random.choice(alpha))
for i in range(0,b):
    pwd2.append(random.choice(num))
for i in range(0,c):
    pwd2.append(random.choice(sym))
random.shuffle(pwd2)
for j in pwd2:
    print(j,end="")

