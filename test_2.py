def DecimalToBinary(num: int, bits: int) -> str:
    """Turns a decimal number into a binary string with a fixed number of bits."""
    return format(num, f'0{bits}b')  # Converts to binary and pads with leading zeros

def create_series(d: int) -> list:
    """Creates a list of integers from 0 -> 2^d - 1."""
    return [i for i in range(2 ** d)]

def ripple_carry4(A: list, B: list, cin: list) -> list[list]:
    """Creates a matrix to test ripple_carry4 with 4-bit inputs and outputs."""
    matrix = []
    for c in cin:
        for i in A:
            for j in B:
                row = []
                row.append(DecimalToBinary(i, 4))  # A in 4-bit binary
                row.append(DecimalToBinary(j, 4))  # B in 4-bit binary
                row.append(DecimalToBinary(c, 1))  # Cin in 1-bit binary
                sum_bin = DecimalToBinary(i + j + c, 4)  # Sum as 4-bit binary
                cout = DecimalToBinary((i + j + c) >> 4, 1)  # Cout as 1-bit binary (overflow)
                row.append(sum_bin)
                row.append(cout)
                matrix.append(row)
    return matrix

def or_xor(a: int, b: int) -> str:
    """Returns the result of a | b and a ^ b, concatenated as an 8-bit binary string."""
    lower_half = DecimalToBinary(a ^ b, 4)
    upper_half = DecimalToBinary(a | b, 4)
    return upper_half + lower_half  # Concatenate the 4-bit results into an 8-bit binary string

def op3_test(A: list, B: list) -> list[list]:
    """Returns a matrix to test op3 with 4-bit inputs and 8-bit outputs."""
    matrix = []
    for a in A:
        for b in B:
            row = []
            row.append(DecimalToBinary(a, 4))  # A in 4-bit binary
            row.append(DecimalToBinary(b, 4))  # B in 4-bit binary
            row.append(or_xor(a, b))           # Concatenated 8-bit result
            matrix.append(row)
    return matrix

def op4_test(A: list, B: list) -> list[list]:
    """Returns a matrix to test op4 with 4-bit inputs and 8-bit outputs."""
    matrix = []
    for a in A:
        for b in B:
            row = []
            row.append(DecimalToBinary(a, 4))  # A in 4-bit binary
            row.append(DecimalToBinary(b, 4))  # B in 4-bit binary
            if a == 0 and b == 0:
                row.append(DecimalToBinary(0, 8))  # Special case: output 0 as 8-bit binary
            else:
                row.append(DecimalToBinary(1, 8))  # Otherwise, output 1 as 8-bit binary
            matrix.append(row)
    return matrix

def concatenate(a: int, b: int) -> str:
    """Concatenates two 4-bit binary numbers into an 8-bit binary string."""
    return DecimalToBinary(a, 4) + DecimalToBinary(b, 4)

def op5_test(A: list, B: list) -> list[list]:
    """Returns a matrix to test op5 with 4-bit inputs and 8-bit outputs."""
    matrix = []
    for a in A:
        for b in B:
            row = []
            row.append(DecimalToBinary(a, 4))  # A in 4-bit binary
            row.append(DecimalToBinary(b, 4))  # B in 4-bit binary
            row.append(concatenate(a, b))      # Concatenated 8-bit result
            matrix.append(row)
    return matrix

if __name__ == '__main__':
    A = create_series(4)  # A and B are 4-bit inputs
    B = create_series(4)
    cin = create_series(1)  # Cin is a 1-bit input

    """Testing ripple_carry4"""
    result_matrix = ripple_carry4(A, B, cin)
    with open("ripple_carry4_test.txt", "w") as f:
        f.write("a b cin Y Cout\n")
        for row in result_matrix:
            f.write(" ".join(row) + "\n")

    """Testing op3"""
    op3_matrix = op3_test(A, B)
    with open("op3_test.txt", "w") as f:
        f.write("A B OPout\n")
        for row in op3_matrix:
            f.write(" ".join(row) + "\n")

    """Testing op4"""
    op4_matrix = op4_test(A, B)
    with open("op4_test.txt", "w") as f:
        f.write("A B OPout\n")
        for row in op4_matrix:
            f.write(" ".join(row) + "\n")

    """Testing op5"""
    op5_matrix = op5_test(A, B)
    with open("op5_test.txt", "w") as f:
        f.write("A B OPout\n")
        for row in op5_matrix:
            f.write(" ".join(row) + "\n")
