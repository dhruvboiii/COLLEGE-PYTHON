a=int(input('Enter a number N:'))
count=0

for i in range(1,a+1):
    if i%2==0:
        count +=1

print(f'Number of even numbers from 1 to{a} is:',count)
