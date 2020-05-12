def notStringContainingE(word):
   """
   return True when word is a string that contains no letter 'e' (or 'E')
   It should work both for lower and upper case.
   When word isn't a string, return True 
   (because it is not a string contaning an E)
   """
   
   if not(type(word)==str):
      return True
   for letter in word:
     if letter == 'e' or letter == 'E':   
       return False
   return True

def hasNoX(word):
   """
   return True when word is a string that contains no letter 'x' 
   (and no letter 'X')
   It should work both for lower and upper case.
   When word isn't a string, return True (because it is not a string 
   with an  x in that case!)
   """
   if (type(word)!=str):
      return True
   for letter in word:
     if letter == 'x' or letter == 'X':
       return False
   return True

def isNumber(item):
   " return True if item is of type int or type float otherwise False "
   if type(item) != int and type(item) != float:
       return False
   return True # HINT You already did this on in a previous lab


def isListOfNumber(theList):
   """
   indicates whether value of argument is a list of only simple numbers
   (int or float) 
   Note: empty list should return True---it doesn't contain anything that 
   ISN'T a simple number
   theList can be anything, and the function will return either True or False.
   """

   if not type(theList)==list:
      return False  # it isn't really a list!

   # Now we can assume that theList really is a list
   # But is it a list of all numerics?
   # If we find even a single item that isn't numeric, we can
   # immediately return false.  
   
   for item in theList:
     if not isNumber(item):
       return False

   # If we get here and didn't return yet, then we know everything
   # in the list is a simple numeric!
   # (i.e. there isn't anything in the list that is NOT simple numeric)
   
   return True


def isListOfIntegers(theList):
    
    if not type(theList)==list:
      return False
    for item in theList:
     if type(item) != int:
       return False
    
    return True

def isListOfEvenIntegers(theList):
    if not isListOfIntegers(theList):
        return False
    else:
        for item in theList:
            if item % 2 == 1:
                return False
    return True


def totalLength(listOfStrings):
    l = 0
    if type(listOfStrings) != list:
        return False
    for item in listOfStrings:
        l = l + len(item)
    return l


def lengthOfEach(listOfStrings):
    if type(listOfStrings) != list:
        return False
    L = len(listOfStrings)
    i = 0
    for item in listOfStrings:
        listOfStrings[i] = len(item)
        i += 1
    return listOfStrings

def countEvens(listOfInts):
    t = 0
    if not isListOfIntegers(listOfInts):
        return False
    for i in listOfInts:
        if i % 2 == 0:
            t += 1
    return t


def onlyEvens(listOfInts):
    res = []
    if not isListOfIntegers(listOfInts):
        return False
    for I in listOfInts:
        if I % 2 == 0:
            res = res + [I]
    return res
    
        
