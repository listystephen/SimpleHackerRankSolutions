if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    max_1 = max(arr)
    arr = filter(lambda a: a != max_1, arr)
    print max(arr)