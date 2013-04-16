# This is where the answers to Chapter 8 questions for the BSS Dev RampUp go
# Name: Elizabeth Tenorio

"""
A program to encrypt a message in ROT13 by shifting a letter tthrough the alphabet 
"""

#ord('a') => 97
#ord('z') => 122
#ord('A') = > 65
#ord('Z') = > 90
#chr(97) => 'a'
#key = 5 
#message = 'Python'

#key is the number of places the letters of the message should be moved during encryption

def rotate_word(message, key):
    new_message = ''
    s = message.lower()
    for letter in s:
        new_ord = key + ord(letter) 
        if new_ord > 122:
            #lowerrcase letters can have ord from 65 to 90
            new_ord = new_ord -26
            new_letter = chr(new_ord)
        else:
            new_letter = chr(new_ord)
            
        new_message = new_message + new_letter
    print new_message.lower()

rotate_word('xyz', 1 )
rotate_word('xyz', 10 )
rotate_word('PYTHON', 13)
