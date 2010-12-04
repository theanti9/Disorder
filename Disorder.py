# Disorder.py - Sorting Module

class InvalidArgument(RuntimeError):
	def __init__(self, msg='Invalid Argument'):
		self.msg = msg
	def getMsg(self):
		return self.msg

# == Order Constants ==
ASC = 0 # ascending
DSC = 1 # descending 

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
		
	def insert(self, data):
		if data == self.data:
			return false
		elif data < self.data:
			if self.left == None:
				self.left = Node(data)
			else:
				self.left.insert(data)
		else:
			if self.right == None:
				self.right = Node(data)
			else:
				self.right.insert(data) 
	def flatten(self):
		if self.left == None and self.right == None:
			return [self.data]
		return _concatList(self.left.flatten() if self.left is not None else None, self.data, self.right.flatten() if self.right is not None else None)
		
# Binary Tree Sort
def BinaryTreeSort(li):
	root = Node(li[0])
	for i in xrange(1, len(li)):
		root.insert(li[i])
	return root.flatten()
		

def _concatList(l1, a, l2):
	li = []
	if l1 is not None:
		for l in l1:
			li.append(l)
	else:
		pass
	if a is not None:
		li.append(a)
	else:
		pass
	if l2 is not None:
		for l in l2:
			li.append(l)
	else:
		pass
	return li