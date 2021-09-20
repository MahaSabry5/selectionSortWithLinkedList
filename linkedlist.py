class Node:
	""" A class that represents each node of linked
		list each node contains some data and pointer
		to the next node (perhaps None)"""

	def __init__(self, data):
		self.data = data
		self.next = None



class LinkedList:
	""" A class for the linked list"""

	def __init__(self):
		self.head = None 		#initially the head doesn't point to any thing

	def add(self, data):
		''' A method that adds a new node at the beginning of the linked list
			making it point to the old head and moves the head to this new
			node '''
		temp = Node(data)
		temp.next = self.head
		self.head = temp

	def sort(self):
		'''The method which sorts the linked list using selection sort'''

		outer_cur = self.head		#A pointer to iterate through all the nodes in 
									#linked list initially it points to the head

		while outer_cur != None:    #while it isn't at the end of the linked list
			inner_cur = outer_cur.next    #another pointer to iterate through the node next
										  #to outer_cur to the end of the linked list

			min_node = outer_cur	  #initially the min node is the outer node
			min_data = outer_cur.data  #untill we find another one with minimum data

			while inner_cur != None:	
				if inner_cur.data < min_data:	#if the data of the current node
												#is less than the minmum so far
					min_data = inner_cur.data   #then update the minimum data
					min_node = inner_cur		#and the minimum node

				inner_cur = inner_cur.next		#move the inner_cur to point to the next node

			tmp = outer_cur.data  	
			outer_cur.data = min_data     #exhange the data of the outer_cur with the 
			min_node.data = tmp     #data of the minimum node
			outer_cur = outer_cur.next  #update the outer_cur

	def isSorted(self):
		''' A method to check if the linked list is sotrted correctly'''
		cur = self.head
		while cur.next != None:
			x = cur.data
			y = cur.next.data
			if x > y:
				return False      #if the data in the current node is greater than the data at
								  #the next node then return false
			cur = cur.next

		return True      #if no such pair found then return true

