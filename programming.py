import argparse
import sys
from programming_unit_test import UnitTest

def find_n_most_frequent_nums(arr, k, n):
    
    """
    Find 'n' most frequent numbers inside a list
    
    Arguments:
        - arr: list, input array
        - k: int, length of input array (len(arr))
        - n: int, n numbers to show
    
    Returns:
        - res: list, a list of answers (number and frequency)
    """
    
    # hash map for each number and its frequency
    hash_map = {}
    for i in range(k):
        # if a number is already in the hash map, increase the count (frequency) by 1
        if arr[i] in hash_map:
            hash_map[arr[i]] += 1
        # if not, set the count to 1
        else:
            hash_map[arr[i]] = 1
    
    # a list for storing the result
    res = []
    j = 0
    for i in hash_map:
        res.append([i, hash_map[i]])
        j += 1
    
    # sort by descending order (number with the highest frequency comes first)
    res = sorted(res, key=lambda x: x[0], reverse=True)
    res = sorted(res, key=lambda x: x[1], reverse=True)
    
    return res


if __name__ == '__main__':
    
    # starts with user input
    arr = []
    k = int(input("Enter number of elements : "))
    for i in range(0, k):
        num = int(input())
        arr.append(num)
        
    n = int(input("Enter n most frequent numbers to show : "))
    
    # basic input test case
    UnitTest.assert_positive_non_zero_k(k)
    UnitTest.assert_positive_non_zero_n(n)
    
    # find n most frequent numbers
    answer = []
    result = find_n_most_frequent_nums(arr, k, n)
    
    # test case 1 & 2
    UnitTest.case_1(arr, n)
    UnitTest.case_2(arr, n)
    
    # we only care about the number (index 0) the 2nd element is the frequency (index 1)
    for i in range(n):
        answer.append(result[i][0])

    print(answer)