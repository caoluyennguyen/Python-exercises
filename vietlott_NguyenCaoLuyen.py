import random

n=int(input("Nhap so lan mua ve:"))
ticket=list()
for i in range(0,n,1):
    k = 0
    b = list()
    print("Chon 6 so nho hon 45 lan thu",n,":")
    while (k < 6):
        m = int(input())
        if (m > 45): continue
        if (b.count(m)): continue
        b.append(m)
        k += 1
    print("6 so ban vua moi chon lan",n,"la:", b)
    ticket.append(b)
print("\nVe ban da mua la:\n",ticket)

system=list()
i=0
l=0
while(i<6):
    l = random.randrange(1, 45, 1)
    if(system.count(l)):continue
    system.append(l)
    i+=1
print("6 so cua he thong la:",system)

profit=0
x=0
for ve in ticket:
    x=0
    for c in system:
        for d in ve:
            if (c == d): x += 1
    if(x==3):profit+=30000
    if(x==4):profit+=300000
    if(x==5):profit+=10000000
    if(x==6):profit+=1000000000

print("CHUC MUNG BAN DA TRUNG",profit,"VND")