class Link(object):
	# Constructor
	def __init__ (self, data, next = None):
		self.data = data
		self.next = next


class CircularList(object):
	# Constructor
	def __init__ (self): 
		self.first = None
  
  
	# Return a string representation of the Circular List
	def __str__ (self):
		st = ""
		current = self.first

		# traverse until we reach the starting link
		while (current.next != self.first):
			s += str(current.data) + " "
			current = current.next

		# when current.next == self.first, return the string
		return st
    
    
	# Insert an element in the list
	def insert (self, item):
		# create a new Link object
		newLink = Link(item)
		# set its address
		current = self.first

		# there is no link
		if (current == None):
			# set link address to itself
			self.first = newLink
			newLink.next = newLink
			
			return

		while (current.next != self.first):
			current = current.next

		#(current.next == self.first):
		current.next = newLink
		newLink.next = self.first


	# Find the link with the given key
	def find (self, key):
		current = self.first

		while (current.data != key):
			current = current.next

		return current

  # Delete a link with a given key
	def delete (self, key):
		current = self.first
		previous = self.first
	
		# if list empty return none
		if (current == None):
			return None

		# while we haven't fully circled the list
		while (previous.next != self.first):
			previous = previous.next

		# (previous.next == self.first)
		# returned to where we started
		# clook for link with matching key value
		while (current.data != key):
			previous = current
			current = current.next

		#(current.data == key)
		if (self.first != self.first.next):
			# continue traversing
			self.first = current.next
		# (self.first == self.first.next)
		else:
			self.first = None

		# because you have deleted the link, now you need
		# to connect the previous link to the next link
		previous.next = current.next


	# Delete the nth link starting from the Link start 
	# Return the next link from the deleted Link
	def deleteAfter (self, start, n):
		current = self.find(start)

		for i in range (1, n):
			current = current.next

		print(str(current.data), end = ' ')
		
		self.delete(current.data)

		return current.next
