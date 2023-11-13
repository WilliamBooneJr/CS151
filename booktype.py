#Create a data type Book with 4 instance variables _title, _author, _publisher and _copyright.
import stdio

class Book:
 
 def __init__(self, title, author, publisher, copyright):
     self._title = title
     self._author = author
     self._publisher = publisher
     self._copyright = copyright
 
 def __str__(self):
   return "Title: " + self._title + "\nAuthor: " + self._author + "\nPublisher: " + self._publisher + "\nCopyRight: " + self._copyright