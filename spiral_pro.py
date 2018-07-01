#!/usr/bin/env python3


def main():
    
    num = int(input())
    nums = [[0] * num for _ in range(num)]

    i, j = 0, 0
    lot, count = 1, 1

    for _ in range(num-num//2):
        
        for j in range(j, num):
            nums[i][j] = lot
            lot += 1
        
        for i in range(i+1, num):
            nums[i][j] = lot
            lot += 1
        
        for i in range(i-1, count-2, -1):
            nums[j][i] = lot
            lot += 1
        
        for j in range(j-1, count-1, -1):
            nums[j][i] = lot
            lot += 1
        
        i += 1
        num -= 1
        count += 1
    
    for line in nums:
        print('\t'.join([str(num) for num in line]))


if __name__ == '__main__':
    main()
