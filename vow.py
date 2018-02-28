r=raw_input()
vow=['a','e','i','o','u','A','E','O','I','U']
k=0
for i in r:
     if  i in vow:
        k=1
if(k==1):
   print "yes"
else:
   print"no"
