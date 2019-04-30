# Linked List data structure

class Link(object):
    def __init__(self, data= None, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList(object):

    def __init__(self):
        self.first = None

    # get number of links in linked list
    def get_num_links(self):
        current = self.first

        if (current == None):
            return 0

        # initialize count
        count = 1

        while (current.next != None):
            current = current.next
            # increment the count
            count += 1

        return count


    # add a data item at the beginning of the list
    def insert_first(self, data):
        new_link = Link(data)

        new_link.next = self.first
        self.first = new_link


    # add a data item at the end of a list
    def insert_last(self, data):
        new_link = Link(data)

        current = self.first
        if current == None:
            self.first = new_link
            return

        while current.next != None:
            current = current.next

        current.next = new_link


    # add an item in an ordered list in ascending order
    def insert_in_order(self, data):
        new_link = Link(data)

        current = self.first
        previous = self.first

        if (current == None) or (current.data >= data):
            new_link.next = self.first
            self.first = new_link
            return

        while (current.next != None):
            if (current.data <= data):
                previous = current
                current = current.next

            else:
                new_link.next = previous.next
                previous.next = new_link
                return


        if (current.data <= data):
            current.next = new_link

        else:
            new_link.next = previous.next
            previous.next = new_link

        return





    # search in an unordered list, return None if not found
    def find_unordered(self, data):
        current = self.first

        if (current == None):
            return None

        while (data != current.data):
            if (current.next == None):
                return None
            else:
                current = current.next

        return current


    # Search in an ordered list, return None if not found
    def find_ordered(self, data):
        current = self.first

        if (current == None):
            return None

        while (current.data != None):
            if (current.next == None):
                return None
            else:
                current = current.next

        return current


    # Delete and return Link from an unordered list, or None if link not found
    def delete_link(self, data):
        previous = self.first
        current = self.first

        if current == None:
            return None

        while current.data != data:
            if current.next == None:
                return None
            else:
                previous = current
                current = current.next

        if current == self.first:
            self.first = self.first.next
        else:
            previous.next = current.next
        return current


    # String representation of data (10 items to a line, 2 spaces between data)
    def __str__(self):
        string = ""
        current = self.first

        items = 0

        while (current != None):
            # add 2 spaces between each data item
            string += str(current.data) + "  "
            current  = current.next

            # increment by 1 number of items
            items += 1

            # once item number reaches 10, start new line
            if items == 10:
                string += "\n"
                # init new number of items for new line
                items = 0

        return string[0:-2]


    # Copy the data in a list and return new list
    def copy_list(self):
        new_list = LinkedList()
        current = self.first

        # beginning copying from end
        while (current != None):
            new_list.insert_last(current.data)
            current = current.next

        return new_list


    # Reverse the contents of a list and return new list
    def reverse_list(self):
        reversed_list = LinkedList()
        current = self.first

        # begin adding data from start of list
        while (current != None):
            reversed_list.insert_first(current.data)
            current = current.next

        return reversed_list


    # Sort the contents of a list in ascending order and return new list
    def sort_list(self):
        sorted_list = LinkedList()
        current = self.first

        while (current != None):
            # add to list in sorted, ascending order
            sorted_list.insert_in_order(current.data)

            if current.next != None:
                current = current.next

            # break when current.next is None
            else:
                break

        return sorted_list



    # Return True if a list is sorted in ascending order 
    def is_sorted(self):
        new_list = LinkedList()
        current = self.first

        while current.next != None:
            # check is list is sorted
            # check current with next data

            # if sorted, then cont
            if current.data <= current.next.data:
                current = current.next

            # if not in ascending, break, False
            else:
                return False

        # finished traversing the list and is indeed sorted
        return True



    # Return True if a list is empty
    def is_empty(self):
        if self.first == None:
            return True

        else:
            return False


    # Merge two sorted lists and return new list in ascending order
    def merge_list(self, other):
        if self.is_empty() == True:
            return other
        elif other.is_empty() == True:
            return self


        merged_list = LinkedList()
        s_list = self.first
        o_list = other.first

        # as long as both are still being traversed
        while (s_list != None) and (o_list != None):
            if s_list.data <= o_list.data:
                merged_list.insert_last(s_list.data)
                s_list = s_list.next

            else:
                merged_list.insert_last(o_list.next)
                o_list = o_list.next

        # sort self list
        if s_list == None:
            while (o_list != None):
                merged_list.insert_last(o_list.data)

                if (o_list.next == None):
                    break

                else:
                    # see next link
                    o_list = o_list.next

        # sort other list
        if o_list == None:
            while (s_list != None):
                merged_list.insert_last(s_list.data)

                if s_list.next == None:
                    break

                else:
                    s_list = s_list.next
        string = ""

        current = merged_list.first

        while (merged_list != None):
            string += str(current.data) + "  "
            if current.next == None:
                break
            else:
                current = current.next

        return string[0:-2]



    # Test if two lists are equal, item by item 
    def is_equal(self, other):
        s_list = self.first
        o_list= other.first

        if (s_list == None) and (o_list == None):
            return True
        elif (s_list == None) or (o_list != None):
            return False

        else:
            # traverse lists
            while (s_list != None) and (o_list != None):
                if s_list.data == o_list.data:
                    s_list = s_list.next
                    o_list = o_list.next
                elif s_list.data != o_list.data:
                    return False
                else:
                    s_list = s_list.next
                    o_list = o_list.next

            if (s_list.next != None) or (o_list.next != None):
                return False
            elif (s_list.data != o_list.data):
                return False
            else:
                return True




    # Return a new list, keeping only the first occurrence of an element
    # and removing all duplicates. Do not change the order of the elements.
    def remove_duplicates(self):
        new_list = LinkedList()
        current = self.first

        # traverse through a list and keep track of all values in this new list
        no_duplicates = []

        # check if value in link matches value in list
        # if so - go to next link
        # if not - create new link with that value and append to
        # new linked list, then add value to list

        while current != None:
            # value exists ?
            if current.data in no_duplicates:
                pass
            else:
                # if not, create new link
                no_duplicates.append(current.data)
                # add to old
                new_list.insert_last(current.data)

            current = current.next

        return new_list
