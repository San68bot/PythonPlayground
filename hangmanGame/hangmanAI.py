#Ai bot for my hangman game

ai_entireWordList = []
ai_mistakeList = []
ai_remainingList = []

ai_onlyLetters_remainingList = []
ai_onlyLetters_indexList = []

def init(entireWordList, mistakeList, remainingList):
    for x in entireWordList:
        ai_entireWordList.append(x)
    for x in mistakeList:
        ai_mistakeList.append(x)
    for x in remainingList:
        ai_remainingList.append(x)


def updateList(mistakeList, remainingList):
    ai_mistakeList.clear()
    for x in mistakeList:
        ai_mistakeList.append(x)

    ai_remainingList = remainingList

    ai_onlyLetters_remainingList.clear()
    ai_onlyLetters_indexList.clear()

    #add any non blank characters to the list
    for i in range(len(ai_remainingList)):
        if ai_remainingList[i] != "_":
            ai_onlyLetters_remainingList.append(ai_remainingList[i])
            ai_onlyLetters_indexList.append(i)

def updateAI():
    #remove any words from ai_entireWordList with characters that are in ai_mistakeList
    for x in ai_entireWordList:
        for y in ai_mistakeList:
            if y in x:
                ai_entireWordList[ai_entireWordList.index(x)] = ""
    #remove any blank characters from ai_entireWordList
    while "" in ai_entireWordList:
        ai_entireWordList.remove("")

    #remove any duplicate words from ai_entireWordList
    for x in ai_entireWordList:
        if ai_entireWordList.count(x) > 1:
            ai_entireWordList.remove(x)
    print("ai_entireWordList: ", ai_entireWordList)