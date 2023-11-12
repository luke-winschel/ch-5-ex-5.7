#Exercise 5.7
#(Duplicate Elimination) Create a function that receives a list and returns a list containing only the unique values in sorted order.

#Define a function
def unique_values():
    #Create two seperate empty lists
    list = []
    list_2 = []
    
    #Allow user to dictate the length of the list
    length = int (input('How long would you like the list to be: '))
    
    #for loop that receives input and fills the first list
    for i in range (length):
        value = int (input('Enter a number: '))
        list += [value]
    #Sorts and prints the first list in ascending order
    list.sort()
    print('This is the first list: ', list)
    
    #for loop that reads the values of list one and compares them to list two to determine if the value is unique
    for x in list:
        if x in list_2:
            continue
        else:
            list_2.append(x)
    #Sorts and prints the second list in ascending order
    list_2.sort()
    print('This is the second list: ', list_2)

#Call the function
unique_values()