#class Book:

    #def __init__(self):
      #  self.title = "Great Expectations"
      #  self.author = "Charles Dickens"

class Book:
    #First def gives class attributes
    def __init__(self, title, author, num_page, current_page):
        self.title = title 
        self.author = author
        self.num_page = num_page
        self.current_page = current_page
        self.bookmarked_page = 1
        
    #Second def 
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.num_page}, Current: {self.current_page}"
    
    def bookmark_page(self):
        self.bookmarked_page = self.current_page

    def turn_page(self, forward): 
        if forward:
            self.current_page = self.current_page + 1
        else:
            self.current_page = self.current_page - 1


#book1 = Book()
#print(book1)

book1 = Book("Great Expectations", "Charles Dickens", 340, 20)
print(book1.title)
print(book1.author)

book2 = Book("To Kill a Mockingbird", "Harper Lee", 293, 40)
print(book2.title)
print(book2.author)

print(book2)

print(book2.current_page)
book2.turn_page(True)
book2.turn_page(False)
book2.turn_page(True)
book2.turn_page(True)
book2.turn_page(True)
book2.turn_page(True)
print(book2.current_page)
book2.bookmark_page()
print(book2.bookmarked_page)