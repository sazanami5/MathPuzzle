card=[]
for i in range(101):
    card.append(False)#　裏がFalse

for n in range(2,101):
    for m in range(0,101,n):
        card[m] = not card[m]

print(card)
for l in range(101):
    if card[l]==False:
        print(l)
