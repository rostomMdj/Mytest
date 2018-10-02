a=["b","a","y","e","r","n"]

b=["","","","","",""]

c="wwe"

print "decouvrez le mot secret!"
print b

while a!=b:
 x=input("lettre")
 if x in a:
  b[a.index(x)]=x
  print str(b) 
 else:
   print "another one maaaan"



print " congrats *_* " 


