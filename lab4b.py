#!/usr/bin/env python3

def join_lists(l1, l2):
    temp_set = set(l1) | set(l2)
    return list(temp_set)

def match_lists(l1, l2):
    temp_set = set(l1) & set(l2)
    return list(temp_set)

def diff_lists(l1, l2):
    temp_set = set(l1) ^ set(l2)
    return list(temp_set)


if __name__ == '__main__':
    list1 = list(range(1,10))
    list2 = list(range(5,15))
    print('list1: ', list1)
    print('list2: ', list2)
    print('join: ', join_lists(list1, list2))
    print('match: ', match_lists(list1, list2))
    print('diff: ', diff_lists(list1, list2))