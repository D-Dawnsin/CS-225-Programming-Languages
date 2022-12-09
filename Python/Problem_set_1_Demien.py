input_year = input("Enter a year: ")
year = int(input_year)

#if no remainder after dividing by 4 and still some remainder after dividing by 100 then it is a leap year
if year % 4 == 0 and year % 100 > 0: 
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

print("------------------- End of Problem 1--------------------")

x = [4] #creates array with the number 4 in it

#function which appends the number 3 to the end of the global variable array x
def antioch(): 
    x.append(3)


def maynard(): 
    x = [1, 2] #creates a new local x varible that is an array with the numbers 1 and 2
     #appends the number 3 to the end of the local x variable within this function ([1,2])
    x.append(3) #due to the scope of the function the x that is being appended is the local variable x here within the function

print(x) #prints the global x varible ([4])
antioch() #appends number 3 to end of original array (the global x variable)
print(x)
maynard() #appends the 3 to the local variable x ([1,2]) that is within the function
print(x) #prints off the global x variable since we only have access global variable when printing outside of a function

print("------------------- End of Problem 3--------------------")

print(int("3"))
print(int(3.7))
print(int(float("3.7")))


print("--------error received for third line-----------")
print (int("3.7"))


