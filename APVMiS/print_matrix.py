# Made by artor1as


def create_matrix(size):
    """
    create_matrix(size) -> stout matrix

    size: size of matrix NxN and must be odd number, because if even number
          it will be no center crossing of diagonals.

    output: matrix consist of diagonals with 2, between diagonals 1 or 0,
            looks like sand watches.

    result: size = 5

            2 0 0 0 2
            1 2 0 2 1
            1 1 2 1 1
            1 2 0 2 1
            2 0 0 0 2

    """
    if size is 1:
        print(2)
        return
    for r in range(size):
        for i in range(size):
            if i == r or i + r == size-1:
                number = 2
            elif (r <= size/2 and i + r > size-1
                    or i > r > size/2
                    or i < r <= size/2
                    or r >= size/2 and i + r < size-1):
                number = 1
            else:
                number = 0
            print(number, end=' ')
        print()


if __name__ == '__main__':
    while True:
        size = input('Enter matrix size (write \'exit\' to stop cycle): ')
        if size == 'exit':
            break
        try:
            size = int(size)
        except ValueError:
            print('Please enter number!')
            continue
        if size % 2 == 0:
            print('Please enter odd number!')
            continue
        create_matrix(size)
