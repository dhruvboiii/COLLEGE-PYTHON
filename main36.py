n = int(input('Enter a number N:'))
smallest = n

for i in range(1, n + 1):
    if i < smallest:
        smallest = i

print(f'The smallest number from 1 to {n} is: {smallest}')
