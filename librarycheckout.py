# Create default value for number of patrons and media in locations
totalbooks = 0
totalbookout = 0
totalvideo = 0
totalvidout = 0
totalpatrons = 0


class Patrons:  # Class to initialize a member with name
    def __init__(self, name=""):
        global totalpatrons
        totalpatrons += 1
        self.name = name
        self.borrowedItems = list()

    # Create media return method
    def checkIn(self, item):

        if item not in self.borrowedItems:  # Checks to see if item is taken or not
            print("Invalid. " + self.name + " did not checked out " + item.title + ".")
        else:  # Patron returns item
            item.available = True
            self.borrowedItems.remove(item)
            print(self.name + " has returned " + item.title + ".")

            if item.type == "book":  # Checks in book
                global totalbookout
                totalbookout -= 1
            elif item.type == "video":  # Checks in video
                global totalvidout
                totalvidout -= 1

    # create media checkout method
    def checkOut(self, item):

        if len(self.borrowedItems) == 2:  # Limits patron to only 2 items checked
            print(self.name + "is no longer able to check out items. Limit of 2 reached.")
        elif not item.available:  # Checks if item is available
            print(item.title + " is not available.")
        else:

            item.available = False  # Displays the patron name and what they checked out
            self.borrowedItems.append(item)
            print(self.name + " has checked out " + item.title + ".")

            if item.type == "book":  # Checks out book
                global totalbookout
                totalbookout += 1
            elif item.type == "video":  # Checks out video
                global totalvidout
                totalvidout += 1

    def displayitems(self):  # Displays a receipt of all items
        if self.borrowedItems:
            print("")
            print("[Patron receipt]")
            print(self.name + " checked out :")
            for item in self.borrowedItems:
                print("-" + item.title + " (" + item.type + ")")
        else:
            print("")
            print("[Patron receipt]")
            print(self.name + " has no checked out media.")


class Media:  # Super class to set title, author and publisher
    title = ""
    author = ""
    publisher = ""
    booklength = ""
    available = True
    type = None

    # Superclass attributes for all forms of media
    def addTitle(self, title):
        self.title = title

    def addAuthor(self, author):
        self.author = author

    def addPublisher(self, publisher):
        self.publisher = publisher


class Book(Media):  # inherit from media
    def __init__(self, title=""):
        global totalbooks
        totalbooks += 1  # creates counter for totalbooks increasing by 1

        self.title = title
        self.booklength = ""
        self.type = "book"

    # Book exclusive attribute of page length
    def pages(self, booklength):
        self.booklength = booklength

    # Force print book object details
    def __repr__(self):  # __repr__ for book info
        return "\nTitle: {}\nAuthor: {}\nPublisher: {}\nPages: {}\n{}\n".format \
            (self.title, self.author, self.publisher, self.booklength, '-' * 30)


class Video(Media):
    def __init__(self, title=""):
        global totalvideo
        totalvideo += 1

        self.title = title
        self.vidlength = ""
        self.type = "video"

    # Video exclusive attribute of minutes long
    def minutes(self, vidlength):
        self.vidlength = vidlength

    # Force print video object details
    def __repr__(self):
        return "\nTitle: {}\nAuthor: {}\nPublisher: {}\nLenth: {}\n{}\n".format \
            (self.title, self.author, self.publisher, self.vidlength, '-' * 30)


# Print receipt of transactions at the end of the day
def librarystatus():
    print("")
    print("************************************************\nRecord of library:")
    print("")
    print("Total number of books: " + str(totalbooks))
    print("Number of books checked out: " + str(totalbookout))
    print("Total number of videos: " + str(totalvideo))
    print("Number of video checked out: " + str(totalvidout))
    print("Total number of members: " + str(totalpatrons))
    print("************************************************")
    print("")


##TESTING
sanchez = Patrons("Chris Sanchez")
kim = Patrons("Patrick Kim")
james = Patrons("James C")
sanchez.displayitems()
kim.displayitems()

book1 = Book("ABC")
book2 = Book("Hello world!")
book1.addAuthor("James")
book2.addAuthor("John")
book2.addPublisher('XYZ Books')
book2.pages(100)

vid1 = Video("Python is fun")
vid1.addAuthor("Sara")
vid1.minutes("30 mins")

print(book1)
print(book2)
print(vid1)

sanchez.checkOut(book1)
sanchez.checkOut(book2)
kim.checkOut(vid1)
sanchez.checkIn(book1)
kim.checkOut(book1)
sanchez.checkIn(book2)
kim.checkOut(book2)

sanchez.displayitems()
kim.displayitems()

librarystatus()