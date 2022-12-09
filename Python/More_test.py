def sieve(lo,hi):
   
   primes = [] #creates the primes list
   flag = True #makes a flag default true

   #Lowest number cant be anything lower than 2
   if(lo < 2):
      return print("Your lo must be bigger than 2")
   if(lo > hi):
       return print("Your lo must be smaller than your hi")


   #if lo is not equal to hi then continue recursion but incrementing lo by 1
   if(lo != hi):
      primes = sieve(lo+1,hi)

   #for i in range of 2 to lo check which numbers are without remainders when dividing by i and set those number's flags to false
   for i in range(2 , lo):
      if (lo%i == 0):
        flag = False
    
    #Finally all of the numbers that still have the flag of True append those numbers to the primes list
   if(flag == True):
      primes.append(lo)

   return primes

list = sieve(2,61)

for i in list:
    print(i) 