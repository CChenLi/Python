import pytest

def isList(x):
    """
    check whether parameter is a list

    """
    if type(x) == list:
        return True
    else:
        return False
    
def largestInt(listOfInts):
    """
    return largest element of a list of ints, 
    raise ValueError if empty, not a list, or not a list of ints
    
    By "largest", we mean a value that is no smaller than any other
      value in the list (There may be more than one instance of that
      value--e.g. in [7,3,7], 7 is largest      
    """
    
    if type(listOfInts)!=list:
       raise ValueError("argument to largestInt should be a list")
   
    if listOfInts==[]:
       raise ValueError("argument to largestInt may not be empty")

    # Now we know there is at least one item in the list.
    # We make an initial assumption that this item will be the largest.
    # We then check every other item in the list--each gets a chance to
    #  knock the maxSoFar out of the winner's circle

    maxSoFar = listOfInts[0]  # the one in position zero is best guess so far

    # Note: we have to start from 0 because we need to check the type
    #  of element[0] to see if it is an int.  Otherwise, we could start from 1
    
    for i in range(0,len(listOfInts)):  # all indexes in the list
        
       if type(listOfInts[i])!=int:      # make sure it is an int
          raise ValueError("element " + str(i) + " isn't an int")

       if listOfInts[i] > maxSoFar:  # compare the new item with maxSoFar
          maxSoFar = listOfInts[i]   # we have a new candidate
                                     # for the title of "largest int"

    # Now we've gone through the entire list.  Every other item on the list
    # has had a chance to defeat maxSoFar as the largest int.  So the one
    # left in maxSoFar must be the largest one.

    return maxSoFar



def indexOfLargestInt(listOfInts):
    """
    return index of largest element of a list of ints
    raise ValueError if non empty, not a list, or not a list of ints
    By "largest", we mean a value that is no smaller than any other 
    value in the list (see comment in definition of largestInt)
    By "index", we mean the subscript that will select that item of
    the list when placed in [].   Since there can be more than one
    largest, we'll return the index of the first such value in those
    cases, i.e. the one with the lowest index.
      
    """

    if type(listOfInts)!=list:
       raise ValueError("argument to indexOfLargestInt should be a list")
    if listOfInts==[]:
       raise ValueError("argument to indexOfLargestInt may not be empty")

    # Now we know there is at least one item in the list.
    # We make an initial assumption that this item will be the largest.
    # We then check every other item in the list--each gets a chance to
    #  knock the maxSoFar out of the winner's circle

    indexOfMaxSoFar = 0    # the one in position zero is the first candidate


    # Note: we have to start from 0 because we need to check the type
    #  of element[0] to see if it is an int.  Otherwise, we could start from 1
    
    for i in range(0,len(listOfInts)):  # all indexes in the list
        
       if type(listOfInts[i])!=int:      # make sure it is an int
          raise ValueError("element " + str(i) + " isn't an int")          

       if listOfInts[i] > listOfInts[indexOfMaxSoFar]:
           # compare the new item with maxSoFar
           indexOfMaxSoFar = i  # we have a new candidate; store the INDEX

    # Now we've gone through the entire list.  Every other item on the list
    # has had a chance to defeat maxSoFar as the largest int.  So the one
    # left in maxSoFar must be the largest one.

    return indexOfMaxSoFar

def smallestInt(listOfInts):
    """
    return smallest element of a list of ints
    raise ValueError if non empty, not a list, or not a list of ints
    By "smallest", we mean a value that is no smaller than any 
    other value in the list
    """
    if type(listOfInts) != list:
        raise ValueError("argument to smallestInt should be a list")
    if listOfInts==[]:
        raise ValueError("argument to smallest may not be empty")
    res = listOfInts[0]
    for i in listOfInts:
        if type(i)!=int:      # make sure it is an int
          raise ValueError("element " + str(i) + " isn't an int")
        elif i < res:
            res = i
    return res
    

def indexOfSmallestInt(listOfInts):
    """
    return index of smallest element of a list of ints
    raise ValueError if non empty, not a list, or not a list of ints
    """
    if type(listOfInts) != list:
        raise ValueError
    if listOfInts ==[]:
        raise ValueError
    s = 0
    res = listOfInts[0]
    for i in range(0, len(listOfInts)):
        if type(listOfInts[i]) != int:
            raise ValueError
        if listOfInts[i] < res:
            res = listOfInts[i]
            s = i
    return s


def longestString(listOfStrings):
    """
    return longestString from a list of strings
    raise ValueError if non empty, not a list, or not a list of strings
    By "longest", we mean a value that is no shorter than any 
    other value in the list
    There may be more than one string that would qualify:
    For example in the list ["dog","bear","wolf","cat"] both bear and 
    wolf are longest strings
    In such cases, return the one with the lowest index (in this case, bear)  
      
    """
    if type(listOfStrings) != list:
        raise ValueError
    if listOfStrings ==[]:
        raise ValueError
    res = listOfStrings[0]
    for i in listOfStrings:
        if type(i) != str:
            raise ValueError
        if len(i) > len(res):
            res = i
    return res


def indexOfShortestString(listOfStrings):
    """
    return index of shortest string from a list of strings
    raise ValueError if non empty, not a list, or not a list of strings
    By "shortest", we mean a value that is no longer than any other 
    value in the list
    There may be more than one string that would qualify,
    For example in the list ["dog","bear","wolf","cat"] both dog and cat 
    are shortest strings
    
    In such cases, return the one with the lowest index (in this case, dog)  
    """
    if type(listOfStrings) != list:
        raise ValueError
    if listOfStrings ==[]:
        raise ValueError
    s = 0
    for i in range(0, len(listOfStrings)):
        if type(listOfStrings[i]) != str:
            raise ValueError
        if len(listOfStrings[i]) < len(listOfStrings[s]):
            s = i
    return s
