#Tuples-they are simillar to list
counties=("machakos","Nairobi","Kisii","Nyeri")
print(counties)
print(counties[3])
 
 #Tuples use() to hold the values
 #List use[]  to hold the values
 #list add a new county our tuple
counties.append("Kisumu")
print(counties)
counties.remove("Kisii")
print(counties)

#list vs tuples
#lists can append/remove items,uses[]
#Tuple cannot append/remove item,uses ()


#in a tuple you can not remove or add something 
#above code will not run