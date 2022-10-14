# Write a function numIncreasing1(L) that takes as input a list of numbers and returns a list of the first sequence 
# within that is increasing order, and has a length of at least 2. If no increasing sequential numbers are found, 
#(ie. the input list is in descending order) then naturally a list of just the first value is returned.

def numIncreasing1(L):
    x = []
    for i in L:
        x.append(i)
    x.sort(reverse = True)
    if x == L:
        return([L[0]])
    elif not L:
        
        return []
   
    else: 
        sublist = [L[0]]
        output = []
        for a in L[1:]:
            if a > sublist[-1]:
                sublist.append(a)
            else:
                output.append(sublist);
                sublist = [a]


        output.append(sublist)
        for i in output:
            if len(i) >= 2:
                return i
                break
            else:
                continue
                
#Now write a function numIncreasing2(L) which applies similar constraints from Question 1a except returns the longest running 
#sequence of increasing numbers L. If two sequences are the same length, return the first sequence.

def numIncreasing2(s):
    if not s:
        return []

    sublist = [s[0]]
    output = []
    for a in s[1:]:
        if a > sublist[-1]:
            sublist.append(a)
        else:
            output.append(sublist);
            sublist = [a]
    output.append(sublist)
    n = len(output[0])
    for i in range(1,len(output)):
        if len(output[i]) > n:
            n = len(output[i])
        else:
            continue
    for j in range(0,len(output)):
        if len(output[j]) == n:
            return output[j]
            break
        else:
            continue
#Write a function uniqueSet(t) which when given a string (with no punctuation) will return a set containing the unique words
# in the string. Capitalizations should be ignored. 

def uniqueSet(t):
    list1 = t.split(" ")
    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)
        else:
            continue
    myset = set(list2)
    return myset

#Given two lists of integers listA and listB, write a function partitionLists that takes two list arguments and one optional 
#boolean parameter largerFirst which defaults to False.
#Your function should return a tuple containing two sorted lists, where the first list is the same length as list A, and the 
#second is the length of list B. All the elements in list A must be less than or equal to those in list B, and the lists 
#should be by default ascending order.
#If largerFirst is True, then the elements in list A must be greater than or equal to those in list B, and the lists should be 
#in descending order.

def partitionLists(listA,listB,largerFirst = False):
    combined_list = listA + listB
    n = len(listA)
    list1 = []
    list2 = []
    count = 0
    if largerFirst == True:
        combined_list.sort(reverse=True)
        for i in combined_list:
            if count < n :
                list1.append(i)
                count = count+1
            else:
                list2.append(i)
        tuple_list = (list1,list2)
        return tuple_list
    else:
        combined_list.sort()
        for i in combined_list:
            if count < n :
                list1.append(i)
                count = count+1
            else:
                list2.append(i)
        tuple_list = (list1,list2)
        return tuple_list
      
#Recursion
        
#Write a function choose(n,k) that recursively computes the number of ways you can choose k out of n items

def choose(n,k):
    if k == 0 :
        return 1
    elif n < k :
        return 0
    else:
        combination = choose(n-1,k-1) + choose(n-1,k)
    return combination
 
#Verifying Palindromes Recursively

def is_palindrome(s):
    if len(s) <= 1:
        return True 
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
    
