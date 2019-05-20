# 插入排序算法
def a(*args):
    print(type(args))
    args = list(args)
    for i in range(1, args.__len__()):
        print(3)
        v = args[i]
        j = i-1
        while j >= 0 and args[j] > v:
            args[j+1] = args[j]
            j = j-1
        args[j+1] = v
        print(2)
    print(args)
    return args


if __name__ == '__main__':
    a(8, 4, 9, 6)
    print(1)
    print(type(a))
    print(a)


# def a(*args):
#     print(args)
#
# if __name__==