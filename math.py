#Add implementation
def add(x,y):
	return x+y
#sub implementation
def substract(x,y):
	return x-y          #on master branch
#mul implementation
def multiply(x,y):
	return m*y          #on bug456 branch
#divide implementation    
def divide(x,y):

	if y==0:                    #on master branch
        return DIVIDE_BY_0_ERROR
    else:
        return x/y 

def square(x):
    pass