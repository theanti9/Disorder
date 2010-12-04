import time, random
import Disorder

print "Insertion sort"
for i in xrange(0,3):
	t1 = time.time()
	Disorder.InsertionSort([random.randint(0,1001) for i in xrange(0,1000)])
	t2 = time.time()
	print "%0.3f ms" % ((t2-t1)*1000.0)
	
print "Bubble sort"
for i in xrange(0,3):
	t1 = time.time()
	Disorder.BubbleSort([random.randint(0,1001) for i in xrange(0,1000)])
	t2 = time.time()
	print "%0.3f ms" % ((t2-t1)*1000.0)
	
print "Quick sort"
for i in xrange(0,3):
	t1 = time.time()
	Disorder.QuickSort([random.randint(0,1001) for i in xrange(0,1000)])
	t2 = time.time()
	print "%0.3f ms" % ((t2-t1)*1000.0)
	

print "Selection sort"
for i in xrange(0,3):
	t1 = time.time()
	Disorder.SelectionSort([random.randint(0,1001) for i in xrange(0,1000)])
	t2 = time.time()
	print "%0.3f ms" % ((t2-t1)*1000.0)
	
print "Shell sort"
for i in xrange(0,3):
	t1 = time.time()
	Disorder.ShellSort([random.randint(0,1001) for i in xrange(0,1000)])
	t2 = time.time()
	print "%0.3f ms" % ((t2-t1)*1000.0)
	
print "Binary Tree sort"
for i in xrange(0,3):
	t1 = time.time()
	Disorder.BinaryTreeSort([random.randint(0,1001) for i in xrange(0,1000)])
	t2 = time.time()
	print "%0.3f ms" % ((t2-t1)*1000.0)
	
print "Merge sort"
for i in xrange(0,3):
	t1 = time.time()
	Disorder.MergeSort([random.randint(0,1001) for i in xrange(0,1000)])
	t2 = time.time()
	print "%0.3f ms" % ((t2-t1)*1000.0)

print "Gnome sort"
for i in xrange(0,3):
	t1 = time.time()
	Disorder.GnomeSort([random.randint(0,1001) for i in xrange(0,1000)])
	t2 = time.time()
	print "%0.3f ms" % ((t2-t1)*1000.0)
	
print "Cocktail sort"
for i in xrange(0,3):
	t1 = time.time()
	Disorder.CocktailSort([random.randint(0,1001) for i in xrange(0,1000)])
	t2 = time.time()
	print "%0.3f ms" % ((t2-t1)*1000.0)