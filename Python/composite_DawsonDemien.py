#!/bin/env python3
#
import sys
#
#  Separate a list of numbers into primes and composites.
#  Primes are identified using sieve of Eratosthenes
# 
#  Usage:  ./composite 15 17 101 189 ... 
#        It will print: 
#          Composite: [15, 189]
#          Prime: [17, 101]
#
#-------------------------------------------
# 
# sieve(lo, hi) returns list of primes from lo to hi, computed by sieving.
#
# lo and hi are further proof of the dislike of full-word-typing: think low and high
#
def sieve(lo,hi):
   
   primes = [] #creates the primes list
   flag = True #makes the flag default true

   #Error handling for if lo is smaller then 2 or if lo is greater than hi
   if(lo < 2):
      return print("Your low must be bigger than 2")
   if(lo > hi):
      return print("Your low must be smaller than your high")

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

# The goal is to:
# separate a set of numbers into primes and composites
#
#  given (set-of-numbers)
#
#  return ( set-of-composites, set-of-primes )
#
def separate(numbs):
   primes = set(sieve(min(numbs), max(numbs)))
   og_range = set(list(range(min(numbs), max(numbs)))) #I altered this method a little to include the orginal number range that way .difference and .intersection would work
   return (og_range.difference(primes), og_range.intersection(primes))

#--------------------------------------------
#
# Main program:
#
#  Extract numbers from argument list.
#  Use lowest and highest ones as argument to seive
#  Must be at least 1 number in the arguments (arguments are passed at the command line!)
#

if (len(sys.argv)>=2):
#Uhoh  What is that Strange 1: action?
#Answer: It makes sure that the user has inputted at least 2 arguments to the command line
   numbs = sys.argv[1:]
# QUESTION FOR YOU: What sort of thing is "numbs"?
#ANSWER: Numbs is the list of arguments (starting with their first argument since sys.argv[0] is the name of the program) so numbs is the the range of numbers from lo to hi
   numbs = [int(x) for x in numbs if x.isdigit()]
   if len(numbs)>0:
   	comp, prim = separate(set(numbs))
   print("Composite: ", sorted(comp))
   print("Prime: ", sorted(prim))
   sys.exit()
#So why does this print work?
#ANSWER: This print works because the list of primes come from the intersection between the orignal number range and the primes list received from seive
# and the composits come from the difference between the primes (from sieve) and the original number range  
#  
# usage
#
print("Prints which numbers are prime and which are composite.")
print("Usage: composite n1 n2 n3 ...")
print("example: composite 3 5 7 9 11 13 15")