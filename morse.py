dict = { 'a':'.-', 'b':'-...',
                    'c':'-.-.', 'd':'-..', 'e':'.',
                    'f':'..-.', 'g':'--.', 'h':'....',
                    'i':'..', 'j':'.---', 'k':'-.-',
                    'l':'.-..', 'm':'--', 'n':'-.',
                    'o':'---', 'p':'.--.', 'q':'--.-',
                    'r':'.-.', 's':'...', 't':'-',
                    'u':'..-', 'v':'...-', 'w':'.--',
                    'x':'-..-', 'y':'-.--', 'z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
a=int(input('press 1 to encrypt and 0 to decrypt'))
if(a==1):
    s=input('Enter the string: \n')
    s.lower()
    tostr=''
    for i in s:
        if i!=' ':
            tostr=tostr+dict[i]+' '
        else:
            tostr=tostr+' '
    print(tostr)
else:
    s=input('New letter is seperated by space and word by 2 spaces so enter the string like that: \n')
    tostr=''
    temp=''
    for i in s:
        if(i!=' '):
            j=0
            temp=temp+i
        else:
            j=j+1
            if j==2:
                tostr=tostr+' '
            else:
                tostr=tostr+list(dict.keys())[list(dict.values()).index(temp)]
                temp=''
    print(tostr)