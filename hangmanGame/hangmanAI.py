#Ai bot for my hangman game
ai_entireWordList = []
ai_mistakeList = []
ai_remainingList = []

ai_onlyLetters_remainingList = []
ai_onlyLetters_indexList = []

newList = []

count = 0
confidence = 0
tnob = 0

def setTNOB(totalNumOfBlanks):
    global tnob
    tnob = totalNumOfBlanks

def updateAI(entireWordList, mistakeList, remainingList):
    global ai_entireWordList
    global ai_mistakeList
    global ai_remainingList

    ai_entireWordList = entireWordList
    ai_mistakeList = mistakeList
    ai_remainingList = remainingList

    addCharacterIndexes()
    removeMistakeWords()
    removeDuplicateWords()
    removeCharacterIndexes()
    calculateConfidence()

    #print("AI_entireWordList: " + str(ai_entireWordList))

def addCharacterIndexes():
    global ai_onlyLetters_remainingList
    global ai_onlyLetters_indexList
    global ai_remainingList

    ai_onlyLetters_remainingList.clear()
    ai_onlyLetters_indexList.clear()

    for i in range(len(ai_remainingList)):
        if ai_remainingList[i] != "_":
            ai_onlyLetters_remainingList.append(ai_remainingList[i])
            ai_onlyLetters_indexList.append(i)
    #print("ai_onlyLetters_remainingList: " + str(ai_onlyLetters_remainingList))
    #print("ai_onlyLetters_indexList: " + str(ai_onlyLetters_indexList))

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

def removeCharacterIndexes():
    global ai_onlyLetters_remainingList
    global ai_onlyLetters_indexList
    global ai_entireWordList
    global newList
    global count

    newList.clear()
    for word in ai_entireWordList:
        count = 0
        for x in range(len(word)):
            for remaining in range(len(ai_onlyLetters_remainingList)):
                if (word[x] == ai_onlyLetters_remainingList[remaining]) and (x == ai_onlyLetters_indexList[remaining]):
                    count += 1
        if count == len(ai_onlyLetters_remainingList):
            newList.append(word)

    for x in newList:
        if x.__len__() != tnob:
            newList.remove(x)
    print("newList: " + str(newList))

def calculateConfidence():
    global ai_entireWordList
    global ai_onlyLetters_remainingList
    global ai_onlyLetters_indexList
    global newList
    global confidence

    confidence = round(100 / len(newList), 2)
    print("Confidence: " + str(confidence) + "%")