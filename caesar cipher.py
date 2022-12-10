m = int(input('enter to encrypt or decrypt 0 or 1: '))
if m==1:
    plaintext = input("Enter the plaintext:")
    key = int(input("Enter the key:"))
    key = 26 - key
    encryption_str = ''
    for i in plaintext:
        if i.isupper():
            temp = 65 + ((ord(i) - 65 + key) % 26)
            encryption_str = encryption_str + chr(temp)
        elif i.islower():
            temp = 97 + ((ord(i) - 97 + key) % 26)
            encryption_str = encryption_str + chr(temp)
        else:
            encryption_str = encryption_str + i

    print("The ciphertext is:", encryption_str)

elif m==0:
    text = input("enter plain text: ")
    decryp_key = int(input('enter key: '))
    decryption_str = ''
    for l in text:
        if l.isupper():
            temp = 65 + ((ord(l) - 65 + decryp_key) % 26)
            decryption_str = decryption_str + chr(temp)
        elif l.islower():
            temp = 97 + ((ord(l) - 97 + decryp_key) % 26)
            decryption_str = decryption_str + chr(temp)
        else:
            decryption_str = decryption_str + l

    print("The ciphertext is:", decryption_str)
input('press enter to close')