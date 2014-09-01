#!/usr/bin/env python


#######################################################################################################

def sort(_list):            #Takes in a list and returns the list in sorted order of string length
    _list.sort(lambda x,y:cmp(len(x),len(y)))
    return(_list)

#######################################################################################################

def compare(threshold): #Implements closure
    return lambda x:x<threshold

func_a=compare(10)
func_b=compare(50)

print func_a(5)
print func_b(100)

########################################################################################################

def divide(x,y):  #Currying, the process of changing a function so that it takes fewer inputs
    return(x/y)

def divisor(d):
    return lambda x:divide(x,d)

half=divisor(2)
third=divisor(3)

print half(16)
print third(9)

############################################################################################################

def _map(_list):   #Maps elements of a list into a new list
   return map(lambda x:x*x,_list)

############################################################################################################

def _reducer(_list):  #Reduces or folds elements of a list
    return reduce(lambda x,y:x*y,_list)

#############################################################################################################

def _filter(_list):     #Returns all filtered elements of the list for which the condition given is true
    return filter(lambda x:x%2==0,_list)

##############################################################################################################





