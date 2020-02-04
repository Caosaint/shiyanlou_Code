# 这里有21根棍子，首先用户选1到4根，然后电脑选（注：用户和电脑一次选的棍子总数只能是5），谁选到最后一根就输，判断一下用户有赢的机会吗？
sticks = 21

print("There are 21 sticks, you can take 1-4 numbers of sticks at a time.")
print("Whoever gets the last stick will lose. ")
while True:
    print("Sticks left:", sticks)
    if sticks == 1:
        print("You took the last stick, you lose")
        break
    sticks_taken = int(input("Take stick(1-4):"))
    if sticks_taken >= 5 or sticks_taken <= 0:
        print("Wrong chioce")
        continue
    print("Computer took: ", (5 - sticks_taken), "\n")
    sticks -= 5  
