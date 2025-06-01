list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# list methods
# append() - adds an item to the end of the list
list.append(22)
print(list)  # prints [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
# insert() - adds an item at a specific index
list.insert(0, 0)  # adds 0 at the beginning
print(list)  # prints [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
# remove() - removes the first occurrence of an item
list.remove(10)  # removes the first occurrence of 10
print(list)  # prints [0, 2, 4, 6, 8, 12, 14, 16, 18, 20, 22]
# pop() - removes and returns the item at a specific index (default is the last item)
last_item = list.pop()  # removes and returns the last item (22)
print(last_item)  # prints 22
list.sort(reverse=True)  # sorts the list in descending order
print(list)  # prints [20, 18, 16, 14, 12, 8, 6, 4, 2, 0]
list.reverse()  # reverses the list
print(list)  # prints [0, 2, 4, 6, 8, 12, 14, 16, 18, 20]
