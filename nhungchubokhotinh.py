def cows_exsist(cowsConditions, cow):
    for i in cowsConditions.values():
        if cow in i:
            return True
    return False

_ = int(input())
cows = "Krixi Toro Emily Max Yasuo Leona Garen Jinx".split(" ")
cows = sorted(cows)
# print(cows)
milked = [False, False, False, False, False, False, False, False]
cowsConditions = dict()
for i in range (_):
    con = input().split()
    x = con[0]
    y = con[5]
    # print(x, y)
    if x in cowsConditions:
        cowsConditions[x].append(y)
    else:
        cowsConditions[x] = [y]
for cow in cows :
    
    if cows_exsist(cowsConditions, cow):
        continue
    if cow not in cowsConditions and milked[cows.index(cow)] == False:
        print(cow)
        milked[cows.index(cow)] = True
        continue

for cow in cowsConditions.keys():
    if milked[cows.index(cow)] == False:
        cow1 = cowsConditions[cow][0]
        cow2 = cowsConditions[cow][1]
        if cow1 in cowsConditions:
            print(cowsConditions[cow1][0])
            milked[cows.index(cowsConditions[cow1][0])] = True
        print(cow1)
        milked[cows.index(cow1)]=True 
        print(cow)
        milked[cows.index(cow)] = True
        print(cow2)
        milked[cows.index(cow2)] = True
        if cow2 in cowsConditions:
            print(cowsConditions[cow2][0])
            milked[cows.index(cowsConditions[cow2][0])] = True
       

    