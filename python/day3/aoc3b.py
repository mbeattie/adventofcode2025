def read_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def calc_joltage(bank):
    bankints = [int(x) for x in bank]
    total = ""

    for i in range(11, -1, -1):
        highest = find_max_except_last(bankints, i)
        place = bankints.index(highest)
        # print("place:", place)
        bankints = bankints[place+1:]
        #print("new bankints:", bankints)
        total = total + str(highest)

    return int(total)

def find_max_except_last(bankints, iteration):
    iteration_value = -(iteration)
    print(f"Finding max in: {bankints} excluding last {iteration} elements.")
    if iteration == 0:
        highest = max(bankints)
        print(f"Finding max in: {bankints}. Highest found: {highest}")
        return highest
    highest = max(bankints[0:iteration_value])
    print(f"Finding max in: {bankints} excluding last {iteration} elements. Highest found: {highest}")
    return highest

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