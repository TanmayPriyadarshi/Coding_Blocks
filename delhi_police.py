def Main():
    try:
        N = int(input("\nEnter the number of car:"))
        if N>1000:
            raise Exception
        for j in range(N):
            cn = input("enter the car number:")
            #print(type(cn))
            lst = [int(number) for number in cn]
            #print(lst)
            l = len(lst)

            if l>0 and l<10:
                even = odd =0
                for i in lst:
                    if i%2==0:
                        even+=i
                    else:
                        odd+=i
                if even%4==0 or odd%3==0:
                    print("allowed to run on sunday")
                else:
                    print("not allowed to run on sunday")
            else:
                raise Exception
    except Exception:
        print("something is not right")



if __name__=='__main__':
    Main()

