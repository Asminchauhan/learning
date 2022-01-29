# if statements the statements in the if should be indented.

if 10 > 5:
    print("10 is greater than 5")

print("Progrm ended")

num = 12 
if num > 5:
    print("Bigger than 5")                 # this is the nested if statement Indentation is used to define the level of nesting
    if num <= 47:
        print("Between 5 and 47")

# The short form of if/else statement is elif

print(1 == 1 and 2 == 2 )

# The result of not True is False, and not False goes to True


number = 3
things = ["String", 0, [1, 2, number], 4.56]  # Lists are things in [] it can also be nested, the elements order is 0,1,2...

print(things[2][2])

str = "Hello world!"
print(str[6])               

#Some types, such as strings, can be indexed like lists.
#Indexing strings behaves as though you are indexing a list containing each character in the string.

nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3)
print(1 in nums)        # To check if the list has element 
print(5 not in nums)


# .append() to add in list, len() to get length of list , .insert(index, element) 
# max(list): Returns the list item with the maximum value
# min(list): Returns the list item with minimum value
# list.count(item): Returns a count of how many times an item occurs in a list
# list.remove(item): Removes an object from a list
# list.reverse(): Reverses items in a list.

# while loops are created, break is added to end loop prematurely 

# the continue statement stops the current iteration and continues with the next one

# It is common to use the for loop when the number of iterations is fixed.  
# For example, iterating over a fixed list of items in a shopping list.

# The while loop is used in cases when the number of iterations is not known 
# and depends on some calculations and conditions in the code block of the loop.

numbers =  list(range(1, 10))
print(numbers)

for i in range(5):
    print('Hello')



