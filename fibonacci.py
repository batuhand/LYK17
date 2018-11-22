def fib(n):
  a,b=0,1
  while b<int(n):
    print(a)
    a,b=b,a+b

a= input("Kaça kadar yazalım : ")
fib(a)