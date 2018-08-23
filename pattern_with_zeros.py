def Main():
    try:
        N = int(input("\nEnter the number:"))
        if N > 100:
            raise Exception
        for i in range(1, N + 1):
            j = 1
            while j <= i:
                if j == 1 or j == i:
                    print(i, end=' ')
                else:
                    print(0, end=' ')
                j += 1
            print('\n')
    except Exception:
        print("\nSomething is not right")


if __name__ == '__main__':
    Main()
