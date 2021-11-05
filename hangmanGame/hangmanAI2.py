#Ai bot for my hangman game
ai_entireWordList = []
ai_mistakeList = []
ai_remainingList = []

ai_onlyLetters_remainingList = []
ai_onlyLetters_indexList = []

def updateAI(entireWordList, mistakeList, remainingList):
    global ai_entireWordList
    global ai_mistakeList
    global ai_remainingList

    ai_entireWordList = entireWordList
    ai_mistakeList = mistakeList
    ai_remainingList = remainingList

    removeMistakeWords()
    removeDuplicateWords()

    print("AI_entireWordList: " + str(ai_entireWordList))

#make any words from entirewordlist that have letters in mistakeList equal to "_"
def removeMistakeWords():
    global ai_entireWordList
    global ai_mistakeList

    #for every individual character in ai_entireWordList remove the word if it has characters from ai_mistakeList
    for x in ai_entireWordList:
        for y in x:
            if y in ai_mistakeList:
                ai_entireWordList.remove(x)
                break

#remove any duplicate words from ai_entireWordList
def removeDuplicateWords():
    global ai_entireWordList
    for x in ai_entireWordList:
        if ai_entireWordList.count(x) > 1:
            ai_entireWordList.remove(x)
