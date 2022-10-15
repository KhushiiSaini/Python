#function to calculate x to the power n
def power(base,exp): 
  if(exp==1):
    return(base) 
  else:
    return(base*power(base,exp-1))
base=int(input("Enter base: "))
exp=int(input("Enter exponential value: ")) 
print(“Result:",power(base,exp))
   
#program to reverse a string
      
def reverse(str1):
  if len(str1)==0:
    return str1 
   else:
    return (reverse(str1[1:]) + str1[0]) 
print(reverse(“reenigne"))
      
#program for generating the fibonacci sequence.
              
def fibonacci(n): 
   if(n <= 1):
      return n 
   else:
      return(fibonacci(n-1) + fibonacci(n-2))
n = int(input("Enter number of terms:")) 
print("Fibonacci sequence:")
for i in range(n):
   print(fibonacci(i),end=" “)
                    
# check whether a given string is palindrome.
         
def recursive_palindrome(str1): 
   if len(str1) <= 1:
      return True 
   else:
      if str1[0] == str1[-1]:
         return recursive_palindrome(str1[1:-1])
      else:
         return False
str1=input("Enter a String :") 
str1=str1.upper() 
if(recursive_palindrome(str1)==True):
   print("String is a Palindrome") 
else:
   print("String is not a Palindrome")
         
#print sum of elements of a list
def list_sum(list1): 
    if len(list1)==1: 
       return list1[0]
    else: 
       return(list1[0]+list_sum(list1[1:]))
list1=[1,2,3,4,5] 
print(list_sum(list1))
      
#find sum of even numbers of a list.
         
def Sum_Even(list1, i, sum=0): 
   if (i < 0):
      print(sum)
      return
   if ((list1[i]) % 2 == 0):
       sum += list1[i] Sum_Even(list1, i - 1, sum)
list1 = [ 10, 12, 3, 54, 55, 126, 7, 81 ] 
Sum_Even(list1, len(list1)- 1)

#find HCF of two numbers
         
def HCF(a,b): 
    if a%b==0:
      return b
    else: 
       return HCF(b,a%b)
x=int(input("Enter a number: "))
y=int(input("Enter second number:"))
hfactor=HCF(x,y)
print("The HCF of %d and %d is %d" %(x,y,hfactor))
         
#find the LCM of two numbers
         
def LCM(a,b):
   for i in range (2,a+1):
      if a%i==0 and b%i==0: 
         break;
       else: i=1 if i==1:
         return a*b
       else: 
         return i*LCM(a//i,b//i)
x=int(input("Enter a number: ")) 
y=int(input("Enter second number:")) 
print("LCM = “,LCM(x,y))
