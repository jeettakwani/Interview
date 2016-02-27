__author__ = 'jtakwani'
#this file contains the heap sort code

def heap_sort(numbers):
    if len(numbers) == 0:
        return "empty array"
    heap_size = len(numbers)-1
    for i in range(((len(numbers)/2)-1),-1,-1):
        max_heapify(i,numbers,heap_size)

    while heap_size!=1:
        temp = numbers[0]
        numbers[0] = numbers[heap_size]
        numbers[heap_size] = temp
        heap_size = heap_size-1
        max_heapify(0,numbers,heap_size)
    return numbers

def max_heapify(parent, numbers,heap_size):
    largest = parent
    if (2*parent)+1 > heap_size or (2*parent)+2 > heap_size:
        return
    if numbers[(2*parent)+1] > numbers[largest]:
        largest = (2*parent)+1
    if numbers[(2*parent)+2] > numbers[largest]:
        largest = (2*parent)+2
    if largest != parent:
        temp = numbers[parent]
        numbers[parent] = numbers[largest]
        numbers[largest] = temp
        max_heapify(largest,numbers,heap_size)
    return numbers


def main():
    print(heap_sort([99,4,23,1,34,46]))
    print(heap_sort([]))

if  __name__ =='__main__':main()