#recursively perform linear search on a list/array

def linSearch(A,ele,pos=0): 
  if pos==len(A):
    return None 
  if A[pos]==ele:
    return pos
  else: 
    return linSearch(A,ele,pos+1)
list1 = [ 2, 3, 4, 10, 40 ] 
skey = 4 pos=linSearch(list1,skey) 
if pos==None:
  print(skey,"not found")
else: 
  print(skey,"found at position”,pos)
        
#recursively perform binary search and return the index.

def binarySearch (list1, begin, end, x): 
    if begin<=end:
        mid = (begin+end)//2 
        if list1[mid] == x:
          return mid
        elif list1[mid] > x:
           return binarySearch(list1,begin,mid-1,x)
        else:
           return binarySearch(list1, mid+1, end, x) 
     else:
        return -1
list1 = [ 2, 3, 4, 10, 40 ]
skey = 4
result = binarySearch(list1, 0, len(list1)-1, skey)
if result != -1:
    print ("Element is present at index %d" % result) 
else:
    print ("Element is not present in list")
        
#binary search without using recursion.

def binarySearch(list1, n, x): 
    begin,end=0,n-1
    while begin <= end:
        mid = (begin + end)//2 
        if list1[mid] == x:
           return mid
        elif list1[mid] < x:
           begin = mid + 1 else:
           end = mid - 1 return -1
list1 = [ 2, 3, 4, 10, 40 ]
skey = 10
result = binarySearch(list1, len(list1), skey) 
if result != -1:
    print("Element %d is present at index %d" %(skey,result)) 
else:
    print("Element %d is not present in list" %skey)
     
#insertion sort
        
def insertionsort(list1):
    for i in range(1, len(list1)):
        key = list1[i]
        j = i-1
        while j >=0 and key < list1[j] :
            list1[j+1] = list1[j]
        j -= 1 list1[j+1] = key
list1 = [12, 6, 70, 5, 16] 
insertionsort(list1)
print("Sorted list is:") 
print(list1)
        
#bubble sort
 
def bsort(list1):
   n=len(list1)
   print("Original list ",list1) 
   for i in range(n-1):
      for j in range(n-i-1):
         if list1[j] > list1[j+1]:
             list1[j],list1[j+1]=list1[j+1],list1[j] 
    print('List after sorting ', list1)
list1=[42,29,74,11,65,58] bsort(list1)
        
#selection sort
def selection_sort(list1): 
    n=len(list1)
    for i in range(0, n - 1):
       small_pos = i
       for j in range(i + 1, n):
          if list1[j] < list1[small_pos]: 
             small_pos = j
       list1[i],list1[small_pos] =list1[small_pos],list1[i] 
       print(list1)
list1 = [8,34,22,50,48,2] 
selection_sort(list1) 
print('Sorted list: ', end='') 
print(list1)
