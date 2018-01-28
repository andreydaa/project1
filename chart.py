#!/usr/bin/env python3

from matplotlib import pyplot as plt


def main():
    t_C = int(input())
    t_F = int(9 / 5 * t_C + 32)
    
    ts_C = list(range(int(input()), int(input())+1))
    ts_F = [int(9 / 5 * i + 32) for i in ts_C]

    plt.plot(ts_F, ts_C, 'g', linewidth=1)
    plt.scatter(t_F, t_C)
    
    plt.xlabel('Fahrenheit')
    plt.ylabel('Celsius')
    plt.title('A graph of temperature')

    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()
