# write down alphabet
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
          'r','s','t','u','v','w','x','y','z']

message = input('Message to encrypt: ')
message = message.lower()               #to also encrypt CAPS
shift = input('Number of shifts? ')
shift = int(shift)

d = {}
cypherText = ''

for i in range(0,26):
    letter = alphabet[i]     #goes through the alphabet
    shiftedLetter = alphabet[(i+shift)%26]
    d[letter] =shiftedLetter

for letter in message:
    if letter in alphabet:          #letters in alphabet shift
        letter = d[letter]
        cypherText = cypherText + letter
    else:
        cypherText = cypherText + letter    #letters not in alphabet stay the same

        
print(cypherText)
