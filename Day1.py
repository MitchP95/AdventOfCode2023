from Utils.FileReader import read_lines_from_file
from Utils.Converters import written_number_to_digit

lines = read_lines_from_file('Inputs/Day1.txt')

# Part 1
total = 0
for line in lines:
    hasFirst = False
    firstValue = ''
    lastValue = ''

    for i in range(len(line)):
        if not hasFirst:
            if (line[i].isdigit()):
                firstValue = line[i]
                hasFirst = True
        else:
            if (line[i].isdigit()):
                lastValue = line[i]

    if (lastValue == ''):
        lastValue = firstValue

    total += int(firstValue + lastValue)
    
print('Part 1 Total:', total)

# Part 2   
import re

pattern = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'
word_mapping = {
    'one' : '1',
    'two' : '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',

}

# get digit as str
def get_digit(num) -> str:
    if num.isdigit():
        return num
    else:
        return word_mapping[num]
        
total = 0
for line in lines:
    nums = ""
    numbers = re.findall(pattern, line.strip())

    first = 0
    last = len(numbers) - 1

    nums += get_digit(numbers[first])
    nums += get_digit(numbers[last])

    total += (int(nums))

print('Part 2 Total:', total)