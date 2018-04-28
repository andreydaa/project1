#!/usr/bin/env python3


def main():
	numbers = input()

	nums = {
	    '0': [' -- ', '|  |', '|  |', '    ', '|  |', '|  |', ' -- '],
	    '1': ['    ', '   |', '   |', '    ', '   |', '   |', '    '],
	    '2': [' -- ', '   |', '   |', ' -- ', '|   ', '|   ', ' -- '],
	    '3': [' -- ', '   |', '   |', ' -- ', '   |', '   |', ' -- '],
	    '4': ['    ', '|  |', '|  |', ' -- ', '   |', '   |', '    '],
	    '5': [' -- ', '|   ', '|   ', ' -- ', '   |', '   |', ' -- '],
	    '6': [' -- ', '|   ', '|   ', ' -- ', '|  |', '|  |', ' -- '],
	    '7': [' -- ', '   |', '   |', '    ', '   |', '   |', '    '],
	    '8': [' -- ', '|  |', '|  |', ' -- ', '|  |', '|  |', ' -- '],
	    '9': [' -- ', '|  |', '|  |', ' -- ', '   |', '   |', ' -- ']
	}

	res = list(zip(*[nums[num] for num in numbers]))

	print('x{}x'.format('-'.join(['----'] * len(numbers))))
	for line in res:
		print('|{}|'.format(' '.join(line)))
	print('x{}x'.format('-'.join(['----'] * len(numbers))))


if __name__ == '__main__':
	main()
