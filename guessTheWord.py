# The purpose of this program is to prompt the user for the word.
# If word is in "romeo.txt", then the user will win, and the amount of times that certain word shows up, will be amount of points that they recieve.
from base64 import decode
import urllib.request
import urllib.error
import urllib.parse

fhandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# I will split the each line in the file handle and add them to the list "empty" so every content of the file is in one big list.
empty = []
# The dictionary's keyword will be the user's answer, and the amount of time it shows up in the file, "romeeo.txt".
count = dict()
# In addition the dictinary making a count of the user's answer, counter will do the same; but it will be used in a different print statement(line 30).
counter = 0
# This is where I prompt the user for a word.
guessTheWord = input("\nGuess the correct word, in order to get a cookie.\n")

for lines in fhandle:
    words = lines.decode().split()
    for word in words:
        # This is what I was talking about in line 9-10.
        empty.append(word)

if guessTheWord in empty:
    for word in empty:
        if guessTheWord == word:
            counter += 1
            count[word] = count.get(word, 0) + 1
    print(count, "\n")
    print("You won.\nTotal points:", counter)
else:
    print("\n")
    print("You lost.\n")
