def upper(world):
    result=""
    for i in world :
        if ord(i) >=97 and ord(i)<=122:
            result+=chr(ord(i)-32)
        else :
            result += i
    return result 

def lower(world):
    result=""
    for i in world :
        if ord(i) >=65 and ord(i)<=90:
            result+=chr(ord(i)+32)
        else :
            result += i
    return result  

def capitaliz(world):
    if ord(world[0]) >=97 and ord(world[0])<=122:
        world = chr(ord(world[0]) - 32) + world[1:]
        return world     

def count(world , substring):
     count = 0
    for i in world:
        if i == subsrring :
            count +=1 
    return count  

def isnumeric(world):
    ans = False
    for i in world :
        if ord(i) >= 48 and ord(i)<=57 :
            ans = True
        else :
            ans = False
            break
    return ans  

def isalnum (world):
    ans = False
    for i in world :
        if  ord(i) >= 48 and ord(i)<=57 :
            ans = True
        elif  ord(i) >= 97 and ord(i)<=122 :
            ans = True
        elif  ord(i) >= 65 and ord(i)<=90 :
            ans = True 
        else :
            ans = False
            break
    return ans

def isupper(world):
    ans = False
    for i in world :
        if ord(i) >= 97 and ord(i)<=122 :
            ans = False
            break  
        else : 
            ans = True  
    return ans

def islower(world):
    ans = False
    for i in world :
        if ord(i) >= 65 and ord(i)<=90 :
            ans = False
            break  
        else : 
            ans = True  
    return ans
