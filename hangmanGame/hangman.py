import random
from hangmanAI import *

#list of random animals
words = ["cat", "dog", "mouse", "bird", "snake", "lion", "tiger", "bear", "elephant", "monkey", 
        "giraffe", "zebra", "cow", "pig", "sheep", "chicken", "duck", "goose", "horse", "penguin", 
        "fish", "shark", "whale", "dolphin", "crocodile", "cobra", "frog", "turtle", "snail", "spider", 
        "ant", "bee", "beetle", "butterfly", "caterpillar", "dragonfly", "ladybug", "mosquito", "panda", 
        "penguin", "pig", "rabbit", "rhinoceros", "snail", "snake", "spider", "squirrel", "turtle", 
        "vulture", "wasp", "zebra", "ape", "sloth", "toad", "baboon", "bat", "beaver", "buffalo", "camel", 
        "cheetah", "chimpanzee", "cougar", "coyote", "deer", "eagle", "falcon", "giraffe", "raindeer", "worthog", 
        "yak", "gazelle", "hyena", "jackal", "jaguar", "kangaroo", "leopard", "lynx", "mandrill", "mink"]

target_word = random.choice(words)
len = target_word.__len__()
guessed_letters = []
ai_active = False
giveup = False

def removeDuplicateWordsInWordList():
    tempwords = []
    for i in words:
        if i not in tempwords:
            tempwords.append(i)
        else:
            tempwords.remove(i)

def main():
    giveup = False
    ai_active = False
    ##print(target_word)
    mistakes = 0
    remaining = []

    removeDuplicateWordsInWordList()
    target_word = random.choice(words)
    len = target_word.__len__()

    for i in target_word:
        remaining.append("_")

    count = 0
    for i in remaining:
        if i == "_":
            count += 1

    setTNOB(count)

    #add characters to guressed
    while ((mistakes <= 5 and check_blanks(remaining)) and (not giveup)):
        #print each character in remaining
        print(" ")
        print(" ".join(remaining))
        print("Mistakes: " + str(mistakes))
        print("Your incorrect guesses: " + str(guessed_letters))

        userGuess = input("Guess a letter: ")
        lengthOfGuessed = userGuess.__len__()

        if userGuess == "giveup":
            giveup = True

        if userGuess == "/s":
            ai_active = True
            userGuess = input("Guess a letter: ")
            lengthOfGuessed = userGuess.__len__()

        #check if input is greater than 1
        if (lengthOfGuessed > 1) and (not giveup):
            print("Please enter only one character")
            continue
        else:
            if (userGuess in guessed_letters) or (userGuess in remaining):
                print("You already guessed that letter")
            else:
                if (target_word.__contains__(userGuess)):
                    #find all instances of the guessed letter
                    for i in range(0, len):
                        if target_word[i] == userGuess:
                            remaining[i] = userGuess
                else:
                    mistakes += 1
                    guessed_letters.append(userGuess)

                #AI code
                if ai_active:
                    updateAI(words, guessed_letters, remaining)
                print("___________________________________" )
    
    
    if (not check_blanks(remaining)):
        print('''
        
        Great Job! You guessed the word (''' + target_word + ''') correctly with ''' + str(mistakes) + ''' mistakes!
        
        ''')
    else:
        print('''
        
        Sorry, you lose!
        Your word was: ''' + target_word + '''
        
        ''')

#function to check if there is any blanks left
def check_blanks(remaining):
    for i in remaining:
        if i == "_":
            return True
    return False

main()