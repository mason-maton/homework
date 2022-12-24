# matan bergenfeld
# 327456984
# Introduction to Computer Science
# targil_8 question_1
# program requests list in order, requests an index. outputs number and index

def list_search(list1, item):
    # function finds location of number in list and returns index
    low = 0
    high = len(list1) - 1
    # Repeat until low and high meet each other
    while low <= high:
        mid = (low + high) // 2
        if list1[mid] == item:
            return mid
        elif list1[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def main():
    print('Enter 10 numbers:')
    list1 = [int(input()) for i in range(10)]
    j = 1
    i = 0
    flag = True
    while j < 10:
        if list1[i] >= list1[j]:
            flag = False
            if flag == False:
                print('ERROR')
                list1 = [int(input()) for i in range(10)]
                j = 1
                i = 0
                flag = True
        i += 1
        j += 1
    print('Enter 1 number:')
    item = int(input())

    if list_search(list1, item) == -1:
        print('Not found')
    else:
        print('The number', item, 'was found at index', list_search(list1, item))


'''Enter 10 numbers:
1
2
3
4
5
6
7
8
9
10
Enter 1 number:
3
The number 3 was found at index 2'''

if __name__ == '__main__':
    main()
