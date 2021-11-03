import random

words = ["cat", "dog", "mouse", "bird", "snake", "lion", "tiger", "bear", "elephant", "monkey", "giraffe", "zebra", "cow", "pig", "sheep", "chicken", "duck", "goose", "horse", "penguin", "fish", "shark", "whale", "dolphin", "crocodile", "cobra", "frog", "turtle", "snail", "spider", "ant", "bee", "beetle", "butterfly", "caterpillar", "dragonfly", "ladybug", "mosquito", "panda", "penguin", "pig", "rabbit", "rhinoceros", "snail", "snake", "spider", "squirrel", "tiger", "turtle", "vulture", "wasp", "zebra"]
target_word = random.choice(words)
len = target_word.__len__()
guessed_letters = []

def main():
    print(target_word)
    mistakes = 0
    remaining = []

    for i in target_word:
        remaining.append("_")

    #add characters to guressed
    while (mistakes <= 5 and check_blanks(remaining)):
        #print each character in remaining
        print(" ")
        print(" ".join(remaining))
        print("Mistakes: " + str(mistakes))
        print("Mistakes: " + str(guessed_letters))
        #print("blanks? " + str(check_blanks(remaining)))

        guessed = get_input()
        lengthOfGuessed = guessed.__len__()

        #check if input is greater than 1
        if lengthOfGuessed > 1:
            print("Please enter only one character")
            continue
        else:
            if (guessed in guessed_letters) or (guessed in remaining):
                print("You already guessed that letter")
            else:
                if (target_word.__contains__(guessed)):
                    #find all instances of the guessed letter
                    for i in range(0, len):
                        if target_word[i] == guessed:
                            remaining[i] = guessed
                else:
                    mistakes += 1
                    guessed_letters.append(guessed)
                print("___________________________________" )
    
    
    if (not check_blanks(remaining)):
        print('''
        
        Great Job! You guessed the word: ''' + target_word + '''!
        
        ''')
    else:
        print('''
        
        Sorry, you lose!
        Your word was: ''' + target_word + '''
        ''')

#function to get user input
def get_input():
    guess = input("Guess a letter: ")
    return guess

#function to check if there is any blanks left
def check_blanks(remaining):
    for i in remaining:
        if i == "_":
            return True
    return False

main()