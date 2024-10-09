hours = int(input())
minutes = int(input())
delay = int(input())

minutes = minutes + delay
hours = (hours + minutes // 60) % 24
minutes = minutes % 60

print(f'{hours:02d}:{minutes:02d}')
