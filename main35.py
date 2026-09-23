n = int(input('Enter a number N:'))
largest = 1

for i in range(1, n + 1):
    if i > largest:
        largest = i

print(f'The largest number from 1 to {n} is: {largest}')
