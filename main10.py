total_seconds = int(input('Enter no. of seconds: '))
hours, remaining_seconds = divmod(total_seconds, 3600)
minutes, seconds = divmod(remaining_seconds, 60)

print(f'The time is {hours} hours, {minutes} minutes, and {seconds} seconds.')