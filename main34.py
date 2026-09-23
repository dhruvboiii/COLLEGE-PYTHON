n=int(input('Enter a number N:'))
sum_odd=0
for i in range(1,n+1):
    if i%2!=0:
        sum_odd +=i

print(f'The sum of odd numbers between 1 and {n} is ',sum_odd)


