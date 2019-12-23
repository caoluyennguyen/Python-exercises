van=0
nguoi=0
may=0
may1=0
may2=0
def choituti(n):
    """Nguoi choi voi may"""
    global van
    global nguoi
    global may
    a=random.randrange(1,4,1)
    print("Lua chon cua may la:")
    if (a == 1):
        print("Keo")
    elif (a == 2):
        print("Bua")
    elif (a == 3):
        print("Bao")

    if (a == n):
        print("Draw")
        van+=1
    elif ((a - n == -1) or (a - n == 2)):
        print("Win")
        nguoi+=1
        van+=1
    elif ((a - n == -2) or (a - n == 1)):
        print("Lose")
        may+=1
        van+=1
def choitutiAI():
    """May tu choi"""
    global van
    global may1
    global may2
    sys1=random.randrange(1,4,1)
    sys2=random.randrange(1,4,1)
    print("\nLua chon cua may 1 la:")
    if (sys1 == 1):
        print("Keo")
    elif (sys1 == 2):
        print("Bua")
    elif (sys1 == 3):
        print("Bao")
    print("Lua chon cua may 2 la:")
    if (sys2 == 1):
        print("Keo")
    elif (sys2 == 2):
        print("Bua")
    elif (sys2 == 3):
        print("Bao")
    if (sys1 == sys2):
        print("Draw")
        van+=1
    elif ((sys1 - sys2 == -1) or (sys1 - sys2 == 2)):
        print("May 2 WIN\nMay 1 lose")
        may2+=1
        van+=1
    elif ((sys1 - sys2 == -2) or (sys1 - sys2 == 1)):
        print("May 1 WIN\nMay 2 lose")
        may1+=1
        van+=1

if __name__ == '__main__':
    """Ham main nguoi choi voi may"""
    print("Keo so 1\nBua so 2\nBao so 3")
    while((nguoi<3)and(may<3)):
        n = int(input("Nhap lua chon cua ban: "))
        while((n<1)or(n>3)):
            n = int(input("Nhap lai lua chon cua ban: "))
        print("Lua chon cua ban la: ")
        if (n == 1): print("Keo")
        if (n == 2): print("Bua")
        if (n == 3): print("Bao")
        choituti(n)
    print("\nTong cong co",van,"van")
    print("Nguoi thang",nguoi,"van")
    print("May thang",may,"van")

# if __name__ == '__main__':
#     """Ham main may tu choi"""
#     while((may1<3)and(may2<3)):
#         choitutiAI()
#     print("\nTong cong co",van,"van")
#     print("May 1 thang",may1,"van")
#     print("May 2 thang",may2,"van")
#     if (may1 > may2):
#         print("Phan thang chung cuoc thuoc ve: May 1")
#     elif (may1 < may2):
#         print("Phan thang chung cuoc thuoc ve: May 2")