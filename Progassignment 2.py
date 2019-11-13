def getGuessedWord(secretWord, lettersGuessed):
     count = 0
    for i, c in enumerate(secretWord):
    	if c in lettersGuessed:
    		count += 1
    if count == len(secretWord):
    	return True
    else:
    	return False