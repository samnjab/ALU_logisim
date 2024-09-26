def DecimalToBinary(num: int) -> int:
    """Turns a decimal number into binary representation"""
    if num == 0:
         return 0
    remainder = num % 2
    return DecimalToBinary(num // 2) * 10 + remainder


def turn_into(num: int, d: int) -> (str, str):
    """ Turns an arbitrarily long binary number into a binary number of length d.
        returns the truncated binary number and its carryout in str format. """
    num_len = len(str(num))
    cout = 0
    while num_len > d:
        cout += 10 ** (len(str(num)) - 1)
        num = num - 10 ** (len(str(num)) - 1)
        num_len = len(str(num))
    s = ''
    for i in range(d - 1, -1, -1):
        s = s + str(num // (10 ** i))
        num = num % (10 ** i)
    return s, str(int(cout / 10 ** d))


def create_series(d: int) -> list:
    """ Creates a list of integers from 0 -> 2 ^ d - 1 """
    v = []
    for i in range(0, 2 ** (d)):
        v.append(i)
    return v


def ripple_carry4 (A: list, B: list, cin: list) -> list[list]:
    """ Creates a matrix of strs to test ripple_carry4 """
    matrix = []
    for c in cin:
        for i in A:
            for j in B:
                row = []
                row.append(turn_into(DecimalToBinary(i), 4)[0])
                row.append(turn_into(DecimalToBinary(j), 4)[0])
                row.append(turn_into(DecimalToBinary(c), 1)[0])
                s, cout = turn_into(DecimalToBinary(i + j + c), 4)
                row.append(s)
                row.append(cout)
                matrix.append(row)

    return matrix


def or_xor(a: int, b: int) -> str:
    """ returns a binary number representation in string """
    lower_half = a ^ b
    h1, cout = turn_into(DecimalToBinary(lower_half), 4)
    upper_half = a | b
    h2, cout2 = turn_into(DecimalToBinary(upper_half), 4)
    return h2 + h1


def op3_test(A: list, B: list) -> list[list]:
    """ returns a matrix of strs to test op3"""
    matrix = []
    for a in A:
        for b in B:
            row = []
            row.append(turn_into(DecimalToBinary(a), 4)[0])
            row.append(turn_into(DecimalToBinary(b), 4)[0])
            row.append(or_xor(a, b))
            matrix.append(row)
            print('row appended:', row)
    return matrix


def op4_test(A: list, B: list) -> list[list]:
    """ returns a matrix of strs to test op4"""
    matrix = []
    for a in A:
        for b in B:
            row = []
            row.append(turn_into(DecimalToBinary(a), 4)[0])
            row.append(turn_into(DecimalToBinary(b), 4)[0])
            if a == 0 and b == 0:
                row.append(turn_into(DecimalToBinary(0), 8)[0])
            else:
                row.append(turn_into(DecimalToBinary(1), 8)[0])
            matrix.append(row)
    return matrix


def concatenate(a: int, b:int) -> str:
    """ returns bin(a) + bin(b) as a string"""
    return turn_into(DecimalToBinary(a), 4)[0] + turn_into(DecimalToBinary(b), 4)[0]


def op5_test(A: list, B: list) -> list[list]:
    """ returns a matrix of strs to test op5"""
    print('A, B:', A , B)
    matrix = []
    for a in A:
        for b in B:
            row = []
            row.append(turn_into(DecimalToBinary(a), 4)[0])
            row.append(turn_into(DecimalToBinary(b), 4)[0])
            row.append(concatenate(a, b))
            matrix.append(row)
    return matrix


if __name__ == '__main__':

    A = create_series(4)
    B = create_series(4)

    """Testing ripple_carry4"""
    cin = create_series(1)
    result_matrix = ripple_carry4(A, B, cin)
    # Open file for writing
    with open("ripple_carry4_test.txt", "w") as f:
        # Write the header
        f.write("a b cin Y Cout\n")

        # Write each row in the matrix to the file
        for row in result_matrix:
            f.write(" ".join(row) + "\n")

    print("Output successfully written to ripple_carry4_test.txt")
    """Testing op3"""
    op3_matrix = op3_test(A, B)
    # Open file for writing
    with open("op3_test.txt", "w") as f:
        # Write the header
        f.write("A B OPout\n")

        # Write each row in the matrix to the file
        for row in op3_matrix:
            f.write(" ".join(row) + "\n")

    """Testing op4"""
    op4_matrix = op4_test(A, B)
    # Open file for writing
    with open("op4_test.txt", "w") as f:
        # Write the header
        f.write("A B OPout\n")

        # Write each row in the matrix to the file
        for row in op4_matrix:
            f.write(" ".join(row) + "\n")

    """Testing op5"""
    op5_matrix = op5_test(A, B)
    # Open file for writing
    with open("op5_test.txt", "w") as f:
        # Write the header
        f.write("A B OPout\n")

        # Write each row in the matrix to the file
        for row in op5_matrix:
            f.write(" ".join(row) + "\n")




