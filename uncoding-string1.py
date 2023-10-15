message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ''
for ch in message :
    if   ch == ' ' :
        ch == ' '
        encoded_message = encoded_message + ch
    elif ch == '!' :
        ch == '!'
        encoded_message = encoded_message + ch
    elif ch == ch.upper() :
        ch = ord(ch) - ord("A")
        ch = (ch + offset) % 26
        ch = chr(ch + ord("A"))
        encoded_message = encoded_message + ch
    elif ch == ch.lower() :
        ch = ord(ch) - ord("a")
        ch = (ch + offset) % 26
        ch = chr(ch + ord("a"))
        encoded_message = encoded_message + ch
        
       
        
print(encoded_message)
    