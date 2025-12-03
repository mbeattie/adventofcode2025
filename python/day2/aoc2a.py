def read_input(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data.strip().split(',')

def find_invalid(number):
    # A number is invalid if it consists of a sequence of digits repeated twice
    length = len(number)
    if length % 2 != 0:
        return False
    half = length // 2
    invalid = number[:half] == number[half:]
    if invalid:
        print(f'Invalid number found: {number}')
    return invalid

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