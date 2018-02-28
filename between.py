n=int(raw_input())
a=int(raw_input())
b=int(raw_input())
k=0
for i in range(a,b):
         if(n==i):
             k=k+1
if(k==0):
   print "no"
else:
   print "yes"
