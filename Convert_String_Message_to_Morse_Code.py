

#This programme converts a string message to morse code

alphabet ="abcdefghijklmnopqrstuvwxyz"
print(len(alphabet))

morse_code={'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.',\
            'f':'..-.','g':'--.','h':'....','i':'..','j':'.---',\
            'k':'-.-','l':'.-..','m':'--','n':'-.','o':'---',\
            'p':'.--','q':'--.-','r':'.-.','s':'...','t':'-',\
            'u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--',\
            'z':'--..'}


message= input("Enter a string message: ")
# Converts message to Lowercase
message=message.lower()
print(message)

encoded_message=""
#Iterate over the letters of the message
for char in message:
    if char ==" ":
    # If the character is a space add '/' to the encoded message
        encoded_message +='/'  
    #Otherwise, if the character is a letter, replace it with 
    #its morse code represantation
    elif char in alphabet:
        encoded_message +=morse_code[char]+' '

print(encoded_message)

