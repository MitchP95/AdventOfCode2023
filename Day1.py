from Utils.FileReader import read_lines_from_file

lines = read_lines_from_file('Inputs/Day1.txt')

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