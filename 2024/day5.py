from math import floor

from openData import getData

def checkValidPage(currentPage, orderingRules):
    for currentPageNumberIndex, currentPageNumber in enumerate(currentPage):
        #pageRules = [r for r in orderingRules if r[0] == currentPageNumber]
        pageRules = list(filter(lambda t: t[0] == currentPageNumber, orderingRules))
        while pageRules:
            currentRule = pageRules.pop()
            for pageNumberIndex, pageNumber in enumerate(currentPage):
                if pageNumber == currentPageNumber:
                    continue
                if currentRule[1] == pageNumber and pageNumberIndex < currentPageNumberIndex:
                    return False
    return True

def correctPageOrder(currentPage, orderingRules):

    for currentNumber in currentPage:
        pageRules = [r for r in orderingRules if r[0] == currentNumber]
        while pageRules:
            currentRule = pageRules.pop()
            if currentRule[1] in currentPage:
                ruleIndex = currentPage.index(currentRule[1])
                currentPageIndex = currentPage.index(currentRule[0])
                if currentPageIndex > ruleIndex:
                    currentPage.remove(currentRule[0])
                    currentPage.insert(ruleIndex, currentRule[0])

    return currentPage

if __name__ == "__main__":
    # input = getData("day5inputtest.txt")
    input = getData("day5Input.txt")
    orderinRules = []
    pages = []
    for item in input:
        if '|' in item:
            page, before = item.split('|')            
            orderinRules.append([int(page), int(before)])
        if ',' in item:
            page = [int(t) for t in item.split(',')]
            pages.append(page)

    finalSum = 0

    incorrectPages = []

    for currentPage in pages:        
        if checkValidPage(currentPage, orderinRules):
            middlePageIndex =  floor(len(currentPage) / 2)
            finalSum += currentPage[middlePageIndex]
        else:
            incorrectPages.append(currentPage)
    
    print("\n\rPart 1 result: ", finalSum)

    finalSum = 0

    for incorrectPage in incorrectPages:
        correctPage = correctPageOrder(incorrectPage, orderinRules)
        middlePageIndex = floor(len(correctPage) / 2)
        finalSum += correctPage[middlePageIndex]

    print("\n\rPart 2 result: ", finalSum)    
