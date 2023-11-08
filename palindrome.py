import stdio
import sys

word = sys.argv[1]

def removespcs(string):
    return string.replace(" ", "")


if word == word[::-1]:
        if word.isalnum():
              stdio.writeln(word + ' is a palindrome')
else:
      
      word2 = removespcs(word)
      if word2.lower() == word2[::-1].lower():
            stdio.writeln(word + ' is an inexact palindrome')
      else:
            stdio.writeln(word + ' is not a palindrome')

      
    

       
       