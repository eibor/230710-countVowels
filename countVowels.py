# simple program to count vowels in an input

while (True):
    myString = input("Please enter a line of text (or type \"end\"): ")

    myString = myString.lower()

    if (myString == "end"):
        print("Bye")
        exit()
    
    vowelCount = [0,0,0,0,0,0]
    for i in range(len(myString)):
        if (myString[i] == "a"):
            vowelCount[0] += 1
            vowelCount[5] += 1
        elif (myString[i] == "e"):
            vowelCount[1] += 1
            vowelCount[5] += 1
        elif (myString[i] == "i"):
            vowelCount[2] += 1
            vowelCount[5] += 1
        elif (myString[i] == "o"):
            vowelCount[3] += 1
            vowelCount[5] += 1
        elif (myString[i] == "u"):
            vowelCount[4] += 1
            vowelCount[5] += 1
    
    # print(vowelCount)
    print("The number of vowels included in your message was: " + str(vowelCount[5]))
    print("A: " + str(vowelCount[0]) + "  E: " + str(vowelCount[1]) + "  I: " + str(vowelCount[2]) + "  O: " + str(vowelCount[3]) + "  U: " + str(vowelCount[4]))
