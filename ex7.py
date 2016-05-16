print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." *10 #what'd that do?  # print "." ten times

end1="c"
end2="h"
end3="e"
end4="e"
end5="s"
end6="e"
end7="B"
end8="u"
end9="r"
end10="g"
end11="e"
end12="r"

#watch that comma at the end. try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,  #cheese comma in the end add space and next print will start after space. Else it will start from new line
print end7 + end8 + end9 + end10 + end11 + end12 # Burger

cheese = end1 + end2 + end3 + end4 + end5 + end6
burger = end7 + end8 + end9 + end10 + end11 + end12
print cheese + burger  #concatenate two string without space
print cheese,  #print it after space
print burger
print cheese  # print cheese and print burger in next line
print burger