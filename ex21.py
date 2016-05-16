def add(a,b):
	print "Adding %d and %d" %(a,b)
	return (a+b)
	
def subtract(a,b):
	print "Subtracting %d and %d" %(a,b)
	return a-b

def multiply(a,b):
	print "Multiplying %d and %d" %(a,b)
	return a*b
	
def divide(a,b):
	print "Divide %d and %d" %(a,b)
	return a/b
	
print "Let's do some math"

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq= divide(100,2)

print "Age: %d, Height:%d, Weight:%d, IQ:%d" %(age,height,weight,iq)

print add(age, subtract(height,multiply(weight,divide(iq,2))))

print multiply(iq, divide(weight,add(height,16)))

