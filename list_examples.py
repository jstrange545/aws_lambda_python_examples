# Creating a list
my_list = [1, 2, 3, 'apple', 'banana', 'red', 'purple', 'orange', 10]
print(my_list)

my_list.append('grapes')
print(my_list)

my_list[0] = 'one'
print(my_list)

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')

print(f"Fruits: {fruits}, Fruits count: {fruits.count('apple')}")

fruits.count('tangerine')

print(f"index: {fruits.index('banana')}")

fruits.index('banana', 4)  # Find next banana starting at position 4

fruits.reverse()
fruits

fruits.append('grape')
fruits

fruits.sort()
fruits

fruits.pop()