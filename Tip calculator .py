print("Welcome to tip calculator")
amt=float(input("Enter the bill amount:"))
p=float(input("Enter the percentage of tip:"))
no=int(input("Enter of people you want to split:"))
tip=(amt)*(p/100)
print(round((tip+amt)/no,2))
#using format
tip=(tip+amt)/no
print(":.2f".format(tip))

