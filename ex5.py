name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74.0 #inches
weight = 180.0 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's a talk about %s." % name
print "He's %d inches tall." %height
print "He 's %s cm tall."% format(height * 2.54,'0.2f')
print "He's %d pounds heavy." %weight
print "He's %s kg heavy." % format(weight*0.453,'0.2f')
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(eyes,hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get it exactly right
print "If I add %d,%d and %d I get %d." %(age, height, weight, age + height + weight)
