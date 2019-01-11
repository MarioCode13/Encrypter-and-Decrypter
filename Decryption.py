#Write down an alphabet
words = open('words.txt')
words = words.read()

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z']

message = input('write a message you want to decrypt: ')
message = message.lower()


for shift in range(1,26):
    d = {}
    cypherText = ''
    for i in range(0,26):
        letter = alphabet[i]
        shiftedLetter = alphabet[(i+shift)%26]
        d[letter] = shiftedLetter
        
    for letter in message:
        if letter in alphabet:
            letter = d[letter]
            cypherText = cypherText + letter
        else:
            cypherText = cypherText + letter

    cypherList = cypherText.split()
    score = 0
    for word in cypherList:
        if word in words:       #word exists in words.txt
            score=score+1
    if (score / len(cypherList)) > 0.5:
        print(cypherText)
        
