a=int(input('Enter a number N:'))
count=0

for i in range(1,a+1):
    if i%2!=0:
        count +=1

print(f'The number of odd numbers in between 1 and {a} is',count)
