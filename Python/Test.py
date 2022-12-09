print(list(range(1,51+1)))

p = 2

def sieve(lo,hi):
#You will need to implement the Sieve of Eratosthenes 
#which finds all the primes in a range of numbers
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes explains it
# A good way to start is to build a list of all the numbers 
# tip: "range" is a tool in python/Google is an OK resource for the language!
#ANSWER: below and FILL IN THIS SECTION!!!!!!!!!! of code.
    intial = [*range(lo,hi+1)] #creates list of numbers entered by user with all set to true at first
    p = 2 #sets p equal to the smallest prime
    prime = []

    if(lo < 2):
        return print("Your low must be bigger than 2")


    #Issue is that idk how to set initial


    for i in intial:
        if(i % p != 0): #If there is a remainder after dividing
            prime.append(i) #add that number to list

    #from this point on i am not too sure
            
    p = min(prime)

    if(p * p <= hi):
        sieve(p, hi)

    else:
        return prime

new = []

new = sieve(2,56)

for i in new:
    print(new[i])