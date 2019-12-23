import random

def tuti(chosen,opponent,sys):
    sys1 = random.randrange(1, 4, 1)
    sys2 = random.randrange(1, 4, 1)
    print("Lua chon cua may",sys[chosen],"la:")
    if (sys1 == 1):
        print("Keo")
    elif (sys1 == 2):
        print("Bua")
    elif (sys1 == 3):
        print("Bao")
    print("Lua chon cua may",sys[opponent],"la:")
    if (sys2 == 1):
        print("Keo")
    elif (sys2 == 2):
        print("Bua")
    elif (sys2 == 3):
        print("Bao")
    if (sys1 == sys2):
        print("Draw")
        return -2
    elif ((sys1 - sys2 == -1) or (sys1 - sys2 == 2)):
        print("May",sys[opponent],"WIN\nMay",sys[chosen],"out")
        return chosen
    elif ((sys1 - sys2 == -2) or (sys1 - sys2 == 1)):
        print("May",sys[chosen],"WIN\nMay",sys[opponent],"out")
        return opponent

if __name__ == '__main__':
    n = int(input("Nhap so luong may tu choi: "))
    while(n<2):
        n = int(input("Nhap so luong may tu choi: "))
    sys = list(range(1,n+1))

    while(n>1):
        #chosen = int(input())
        chosen = random.randrange(0,n,1,int)
        opponent = random.randrange(chosen - 1, chosen + 1, 1)
        while (opponent == chosen):
            opponent = random.randrange(chosen - 1, chosen + 1, 1)
        if (opponent == (-1)):
            opponent = (n - 1)
        elif (opponent == n):
            opponent = 0
        print("\nMay duoc chon la may thu", sys[chosen])
        print("May duoc chon de choi cung la may thu", sys[opponent])
        print(sys)
        a = int(tuti(chosen,opponent,sys))
        if(a>=0):
            print("May bi loai la may",sys[a])
            sys.remove(sys[a])
            n=n-1
        print("So may con lai la",n,"may")
        print(sys)

    print("\nPhan thang chung cuoc thuoc ve may",sys[0])
