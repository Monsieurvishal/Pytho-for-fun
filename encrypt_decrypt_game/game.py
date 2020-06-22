import random
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS = LETTERS.lower()


def encrypt(message, key):
    ''' This function lets you to encrypt your message based on a key '''
    encrypted = ''
    for chars in message:
        if chars in LETTERS:
            num = LETTERS.find(chars)
            num += key
            if num>25:
                num=num%25
                num=num-1
            encrypted =encrypted + LETTERS[num]

    return encrypted

def decrypt(message, key):
    ''' This function lets you to decrypt your message based on a key '''
    decrypted = ''
    for chars in message:
        if chars in LETTERS:
            num = LETTERS.find(chars)
            if num>25:
                num=num%25
                num=num-1
            num = num -key
            decrypted =decrypted+LETTERS[num]

    return decrypted

def main():
    
 
    message1 = str(input('Enter your message: '))
    key = random.randint(1, 26)
    print(encrypt(message1, key))
    encrypted_message=encrypt(message1, key)
    
    while True:
        key_user = int(input('Enter key to decrypt '))
        user_decrypt=decrypt(encrypted_message, key_user)
        if message1==user_decrypt:
            print("Won!!")
            break
        else:
            key_user = print('Try agin!')
                
                
            
            

if __name__ == '__main__':
    main()
    
"""
output:

Enter your message: v
x
Enter key to decrypt 2
Won!!

"""
