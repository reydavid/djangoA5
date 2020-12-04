#Create a function that accepts a string and returns a Boolean based on if it is a palindrome.

#Example ("Car"=Flase, "mom"=> True)

#Input String

#Output Boolean

# x=arr[]
# y
#racecar = racecar
#step through string in reverse
#begin len(str)-1
#end 0
#step -1
#string

def isPalindrome(string):
    temp =""
    for i in range(len(string)-1, -1, -1):
       temp = temp + string[i]
    print(temp)
    if temp == string:
        return True
    return False

string = "racecar"

print(isPalindrome(string))

            