import re

fh = open('regex_sum_2333709.txt')
total = 0
for line in fh:
    line = line.strip()
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        total = total + int(number)

print(total)