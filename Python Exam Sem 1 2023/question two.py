# i

class Book:

    def __init__(self, title, author, pages):


       self.title = title
       self.author = author
       self.pages = pages

author_one = Book('Greys Anatomy', 'Dwayne', '5000')
print(author_one.title)
print(author_one.author)
print(author_one.pages)
     

# ii

class Ebook(Book):
    def  __init__(self, title, author, pages, format):
        super().__init__(title,author,pages, format)

        self.format = format


author_one = (Book, 'PDF Format')

print(format)



# iii

print(author_one.title, author_one.author )


# iv 

# a
# Classes are a segment of a function that contains attributes of the function.

# b
# Objects are instances modified from the class.  

