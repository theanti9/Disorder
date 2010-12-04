# Disorder.py - Sorting Module

class InvalidArgument(RuntimeError):
	def __init__(self, msg='Invalid Argument'):
		self.msg = msg
	def getMsg(self):
		return self.msg

# Insertion Sort
def InsertionSort(li):
	if not isinstance(li, list):
		raise InvalidArgument()
	for i in xrange(0, len(li)):
		for j in xrange(i, len(li)):
			if li[j] < li[i]:
				tmp = li[i]
				li[i] = li[j]
				li[j] = tmp
	return li
	
# Bubble Sort
def BubbleSort(l):
	if not isinstance(li, list):
		raise InvalidArgument()
	ordered = False
	n = len(li)
	while (ordered == False):
		ordered = True
		newn = 0
		for i in xrange(0, n-1):
			if li[i] > li[i+1]:
				tmp = li[i]
				li[i] = li[i+1]
				li[i+1] = tmp
				ordered = False
				newn = i + 1
		n = newn
	return li
	
# Quick Sort
def QuickSort(li):
	if not isinstance(li, list):
		raise InvalidArgument()
	less = []
	more = []
	if len(li) <= 1:
		return li
	pivot = li.pop()
	for i in li:
		if i < pivot:
			less.append(i)
		else:
			more.append(i)
	return _concatList(QuickSort(less), pivot, QuickSort(more))
	
	
# Selection Sort
def SelectionSort(li):
	if not isinstance(li, list):
		raise InvalidArgument()
	for i in xrange(0, len(li)-1):
		lowest = (i, li[i]) # lowest[0] is the index, lowest[1] is the value at that index
		for j in xrange(i, len(li)):
			if li[j] < lowest[1]:
				lowest = (j, li[j])
		tmp = li[i]
		li[i] = li[lowest[0]]
		li[lowest[0]] = tmp
	return li

# Shell Sort
def ShellSort(li):
	if not isinstance(li, list):
		raise InvalidArgument()
	inc = int(round(len(li) / 2))
	while inc > 0:
		for i in xrange(inc, len(li)):
			temp = li[i]
			j = i
			while j >= inc and li[j - inc] > temp:
				li[j] = li[j - inc]
				j = j - inc
			li[j] = temp
		inc = int(round(inc / 2.2))
	return li
	
# Binary Tree Node
class Node:
	left, right, data = None, None, 0
	
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data
		
	# add data to the tree
	def insert(self, data):
		# return false if the data is a duplicate
		if data == self.data:
			return false
			
		# if data is less than the current node go left
		elif data < self.data:
			# if no data here, make a new node
			if self.left == None:
				self.left = Node(data)
				
			# else try the same on its left child
			else:
				self.left.insert(data)
				
		# if its greater, go right
		else:
			# if no data here, make a new node
			if self.right == None:
				self.right = Node(data)
				
			# else try the same on its right child
			else:
				self.right.insert(data) 
				
	# flatten a node into a list
	def flatten(self):
		# if no children, return this nodes data as a list
		if self.left == None and self.right == None:
			return [self.data]
		# create empty list
		li = []
		
		# append the first list
		if self.left is not None:
			li.extend(self.left.flatten())
			
		# append data
		li.append(self.data)
		
		# append the second list
		if self.right is not None:
			li.extend(self.right.flatten())
			
		return li
		
# Binary Tree Sort
def BinaryTreeSort(li):
	# create the root node with the first element
	root = Node(li[0])
	
	# add each element to the tree
	for i in xrange(1, len(li)):
		root.insert(li[i])
		
	#flatten the tree
	return root.flatten()
	
# Merge Sort
def MergeSort(li):
	import heapq
	if len(li) <= 1:
		return li
	mid = len(li) / 2
	left = li[0:mid]
	right = li[mid:]
	left = MergeSort(left)
	right = MergeSort(right)
	return list(heapq.merge(left, right))
		
# Gnome Sort		
def GnomeSort(li):
	i = 1
	while i < len(li):
		if li[i] >= li[i-1]:
			i += 1
		else:
			tmp = li[i]
			li[i] = li[i-1]
			li[i-1] = tmp
			if i > 1:
				i -= 1	
	return li

# Cocktail Sort
def CocktailSort(li):
	begin = -1
	end = len(li) - 1
	swapped = True
	while swapped:
		swapped = False
		begin += 1
		for i in xrange(begin, end):
			if li[i] > li[i+1]:
				tmp = li[i]
				li[i] = li[i+1]
				li[i+1] = tmp
				swapped = True
		if not swapped:
			break
		swapped = False
		end -= 1
		for i in xrange(end, begin, -1):
			if li[i] > li[i+1]:
				tmp = li[i]
				li[i] = li[i+1]
				li[i+1] = tmp
				swapped = True
	return li

# Concatenate two sorted lists
# used for Quick Sort
def _concatList(l1, a, l2):
	# create a new list
	li = []
	if l1 is not None:
		li.extend(l1)
		
	if a is not None:
		# append the middle if there is one
		li.append(a)
		
	if l2 is not None:
		# append each of the elements from l2
		li.extend(l2)
		
	return li