def min (num1 , num2 ):
     if num1 > num2:
         print (num2)
     else :
         print (num1)
       
def max (num1 , num2 ):
     if num1 > num2:
         print (num1)
     else :
         print (num2)

 def absolute (num):
    if num < 0 :
        return -num
    return num      

def msx (num1 , num2 ):
    num1 = absolute (num1)
    num2 = absolute (num2)
     if num1 > num2:
         return (num1)
     else :
          return (num2)
