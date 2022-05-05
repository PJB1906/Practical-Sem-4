def encrypted(ptext,key):
    cipher=''
    for char in ptext:
        if char==' ':
            cipher=cipher+char
        elif char.isupper():
            cipher=cipher+chr((ord(char)+key-65)%26+65)
        else:
            cipher=cipher+chr((ord(char)+key-97)%26+97)
    return cipher


def decryption(ctext,key):
    ptext=''
    for char in ctext:
        if char==' ':
            ptext=ptext+char
        elif char.isupper():
            ptext=ptext+chr((ord(char)-key-65)%26+65)
        else:
            ptext=ptext+chr((ord(char)-key-97)%26+97)
    return ptext

ctext=input("Enter the cipher text: ")
key=int(input("Enter the key: "))
print("The decrypted message is: ",decryption(ctext,key))
