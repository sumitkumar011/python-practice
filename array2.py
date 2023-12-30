ar=[]
m=int(input("enter the number "))
for i in range (m):
    n=int(input("enter the no"))
    ar.append(n)
print(ar)
v=int(input("enter the number :"))
for i in range(m):
  if v==ar[i]:
      print("no found at location ",i+1)
      break
else:
      print("this no is not preent")
