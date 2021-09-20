from random import randrange
from time import time
from linkedlist import LinkedList




def FormArrayAndList(array , ls):
	''' A method that forms both the array and linked list
		with 10000 items of random values between -1000 and 1000
		both should have the same elements with the same order'''


	for i in range(10000): #first form the array
		x = int(randrange(-1000, 1001))
		array.append(x)

	for i in range(10000-1 , -1 , -1): #then the linked list
		ls.add(array[i])

def SelectionSortArray(array):
	''' A method to sort the array by selection sort'''
	n = len(array)
	for i in range(n-1):
		min_item = array[i]
		min_pos = i
		for j in range(i + 1 , n):
			if array[j] < min_item:
				min_item = array[j]
				min_pos = j

		tmp = array[min_pos]
		array[min_pos] = array[i]
		array[i] = tmp

def isSortedArray(array):
	''' A method to check if the array is sorted'''
	for i in range(len(array)-1):
		if array[i] > array[i+1]:
			return False
	return True

def main():
	ls = LinkedList()	#declare a new linked list
	array = list()		#and a new array
	FormArrayAndList(array, ls)	#and form both of them

	start_time1 = time()
	SelectionSortArray(array)	#first sort the array
	end_time1 = time()

	elapsed_time1 = format(end_time1 - start_time1 , '.3f') #set the precision to 3 decimal points
	if isSortedArray(array): #if it is correctly sorted print its running time
		print('The array has been sorted successfully and it took ' , elapsed_time1 , ' seconds')
	else:
		print('something wrong')

	start_time2 = time()
	ls.sort()	#sort the linked list
	end_time2 = time()

	elapsed_time2 = format(end_time2 - start_time2 , '.3f')
	if ls.isSorted():	#if it is sorted correctly print its running time
		print('The linked list has been sorted successfully and it took ' , elapsed_time2 , ' seconds')
	else:
		print('something wrong')


if __name__ == '__main__':
	main()
