
def read_file(filename):
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]

def interpret_input(input):
    direction = input[0]
    distance = input[1:]
    return direction, int(distance)

def apply_move(position, direction, distance):
    if direction == 'L':
        new_pos = position - distance
        if new_pos < 0:
            new_pos = new_pos % 100
    elif direction == 'R':
        new_pos = position + distance
        if new_pos >= 100:
            new_pos = new_pos % 100
    print(f"Moved {direction}{distance} from {position} to {new_pos}")
    return new_pos

def main():
    position = 50
    moves = read_file("input1a.txt")
    num_zeroes = 0

    for move in moves:
        dir, dist = interpret_input(move)
        position = apply_move(position, dir, dist)
        if position == 0:
            num_zeroes = num_zeroes + 1
    
    print(f"Number of Zeros: {num_zeroes}")

if __name__ == '__main__':
    main()



