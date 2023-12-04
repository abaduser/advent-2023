import random


def combine_first_last(listofnumbers):
    return int(listofnumbers[0] + listofnumbers[-1])

def extract_value_from_string(line):
    first_number = None
    second_number = None
    for c in line:
        if c.isdigit():
            first_number = c
            break
    if first_number == None:
        return 0
    for c in line[::-1]:
        if c.isdigit():
            second_number = c
            break
    assert first_number and second_number, f"Didn't get both numbers,{first_number}-{second_number}"
    return (int(f"{first_number}{second_number}"))

def extract_numerals(line):
    numbers = {
        "one" : '1',
        "two" : '2',
        "three" : '3',
        "four" : '4',
        "five" : '5',
        "six" : '6',
        "seven" : '7',
        "eight" : '8',
        "nine" : '9'
    }
    result = []
    for i in range(len(line)):
        if line[i].isdigit():
            result.append(line[i])
            continue
        for k in range(3,6):
            current_slice = line[i:i+k]
            if current_slice in numbers.keys():
                result.append(numbers[current_slice])
                break
    return result

def main():
    
    file_lines = [] 
    calibrated_sum = None 
    no_numeral_sum = None
    # write the lines in the file to file_lines 
    with open("./input", "r") as file:
        for line in file.readlines():
            file_lines.append(line)

    calibrated_sum = sum([extract_value_from_string(line) for line in file_lines])
    print(f"calibrated_sum: {calibrated_sum}")
    values = [extract_numerals(line) for line in file_lines]
    combined = [combine_first_last(lists) for lists in values]
    # [print("{0}".format(x)) for x in random.sample(list(zip(file_lines,values,combined)), 10)]
    no_numeral_sum = sum([combine_first_last((extract_numerals(line))) for line in file_lines])
    print(f"calibrated_sum without numerals: {no_numeral_sum}")
main()
