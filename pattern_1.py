def Main():
    try:
        N = int(input("\nEnter the number:"))
        if N>10:
            raise Exception
        for i in range(N+1,1,-1):
            j=1
            while j<=N:
                if j>=i:
                    print('*',end = ' ')
                else:
                    print(j,end = ' ')
                j+=1
            j=5-i
            while j>1:
                print('*',end=' ')
                j-=1
            print("\n")
    except Exception:
        print("\n Something is not Right")

if __name__=='__main__':
    Main()