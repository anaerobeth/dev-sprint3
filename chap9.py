# This is where the answers to Chapter 9 questions for the BSS Dev RampUp go
# Elizabeth Tenorio

#Ex. 9.1:
print "Ex. 9.1: Words longer than 20 characters"
fin = open('words.txt')
for line in fin:
    word = line.strip()
    if len(word) >= 20:
        print (word)


#Ex. 9.2:
print "Ex. 9.2: This function returns True if the given word does not have the letter 'e' in it"
def has_no_e(word):
    e_count = 0
    for letter in word:
        if letter == 'e':
            e_count = e_count + 1
#            print letter
#            print e_count
    if e_count == 0:
        return True
        #print word, ':', 'True'
    else: 
        return False
        #print word, ':', 'False'

print has_no_e('elephant')
print has_no_e('dog')

print "Words that have no 'e'"
e_word_count = 0
no_e_word_count = 0
fin = open('words.txt')
for line in fin:
    word = line.strip()
    if has_no_e(word):
        print (word)
        no_e_word_count = no_e_word_count + 1
    else:
        e_word_count = e_word_count + 1

print no_e_word_count, "words without 'e'"
print e_word_count, "total number of words"
per_e =  e_word_count * 100 / (no_e_word_count + e_word_count)
print "Percentage of words in the list without 'e':", per_e 

#Ex. 9.3:
print "Ex. 9.3: Returns True if the word does net use any forbidden letters"




#Ex. 9.4:



