def read_input(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data.strip().split(',')

def find_invalid(number):
    # A number is invalid if it consists of a sequence of digits repeated N times
    
    # This function returns None if there is no repetition (it is valid)
    # And returns a value if it does repeat.
    invalid = principal_period(number)

    if invalid:
        print(f'Invalid number found: {number}')
    return invalid

def principal_period(s):
    # https://stackoverflow.com/questions/29481088/how-can-i-tell-if-a-string-repeats-itself-in-python
    # This is a brilliant solution
    # Take the string and concat it with itself
    # Remove the first and last digits so that it doesnt directly match against the original strings
    # find if the original string is a substring of the new concat'd string
    # If yes, it means that there is repetition because it matched the latter part of the first and the first part of the latter
    # It returns the index where the match started, which is the first place the repetition happens
    # use this to index the original string from the start to the repetition index.
    i = (s+s).find(s, 1, -1)
    return None if i == -1 else s[:i]

def main():
    input_data = read_input('input2a.txt')
    total_invalid = 0

    for idrange in input_data:
        start, end = idrange.split('-')
        for number in range(int(start), int(end) + 1):
            str_number = str(number)
            if find_invalid(str_number):
                total_invalid += number

    print(f'Total of invalid numbers: {total_invalid}')

if __name__ == '__main__':
    main()