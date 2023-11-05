from functools import reduce
# Define a function to multiply two numbers
def multiply(x, y):
    return x * y

sample_list = [2, 3, 6]

# Use the reduce function to multiply all items in the list
result = reduce(multiply, sample_list)

print("Result:", result)

#QUESTION 2
def sort_list(input_list):
    # sort the list in increasing order based on the last element in each tuple
    sorted_list = sorted(input_list, key=lambda x: x[-1])
    
    return sorted_list

sample_lists = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
result = sort_list(sample_lists)
print("Result =", result)

#QUESTION 3
d1 = {'a':100, 'b':200, 'c':300}
d2 = {'a':300, 'b':200, 'd':400}
dict_result = {key: d1.get(key, 0) +  d2.get(key, 0) for key in set(d1) | set(d2)}
print("Dict Result = ", dict_result)

#QUESTION 4
n = int(input("Enter an integral number: "))  # Read the input value
result = {}  # Create an empty dictionary to store the squares
# Use a for loop to generate the dictionary
for i in range(1, n + 1):
    result[i] = i * i
# Print the dictionary
print(result)

#QUESTION 5
list = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# Function to sort the tuple by its float element
def sort_tuple(list):
    sorted_list = sorted(list, key=lambda x: float(x[1]), reverse=True)
    return sorted_list
sorted_list = sort_tuple(list)
print(sorted_list)
#QUESTION 6
my_set = {0, 1, 2, 3, 4}
print(my_set)
#To iterate over sets, you can use the for loop
my_set = {0, 1, 2, 3, 4}
for item in my_set:
    print(item)
    #Add member in a set
    my_set = {0, 1, 2, 3, 4}
    my_set.add(5)
    print(my_set)
    #Remove items from a given set
    my_set ={0, 1, 2, 3, 4}
    my_set.remove(2)
    print(my_set)
"""def subtract(a,b):
    result= a-b
    return result
  
x = int(10)
y = int(3)
result = subtract(x, y)"""
