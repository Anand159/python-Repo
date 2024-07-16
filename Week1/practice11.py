print("\n")
print("Practice 11:")
print("Dictionary Methods")
print("• Create a dictionary with five key-value pairs representing different cities and their")
print("populations.")
print("• Use the get method to access the population of a specific city.")
print("• Use the pop method to remove a city from the dictionary.")
print("• Print the final dictionary.")
print("\n")
dic={
     "Mumbai"	: 12442373 ,	
      "Delhi"	: 11034555	,
     "Bangalore"	: 8443675	,
     "Hyderabad"	: 6993262
}
print("Dictionary :- ",dic)
Get=dic.get("Mumbai")
print("Get of specific city 'Mumbai' :-",Get)
dic.pop("Delhi")
print("Pop in dictionary :- ",dic)
