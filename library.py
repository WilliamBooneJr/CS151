#Create a client called library.py. 
#Create an InStream object with the file name specified as a command-line argument. 
#(The file books.txt  is provided for you as an example of a file to read in.) 
#Read in the file creating instances of Books and adding them to a library. 
#Write to standard output the number of books in the library. 
#Using a for loop, print each book.

import stdio
import sys
from instream import InStream
from booktype import Book


def main():
    inputstream = InStream(sys.argv[1])
    library = []
    while inputstream.hasNextLine():
        title = inputstream.readLine()
        author = inputstream.readLine()
        publisher = inputstream.readLine()
        copyright = inputstream.readLine()
        book = Book(title, author, publisher, copyright)
        library.append(book)
    
    stdio.writeln(len(library))
    for book in library:
        stdio.writeln(book.__str__())
        


if __name__ == '__main__':
    main()
