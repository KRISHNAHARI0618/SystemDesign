print("Printing Fibonacci Numbers ....")

# Fibonacci Numbers ..

n1 = 0
n2 = 1
print(n1,n2)
fib_list = []
fib_list.append(n1)
fib_list.append(n2)
for i in range(2,20):
    sum = n1+n2
    print(sum,end=" ")
    fib_list.append(sum)
    n1 = n2
    n2 = sum
print()
print(fib_list)