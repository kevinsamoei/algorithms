"""You are presented with two arrays, all containing positive integers. One of the arrays will have one extra number, see below:

[1,2,3] and [1,2,3,4] should return 4

[4,66,7] and [66,77,7,4] should return 77 """

def find_missing(first, second):
    len_first = len(first)
    len_second = len(second)

    if len_first == len_second:
        return 0
    else:
        for i in second:
            if i not in first:
                return i