def read_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def calc_joltage(bank):
    bankints = [int(x) for x in bank]
    tens = max(bankints[0:-1]) #all but last so that we have a ones place
    tensplace = bank.find(str(tens))
    ones = max(bankints[tensplace+1:])

    total = str(tens) + str(ones)

    return int(total)

def main():
    filename = 'input3a.txt'
    totaljolts = 0

    banks = read_file(filename)
    for bank in banks:
        result = calc_joltage(bank)
        totaljolts += int(result)
        print(f"Bank: {bank} => Result: {result}")

    print(f"Total Jolts: {totaljolts}")

if __name__ == "__main__":
    main()