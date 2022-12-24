# matan bergenfeld
# 327456984
# Introduction to Computer Science
# targil_8 question_3
# program sorts matrix in two groups without sorting some


def main():
    print('Enter the values:')
    matrix = [[int(input()) for _ in range(10)] for _ in range(10)]
    # matrix = [[num for num in range(10)] for _ in range(10)]
    print_matrix("Before sorting:", matrix)
    first_part = [a[i + 1:] for i, a in enumerate(matrix[:-1])]
    all_first_numbers = merge_lists(first_part)
    sorted_first = list(reversed(insertion_sort(all_first_numbers)))

    second_part = [a[:i + 1] for i, a in enumerate(matrix[1:])]
    all_second_numbers = merge_lists(second_part)
    sorted_second = list(reversed(insertion_sort(all_second_numbers)))

    sorted_matrix = [*matrix]
    for i_row in range(9):
        for i_col in range(i_row + 1, 10):
            sorted_matrix[i_row][i_col] = sorted_first.pop()

    for i_row in range(1, 10):
        for i_col in range(i_row):
            sorted_matrix[i_row][i_col] = sorted_second.pop()
    print_matrix("Sorted matrix:", sorted_matrix)


def print_matrix(prefix, matrix):
    '''
    :param prefix: prefix to be printed
    :param matrix: matrix to be printed
    '''
    print(prefix)
    [print(str(row).replace("[", "").replace("]", "").replace(",", "")) for row in matrix]


def merge_lists(lst):
    '''
    :param lst: lst to be flattend
    :return: flat list
    '''
    merged = []
    for val in lst:
        merged = [*merged, *val]
    return merged


def insertion_sort(lst):
    '''
    :param lst: list to be sorted
    :return: copy of sorted list
    '''
    _lst = [*lst]
    for i in range(1, len(_lst)):
        value = _lst[i]
        j = i - 1
        while j >= 0 and value < _lst[j]:
            _lst[j + 1] = _lst[j]
            j -= 1
        _lst[j + 1] = value
    return _lst


if __name__ == '__main__':
    main()
'''example:
Enter the values:
Before sorting:
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
Sorted matrix:
0 1 2 2 3 3 3 4 4 4
0 1 4 5 5 5 5 5 6 6
0 0 2 6 6 6 6 7 7 7
0 0 0 3 7 7 7 7 8 8
0 0 0 1 4 8 8 8 8 8
1 1 1 1 1 5 8 9 9 9
1 1 2 2 2 2 6 9 9 9
2 2 2 3 3 3 3 7 9 9
3 3 4 4 4 4 4 5 8 9
5 5 5 6 6 6 7 7 8 9'''
