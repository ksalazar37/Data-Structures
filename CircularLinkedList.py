class Link(object):
    def __init__(self, data= None, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


# create circular linked list in which the last link points to the first link again instead of null
# null pointer means an empty circular list
class CircularList(object):

    #constructor
    def __init__(self):
        self.first = None
       
       
    def __str__ (self):
        string = ""
        current = self.first

        # cont traversing until reach first link again
        while current.next != self.first:
            string += str(current.data) + "\n"
            current = current.next

        return string

    # insert data value in list
    def insert(self, data):
        # create new link object
        new_link = Link(data)
        current = self.first

        if current == None:
            # set link address to itself if there is no link
            self.first = new_link
            new_link.next = new_link
            return
        while current.next != self.first:
            current = current.next

        current.next = new_link
        new_link.next = self.first



    # find link with given value
    def find (self, data):
        current = self.first

        while current.data != data:
            current = current.next

        return current


    # delete link with given value
    def delete(self, data):
        current = self.first
        previous = self.first

        # if empty list
        if current == None:
            return None

        # while we have not yet finished circling the list
        while previous.next != self.first:
            previous = previous.next

        while current.data != data:
            previous = current
            current = current.next

        if self.first != self.first.next:
            # continue
            self.first = current.next
        else:
            self.first = None

        # delete link and so connect prev link to next link
        previous.next = current.next


    # return nth link starting from link start
    # return next link from the deleted link
    def delete_after (self, start, n):
        current = self.find(start)

        for i in range(1, n):
            current = current.next

        print(str(current.data), end = "\n")
        self.delete(current.data)
        return current.next
