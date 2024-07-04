# Vishwakarma

defaultParagraph = "The city buzzed with an energy that was palpable, palpable in the crowded streets and bustling cafes. Cafes where people gathered, gathered to savor their moments of connection and solitude alike. Alike, they sought refuge from the demands of everyday life, life that seemed both hectic and strangely beautiful. Beautiful in its contrasts, contrasts of light and shadow playing on the architecture that soared above. Above all, the city pulsed with a heartbeat that echoed through its streets, streets where stories unfolded and dreams took flight."
gap = "\033[91m" + "-------------------------------" + "\033[0m"


print(gap)
print("Program loaded successfully")
print(gap)


way = input("Do you have your own paragraph? '1' to use your own, or '0' to use the default: ")

while way != "0" and way != "1":
    print(gap)
    way = input("Either write '1' to use your own paragraph or '0' to use the Defaut paragraph: ")

print(gap)


if way == "0":
    useDefault = True
    print("You will be using the DEFAULT paragraph")
else:
    useDefault = False
    inputParagraph = input("Paste or write your text/paragraph: ")


print(gap)
if useDefault:
    print("---- Here is the default paragraph ---- \n" + defaultParagraph)
else:
    print("---- Here is the paragraph that will be used ---- \n" + inputParagraph)
print(gap)

inputWordToFind = input("What word would you like to find in this paragraph? ")
inputWordToFindSmallCase = inputWordToFind.lower()
print(gap)


if useDefault:
    finder = defaultParagraph.find(inputWordToFindSmallCase)
else:
    finder = inputParagraph.find(inputWordToFindSmallCase)

if finder != "-1":
    print("The word was found")
    print(gap)
    

    replaceConfirmation = input("Do you want to replace this word with something else? YES = '1'   NO = '0': ")
    print(gap)

    while replaceConfirmation != "0" and replaceConfirmation != "1":
        replaceConfirmation = input("Incorrect input. '1' to replace or '0' to skip: ")
        print(gap)
    
    if replaceConfirmation == "1":

        inputWordToReplace = input("Enter the word to replace it with: ")

        if useDefault:
            modifiedParagraph = defaultParagraph.replace(inputWordToFind, inputWordToReplace)
        else:
            modifiedParagraph = inputParagraph.replace(inputWordToFind, inputWordToReplace)
        print(gap)
        print("Paragraph after replacement:")
        print(modifiedParagraph)

elif finder == "-1":

    while finder == "-1":
        inputWordToFind = input("That word was not found in the paragraph. Try another word: ")
        if useDefault:
            finder = defaultParagraph.find(inputWordToFindSmallCase)
        else:
            finder = inputParagraph.find(inputWordToFindSmallCase)
        print(gap)

print(gap)
