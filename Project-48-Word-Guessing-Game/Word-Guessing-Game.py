from random import randint
words = ["apple","mango","computer","mouse","person","friend","father","mother","sister","brother","daughter","sibling","parents","guardian","neighbour"]
word = words[randint(0,len(words))]
guess = ["*"] * len(word)
wrong = []
attempts=6
print("word is {} its length is {}".format("".join(guess),len(guess)))
while(attempts and guess.count('*')>0):
    print("You've {} attempts left".format(attempts))
    char = input("Enter a char: ")
    char=char[0]
    if char in word:
        print("correct..")
        index = word.index(char)
        guess[index] = word[index]
    else:
        if char not in wrong:
            attempts-=1
            wrong.append(char)
        print("Previous guess: {}".format(''.join(wrong)))
        print("try again...")
        
    print("word is {}".format("".join(guess)))
if attempts==0:
    print("Sorry! You lost the game.")
    print("The word was {}".format(word))
else:
    print("Congratulations! you got the word")
