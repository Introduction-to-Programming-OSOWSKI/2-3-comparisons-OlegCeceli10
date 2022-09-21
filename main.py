#WRITE YOUR CODE IN THIS FILE
def greaterThan(x,y):
    if x<y:
        return False
    else:
        return True
    
def lessThan(x,y):
    if x<y:
        return True
    else:
        return False

def equalTo(x,y):
    if x==y:
        return True
    else:
        return False

def greaterOrEqual(x,y):
    if x>=y:
        return True
    else:
        return False

def lessOrEqual(x,y):
    if x<=y:
        return True
    else: 
        return False

print (lessOrEqual(10, 200))
