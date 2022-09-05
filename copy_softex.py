import copy 
li1 = [1, 2, [3,5], 4] 
li2 = copy.copy(li1) 
li3 = copy.deepcopy(li1)
print ("The original elements before shallow copying") 
for i in range(0,len(li1)): 
    print (li1[i],end=" ") 
  
print("\r") 
li2[2][0] = 7
print ("The original elements after shallow copying") 
for i in range(0,len( li1)): 
    print (li1[i],end=" ")

print("\r")    
print ("The elements after deep copying") 
for i in range(0,len( li3)): 
    print (li3[i],end=" ")