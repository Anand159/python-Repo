print("\n")
print("Practice 10:")
print("Dictionary Basics")
print("1. Create a dictionary with three key-value pairs representing a student's name, age, and grades.")
print("2. Update the student's age.")
print("3. Add a new key-value pair for the student's favorite subject.")
print("4. Print the final dictionary.")
print("\n")
dic={ "student" : "Anand" ,
     "age" : 18 ,
     "grade" : "A"
}
print("dictionary :- ",dic)
dic.update({"age":19})
print("update dictionary :- ",dic)
dic.update({"subject" : "Math"})
print("Add a new key-value pair :- ",dic)

