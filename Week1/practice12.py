print("\n")
print("Practice 12:")
print("Nested Dictionaries")
print("• Create a dictionary where each key is a country and the value is another dictionary with keys 'capital' and 'population'.")
print("• Access and print the capital of one country.")
print("• Update the population of another country.")
print("• Print the final dictionary.")
print("\n")
 
Counties={
        "Indai" :{"capital" : "New Delhi","population ": 1442195981},
        "Japan" :{"capital" : "Tokyo" , "population" : 14094034}	,
        "Russia" :{"capital" :"Moscow" , "population"	 : 13104177}	
}
print("dictionary country :- ")
print(Counties)
access=Counties["Japan"]["capital"]
print("print the capital of one country :- ",access)
print("Update the population of Russia country :-")
Counties["Russia"]["population"]=144713314
print(Counties)
