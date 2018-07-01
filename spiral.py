#!/usr/bin/env python3


def main():
    
    num = int(input())
    nums = [[0] * num for _ in range(num)]
    num_sqr = list(range(1, num ** 2 + 1))

    f = num - 1
    i, lot, count = 0, 0, 0
    for _ in range(num+f):
        count += 1
        for j in range(i, f+1):
            if count == 1:
                nums[i][j] = num_sqr[lot]
                lot += 1
            elif count == 2 and j != i:
                nums[j][f] = num_sqr[lot]
                lot += 1
            elif count == 3 and j != i:
                nums[f][f-j+i] = num_sqr[lot]
                lot += 1
            elif count == 4 and i < j < f:
                nums[f-j+i][i] = num_sqr[lot]
                lot += 1
        
        if count == 4:
            i += 1
            f -= 1
            count = 0
    
    for lst in nums:
        print('\t'.join([str(i) for i in lst]))


if __name__ == '__main__':
    main()
