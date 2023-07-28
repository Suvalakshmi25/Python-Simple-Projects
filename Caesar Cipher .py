letter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction=input("Type 'encode' to encrypt,type 'decode' to decrypt:\n")
text=input("Type your message:\n").lower()
shift=int(input("Type the shift number:\n"))
#ENCODE
def encrypt(input_txt,shift_amt):
    s=""
    for le in input_txt:
        pos=letter.index(le)
        newpos=pos+shift_amt
        """
        if newpos>25:
            newpos=shift_amt-(26-pos)
            s+=letter[-(26-newpos)]
        else:
            s += letter[newpos]
            """
        s += letter[newpos]
    print(s)
#DECODE
def decrypt(input_txt,shift_amt):
    s=""
    for le in input_txt:
        pos=letter.index(le)
        newpos=pos-shift_amt
        s+=letter[newpos]
    print(s)

#MAIN
if direction=="encode":
    encrypt(text,shift)
elif direction=="decode":
    decrypt(text,shift)
else:
    print("Invalid")