def Main():
    try:
        N = int(input("\nEnter the number"))
        if N > 10:
            raise Exception
        for i in range(1, N + 1):
            j = 1
            while j <= N:
                if j <= i:
                    print(j, end=' ')
                else:
                    print(' ', end=' ')
                j += 1
            j = N - 1
            while j >= 1:
                if j > i:
                    print(' ', end=' ')
                else:
                    print(j, end=' ')
                j -= 1
            print("\n")
    except Exception:
        print("\nSomething is not right")


if __name__ == '__main__':
    Main()
