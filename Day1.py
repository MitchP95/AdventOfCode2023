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
    
print(total)

# Part 2
total = 0
for line in lines:
    hasFirst = False
    firstValue = ''
    lastValue = ''

    startPointer = 0
    for i in range(len(line)):
        if (written_number_to_digit(line[startPointer:i]) != -1):
            if not hasFirst:
                firstValue = written_number_to_digit(line[startPointer:i])
                hasFirst = True
            else:
                lastValue = written_number_to_digit(line[startPointer:i])

            startPointer = i + 1
        else:
            print(line[startPointer:i])
        
    if (lastValue == ''):
        lastValue = firstValue

    total += int(firstValue + lastValue)
    
print(total)