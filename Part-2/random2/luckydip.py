import random

lottery_nos=[]
for x in range(100):
    lottery_nos.append(random.randint(100,200))

#print(lottery_nos)

luckydip=random.sample(lottery_nos,2)
print(luckydip)