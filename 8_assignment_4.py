# matan bergenfeld
# 327456984
# Introduction to Computer Science
# targil_8 question_4
# program bubble sort by first digit or next

# added another line

def bubble_sort(nums: list):
    # bubble sorts
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if is_bigger(nums[j], nums[j + 1]):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


def is_bigger(first_num, second_num):
    # if first digs are equal...
    if get_num(first_num, 1) > get_num(second_num, 1):
        return True

    elif get_num(first_num, 1) == get_num(second_num, 1):
        for i in range(1, get_nums_len(first_num)):
            if get_num(first_num, i + 1) < get_num(second_num, i + 1):
                return False
            if get_num(first_num, i + 1) > get_num(second_num, i + 1):
                return True
    return False


def get_num(num, idx):
    # get num at index
    ln = get_nums_len(num)
    return (num // (10 ** (ln - idx))) % 10 if ln >= idx else -1


def get_nums_len(num):
    # get nums length
    counter = 0
    while num > 0:
        num = num // 10
        counter += 1
    return counter


def main():
    print('Enter 15 numbers:')
    num_list = [int(input()) for i in range(15)]
    bubble_sort(num_list)
    print('After sorting:')
    [print(num) for num in num_list]


if __name__ == '__main__':
    main()

'''example
Enter 15 numbers:
435
6
34
56
78
645
345
24
68
46
43
5
6
8
9
After sorting:
24
34
345
43
435
46
5
56
6
6
645
68
78
8
9'''
