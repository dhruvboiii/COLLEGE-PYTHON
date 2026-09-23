a=int(input('Enter a number N:'))

factorial=1
if a==0:
    print('The factorial of 0 is 1')
elif a<0:
    print('Negative number does not have a factorial')
else:
 for i in range(1,a+1):
    factorial*=i
print(f'The factorial of {a} is {factorial}')