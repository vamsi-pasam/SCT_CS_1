letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encryption(normal_text,shiftpos):
    cipher_text=""
    for x in normal_text:
        pos=letters.index(x)
        newpos=(pos+shiftpos)%26
        cipher_text+=letters[newpos]
    print(cipher_text)
def decryption(encrypted_text,shiftpos):
    original_text=""
    for x in encrypted_text:
        pos=letters.index(x)
        newpos=(pos-shiftpos)%26
        original_text+=letters[newpos]
    print(original_text)
flag=False
while(not flag):
    what_action_you_do=input("choose either encrypt or decrypt\n")
    text=input("enter your text\n")
    shift=int(input("enter the shift position\n"))
    if what_action_you_do=="encrypt":
        encryption(normal_text=text,shiftpos=shift)
    elif what_action_you_do=="decrypt":
        decryption(encrypted_text=text,shiftpos=shift)
    again=input("do you want to continue enter 'yes' or 'no'\n")
    if again=="no":
        flag=True
        print("task ended")
        
