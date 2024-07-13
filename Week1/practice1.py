#Practice 1:
#1. Create a list of the first 10 square numbers.
#Example: square number means [1,4,9,……..]
#2. Replace the third element with 50.
#3. Insert a new element 25 at the fifth position.
#4. Remove the last element from the list.
#5. Print the final list.

square=[1,4,3,16,25,36,49,64,81,100]
print("square is list :- ",square)
square[2]=50
print("Replace 3 element with 50",square)
square.insert(4,25)
print("inset new element",square)
square.pop()
print("last element of list",square)

