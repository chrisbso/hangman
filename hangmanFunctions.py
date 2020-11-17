from random import randint, seed
import os
def instanceGame(fileName: str = "", attempts: int = 5) -> None:
    '''
    Instances the Hangmang game.
        ARGS:
            fileName: Name of .txt-file containing the random words to guess.
        RETURNS:
            N/A
    '''

    guessingGame(getGuessWord(fileName),attempts)
            
#get the guess word
def getGuessWord(fileName: str) -> str:
    guessWord = "";
    try: #try to read the file, check that its not empty.
        numLines = sum(1 for line in open(fileName))
        if not numLines:
            raise #raise an error (idk what error to raise, wtf).
        lineNum = randint(1,numLines)
        i = 0
        with open(fileName) as f:
            for line in f:
                i = i + 1
                if i == lineNum:
                    if "\n" in line:
                        guessWord = line[:-1]
                    else:
                        guessWord = line                    
                    break;
    except:
        print("Error reading .txt-file.")
        while True:
            guessWord = input("No .txt-file found. Enter your desired guess word: ")
            yesNoInput = input("Is '" + guessWord.upper() + "' your desired guess word? [Y/N]: ")
            if guessWord:
                if yesNoInput.upper() == "Y":
                    break 
            else:
                print("Enter something valid.")
    return guessWord.upper()


def guessingGame(guessWord,attempts) -> None:
    os.system('cls')
    isGameOver = False
    guessedLetters = ""
    startAttempts = attempts
    print("\n","_ " * len(guessWord),"\n")
    while attempts and not isGameOver:
        print("You have " + str(attempts) + " attempt(s) left.\n\n\n")
        alreadyGuessed = True
        while alreadyGuessed: #check the output
            playerGuess = input("Input your guess letter: ")
            if len(playerGuess) != 1 or not playerGuess.isalpha():
                os.system('cls')
                getGameStatusAndPrint(guessedLetters, guessWord, attempts)
                print("... I said LETTER!\n\n\n")
                continue
            alreadyGuessed = False
            for letter in guessedLetters:
                if letter == playerGuess.upper():
                    alreadyGuessed = True
                    break
            if alreadyGuessed:
                os.system('cls')
                getGameStatusAndPrint(guessedLetters, guessWord, attempts)
                print("\n\nYou have already guessed the letter '" + playerGuess.upper() + "'.\n")
        guessedLetters = guessedLetters + playerGuess.upper()
        foundLetter = False
        for letter in guessWord: #if the player-guessed letter is in the guess word, we don't subtract attempts
            if playerGuess.upper() ==  letter:
                foundLetter = True
                break
                
        if not foundLetter: attempts = attempts - 1
        os.system('cls')
        isGameOver = getGameStatusAndPrint(guessedLetters, guessWord, attempts)
        if isGameOver:
            print("-"*80)
            if attempts < 1:
                print("\nYou ran out of attempts! Game over.\nThe word to guess was '" + guessWord+ "'.\n\n")
            else:
                print("\nYou guessed the word '" + guessWord + "' with " + str(attempts) + " out of " + str(startAttempts) + " attempts left!\n")
                print("Congratulations!\n")
            print("-"*80)
            os.system("pause")
            break

                  

def getGameStatusAndPrint(guessedLetters: str,guessWord: str,attempts: int) -> bool:
    if attempts < 1:
        return True
    correctlyGuessed = "_" * len(guessWord)
    toPrintIncorrGuessed = ""
    splitted = list(correctlyGuessed)
    for i,gLetter in enumerate(guessedLetters):
        foundLetter = False
        for j,wLetter in enumerate(guessWord):
            if gLetter == wLetter:
                foundLetter = True
                splitted[j] = gLetter
        if foundLetter is False:
            toPrintIncorrGuessed = toPrintIncorrGuessed + gLetter
    correctlyGuessed = ''.join(splitted)
    if correctlyGuessed == guessWord:
        return True
                
    splitted = list(" " * (2*len(correctlyGuessed)-1))
    for i in range(0,len(correctlyGuessed)):
        splitted[2*i] = correctlyGuessed[i]
    toPrintCorrGuessed = ''.join(splitted)
        
    
    print("\n",toPrintCorrGuessed,"\t Incorrect guesses: ", toPrintIncorrGuessed)
    print()
    
    return False
    
              
              
    