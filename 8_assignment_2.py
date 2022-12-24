# matan bergenfeld
# 327456984
# Introduction to Computer Science
# targil_8 question_2
# program recieves lists merges and sorts into one list escending
def list_maker():
    list1 = [] * 10
    for i in range(10):
        num = int(input())
        if num != 0:
            list1.append(num)
        else:
            break
    return list1


def check_lst_error(list):
    sorted_list = sorted([*list])
    sorted_list.sort(reverse=True)
    is_sorted = list == sorted_list
    if not is_sorted or (len(set(list)) != len(list)):
        print("ERROR")
        list = list_maker()
        return list
    return list


def main():
    print('Enter values for the first list:')
    list1 = list_maker()
    list1 = check_lst_error(list1)
    print('Enter values for the second list:')
    list2 = list_maker()
    list2 = check_lst_error(list2)
    print('Enter values for the third list:')
    list3 = list_maker()
    list3 = check_lst_error(list3)
    merged_list = [*list1, *list2, *list3]
    merged_list.sort(reverse=True)
    # uniqe_merged = list(set(merged_list))
    clean = str(merged_list)[1:-1]

    print("Merged list is:\n", clean.replace(",", ""))


if __name__ == '__main__':
    main()
'''Enter values for the first list:
21
3
5
0
ERROR
8
5
0
Enter values for the second list:
7
3
0
Enter values for the third list:
4
2
0
Merged list is:
 8 7 5 4 3 2  '''
