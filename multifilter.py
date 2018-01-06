#!/usr/bin/env python3


class multifilter:

    @staticmethod
    def judge_half(pos, neg):
        return pos >= neg

    @staticmethod
    def judge_any(pos, neg):
        return pos >= 1

    @staticmethod
    def judge_all(pos, neg):
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.items = []
        for i in iterable:
            pos, neg = 0, 0
            for j in funcs:
                if j(i):
                    pos += 1
                else:
                    neg += 1
            if judge(pos, neg):
                self.items.append(i)
    
    def __iter__(self):
        for item in self.items:
            yield item
