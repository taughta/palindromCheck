print("Enter a word:")

try:
    theWord = input()
except Exception:
    raise

theWord = theWord.lower()

def isPalindrom(givenWord):
    palindromised = (givenWord[-1:((len(theWord)) * -1) -1:-1])
    print("The given word is:\n",givenWord)
    print("The mirror version of the world is\n", palindromised)
    if givenWord == palindromised:
        return "\n--> The word is a palindrome."
    else:
        return "\n--> The word is NOT a palindrome."

print(isPalindrom(theWord))
